# contexto

Contexto de negocio, decisiones y pendientes. Ver [[arquitectura]] · [[memoria]] · [[blu-crm]].

## Objetivo

Producto CRM para ~10 clientes de BLU. Cada uno envía ~100k correos/mes (≈1M/mes total) + WhatsApp de bajo volumen.

## Decisiones tomadas

- **Proveedor de email: Amazon SES** (vs Mailgun ~$600/mes o Postmark, inviable para bulk). SES ~$100/mes a 1M. Se descartó SMTP propio (IP virgen, warm-up, blacklists, mantenimiento eterno).
- **Aislamiento de reputación:** cada cliente con su dominio + configuration set; auto-pause por tenant con umbrales más bajos que AWS (queja 0.08%, rebote 4%).
- **Subdominio dedicado para envío:** se usa `send.blustudioinc.com` (NO la raíz ni el subdominio de la app `crm.`), para aislar reputación. Ya verificado con DKIM.
- **Listas de contactos:** implementadas como segmentos estáticos (ya estaban en el modelo).
- **Diseño del panel:** se descartó el tema oscuro inicial; se replicó el design system del Mini SaaS de BLU (tema claro).
- **La config de AWS la maneja el owner**, no los devs: no se documenta en el repo (se quitaron las guías AWS de `docs/`). Los devs trabajan con `SES_FAKE=true` (sin cuenta AWS) o con las variables que provee el owner.
- **Repo:** GitHub `BluIncStudio/blu-crm` (privado). Convención: **sin coautoría de IA** en commits. `.claude/CLAUDE.md` es de uso interno (contexto personal, bóveda) -> gitignoreado, no se sube.

## Reglas de negocio

- Hard bounce y queja -> suppression permanente automática. Soft bounce -> reintentar.
- Import descarta y cuenta: inválidos (sintaxis), suprimidos, duplicados. Normaliza email a minúsculas.
- Consentimiento: registro en `consents` (prueba legal); el import puede marcar como suscrito.
- Editar/borrar campaña solo si está en draft/scheduled.
- **Sandbox de SES:** hasta salir del sandbox, solo se envía a destinatarios verificados. Salir del sandbox lo hace el owner.

## Estado del pilar email (2026-08-04): COMPLETO y probado con SES real

Se envió un correo real, entregado y firmado con DKIM desde `send.blustudioinc.com`. Verificado el circuito: dominio -> config set -> campaña por segmento -> Horizon -> SES -> entregado, con List-Unsubscribe.

## Datos AWS del cliente (referencia, no versionar)

- Cuenta AWS `830204833423`, región `us-east-1`. Usuario IAM `blu-crm-ses` con `AmazonSESFullAccess` (amplio, a nivel cuenta — conviene una key least-privilege por dominio para los devs).
- Topic SNS `blucrm-ses-events`. Dominio verificado `send.blustudioinc.com` (DNS en Cloudflare).
- Sandbox: producción NO solicitada aún. La key de la sesión quedó expuesta en chat -> rotar/crear key dedicada.

## Coexistencia con Mail-in-a-Box del cliente

Si el cliente ya usa MIAB para su correo, SES convive sin pisarse: bulk desde un **subdominio dedicado** (no la raíz), DKIM de SES con selectores distintos, MX sigue en MIAB, SPF via Custom MAIL FROM del subdominio, CNAME de SES en el "Custom DNS" de MIAB.

## Pendientes

- **Salir del sandbox de SES** + subir cuota (owner) para enviar a cualquier destinatario.
- **Suscribir el webhook SNS** a `/api/webhooks/ses` cuando haya URL pública (deploy en `crm.blustudioinc.com`) -> cierra el circuito de rebotes/quejas.
- **Rotar la access key** expuesta / crear key dedicada least-privilege para el dev.
- **Pilar WhatsApp** end-to-end (cola `whatsapp-send` + QR + pantallas del panel).
- Dashboard de Horizon sin proxear en nginx; validación MX opcional en import; editar campaña/segmentos desde el panel.
