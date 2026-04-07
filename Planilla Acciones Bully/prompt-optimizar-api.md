# Prompt para Claude Code - Optimizar API Bully

Copia y pega esto en Claude Code:

---

Necesito optimizar el archivo `app.py` de mi API Flask que consulta opciones financieras de Yahoo Finance. El problema es que cada request a `/options` tarda ~4-5 segundos porque hace demasiadas llamadas HTTP y DB innecesarias.

## Diagnostico actual

Cada llamada a `/options` hace esto:

1. `curl_cffi.Session()` + `session.get("https://fc.yahoo.com")` — nueva sesion + precalentar cookies
2. `session.get("https://query1.finance.yahoo.com/v1/test/getcrumb")` — obtener crumb
3. `SELECT COUNT(1) FROM fair_values WHERE ticker = ?` — verificar si ticker existe
4. (posible) `INSERT INTO fair_values` — crear ticker si no existe
5. `SELECT TOP 1 fair_value, nextReport FROM fair_values WHERE ticker = ?` — obtener datos
6. `ticker.options` — pedir expirations a Yahoo (HTTP)
7. `log_raw_option_response()` en expirations — HTTP GET extra SOLO para debug
8. `log_raw_option_response()` en la cadena — OTRO HTTP GET extra SOLO para debug
9. `ticker.option_chain(exp)` — pedir la cadena real a Yahoo

Son ~5 HTTP requests a Yahoo + 2-3 DB queries POR CADA FILA de mi planilla de Google Sheets.
Cuando actualizo 30 filas, son 150+ requests HTTP a Yahoo Finance. Tarda mas de 2 minutos.

## Optimizaciones que necesito

### 1. Cache de sesion/crumb (LA MAS IMPORTANTE)
- El crumb de Yahoo dura varios minutos. No necesito uno nuevo por cada request.
- Crear un cache global con TTL de 5 minutos para la sesion `curl_cffi` y el crumb.
- Si el crumb expira o falla, renovar automaticamente.
- Usar un lock (threading.Lock) para que solo un thread renueve el crumb a la vez.

### 2. Eliminar `log_raw_option_response()`
- Esta funcion hace un HTTP GET real a Yahoo Finance SOLO para loguear la respuesta.
- Se llama 2 veces por request (una para expirations, otra para la chain).
- Son 2 requests HTTP completamente innecesarios por cada fila.
- ELIMINAR estas llamadas. Solo dejar los `app.logger.info()` normales.

### 3. Cache de fair_data (DB)
- Si pido AAPL 5 veces en 30 segundos, el fair_value no cambia.
- Cachear los resultados de `fetch_fair_data()` con TTL de 60 segundos por simbolo.
- Usar un dict simple con timestamp.

### 4. Cache de ticker.options (expirations)
- Las fechas de expiracion disponibles no cambian durante el dia.
- Cachear `ticker.options` por simbolo con TTL de 10 minutos.

### 5. Connection pooling para SQL Server
- En vez de abrir/cerrar conexion en cada request con `get_db_connection()`, usar un pool.
- Puede ser tan simple como mantener una conexion global o usar pyodbc con pool.

### 6. Reducir logging excesivo
- Eliminar `session_attrs_snapshot()` — es solo para debug de desarrollo.
- Eliminar los logs de `log_yf_session()` que se llaman multiples veces por request.
- Dejar solo los logs esenciales: inicio del request, resultado, y errores.

## Requisitos

- Mantener la misma interfaz de API: `GET /options?symbol=X&type=X&expiration_date=X&strike=X`
- Mantener la misma estructura de respuesta JSON (mismos campos).
- Mantener la consulta a la DB de `fair_values` (pero cacheada).
- No romper la logica de `build_yahoo_session_with_crumb()` — solo cachearla.
- Usar `threading.Lock` para thread-safety en los caches.
- El objetivo es que cada request pase de ~4-5 segundos a ~1-2 segundos.

## Estructura esperada del cache

```python
import threading
import time

class SessionCache:
    """Cache thread-safe para sesion Yahoo y crumb."""
    def __init__(self, ttl=300):  # 5 minutos
        self.session = None
        self.crumb = None
        self.expires_at = 0
        self.ttl = ttl
        self.lock = threading.Lock()

    def get_or_refresh(self):
        """Devuelve (session, crumb) del cache o renueva si expiro."""
        ...

class DataCache:
    """Cache generico con TTL por key."""
    def __init__(self, ttl=60):
        self.data = {}
        self.ttl = ttl
        self.lock = threading.Lock()

    def get(self, key):
        ...

    def set(self, key, value):
        ...
```

Hacelo paso a paso, probando que compile. Mantene las funciones que SI se usan (como `fetch_fair_data`, `fetch_yahoo_options_data`, el endpoint `/options`) pero optimizadas con cache.

---

## Ver tambien

- [[Planilla Acciones Bully/Documentacion Apps Script - Opciones API|Documentacion Apps Script]] — Referencia del script que consume esta API
- [[Planilla Acciones Bully/prompt-agregar-stock-data-api|Prompt - Agregar stock data API]] — Siguiente paso: agregar datos de stock
