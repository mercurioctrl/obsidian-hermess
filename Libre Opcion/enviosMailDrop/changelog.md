# Changelog — enviosMailDrop

## 2026-05-11 (sesión 1)

- **feat:** Creación del proyecto `enviosMailDrop` para campaña Opción Fest
- **feat:** Plantilla HTML `template_wallet_airdrop.html` con botones para registro y billetera
- **feat:** Script `send_wallet_airdrop.py` con comandos `add`, `run`, `status`
- **feat:** Tabla `mail_campana_envios` en SQL Server (DB `LO`) para control de envíos
- **fix:** Header `From` corregido para compatibilidad con OpenDKIM (RFC 5322)
- **fix:** Agregados headers `Date` y `Message-Id` faltantes (penalizaban SpamAssassin -1.5)
- **fix:** Agregado `text/plain` al mensaje MIME para mejorar deliverability
- **fix:** Removidos restos de Gmail en `template.html` (proxy URLs, `data-saferedirecturl`, clases `CToWUd`)
- **chore:** Vinculado proyecto a Obsidian en `Libre Opcion/enviosMailDrop`

## 2026-05-11 (sesión 2)

- **feat:** Script `enviar_airdrop.py` — envío masivo desde `LO.dbo.airdrop_recipients`, reemplaza flujo anterior
- **feat:** Script `cron_airdrop_wallet.py` — acreditación automática de wallet, diseñado para correr en cron
- **feat:** Tabla `LO.dbo.airdrop_recipients` como tabla principal de la campaña (`email_sent_at`, `airdrop_done_at`, `user_id`, `amount_usd`)
- **feat:** Columnas `mail_intentos` y `mail_error` agregadas a `airdrop_recipients` para tracking de fallos
- **feat:** BCC automático a `notificalibreopcion@gmail.com` en cada envío
- **feat:** Cron configurado cada 2 minutos: `*/2 * * * * python3 cron_airdrop_wallet.py`
- **feat:** Lógica anti-duplicados en insert de emails (por email único en tabla)
- **ops:** Primer envío masivo: 20 emails enviados, 16 wallets acreditadas (5 sin usuario registrado aún)

Archivos: `enviar_airdrop.py`, `cron_airdrop_wallet.py`

## Ver también

- [[arquitectura]] — decisiones técnicas
- [[contexto]] — problemas encontrados durante la sesión
