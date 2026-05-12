# Contexto — enviosMailDrop

## Campaña activa

**Opción Fest** — airdrop de $15.000 en billetera virtual para usuarios de Libre Opción.
- Destino sin cuenta: `https://registrate.libreopcion.com`
- Destino con cuenta: `https://libreopcion.com.ar/mi-cuenta/wallet`
- BCC en cada envío: `notificalibreopcion@gmail.com`

## Flujo operativo

1. Cargar emails en `LO.dbo.airdrop_recipients` (insert manual o bulk)
2. Correr `enviar_airdrop.py` manualmente para enviar los mails pendientes
3. El cron `cron_airdrop_wallet.py` (cada 2 min) detecta usuarios registrados y acredita la wallet automáticamente

## Reglas de negocio

- Máximo 3 intentos de envío por email (`mail_intentos < 3`)
- Si `email_sent_at IS NULL` → pendiente de envío
- Si `email_sent_at IS NOT NULL AND airdrop_done_at IS NULL` → pendiente de acreditación (cron reintenta indefinidamente hasta que el usuario se registre)
- Si un email no existe en `LO.dbo.usuarios.correo` → queda pendiente, el cron lo reintenta en cada ciclo
- Anti-duplicados: el insert verifica existencia antes de insertar

## Tabla principal: LO.dbo.airdrop_recipients

| Columna | Uso |
|---|---|
| `email` | UNIQUE — nunca duplicado |
| `email_sent_at` | NULL = mail no enviado |
| `airdrop_done_at` | NULL = wallet no acreditada |
| `user_id` | ID del usuario LO cuando matchea |
| `amount_usd` | Monto acreditado en USD |
| `mail_intentos` | Contador de intentos de envío |
| `mail_error` | Último error de envío |

## Problemas resueltos

### DKIM no firmaba los emails
OpenDKIM logueaba `can't parse From: header value` — Python codificaba nombre + email
juntos en un encoded-word MIME violando RFC 5322.
**Fix:** `formataddr((str(Header(nombre, "utf-8")), email))` — solo el nombre va codificado.

### Emails no llegaban a Gmail
1. `From` mal formado → DKIM no firmaba → Gmail rechazaba (550-5.7.1)
2. Faltaban `Date` y `Message-Id` → SpamAssassin -1.5 puntos
3. Faltaba `text/plain` en el MIME

**Score mail-tester.com:** 7.5/10

### SPF con `?all` (pendiente)
Usar `~all` en DNS de `libreopcion.com` mejoraría el score.

## Ver también

- [[arquitectura]] — estructura técnica
- [[changelog]] — historial de cambios
