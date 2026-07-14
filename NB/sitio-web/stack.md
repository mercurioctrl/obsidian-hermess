# Stack

Ver índice: [[sitio-web]]

## API REST (`sitio-api-rest-v3`)

- **PHP** + **Slim 4** (framework HTTP/routing)
- **PDO sqlsrv** → SQL Server (bases `NB_WEB`, `NewBytes_DBF`, `PRODUCTOS`)
- **Pimple** — contenedor DI
- **robmorgan/phinx** — migraciones
- **firebase/php-jwt** — auth JWT
- **phpmailer/phpmailer** — envío de correos
- **phpoffice/phpspreadsheet** — export Excel/CSV
- **predis/predis** `^1.1` — cliente Redis (cache). Instalado manualmente, no venía en `composer.json` original.
- Integraciones externas: **Producteca**, **MS Envios**, **MercadoPago**.

## Frontend (`sitio-wep-app-v2`)

- **Nuxt.js** `^2.15.8` (SSR, Vue 2)
- **Vue** `^2.6.14`
- **bootstrap-vue** `^2.21.2` — UI
- **@nuxtjs/auth-next** — autenticación
- **vuex-persistedstate** — persistencia de carrito/auth
- **axios** — HTTP hacia la API
- **MercadoPago SDK** — pagos (módulo Nuxt custom)
- Brevo, gtag, metricool — analítica/marketing (client-only)

### Notas de build

- Node 18 requiere `NODE_OPTIONS=--openssl-legacy-provider` (Webpack 4). Ver [[infraestructura]].

## Ver también

- [[arquitectura]] · [[infraestructura]]
