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

Carga `.env` y `cuits.yaml`. Dataclasses `Settings`, `Cuit`, `DbSettings`.

### `afip/scraper.py` — Playwright

Navega AFIP con Chromium. Guarda `storageState` por CUIT en `storage/sessions/<cuit>.json` para reutilizar cookies entre corridas.

**Flujo interno:**

1. **Login** en `https://auth.afip.gob.ar/contribuyente_/login.xhtml` (selectores `#F1:username`, `#F1:password`).
2. Portal ARCA: buscador `input[placeholder*='Buscá']` → tipear "Mis Comprobantes".
3. **Servicio abre en pestaña nueva** (`context.expect_page()`) en `fes.afip.gob.ar/mcmp/`.
4. Pantalla "Elegí una persona": click en el CUIT a representar.
5. Click en tarjeta Recibidos.
6. Date range: **daterangepicker.js** — fill `daterangepicker_start/end` + click `.applyBtn`.
7. Click `#buscarComprobantes`. Esperar `#tablaDataTables`.
8. Click `button[title='Exportar como CSV']` → capturar download.
9. AFIP entrega **ZIP con CSV adentro** → extraer con `zipfile`.

**Debug:** flag `--debug` toma screenshots en cada paso y dumpea HTML si falla la exportación.

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

### Sesión persistente por CUIT

Evita loguearse cada corrida. Cookies en `storage/sessions/<cuit>.json`.

### Docker-first

Portable al server sin instalar Python 3.11, Playwright, Chromium ni FreeTDS a mano. La imagen oficial de Playwright ahorra ~15 min de setup.

### Idempotencia vía MERGE

El índice único `UX_AfipRec_natural` sobre `(cuit_titular, tipo_comprobante, punto_venta, numero_desde, nro_doc_emisor)` garantiza una fila por comprobante. `MERGE WHEN NOT MATCHED` inserta solo los nuevos. Podés re-procesar rangos N veces sin efectos. Ver [[migracion]].

## Ubicación de datos

| Dato                    | Ubicación                                           |
|-------------------------|-----------------------------------------------------|
| Credenciales            | `.env` (`AFIP_USER`, `AFIP_PASS`, `DB_*`)           |
| Lista de CUITs          | `cuits.yaml`                                        |
| Sesiones / cookies      | `storage/sessions/<cuit>.json`                      |
| CSVs finales            | `storage/output/<cuit>/recibidos_<desde>_<hasta>.csv` |
| Logs                    | `storage/logs/sincro.log` (rotado, 5 MB × 5)        |
| Datos estructurados     | SQL Server — ver [[tabla-referencia]]               |

## Lo que rompe si AFIP cambia la UI

| Archivo              | Zona                                                   |
|----------------------|--------------------------------------------------------|
| `scraper.py:_login`  | Selectores del login                                   |
| `_open_mis_comprobantes` | Buscador del portal ARCA                           |
| `_seleccionar_cuit_representado` | Pantalla "Elegí una persona"               |
| `_descargar_recibidos` | Tab Recibidos + daterangepicker + BUSCAR + Exportar |

Todos los selectores están concentrados en `afip/scraper.py`.

## Ver también

- [[sincroAfip]] — índice del proyecto.
- [[despliegue]] — cómo opera en producción.
- [[migracion]] — DDL y evolución de la tabla.
- [[tabla-referencia]] — columnas y códigos AFIP.
