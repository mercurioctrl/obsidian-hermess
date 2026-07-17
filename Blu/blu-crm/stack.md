# stack

Tecnologías del CRM. Ver también [[arquitectura]] · [[blu-crm]].

## Backend
- Laravel 11 · PHP 8.3
- Sanctum (auth por tokens) · Horizon (colas) · aws/aws-sdk-php (envío SES)
- MySQL 8 · Redis 7 (cache, sesiones, colas)

## Frontend
- Nuxt 3 (SPA, `ssr:false`) · Vue 3 · Tailwind · Pinia
- `@nuxt/icon` (íconos lucide) + componentes en `components/ui/` (FormField, Modal, DataTable, StatsCard, StatusBadge, Toast)
- Design system replicado del Mini SaaS de BLU (ver [[bluMiniErp/Design Tokens]])

## Microservicio WhatsApp
- Node 20 · whatsapp-web.js + Puppeteer/Chromium · BullMQ (cola `whatsapp-send`) · Express

## Infra
- Docker Compose, 8 servicios: nginx, frontend, backend, horizon, scheduler, whatsapp, db, redis
- Puertos host: 8840 (panel+API), 8831 (QR WhatsApp), 3312 (MySQL)

## Convenciones y gotchas
- Enums en columnas `string` casteadas a PHP enum (patrón BLU)
- `platform.php` fijado a 8.3 en composer (evita que resuelva Symfony 8)
- Frontend: `npm install --legacy-peer-deps` (conflicto @nuxt/icon + @pinia/nuxt)
