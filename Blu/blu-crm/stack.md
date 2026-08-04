# stack

Tecnologías del CRM. Ver también [[arquitectura]] · [[memoria]] · [[blu-crm]].

## Backend
- Laravel 11 · PHP 8.3
- Sanctum (auth por tokens) · Horizon (colas) · aws/aws-sdk-php (SES v2: envío + identidades + config sets)
- MySQL 8 · Redis 7 (cache, sesiones, colas)
- Comando propio: `php artisan ses:provision-tenant <id|slug>` (Config Set + event destination SNS)

## Frontend
- Nuxt 3 (SPA, `ssr:false`) · Vue 3 · Tailwind · Pinia
- `@nuxt/icon` (íconos lucide) + componentes en `components/ui/` (FormField, Modal, DataTable, StatsCard, StatusBadge, Toast)
- Todas las llamadas API por `composables/useApi.ts` (Bearer + 401 -> logout)
- Design system replicado del Mini SaaS de BLU (ver [[bluMiniErp/Design Tokens]])
- Páginas: login, dashboard, plantillas, contactos, listas, campañas, **dominios**

## Microservicio WhatsApp
- Node 20 · whatsapp-web.js + Puppeteer/Chromium · BullMQ (cola `whatsapp-send`) · Express

## Infra
- Docker Compose, 8 servicios: nginx, frontend, backend, horizon, scheduler, whatsapp, db, redis
- Puertos host: 8840 (panel+API), 8831 (QR WhatsApp), 3312 (MySQL)
- nginx: resolver Docker + `proxy_pass` por variable (evita 502 tras recrear contenedores)

## Servicios externos
- **Amazon SES** (cuenta `830204833423`, `us-east-1`): envío + DKIM + Configuration Sets. Eventos por SNS (topic `blucrm-ses-events`) -> webhook.
- Config env-driven: `AWS_*`, `SES_SNS_TOPIC_ARN`, `SES_FAKE` (fake para dev/tests sin AWS).

## Convenciones y gotchas
- Enums en columnas `string` casteadas a PHP enum (patrón BLU)
- `platform.php` fijado a 8.3 en composer (evita que resuelva Symfony 8)
- Frontend: `npm install --legacy-peer-deps` (conflicto @nuxt/icon + @pinia/nuxt)
- Código *baked* en la imagen (rebuild para aplicar cambios); imagen prod sin dev-deps (ver [[memoria]])

## Documentación (repo)
- `docs/ARCHITECTURE.md`, `docs/DEPLOYMENT.md`, `docs/DEVELOPMENT.md`, `docs/DATA_MODEL.md`
