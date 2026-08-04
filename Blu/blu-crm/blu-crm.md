# blu-crm

CRM multi-tenant de BLU con dos pilares: **email masivo (Amazon SES)** y **WhatsApp (whatsapp-web.js / Puppeteer)**. Pensado para ~10 clientes enviando ~100k correos/mes cada uno.

## Notas del proyecto

- [[arquitectura]] — Diseño: multi-tenancy, los dos pilares, dominios/DKIM, servicios Docker, flujos
- [[stack]] — Tecnologías, versiones, puertos, dependencias clave, servicios externos
- [[changelog]] — Registro de lo trabajado
- [[contexto]] — Reglas de negocio, decisiones, datos AWS y pendientes
- [[memoria]] — Memoria operativa (gotchas de build/operación, credenciales demo)

## Estado (2026-08-04)

- Infraestructura Docker (8 servicios) — puertos 8840 / 8831 / 3312
- Base de datos (16 tablas de dominio) + modelos Eloquent + enums
- **Pilar EMAIL COMPLETO y probado con SES real:** plantillas, contactos, listas, campañas, envío por SES, dominios + verificación DKIM, provisión de config sets por tenant (`ses:provision-tenant`), webhook rebotes -> suppression -> auto-pause, List-Unsubscribe + baja. Envío real entregado desde `send.blustudioinc.com`.
- Panel web (Nuxt 3) con el design system de BLU (incluye módulo Dominios)
- Repo en GitHub `BluIncStudio/blu-crm` (privado) + docs para devs en `docs/`
- **Pendiente:** salir del sandbox SES + suscribir webhook SNS con URL pública (deploy); pilar WhatsApp end-to-end

## Acceso

- Repo local: `/var/www/blu/blu-crm` · GitHub: `git@github.com:BluIncStudio/blu-crm.git`
- Panel: http://localhost:8840 — login demo `admin@blu.test` / `password`

Última sincronización: 2026-08-04
