# changelog

## 2026-07-17

Construcción inicial completa del CRM.

**Infraestructura**
- Stack Docker de 8 servicios (esquema de blus sas + `horizon` para colas + microservicio `whatsapp` Node/Chromium)
- `start.sh`/`stop.sh`, nginx, puertos 8840 / 8831 / 3312

**Base de datos y dominio**
- 16 tablas de dominio + 17 modelos Eloquent + 17 enums (relaciones, scopes y helpers verificados contra la BD)

**Pilar email (Amazon SES)**
- Envío de campañas: pre-flight (consentimiento + suppression) -> cola Horizon -> Job SES con throttling
- Webhook SNS/SES (`/api/webhooks/ses`): rebote/queja -> suppression -> auto-pause por tenant
- CRUD de plantillas, contactos (con importación + higiene), listas (segmentos), campañas
- Auth (login/logout/me con Sanctum)

**Panel web (Nuxt 3)**
- Login, dashboard, plantillas, contactos, listas, campañas
- Rediseñado al design system de BLU (tema claro, componentes `ui/`, íconos lucide)

Archivos clave: `backend/app/Http/Controllers/`, `backend/app/Services/`, `frontend/pages/`, `docker-compose.yml`
