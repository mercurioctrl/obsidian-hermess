# arquitectura

Diseño del CRM multi-tenant de BLU. Ver también [[stack]] · [[contexto]] · [[blu-crm]].

## Idea central

Los dos pilares (email y WhatsApp) son, en el fondo, **sistemas de colas asíncronas con workers**. El 90% del valor no es *enviar*, sino **saber cuándo NO enviar** (el "escudo" de reputación).

## Multi-tenancy

- DB compartida MySQL con `tenant_id` en todas las tablas de negocio (correcto para ~10 clientes).
- Aislamiento verificado en cada módulo: un cliente no ve ni usa datos de otro (scoping por tenant; 404/422).
- Aislamiento de reputación de email: dominio propio por cliente + auto-pause por tenant.

## Servicios Docker

nginx (proxy `/api`->backend, resto->frontend) · frontend (Nuxt) · backend (Laravel API) · horizon (worker de colas — TODO el envío pasa por acá) · scheduler · whatsapp (Node, 1 sesión/tenant) · db (MySQL) · redis.

## Pilar EMAIL (Amazon SES)

**Por qué SES:** el más barato a escala (~$100/mes por 1M correos vs ~$600 Mailgun). Trae el circuito de rebotes por SNS de fábrica; encima se construye suppression + auto-pause.

**Flujo de envío** (DDD: Request -> Controller -> Service -> Job):
1. `SendCampaignService` (pre-flight): resuelve audiencia (lista o todos) -> filtra consentimiento -> cruza suppression list -> crea `email_messages` (queued) -> despacha jobs con delay (`throttle_per_minute`).
2. `SendCampaignEmail` (Job en Horizon): envía por SES con header `X-SES-CONFIGURATION-SET` del tenant, guarda `provider_message_id`, suma `sent_count` + `sending_stats.sent`.

**Flujo de rebotes** (el escudo):
1. SNS -> `SesWebhookController` (valida firma) -> `ProcessSesNotification`.
2. Dedup por `webhook_events.sns_message_id` -> ubica el `email_message` por `provider_message_id`.
3. Hard bounce / queja -> marca el mensaje + inserta en `suppressions` (bloquea al contacto).
4. Suma `sending_stats` -> evalúa auto-pause: si queja > 0.08% o rebote > 4% (ventana 7 días, mín. 100 envíos) -> pausa al tenant ANTES de que AWS suspenda la cuenta.

El círculo cierra: el `provider_message_id` que captura el envío es el que usa el webhook para encontrar el mensaje al rebotar.

**Listas** = segmentos estáticos (`segments` + pivote `contact_segment`). Un contacto puede estar en varias. La campaña apunta a una lista o a todos los suscritos.

## Pilar WHATSAPP (whatsapp-web.js)

- Microservicio Node separado (Puppeteer necesita Chromium vivo, incompatible con el modelo request/response de PHP).
- 1 sesión por tenant, LocalAuth persistido en volumen. Endpoints: start / QR / status / send.
- Cola `whatsapp-send` (BullMQ) con delay aleatorio anti-ban; reporta `ack` (enviado/entregado/leído) a Laravel por webhook.
- Bajo volumen (cientos/mes por cliente): Puppeteer alcanza. Volumen alto requeriría la WhatsApp Cloud API oficial.

## Modelo de datos (16 tablas)

tenants, users, sending_domains, contacts, consents, segments, contact_segment, suppressions, email_templates, campaigns, email_messages, email_events, whatsapp_sessions, whatsapp_campaigns, whatsapp_messages, imports, sending_stats, webhook_events. (Detalle completo en `docs/DATA_MODEL.md` del repo.)

- **Corazón:** `email_messages` (1 fila por destinatario, cruza con SNS).
- **Escudo:** `suppressions` (unique `tenant_id + channel + value`, lookup instantáneo en pre-flight).

## Decisiones y por qué

- Enums como `string` en DB + cast PHP (convención BLU; evita ALTER de enums en MySQL).
- Columna JSON de contacto renombrada `attributes` -> `custom_attributes` (choca con `$attributes` de Eloquent).
- Panel Nuxt SPA (`ssr:false`) con el design system del Mini SaaS de BLU.
