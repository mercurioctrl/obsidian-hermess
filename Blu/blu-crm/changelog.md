# changelog

## 2026-08-03/04

Cierre del pilar EMAIL con SES **real** + repo en GitHub + docs para devs.

**Dominios de envío + verificación DKIM (lo que estaba pendiente)**
- Trato con SES detrás de interfaces mockeables (`SesIdentityManager`, `SesConfigurationSetManager`), impl real (SDK SES v2) y fake determinista, elegidas por el flag `SES_FAKE`.
- `SendingDomainController` a CRUD + acción `verify`; `SendingDomainResource` expone los 3 CNAME de DKIM + TXT DMARC. Página `pages/dominios/` en el panel.
- Comando `php artisan ses:provision-tenant <id|slug>`: crea el Configuration Set + event destination (Bounce/Complaint/Delivery) -> topic SNS. Idempotente.

**List-Unsubscribe + baja (lo que estaba pendiente)**
- Headers `List-Unsubscribe` + `List-Unsubscribe-Post: One-Click` (RFC 8058) con URL firmada por contacto. Endpoint público firmado `GET/POST /api/unsubscribe/{contact}`. `UnsubscribeService` -> consentimiento + suppression + consents. Merge tag `{{unsubscribe_url}}`.

**AWS conectado y probado end-to-end (real)**
- Creds IAM en `.env`, `SES_FAKE=false`. Dominio `send.blustudioinc.com` verificado (DKIM SUCCESS, DNS en Cloudflare).
- Config Set del tenant demo provisionado contra SES real.
- **Envío real entregado** a un destinatario verificado (sandbox) desde `send.blustudioinc.com`, firmado con DKIM + List-Unsubscribe.

**Bugs corregidos**
- Audiencia por segmento insertaba el id del pivote como `contact_id` (colisión de columna `id` en el `belongsToMany`) -> `->select('contacts.*')` + test de regresión.
- 502 de nginx tras recrear contenedores: `upstream` cacheaba la IP -> resolver de Docker (`127.0.0.11`) + `proxy_pass` por variable (resuelve por request).

**Repo y documentación**
- Repo en GitHub: `git@github.com:BluIncStudio/blu-crm.git` (privado, `main`).
- Docs para devs en `docs/`: `ARCHITECTURE.md`, `DEPLOYMENT.md`, `DEVELOPMENT.md` (+ `DATA_MODEL.md`).
- La config de AWS es de uso del owner: no se documenta en el repo. `.claude/CLAUDE.md` destrackeado (uso interno).

Archivos clave: `backend/app/Services/Ses/`, `backend/app/Console/Commands/ProvisionTenantSes.php`, `backend/app/Http/Controllers/{SendingDomain,Unsubscribe}Controller.php`, `frontend/pages/dominios/`, `nginx/default.conf`, `docs/`.

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
