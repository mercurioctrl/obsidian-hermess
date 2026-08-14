# Arquitectura

## Flujo end-to-end

```
cron / CLI → sincro.py → AfipScraper (Playwright)
                               ↓
                      Portal AFIP → Mis Comprobantes → Recibidos → Exportar CSV
                               ↓
                      storage/output/<cuit>/*.csv
                               ↓
                      DbLoader (pymssql)
                               ↓
                      SQL Server: NewBytes_DBF.dbo.AfipComprobantesRecibidos
                      (staging + MERGE → idempotente)
```

Ver [[stack]] para tecnologías y versiones.

## Componentes

### `sincro.py` — orquestador CLI

Recibe parámetros, arma el plan (CUITs × rango), y por cada CUIT corre `scrape → load`. Flags:

- `--ultimos-dias N` / `--desde / --hasta` — rango a descargar.
- `--cuit 30-XXXXXXXX-X` — filtra a un CUIT puntual.
- `--skip-db` — no cargar (solo CSVs).
- `--skip-scrape` — solo cargar CSVs ya bajados (re-procesar sin pegarle a AFIP).

### `afip/config.py` — configuración

Carga `.env` y `cuits.yaml`. Dataclasses `Settings`, `Cuit`, `DbSettings`. Valida credenciales mínimas: `AFIP_USER`, `AFIP_PASS` y `CAPTCHA_API_KEY` (esta última obligatoria desde ago-2026).

### `afip/scraper.py` — Playwright

Navega AFIP con Chromium. Guarda `storageState` por CUIT en `storage/sessions/<cuit>.json` con la intención de reutilizar cookies, aunque en la práctica AFIP no las conserva (ver decisión abajo).

**Flujo interno:**

1. **Login** en `https://auth.afip.gob.ar/contribuyente_/login.xhtml`.
   - Selectores `#F1:username` + `#F1:btnSiguiente` → `#F1:password`.
   - **Captcha** (desde 2026-08-06): AFIP muestra un captcha de texto (`img[alt='Captcha']`, JPEG base64). Se resuelve con [[stack|2Captcha]] vía `afip/captcha.py` y la solución va a `#F1:captchaSolutionInput` antes de `#F1:btnIngresar`. Si falla, se reintenta con un captcha nuevo hasta `LOGIN_INTENTOS` veces.
2. Portal ARCA: buscador `input[placeholder*='Buscá']` → tipear "Mis Comprobantes".
3. **Servicio abre en pestaña nueva** (`context.expect_page()`) en `fes.afip.gob.ar/mcmp/`.
4. Pantalla "Elegí una persona": click en el CUIT a representar.
5. Click en tarjeta Recibidos.
6. Date range: **daterangepicker.js** — fill `daterangepicker_start/end` + click `.applyBtn`.
7. Click `#buscarComprobantes`. Esperar `#tablaDataTables`.
8. Click `button[title='Exportar como CSV']` → capturar download.
9. AFIP entrega **ZIP con CSV adentro** → extraer con `zipfile`.

**Debug:** flag `--debug` toma screenshots en cada paso y dumpea HTML si falla la exportación.

### `afip/captcha.py` — resolvedor de captcha

Función `resolver_captcha_dataurl(src, api_key)`: recibe el `src` del `<img>` del captcha (data URL base64) y lo manda a **2Captcha** vía la librería oficial `twocaptcha`. Devuelve el texto reconocido (~99% al primer intento). La API key sale de `.env` (`CAPTCHA_API_KEY`). Único consumidor: `scraper.py:_login`.

### `afip/db.py` — loader

Parsea el CSV (`;` delimiter, UTF-8, decimales con coma → punto, vacíos → NULL). Conecta con pymssql (TDS 7.4). Crea `#staging` temp, `executemany INSERT`, luego `MERGE ... WHEN NOT MATCHED`. `OUTPUT $action` da el count de insertados vs. duplicados.

## Decisiones de diseño

### Scraping vs. Web Services de ARCA

Los WS oficiales (WSFE, WSMTXCA) sirven para **emitir** comprobantes, no para listar **recibidos**. El único lugar confiable es Mis Comprobantes (webapp). Todo software contable del mercado que integra recibidos hace scraping también.

### pymssql vs. pyodbc

- Wheels `manylinux` precompilados → Dockerfile no necesita instalar driver ODBC.
- Placeholders `%s` simples.
- Soporta TDS 7.4 nativo.
- Tradeoff: en macOS requiere `brew install freetds`. En Docker anda directo.

### Sesión (no) persistente por CUIT

Se guarda `storage/sessions/<cuit>.json` con las cookies con la intención de reutilizar la sesión. **En la práctica AFIP no la conserva**: al volver a `login.xhtml` el form reaparece siempre, así que se hace login completo (y captcha) en **cada** corrida. Se sigue guardando el `storageState` por si AFIP cambia esto, pero hoy no evita el login. Consecuencia: **cada corrida del cron consume un captcha de 2Captcha**.

### 2Captcha para el captcha del login

El 2026-08-06 AFIP agregó un captcha de texto y rompió el scraper. Caminos evaluados:

- **OCR local (tesseract)** → descartado: 0/6 en captchas reales (fuente distorsionada + líneas diagonales; ni con preprocesado agresivo el techo pasa de 0).
- **Modelo local entrenado (CRNN)** → descartado: juntar el dataset implicaba pegarle mucho al login de AFIP, con **riesgo de bloquear la cuenta** (la misma que usa contabilidad).
- **Servicio anti-captcha (2Captcha)** → elegido: ~99% al primer intento, sin riesgo de bloqueo, costo ~USD 0.5-1 cada 1000 (~EUR 0.05-0.10/día al ritmo cada-15-min).

Tradeoff: 2Captcha es **prepago** — sin saldo, el cron deja de loguear. Vigilar el saldo. Ver [[contexto]] y [[despliegue]].

### Docker-first

Portable al server sin instalar Python 3.11, Playwright, Chromium ni FreeTDS a mano. La imagen oficial de Playwright ahorra ~15 min de setup.

### Idempotencia vía MERGE

El índice único `UX_AfipRec_natural` sobre `(cuit_titular, tipo_comprobante, punto_venta, numero_desde, nro_doc_emisor)` garantiza una fila por comprobante. `MERGE WHEN NOT MATCHED` inserta solo los nuevos. Podés re-procesar rangos N veces sin efectos. Ver [[migracion]].

## Ubicación de datos

| Dato                    | Ubicación                                           |
|-------------------------|-----------------------------------------------------|
| Credenciales            | `.env` (`AFIP_USER`, `AFIP_PASS`, `CAPTCHA_API_KEY`, `DB_*`) |
| Lista de CUITs          | `cuits.yaml`                                        |
| Sesiones / cookies      | `storage/sessions/<cuit>.json`                      |
| CSVs finales            | `storage/output/<cuit>/recibidos_<desde>_<hasta>.csv` |
| Logs                    | `storage/logs/sincro.log` (rotado, 5 MB × 5)        |
| Datos estructurados     | SQL Server — ver [[tabla-referencia]]               |

## Lo que rompe si AFIP cambia la UI

| Archivo              | Zona                                                   |
|----------------------|--------------------------------------------------------|
| `scraper.py:_login`  | Selectores del login + captcha (`img[alt='Captcha']`, `#F1:captchaSolutionInput`) |
| `captcha.py`         | Falla de 2Captcha (sin saldo, API key inválida, servicio caído) |
| `_open_mis_comprobantes` | Buscador del portal ARCA                           |
| `_seleccionar_cuit_representado` | Pantalla "Elegí una persona"               |
| `_descargar_recibidos` | Tab Recibidos + daterangepicker + BUSCAR + Exportar |

Todos los selectores están concentrados en `afip/scraper.py`.

## Ver también

- [[sincroAfip]] — índice del proyecto.
- [[despliegue]] — cómo opera en producción.
- [[migracion]] — DDL y evolución de la tabla.
- [[tabla-referencia]] — columnas y códigos AFIP.
