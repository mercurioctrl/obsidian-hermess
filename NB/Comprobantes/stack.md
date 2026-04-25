# Stack

Tecnologías de [[Comprobantes]]. Para cómo encajan entre sí ver [[arquitectura]].

## API — `microservicio-comprobantes-v2`

| Componente       | Valor                                       |
|------------------|---------------------------------------------|
| Lenguaje         | PHP 8.0                                     |
| Framework        | Slim 4                                      |
| Web server       | Apache 2 (mpm_prefork, `libapache2-mod-php8.0`) |
| SO contenedor    | Ubuntu 18.04                                |
| DB de negocio    | **SQL Server** (via `sqlsrv` + `pdo_sqlsrv`) |
| DB local app     | MySQL (solo Phinx, datos no-negocio)        |
| Migraciones      | robmorgan/phinx ^0.12.7                     |
| DI               | pimple/pimple ^3.4                          |
| PSR-7            | slim/psr7 ^1.3                              |
| JWT              | firebase/php-jwt ^5.3                       |
| Logging          | monolog/monolog ^2.2 + panique/pdo-debug    |
| Mail             | phpmailer/phpmailer ^6.6                    |
| Excel            | phpoffice/phpspreadsheet ^1.23              |
| Validación       | cakephp/validation ^4.2                     |
| Números a letras | luecano/numero-a-letras ^3.0                |
| Pagos            | mercadopago/dx-php ^2.4                     |
| Env              | vlucas/phpdotenv ^5.3                       |
| Deploy           | Docker + docker-compose (puerto host 8088)  |

### Servicios externos consumidos

- **Facturu UY** — Emisión de facturas electrónicas Uruguay (`src/Support/FacturuUY.php`)
- **MSCobros / MSExpedicion / MSPostventa** — Otros microservicios internos de NB

## Web app — `servicio-compobante-pdf-web-app`

| Componente       | Valor                                |
|------------------|--------------------------------------|
| Framework        | Nuxt 2.15 (Vue 2 SSR)                |
| HTTP client      | @nuxtjs/axios ^5.13                  |
| PDF              | jspdf ^2.5 + jspdf-autotable ^3.5    |
| QR               | qrcode ^1.5 + vue-qr ^3.2            |
| HTML→canvas      | html2canvas ^1.3 + nuxt-html2canvas-proxy |
| Números          | format-number ^3.0 + conversor-numero-a-letras-es-ar ^1.0 |
| SVG              | @nuxtjs/svg ^0.4                     |
| Env              | @nuxtjs/dotenv ^1.4                  |
| Lint             | ESLint 8 + @nuxtjs/eslint-config/module (autofix en build) |
| Server extra     | Express (montado como serverMiddleware para `/api/generar-pdf/:id/:token`) |
| Deploy           | PM2 (ecosystem.config.js)            |

### Variables de entorno

| Variable   | Ejemplo                    | Uso                                    |
|------------|----------------------------|----------------------------------------|
| APP_HOST   | `http://0.0.0.0`           | Host de la app para construir URL_APP  |
| API_HOST   | `ms-comprobantes.lio.red/` | Base URL del API PHP para axios        |
| API_SSL    | `1`                        | Fuerza `https://` si es 1              |
| NODE_ENV   | `production`               | Modo Nuxt                              |
| PORT       | `3001`                     | Puerto del servidor Nuxt               |

## Ver también

- [[Comprobantes]]
- [[arquitectura]]
- [[contexto]]
