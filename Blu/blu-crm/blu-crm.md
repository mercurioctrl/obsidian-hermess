# blu-crm

CRM multi-tenant de BLU con dos pilares: **email masivo (Amazon SES)** y **WhatsApp (whatsapp-web.js / Puppeteer)**. Pensado para ~10 clientes enviando ~100k correos/mes cada uno.

## Notas del proyecto

- [[arquitectura]] — Diseño: multi-tenancy, los dos pilares, servicios Docker, flujos
- [[stack]] — Tecnologías, versiones, puertos, dependencias clave
- [[changelog]] — Registro de lo trabajado
- [[contexto]] — Reglas de negocio, decisiones y pendientes
- [[memoria]] — Memoria operativa del proyecto (gotchas, credenciales demo)

## Estado (2026-07-17)

- Infraestructura Docker (8 servicios) — puertos 8840 / 8831 / 3312
- Base de datos (16 tablas de dominio) + 17 modelos Eloquent + 17 enums
- Pilar EMAIL completo: plantillas, contactos, listas, campañas, envío por SES, webhook rebotes -> suppression -> auto-pause
- Panel web (Nuxt 3) con el design system de BLU
- Pendiente: dominios + verificación SES (creds AWS); pilar WhatsApp end-to-end

## Acceso

- Repo local: `/var/www/blu/blu-crm`
- Panel: http://localhost:8840 — login demo `admin@blu.test` / `password`

Última sincronización: 2026-07-17
