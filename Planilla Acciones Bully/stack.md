# Stack — bully

## Lenguaje / Runtime
- **Python 3** (sistema, `/usr/bin/python3`)

## Dependencias clave
| Paquete | Para qué |
|---|---|
| `curl_cffi` | Cliente HTTP que imita el fingerprint TLS de Chrome — **pasa el anti-bot de Cloudflare** de investing.com. Reemplazó a `requests`. Instalado con `pip3 install curl_cffi --break-system-packages` |
| `pyodbc` + `ODBC Driver 18 for SQL Server` | Conexión a SQL Server externo (`NB_WEB`) |
| `yfinance` | Cadena de opciones desde Yahoo Finance |
| `flask` | API `/options` (`app.py`) |
| `camoufox` (Firefox stealth) | Harvester de cookies de investing.com (`fv_cookies.py`) |
| `smtplib` (stdlib) | Envío de mail de alerta (`fv_monitor.py`) |

## Servicios externos
- **investing.com Pro** — GraphQL `https://es.investing.com/pro/_/api/query` (fair value, next earnings). Detrás de Cloudflare.
- **SQL Server** — `190.210.23.97,4444`, base `NB_WEB`, tabla `dbo.fair_values`
- **Surfshark VPN** — via gluetun (Docker), proxy HTTP en `127.0.0.1:18888` (opcional, ya no imprescindible)
- **Mail-in-a-Box** — `box.lio.red` (SMTP 587 STARTTLS) para las alertas de `fv_monitor.py`

## Cron (usuario hermess)
```
0 */2 * * *   fv_run.sh fv2.py        # fair_value cada 2h
45 */2 * * *  fv_run.sh fv3.py        # nextReport cada 2h a los :45
*/5 * * * *   fv_watcher.py           # incremental cada 5 min
0 * * * *     fv_monitor.py           # monitor + alerta mail cada hora
```

## Secretos (NO en git — `.gitignore`)
- `investing_cookies.json` — cookies activas de investing.com
- `fv_alert.env` — credenciales SMTP del monitor
- `.fv_monitor_state` — estado OK/BROKEN del monitor

## Ver también

- [[Planilla Acciones Bully/arquitectura|Arquitectura]]
- [[Planilla Acciones Bully/bully|bully (índice)]]
