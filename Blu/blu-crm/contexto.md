# contexto

Contexto de negocio, decisiones y pendientes. Ver [[arquitectura]] · [[memoria]] · [[blu-crm]].

## Objetivo

Producto CRM para ~10 clientes de BLU. Cada uno envía ~100k correos/mes (≈1M/mes total) + WhatsApp de bajo volumen.

## Decisiones tomadas

- **Proveedor de email: Amazon SES** (vs Mailgun ~$600/mes o Postmark, inviable para bulk). SES ~$100/mes a 1M. Se descartó SMTP propio (IP virgen, warm-up, blacklists, mantenimiento eterno).
- **Aislamiento de reputación:** cada cliente con su dominio + configuration set; auto-pause por tenant con umbrales más bajos que AWS (queja 0.08%, rebote 4%).
- **Listas de contactos:** implementadas como segmentos estáticos (ya estaban en el modelo).
- **Diseño del panel:** se descartó el tema oscuro inicial; se replicó el design system del Mini SaaS de BLU (tema claro).

## Reglas de negocio

- Hard bounce y queja -> suppression permanente automática. Soft bounce -> reintentar.
- Import descarta y cuenta: inválidos (sintaxis), suprimidos, duplicados. Normaliza email a minúsculas.
- Consentimiento: registro en `consents` (prueba legal); el import puede marcar como suscrito.
- Editar/borrar campaña solo si está en draft/scheduled.

## Coexistencia con Mail-in-a-Box del cliente

Si el cliente ya usa MIAB para su correo, SES convive sin pisarse:
- Enviar el bulk desde un **subdominio dedicado** (ej. `envios.dominio.com`), no la raíz -> aísla reputación.
- DKIM de SES usa selectores distintos -> no choca con el DKIM de MIAB.
- MX sigue en MIAB. SPF: usar Custom MAIL FROM de SES en el subdominio (no toca la raíz).
- DMARC de la raíz aplica al subdominio; alinea por DKIM del subdominio.
- Los CNAME de SES se agregan en el panel "Custom DNS" de MIAB, al lado de lo existente.

## Pendientes

- **Dominios + verificación SES (DKIM/SPF):** único paso que necesita credenciales AWS reales. El usuario ya tiene cuenta AWS; falta: credenciales IAM (AmazonSESFullAccess) al `.env`, verificar un dominio, y (para producción) salir del sandbox + subir cuota.
- **Webhook de rebotes** necesita URL pública (ngrok para probar / deploy con HTTPS).
- **Pilar WhatsApp** end-to-end (QR + envío) + pantallas.
- Módulo de dominios en el panel (generar CNAME, verificar, config set por cliente).
- Dashboard de Horizon sin proxear en nginx; List-Unsubscribe + endpoint público de baja.
