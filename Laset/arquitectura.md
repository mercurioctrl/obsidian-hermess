# Arquitectura

Ver también: [[Laset]] · [[stack]] · [[operaciones]] · [[troubleshooting]]

## Modelo general
- **Fronts**: apps Nuxt 2 (SSR, `nuxt start`) como procesos **PM2** en el host (no dockerizados).
  Config en `app/.env`, exponen `NODE_PORT`.
- **Backs** en **Docker**, tres sabores:
  - **Phinx/Slim (PHP)**: cobros, expedicion, postventa, comprobantes → `DB_HOST/DB_PORT/DB_USER/DB_PASS`.
  - **Laravel**: compras, pedidos → `DB_HOST/DB_PORT/DB_USERNAME/DB_PASSWORD`.
  - **FastAPI (Python)**: ms-metadata → `.env` (proceso) + `.env.docker` (contenedor).

## Convivencia con la otra empresa (sufijo `laset`)
- Contenedores con sufijo `-laset`, red Docker compartida `laset-net` (única, `external`),
  puertos backs `81xx` / fronts `39xx`, instancias PM2 con sufijo `Laset`.

## Topología / puertos

| Módulo | Front (PM2 / puerto) | Back (contenedor / puerto) |
|---|---|---|
| cobros | WebCashBoxLaset :3901 | cobros-api-rest-laset :8183 (Phinx) |
| compras | WebComprasLaset :3902 | api-rest-compras-apirest-laravel-laset :8196 (Laravel) |
| expedicion | WebExpeditionLaset :3903 | expedition-api-rest-laset :8184 (Phinx) |
| inventario | WebInventarioLaset :3904 | → ms-metadata :8185 *(tentativo)* |
| pedidos | WebPedidosLaset :3905 | api-rest-pedidos-apirest-laravel-laset :8193 (Laravel) |
| postventa | WebAfterSalesLaset :3906 | postventa-api-rest-laset :8182 (Phinx) |
| comprobante-pdf | WebComprobantesPdfLaset :3907 | microservicio-comprobantes-laset :8188 (PHP) |
| — | — | ms-metadata-laset :8185 (FastAPI) |

## Wiring de endpoints
Regla: se conserva el **path** original (`/v1`, `/v2`); solo cambia el host por el destino local.
- **Front → back**: `API_HOST=http://localhost:<puerto-back>/<path>` (el front corre en el host).
- **Back → back** (dentro de `laset-net`): por **nombre de contenedor**, ej.
  pedidos/compras → `API_VOUCHER_URL=http://microservicio-comprobantes-laset/v2`.
  (`localhost` no sirve dentro de un contenedor.)
- Endpoints externos (ms-envios, Jira, static): quedan con los valores del backup.

## Base de datos
Una SQL Server para todos los back: `db-nb-massql-dev.blu.net.ar,4444`, DB `NB_WEB`, user `cmercurio`.
El host está en LAN `10.10.10.0/23`; los IPs privados del `env-backup` (172.31.x, 192.168.0.42)
NO son alcanzables desde acá (son de VPC AWS). Login validado end-to-end.

## Imágenes Docker
El `Dockerfile` PHP no buildea directo (`pecl install sqlsrv` sobre PHP 7.4, requiere ≥8.3).
Solución: reutilizar las imágenes ya construidas del host, re-etiquetadas `*-laset:latest`, y
referenciarlas con `image:` en cada `docker-compose.yml`. El código va por volumen
`./app:/var/www/app`, así que la imagen es solo runtime. Detalle en [[operaciones]].
