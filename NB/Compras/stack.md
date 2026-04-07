# Stack tecnológico

## API

| Tecnología | Versión | Uso |
|------------|---------|-----|
| PHP | 8.1 | Runtime |
| Laravel | 9.x | Framework |
| SQL Server | — | Base de datos (externa) |
| FreeTDS / pdo_dblib | — | Driver de conexión a SQL Server |
| firebase/php-jwt | 6.x | Tokens JWT para autenticación |
| Guzzle | 7.x | Cliente HTTP para APIs externas |
| PHPUnit | 9.x | Tests |
| Laravel Pint | 1.x | Linting/formato PHP |

### Infraestructura API

- **Docker:** Ubuntu 22.04 + Apache + PHP 8.1 (mod_php)
- **Puerto:** 8096 → 80
- **Crontab:** Configurado en el contenedor (`docker/crontab`)

## Frontend

| Tecnología | Versión | Uso |
|------------|---------|-----|
| Nuxt | 2.15.x | Framework SSR/SPA |
| Vue | 2.6.x | UI reactiva |
| Ant Design Vue | 1.7.x | Componentes UI |
| Vuex | — | Estado global (via Nuxt) |
| Axios | — | HTTP client (`@nuxtjs/axios`) |
| `@nuxtjs/auth-next` | 5.x | Autenticación |
| VeeValidate | 3.x | Validación de formularios |
| Chart.js + vue-chartjs | 3.x / 4.x | Gráficos en dashboard |
| Less | 4.x | Preprocesador CSS |
| ESLint + Prettier + Stylelint | — | Linting |
| PM2 | — | Process manager en producción |

### Variables de entorno clave

**API** (`.env`):
- `DB_CONNECTION=sqlsrv` — Conexión a SQL Server
- `BASE_PATH=/v1` — Prefijo de rutas API
- `JWT_SIGNATURE_KEY` — Clave para firmar tokens
- `API_VOUCHER_URL` — MS Comprobantes
- `API_MSENVIO_URL` — MS Envíos
- `STATIC_URL` — URL de imágenes estáticas

**Frontend** (`.env`):
- `API_HOST` — URL de la API
- `NODE_PORT` — Puerto del dev server (default 3002)
- `COMPROBANTES` — URL del servicio de comprobantes
- `SUPPORT` — URL del servicio de soporte
- `JWT_SUPPORT_JIRA` — Token para integración Jira

## Servicios externos

- **MS Comprobantes** (`API_VOUCHER_URL`) — Generación de comprobantes fiscales
- **MS Envíos** (`API_MSENVIO_URL`) — Gestión de envíos
- **API Posiciones Arancelarias** — Búsqueda externa de posiciones (endpoint `tariffPositionExternal`)
- **Jira** — Integración de soporte desde el frontend (`plugins/apiJira.client.js`)
- **Imágenes estáticas** (`STATIC_URL`) — CDN de imágenes de productos

## Ver también

- [[arquitectura|Arquitectura]]
- [[changelog|Changelog]]
