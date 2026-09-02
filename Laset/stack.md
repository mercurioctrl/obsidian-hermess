# Stack

Ver también: [[Laset]] · [[arquitectura]]

## Frontend
- **Nuxt 2** (`^2.15.x`), Vue 2, SSR (`nuxt start`).
- Node **18** en el host → build requiere `NODE_OPTIONS=--openssl-legacy-provider`.
- Gestor de procesos: **PM2** (modo cluster, `instances: 2` por app).
- `comprobante-pdf` usa `nuxt-html2canvas-proxy` → dep nativa `canvas` (libs cairo/pango).

## Backend
- **PHP 8.0 + Slim 4 + Phinx** (cobros, expedicion, postventa, comprobantes). PDO `sqlsrv`.
- **Laravel 9** (compras, pedidos). PDO `sqlsrv`.
- **FastAPI (Python)** + ODBC Driver 17 for SQL Server (ms-metadata).
- Contenedores Docker (Ubuntu 20.04 + Apache + PHP), código por volumen.

## Base de datos
- **SQL Server**: `db-nb-massql-dev.blu.net.ar,4444`, DB `NB_WEB`
  (las queries cruzan también `NewBytes_DBF`, `NEW_BYTES`).

## Servicios externos (no en estas carpetas)
- ms-envios, soporte/Jira (JWT), host de estáticos `static.nb.com.ar`, MercadoLibre, Getnet.
  Quedan con los valores del `env-backup`.

## Infra
- Host `hermess-pc`, LAN `10.10.10.0/23`. Docker + PM2. Red Docker `laset-net`.
- Compartido con el ERP de NB/"blu" (ver [[arquitectura]]).
