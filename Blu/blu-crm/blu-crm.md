# blu-crm

CRM multi-tenant de BLU con dos pilares: **email masivo (Amazon SES)** y **WhatsApp (whatsapp-web.js / Puppeteer)**. Pensado para ~10 clientes enviando ~100k correos/mes cada uno.

## Estado (2026-07)

- ✅ Infraestructura Docker (8 servicios: nginx, frontend, backend, horizon, scheduler, whatsapp, db, redis) — puertos 8840 / 8831 / 3312
- ✅ Base de datos (16 tablas) + modelos Eloquent + enums
- ✅ Pilar EMAIL completo: plantillas, contactos, listas, campañas, envío por SES, webhook de rebotes → suppression → auto-pause
- ✅ Panel web (Nuxt 3) con el design system de BLU (mini-saas)
- ⬜ Dominios + verificación SES (DKIM/SPF) — necesita credenciales AWS
- ⬜ Pilar WhatsApp end-to-end (QR + envío) + pantallas

## Stack

Laravel 11 (PHP 8.3) · Nuxt 3 · MySQL 8 · Redis + Horizon · Amazon SES · whatsapp-web.js · Docker

## Notas

- Repo local: `/var/www/blu/blu-crm`
- Login demo del panel: `admin@blu.test` / `password`
- Aislamiento de reputación: dominio propio por cliente + auto-pause (queja > 0.08% o rebote > 4%)
