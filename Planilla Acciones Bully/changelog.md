# Changelog — bully

## 2026-08-07

- **fix: guardar NULL en vez del texto de error** en `fair_value`/`nextReport`.
  Antes, cuando Investing respondía "no tiene sentido", se guardaba la frase completa
  en la columna (ej: CRWV quedaba con `"El valor de mercado de CoreWeave no tiene sentido"`).
  Ahora `parse_fair_value` devuelve `None` → columna limpia y se reintenta.
- **fix: reintento (x3)** en `fetch_fair_value` cuando Investing responde sin número
  (sus respuestas son inconsistentes: a veces el número, a veces el error).
- **fix: guard `if __name__ == "__main__"`** en `fv2.py` — importar el módulo ya no dispara el scrape.
- **feat: `fv_monitor.py`** — monitor horario que avisa por mail a `cmercurio@blustudioinc.com`
  cuando el scraping se rompe (transición OK→roto) y cuando se recupera.

  Commits: `b560494`, `4751ce5`

## 2026-08-05

- **fix: Cloudflare bloqueaba con 403** ("Just a moment"). Endureció la detección de bots;
  la librería `requests` de Python ya no pasa el challenge (con o sin VPN — probado desde IP host).
  **Solución:** `from curl_cffi import requests` + `impersonate="chrome"` (imita el TLS de Chrome).
  Aplicado a `fv2.py`, `fv3.py` y `fv_watcher.py`. Test: 139/139 tickers OK.
- **fix: `fv_watcher.py` nunca corría** — `SyntaxError` en la línea 168 (`except` mal indentado)
  desde su creación (4-ago). Nunca rellenó un solo registro. Corregido.

  Commits: `8b8f098`, `20a3886`

Archivos principales: `fv2.py`, `fv3.py`, `fv_watcher.py`, `fv_monitor.py`

## Ver también

- [[Planilla Acciones Bully/arquitectura|Arquitectura]]
- [[Planilla Acciones Bully/contexto|Contexto y decisiones]]
- [[Planilla Acciones Bully/bully|bully (índice)]]
