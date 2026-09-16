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

## Acceso: dominio único + SSO (2026-09-15)

Las apps ya no se usan por su puerto: se sirven desde **`http://laset.local`**, cada una bajo su
path (`router.base`) detrás de un reverse proxy Apache. Al compartir origen comparten la sesión de
`auth-next`; los 6 backs comparten la clave de firma del JWT, así que el token vale en todos.

| Path | App | Puerto | Back |
|---|---|---|---|
| `/pedidos` | Pedidos | 3905 | :8193 |
| `/inventario` | Inventario | 3904 | :8185 |
| `/compras` | Compras | 3902 | :8196 |
| `/cobros` | Cobros | 3901 | :8183 |
| `/expedicion` | Expedición | 3903 | :8184 |
| `/postventa` | Postventa | 3906 | :8182 |
| `/comprobantes` | Comprobantes PDF | 3907 | :8188 |

`/` redirige a `/inventario/`. Comprobantes no tiene login ni header: queda fuera del menú.

**Tres reglas que no se pueden romper:**
1. `build.publicPath` **relativo** (`'_nuxt/'`). Nuxt 2 le prepende `router.base`; uno absoluto
   monta en `/pedidos/pedidos/_nuxt/` y todos los assets dan 404. El SSR igual pinta el HTML, así
   que la app *parece* andar pero nunca hidrata.
2. Los middlewares de permisos **releen el usuario de la base por `UserId`**, nunca del payload del
   token. Cada back mete su propia forma de usuario en el JWT; leer del payload hace que el back
   devuelva 401 con tokens ajenos, y ese 401 borra la sesión de **todo** el ERP.
3. Todos los backs firman con `md5(JWT_SIGNATURE_KEY)` HS256. `ms-metadata` (PyJWT) además necesita
   `options={"verify_aud": False}`, porque los PHP usan `aud` como huella de navegador.

El menú entre apps es `components/AppSwitcher.vue`, **duplicado en los 6 fronts** (el monorepo no
tiene paquete compartido: si se cambia, hay que cambiarlo en los 6).

El vhost (`/etc/apache2/sites-available/laset.local.conf`) **no está versionado**: vive solo en el host.

Detalle completo en `docs/dominio-unico-sso.md` del repo. Síntomas en [[troubleshooting]].

## Precios: listas de color (Laset, 2026-09-11)

Laset no usa el esquema npvp/ntarifapp heredado de NB. Usa **4 listas de color**, cada una
`base × (1 + % propio)`:

- Tablas: `LASET_LISTA_COLOR` (las 4 listas y su % global), `LASET_LISTA_COLOR_ARTICULO` (override
  de % **o** precio por artículo), `LASET_CLIENTE_LISTA_COLOR` (lista por defecto de cada cliente).
- Config desde **inventario** → ms-metadata (`/colorLists`, `/items/{id}/colorPrices`).
- Aplicación por cliente en **pedidos**: el precio sale de la lista del cliente, con override
  editable en el modal de la orden.
- En la grilla de Precios cada columna muestra **precio y %**, los dos editables y sincronizados:
  el % de un precio manual es *derivado del costo*, no persistido.
- Todo scopeado a `companyCode 11`.

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
