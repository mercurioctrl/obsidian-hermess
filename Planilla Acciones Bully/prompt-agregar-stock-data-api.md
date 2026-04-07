# Prompt para Claude Code - Agregar datos de stock a la API

Copia y pega esto en Claude Code:

---

En `app.py`, necesito que el endpoint `/options` devuelva tambien los datos del stock subyacente ademas de los datos de opciones. Esto es para eliminar las formulas GOOGLEFINANCE de mi planilla de Google Sheets.

## Campos nuevos a agregar en la respuesta JSON

Cada objeto en el array de respuesta ya tiene estos campos:
- type, strike, lastPrice, bid, ask, volume, openInterest, impliedVolatility, expirationDate, fairValue, nextReport

Necesito agregar estos 5 campos nuevos:
- `stockPrice` — precio actual del stock (equivalente a `GOOGLEFINANCE(symbol,"price")`)
- `changePct` — cambio porcentual del dia (equivalente a `GOOGLEFINANCE(symbol,"changepct")`)
- `low52` — minimo de 52 semanas (equivalente a `GOOGLEFINANCE(symbol,"low52")`)
- `high52` — maximo de 52 semanas (equivalente a `GOOGLEFINANCE(symbol,"high52")`)
- `beta` — beta del stock (equivalente a `GOOGLEFINANCE(symbol,"beta")`)

## Como obtenerlos

Ya tenemos un objeto `ticker = yf.Ticker(symbol)` en `fetch_yahoo_options_data()`.
Usar `ticker.info` que devuelve un dict con toda la info del stock. Los keys relevantes son:

```python
info = ticker.info  # o ticker.fast_info para menos datos pero mas rapido
stock_data = {
    "stockPrice": info.get("currentPrice") or info.get("regularMarketPrice"),
    "changePct": info.get("regularMarketChangePercent"),
    "low52": info.get("fiftyTwoWeekLow"),
    "high52": info.get("fiftyTwoWeekHigh"),
    "beta": info.get("beta"),
}
```

## Donde agregarlo

En la funcion `fetch_yahoo_options_data()`, obtener `ticker.info` UNA SOLA VEZ (antes del loop de expirations) y cachear los valores. Despues incluirlos en cada objeto del array `results`:

```python
results.append({
    # campos existentes...
    "type": side_name,
    "strike": row["strike"],
    "lastPrice": row.get("lastPrice"),
    # ... etc ...
    "fairValue": fair_value,
    "nextReport": next_report,
    # CAMPOS NUEVOS:
    "stockPrice": stock_data["stockPrice"],
    "changePct": stock_data["changePct"],
    "low52": stock_data["low52"],
    "high52": stock_data["high52"],
    "beta": stock_data["beta"],
})
```

## Importante

- Obtener `ticker.info` una sola vez por request, NO dentro del loop.
- Si el cache de sesion ya esta implementado, `ticker.info` deberia ser rapido porque reutiliza la sesion.
- Si `ticker.info` falla, los campos nuevos deben ser `None` (no romper el request).
- Cachear `ticker.info` con TTL de 60 segundos por simbolo (igual que fair_data) para que si se piden varias opciones del mismo stock no haga multiples llamadas.

---

## Ver tambien

- [[Planilla Acciones Bully/Documentacion Apps Script - Opciones API|Documentacion Apps Script]] — Referencia del script (v5 implementa estos campos)
- [[Planilla Acciones Bully/prompt-optimizar-api|Prompt - Optimizar API]] — Paso previo: cache y optimizacion de la API
