# arquitectura

Diseño del CRM multi-tenant de BLU. Ver también [[stack]] · [[contexto]] · [[memoria]] · [[blu-crm]].

## Idea central

Los dos pilares (email y WhatsApp) son, en el fondo, **sistemas de colas asíncronas con workers**. El 90% del valor no es *enviar*, sino **saber cuándo NO enviar** (el "escudo" de reputación).

## Multi-tenancy

- DB compartida MySQL con `tenant_id` en todas las tablas de negocio (correcto para ~10 clientes).
- **Sin global scope ni paquete de tenancy**: el aislamiento es manual y explícito (cada query filtra `->where('tenant_id', ...)`). Verificado por tests: un cliente no ve datos de otro (404).
- Aislamiento de reputación de email: dominio propio por cliente + Configuration Set por tenant + auto-pause por tenant.

## Servicios Docker

nginx (proxy `/api`->backend, resto->frontend) · frontend (Nuxt) · backend (Laravel API) · horizon (worker de colas — TODO el envío pasa por acá) · scheduler · whatsapp (Node, 1 sesión/tenant) · db (MySQL) · redis.

## Pilar EMAIL (Amazon SES) — COMPLETO y probado con SES real

**Por qué SES:** el más barato a escala (~$100/mes por 1M correos vs ~$600 Mailgun). Trae el circuito de rebotes por SNS de fábrica; encima se construye suppression + auto-pause.

### Dominios de envío + verificación DKIM
- El trato con SES está detrás de interfaces mockeables (`app/Services/Ses/Contracts/`): `SesIdentityManager` (verificar dominios, Easy DKIM) y `SesConfigurationSetManager` (provisión de config sets). Dos impls cada una: real (SDK SES v2) y fake determinista.
- El binding en `AppServiceProvider` elige según el flag **`SES_FAKE`** (`true` = sin llamadas a AWS: dev local y tests sin credenciales).
- Flujo: panel **Dominios** (o `POST /api/sending-domains`) -> `CreateEmailIdentity` -> guarda 3 tokens DKIM -> el resource expone 3 CNAME + TXT DMARC -> el cliente los publica en su DNS -> `POST .../verify` (`GetEmailIdentity`) -> `verified`. Funciona **desde local** (llamada saliente).
- Config Set por tenant: `php artisan ses:provision-tenant <id|slug>` crea el set + event destination (Bounce/Complaint/Delivery) -> topic SNS. Idempotente.

### Flujo de envío (DDD: Request -> Controller -> Service -> Job)
1. `SendCampaignService` (pre-flight): resuelve audiencia (lista o todos) -> filtra consentimiento -> cruza suppression list -> crea `email_messages` (queued) -> despacha jobs con delay (`throttle_per_minute`).
2. `SendCampaignEmail` (Job en Horizon): envía por SES con header `X-SES-CONFIGURATION-SET` del tenant + headers `List-Unsubscribe`/`List-Unsubscribe-Post` (URL firmada por contacto), guarda `provider_message_id`, suma `sent_count` + `sending_stats.sent`.

### Flujo de rebotes (el escudo)
1. SNS -> `SesWebhookController` (valida firma) -> `ProcessSesNotification`.
2. Dedup por `webhook_events.sns_message_id` -> ubica el `email_message` por `provider_message_id`.
3. Hard bounce / queja -> marca el mensaje + inserta en `suppressions` (bloquea al contacto).
4. Suma `sending_stats` -> evalúa auto-pause: si queja > 0.08% o rebote > 4% (ventana 7 días, mín. 100 envíos) -> pausa al tenant ANTES de que AWS suspenda la cuenta.
- El webhook necesita **URL pública** (SNS no llega a localhost). En dev: ngrok + `SES_VERIFY_SNS_SIGNATURE=false`.

### Baja / List-Unsubscribe
- Cada email lleva `List-Unsubscribe` + `List-Unsubscribe-Post: One-Click` (RFC 8058) con URL firmada (`URL::signedRoute`, usa `APP_URL`). Endpoint público con middleware `signed`: `POST /api/unsubscribe/{contact}` (one-click) y `GET` (página de confirmación). `UnsubscribeService` marca consentimiento + suppression + `consents`. Merge tag `{{unsubscribe_url}}` para link visible.

**Listas** = segmentos estáticos (`segments` + pivote `contact_segment`). Un contacto puede estar en varias. La campaña apunta a una lista o a todos los suscritos. (Ojo: el pivote tiene columna `id` propia -> la audiencia debe seleccionar `contacts.*`.)

## Pilar WHATSAPP (whatsapp-web.js) — PENDIENTE de cablear

- Microservicio Node separado (Puppeteer necesita Chromium vivo, incompatible con el modelo request/response de PHP).
- 1 sesión por tenant, LocalAuth persistido en volumen. Endpoints: start / QR / status / send.
- Cola `whatsapp-send` (BullMQ) con delay aleatorio anti-ban; reporta `ack` (enviado/entregado/leído) a Laravel por webhook.
- El esquema de datos ya existe; falta cablear la cola end-to-end + QR + pantallas.

## Modelo de datos (16 tablas)

tenants, users, sending_domains, contacts, consents, segments, contact_segment, suppressions, email_templates, campaigns, email_messages, email_events, whatsapp_sessions, whatsapp_campaigns, whatsapp_messages, imports, sending_stats, webhook_events. (Detalle completo en `docs/DATA_MODEL.md` del repo.)

- **Corazón:** `email_messages` (1 fila por destinatario, cruza con SNS).
- **Escudo:** `suppressions` (unique `tenant_id + channel + value`, lookup instantáneo en pre-flight).

## Decisiones y por qué

- **Servicios externos detrás de interfaz mockeable** (patrón `SesIdentityManager` + fake, flag `SES_FAKE`): hace todo testeable sin la dependencia real. Repetir para cualquier integración nueva.
- Enums como `string` en DB + cast PHP (convención BLU; evita ALTER de enums en MySQL).
- Columna JSON de contacto renombrada `attributes` -> `custom_attributes` (choca con `$attributes` de Eloquent).
- Panel Nuxt SPA (`ssr:false`) con el design system del Mini SaaS de BLU.
- **nginx sin `upstream`**: usa resolver de Docker (`127.0.0.11`) + `proxy_pass` por variable -> resuelve la IP por request y evita el 502 tras recrear contenedores.
- Todo AWS es **env-driven** (creds + topic + `SES_FAKE`) para replicar la instancia por cliente cambiando solo el `.env`.
