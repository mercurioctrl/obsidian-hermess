# Contexto y decisiones — bully

## Cloudflare y el fingerprint TLS (clave)
El bloqueo `403 "Just a moment"` de investing.com **no es por IP ni por cookies** — es por el
**fingerprint TLS (JA3)** del cliente HTTP. La librería `requests` de Python es detectada como bot.
`curl_cffi` con `impersonate="chrome"` imita el TLS de Chrome real y pasa el challenge.
Verificado el 5-ago: `requests` daba 403 incluso desde la IP del host sin VPN; `curl_cffi` → 200.

**Consecuencia:** la **VPN (gluetun/Surfshark) ya no es imprescindible**. Se dejó en `fv_run.sh`
por si vuelve el rate-limit (429), pero el scraping funciona desde la IP del host.

## Respuestas inconsistentes de Investing
Para un mismo ticker, investing.com a veces devuelve el número y a veces
"El valor de mercado de X **no tiene sentido**" (típico en IPOs recientes / sin ganancias, ej: CRWV).
Por eso:
- Cuando no hay número → se guarda **NULL**, nunca el texto de error.
- `fetch_fair_value` **reintenta hasta 3 veces** para agarrar el número en la misma corrida.

## Diagnóstico del "¿desde cuándo se rompió?"
Los logs (`/tmp/fv2.log`, `fv3.log`) no tienen timestamp por línea y se recrearon el **4-ago**.
Todas las corridas registradas desde entonces fallaron. El cron corre desde ≥5-jul, pero no
sobrevive log de resultados anterior al 4-ago. Conclusión: rotura confirmable **desde el 4-ago a la tarde**.

## Monitoreo por mail
`fv_monitor.py` avisa a `cmercurio@blustudioinc.com` cuando el scraping se rompe.
SMTP self-hosted (`box.lio.red`, Mail-in-a-Box). **Pendiente:** cargar la contraseña del buzón
en `fv_alert.env` (`SMTP_PASS`) para activar el envío.

## Preferencias de git (proyecto bully)
- Commits a nombre del usuario, **sin** `Co-Authored-By`.
- No `git push` sin pedido explícito.

## Ver también

- [[Planilla Acciones Bully/arquitectura|Arquitectura]]
- [[Planilla Acciones Bully/stack|Stack]]
- [[Planilla Acciones Bully/changelog|Changelog]]
- [[Planilla Acciones Bully/bully|bully (índice)]]
