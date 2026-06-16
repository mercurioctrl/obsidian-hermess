# Contexto — inventario

Información de entorno local, variables de entorno y gotchas del proyecto.

## Entorno local

### Mac (hermess) — `/Users/hermess/www/inventario/`

```bash
# Backend — OPENSSL_CONF es OBLIGATORIO (ver gotchas: TLS 1.0)
cd ms-metadata
OPENSSL_CONF=$PWD/openssl_legacy.cnf .venv/bin/uvicorn main:app --reload --port 8081 --host 0.0.0.0

# Frontend
cd inventario-web-app/app
npm run dev   # http://localhost:3000 — API_HOST=http://0.0.0.0:8081
```

- Venv del backend: `.venv` (Python 3.9), todas las deps instaladas
- Ambos repos en rama `catri-fine-tuning` (2026-06-11)

### Linux (/var/www/nb/inventario) — setup anterior

```bash
cd ms-metadata && uvicorn main:app --host 0.0.0.0 --port 8000 --reload
cd inventario-web-app/app && npm run dev
```

- **Swagger UI**: http://localhost:{puerto}/docs

## Variables de entorno

### ms-metadata/.env

```
DB_DRIVER=ODBC Driver 18 for SQL Server
DB_SERVER=190.210.23.97,4444        # formato host,puerto (no DB_HOST/DB_PORT)
DB_NAME=NB_WEB
DB_USER=web                          # (antes emanzando_devweb01)
DB_PASS=...                          # la variable es DB_PASS, no DB_PASSWORD
ALLOWED_ORIGINS=http://localhost:3000,...
OPENAI_API_KEY=...                   # placeholder alcanza para levantar; real para IA
STATIC_URL=https://static.nb.com.ar/ # sin esto revienta models.py con productos con foto
```

### inventario-web-app/app/.env

```
API_HOST=http://0.0.0.0:8081   # (en linux era :8000)
NODE_PORT=3000
NODE_ENV=development
```

## Gotchas conocidos

| Problema | Causa | Solución |
|----------|-------|---------|
| **`npm install <pkg>` con el dev server corriendo → RuntimeError / loader infinito** (ej. al instalar `xlsx`) | Instalar deps mientras `npm run dev` corre deja webpack/HMR con estado inconsistente | **Reiniciar `npm run dev`** después de instalar; en el browser hard-reload |
| **Grilla de Precios tardaba ~4.4s** | NO era `get_items_prices` (0.08s) sino la query principal `get_items_stocks` (~3.8s) con ~10 subqueries correlacionadas que Precios no muestra | **Resuelto (2026-06-15)**: path liviano `get_items_prices_grid` con `pricesView=1` (~0.9s) + count `COUNT(DISTINCT)` + paralelo. ~5s → ~1,5s. Stock intacto |
| **El `<th>` con checkbox de header queda vacío** (slot de title no renderiza) | Ant 1.x solo aplica `slots.title` si `column.title === undefined` (`lib/table/index.js`); un `title:""` lo bloquea | NO poner `title` en la columna (que quede undefined) y usar `slots: { title: '<slot>' }` |
| **Celdas editables: cambio de UX** | `EditablePriceCell` ahora muestra texto y monta el input de Ant solo al click (perf: evita miles de inputs) | Se clickea la celda para editar; no hay tab entre celdas. Es a propósito |
| **Tiempos altos/variables del SQL Server** | `190.210.23.97` es un server remoto compartido; la misma query va de 0.3s a 4s según carga | No es del código; comparar mejoras siempre en runs relativos |
| **`ULTIMA_COMPRA` no existe** en `articulo` | Solo existe en `clientes`; para artículo la fecha de ingreso es `ULTIMO_INGRESO` | Usar `articulo.ULTIMO_INGRESO` (y `ULTIMA_VENTA`) |
| **pyodbc 08001 "TCP Provider: 10054"** en todo endpoint con DB, aunque TCP y ping al server andan (parece firewall/VPN, NO lo es) | El SQL Server de prod solo habla **TLS 1.0** y OpenSSL 3.x lo rechaza por defecto (ambos drivers ODBC 17/18, con o sin `Encrypt`) | Levantar uvicorn con `OPENSSL_CONF=openssl_legacy.cnf` (commiteado en el repo: `MinProtocol=TLSv1`, `SECLEVEL=0`) |
| **Filas desalineadas** con columna fija en tablas antd 1.x | `fixed:'left'` clona la tabla en un overlay y sincroniza alturas por JS — siempre se desfasa | CSS `position:sticky` + fondos opacos por estado (misma tabla ⇒ alineación perfecta). Ver `pages/itemsPrices.vue` |
| **Cabeceras corridas** con header fijo (`scroll.y`) | Header y body son tablas separadas; con `scroll.x:'max-content'` cada una calcula anchos distintos | `scroll.x` numérico (suma de anchos visibles) + `table-layout:fixed; min-width:100%` en ambas |
| Item no aparece al deep-linkear a Productos | La query default de la pestaña lleva `noImage=1` y `stock=1`, que FILTRAN | Omitir ambos en deep-links; buscar por ID numérico (`ID_ARTICULO` via LIKE) |
| **Cabeceras se ven "por dentro" de la columna Título** al scrollear | El `<th>` sticky no recibe la CSS class confiable en la tabla de header separada de antd | Estilo **inline** vía `customHeaderCell` (fondo opaco + z-index). Sombra sutil (`2px/5%`) |
| `fetchCompetition` crashea en SSR (`Not authenticated` / token sync) | Dispatch fire-and-forget durante SSR pierde el contexto req/res de auth | Guardar con `process.client` antes de despachar |
| Servidor backend crashea al iniciar | `ALLOWED_ORIGINS` no definido (`.split(",")` sin default) | Asegurarse de que la variable esté en `.env` |
| `.env` original tenía nombres incorrectos | El código espera `DB_SERVER`, `DB_PASS`, `DB_DRIVER` (no `DB_HOST`, `DB_PASSWORD`, `DB_TYPE`) | Copiar `.env_example` y completar con los nombres correctos |
| `FastAPIDeprecationWarning: regex has been deprecated` | `main.py` usa parámetro `regex` deprecado | No rompe nada, es un warning |
| `Cannot find module ../build-version.json` al iniciar dev | Lo genera `scripts/update-build-version.js` solo al hacer `npm run build` | No rompe nada en dev |
| 401 al iniciar el frontend | El middleware `auth` redirige todas las rutas a `/login` si no hay token | Comportamiento normal |

## Deploy a producción

La feature de competencia **no agrega variables `.env`** (la URL de partpicker está
hardcodeada en `competition.py`). Checklist al pasar a prod:

1. **Salida HTTPS a `partpicker.blustudioinc.com`** desde el server — si el egress
   está bloqueado, `/itemsCompetition` da 500 y la grilla degrada a "-".
2. **`requests` instalado** en el Python de prod (los scrapers ya lo usan).
3. **Permiso de escritura en `NewBytes_DBF.dbo.scrap_hg`** para el usuario de DB
   (el "Guardar y rematchear" hace UPDATE/INSERT — misma tabla del scraper hardgamers).
4. **`OPENSSL_CONF` NO hace falta en prod** (solo es workaround de dev local con
   OpenSSL 3.x — ver gotcha TLS arriba).
5. Primera llamada a `/itemsCompetition` tras cada reinicio: ~30s (warm-up del
   catálogo); instantánea después, refresca sola cada 30 min.

## Reglas de negocio relevantes

- **Precios**: al fijar un precio a mano, la utilidad derivada se aplica SIEMPRE
  a la primera del par (PL1/MAY1/LO1/PML); la segunda queda fija. Ver [[modulo-precios]].
- **Mayoristas se comparan sin IVA** (campo `precio_sin_iva` de partpicker) contra
  los precios USD propios; resellers en ARS final como referencia de clientes.
- `scrap_hg.search_keys` es compartida entre la sección Precios y el scraper de
  hardgamers — editar keywords afecta a ambos.
- Pendiente de decisión: si `libre-opcion` (canal propio) debe excluirse del
  bloque de resellers en competencia.

## Ver también

- [[inventario]] · [[arquitectura]] · [[stack]] · [[modulo-precios]]
