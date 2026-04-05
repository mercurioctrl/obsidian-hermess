# Stack e Infraestructura

## Backend

| Tecnología | Versión | Uso |
|-----------|---------|-----|
| Laravel | ^9.19 | Framework PHP |
| PHP | ^8.0.2 (Docker: 8.1) | Runtime |
| SQL Server | ODBC 17/18 | Base de datos principal |
| Laravel Sanctum | ^3.0 | Autenticación JWT |
| Guzzle | ^7.8 | HTTP client para APIs externas |
| maatwebsite/excel | ^3.1 | Exports Excel |
| PHPMailer | ^6.9 | Envío de emails |
| firebase/php-jwt | ^6.8 | JWT tokens |
| Laravel Pint | dev | Code style |

### Docker

- **Base:** Ubuntu 22.04
- **Web server:** Apache 2 (mpm_prefork)
- **PHP extensions:** mysql, zip, gd, mbstring, curl, xml, bcmath, sybase, sqlsrv, pdo_sqlsrv
- **ODBC:** unixodbc + Microsoft SQL Server drivers 17/18
- **TLS:** 1.0 habilitado para compatibilidad con SQL Server legacy
- **Cron:** Rotación y limpieza de logs diaria

## Frontend

| Tecnología | Versión | Uso |
|-----------|---------|-----|
| Nuxt.js | ^2.15.8 | Framework SSR/SPA |
| Vue.js | ^2.6.14 | UI framework |
| Ant Design Vue | ^1.7.8 | Componentes UI |
| @nuxtjs/auth-next | 5.0.0-* | Autenticación |
| @nuxtjs/axios | ^5.13.6 | HTTP client |
| @nuxtjs/pwa | ^3.3.5 | Progressive Web App |
| chart.js | ^3.8.0 | Gráficos en dashboards |
| Firebase | ^10.13.1 | Push notifications |
| vee-validate | ^3.4.14 | Validación de formularios |
| jspdf | ^3.0.1 | Generación de PDFs |
| v-mask | ^2.3.0 | Máscaras de input |
| webpack | ^4.46.0 | Bundler |
| LESS | ^4.1.3 | Preprocesador CSS |
| Moment.js | (via @nuxtjs/moment) | Fechas, locale español |

### Nota: Node.js

Con Node v17+ se requiere `NODE_OPTIONS=--openssl-legacy-provider` porque webpack 4 usa `createHash('md4')` que fue removido en OpenSSL 3.

## Integraciones externas

| Servicio | Uso | Config env |
|----------|-----|------------|
| ms-comprobantes | Facturación/comprobantes | `API_VOUCHER_URL` / `COMPROBANTES` |
| ms-envios | Cotización y gestión de envíos | `API_MSENVIO_URL` / `ENVIOS` |
| BCRA | Consulta deudas en banco central | BcraApiExternal |
| Firebase | Push notifications | `FIREBASE_*` vars |
| Jira | Ticketing de soporte | `JWT_SUPPORT_JIRA` |
| Mercado Libre | Sync productos/precios | MercadoLibreService |
| Mercado Pago | Gateway de pagos | MercadoPagoModal |

## Deploy

- **Backend:** Docker Compose → container `api-rest-pedidos-apirest-laravel` (8093:80)
- **Frontend:** PM2 (scripts en `start-example.sh` / `stop-example.sh`)
- **CI/CD:** GitHub Actions, branch `gamma`, deploy via SSH con `deployPedidos.sh`
- **DB:** SQL Server externo (no en Docker)

## Ver también

- [[arquitectura]] — Patrones y estructura
- [[contexto]] — Gotchas técnicos
