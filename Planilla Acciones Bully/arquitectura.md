# Arquitectura — bully

## Visión general

Sistema de dos capas: una **API Flask** que sirve datos a la planilla, y **scrapers Python** que alimentan la base de datos.

```
Google Sheets (Apps Script)
        │
        ▼
  Flask API (app.py)
  /options?symbol=AAPL
        │
        ├─── yfinance ──→ Yahoo Finance (cadena de opciones)
        │
        └─── SQL Server ──→ NB_WEB.dbo.fair_values
                                    ▲
                    ┌───────────────┼───────────────┐
              fv2.py (fair_value)  fv3.py       fv_watcher.py
              batch cada 2h      (nextReport)   (incremental 5min)
                    │             batch 2h            │
                    └──────────────┴─────────────────┘
                                   │
                      investing.com Pro (GraphQL)
                      curl_cffi impersonate=chrome
                      (pasa el anti-bot de Cloudflare)
```

## Base de datos

**Tabla:** `NB_WEB.dbo.fair_values`

| Columna | Tipo | Descripción |
|---|---|---|
| ticker | varchar | Símbolo (ej: AAPL, FOUR) |
| fair_value | varchar | Valor razonable en formato europeo (ej: `66,22`). **NULL** si Investing no devuelve número |
| nextReport | varchar | Fecha del próximo earnings |
| updated_at | datetime | Última actualización |
| created_at | datetime | Creación del registro |

El fair_value se guarda como string con formato europeo (coma decimal). `app.py` lo normaliza a float al servirlo.
Si Investing responde sin número (ej: "no tiene sentido"), se guarda **NULL** (no el texto de error) — así se reintenta en la próxima corrida.

## Anti-bot: Cloudflare + curl_cffi (importante)

investing.com está detrás de Cloudflare, que valida el **fingerprint TLS (JA3)** del cliente.
La librería `requests` de Python es detectada y recibe un challenge (`403 "Just a moment"`),
**con o sin VPN** (el bloqueo no es por IP, es por fingerprint).

**Solución:** `from curl_cffi import requests` + `impersonate="chrome"`, que imita el TLS de Chrome real.
Con esto el scraping funciona incluso desde la IP del host — la **VPN de `fv_run.sh` ya no es imprescindible**.

## Flujo de scraping (fv2.py / fv3.py)

1. `fv_run.sh` refresca cookies via `fv_cookies.py` (Camoufox)
2. (Opcional) Levanta gluetun (Surfshark VPN como proxy HTTP en 127.0.0.1:18888)
3. Corre el script con `FV_PROXY` seteado (si hay VPN)
4. El script consulta investing.com Pro (GraphQL) por cada ticker con `curl_cffi` (impersonate chrome)
5. Extrae el número del texto: regex `es de ([\d.,]+)`; si no hay número → NULL
6. `fetch_fair_value` reintenta hasta 3 veces cuando Investing responde sin número (respuestas inconsistentes)
7. MERGE upsert en SQL Server
8. Baja el container VPN (si se usó)

`fv2.py` tiene el bloque ejecutable bajo `if __name__ == "__main__"` (importarlo no dispara el scrape).

## Flujo incremental (fv_watcher.py)

- Corre cada 5 minutos via cron
- Busca filas con `created_at >= ahora - 10min` y `fair_value IS NULL`
- Llena fair_value y nextReport sin VPN (pocos tickers, sin riesgo de rate-limit)
- `app.py` crea el registro vacío si recibe un ticker nuevo

## Monitoreo (fv_monitor.py)

- Corre cada hora via cron
- Hace 1 request de prueba (AAPL) con `curl_cffi`; clasifica OK / ROTO
- Manda mail a `cmercurio@blustudioinc.com` **sólo en la transición** OK→roto (y otro de recuperación)
- SMTP en `box.lio.red` (Mail-in-a-Box de blustudioinc.com), credenciales en `fv_alert.env` (gitignoreado)
- Estado persistido en `.fv_monitor_state` para no spamear

## Endpoint API

```
GET /options?symbol=AAPL
GET /options?symbol=AAPL&type=call
GET /options?symbol=AAPL&expiration_date=20-06-2025&strike=200
```

Respuesta por opción:
```json
{
  "type": "Call",
  "strike": 200,
  "lastPrice": 5.2,
  "bid": 5.1,
  "ask": 5.3,
  "volume": 1200,
  "openInterest": 8000,
  "impliedVolatility": 0.35,
  "expirationDate": "2025-06-20",
  "fairValue": 236.85,
  "nextReport": "2025-07-31"
}
```

## Ver también

- [[Planilla Acciones Bully/stack|Stack]]
- [[Planilla Acciones Bully/contexto|Contexto y decisiones]]
- [[Planilla Acciones Bully/changelog|Changelog]]
- [[Planilla Acciones Bully/bully|bully (índice)]]
