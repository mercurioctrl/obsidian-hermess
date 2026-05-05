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
                           ┌────────┴────────┐
                      fv2.py (batch)   fv_watcher.py (incremental)
                           │
                      investing.com Pro (GraphQL)
                           │
                      gluetun VPN (Surfshark)
```

## Base de datos

**Tabla:** `NB_WEB.dbo.fair_values`

| Columna | Tipo | Descripción |
|---|---|---|
| ticker | varchar | Símbolo (ej: AAPL, FOUR) |
| fair_value | varchar | Valor razonable en formato europeo (ej: `66,22`) |
| nextReport | varchar | Fecha del próximo earnings |
| updated_at | datetime | Última actualización |
| created_at | datetime | Creación del registro |

El fair_value se guarda como string con formato europeo (coma decimal). `app.py` lo normaliza a float al servirlo.

## Flujo de scraping (fv2.py)

1. `fv_run.sh` refresca cookies via `fv_cookies.py` (Camoufox)
2. Levanta gluetun (Surfshark VPN como proxy HTTP en 127.0.0.1:18888)
3. Espera hasta 90s que el túnel esté activo
4. Corre `fv2.py` con `FV_PROXY` seteado
5. fv2.py consulta investing.com Pro (GraphQL) por cada ticker
6. Extrae el número del texto: regex `es de ([\d.,]+)`
7. MERGE upsert en SQL Server
8. Baja el container VPN

## Flujo incremental (fv_watcher.py)

- Corre cada 5 minutos via cron
- Busca filas con `created_at >= ahora - 10min` y `fair_value IS NULL`
- Llena fair_value y nextReport sin VPN (pocos tickers, sin riesgo de rate-limit)
- `app.py` crea el registro vacío si recibe un ticker nuevo

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
- [[Planilla Acciones Bully/bully|bully (índice)]]
