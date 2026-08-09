# bully — API + Fair Value Scraper

Backend Python de la [[Planilla Acciones Bully/Planilla Acciones Bully|Planilla Acciones Bully]].
Sirve opciones financieras desde yfinance y fair values scrapeados de investing.com Pro.

**API pública:** `https://api.bully.lio.red/options`
**Repo:** `/var/www/bully/bully` (tiene su propio `CLAUDE.md` con todo el contexto para retomar rápido)
**Última sincronización:** 2026-08-09

---

## Componentes

| Archivo | Rol |
|---|---|
| `app.py` | Flask API — endpoint `/options` |
| `fv2.py` | Scraper batch de **fair_value** — 139 tickers → SQL Server (cron cada 2h) |
| `fv3.py` | Scraper batch de **nextReport** (próximos earnings) — cron cada 2h a los :45 |
| `fv_watcher.py` | Watcher incremental — rellena fair_value/nextReport de tickers nuevos (cron cada 5 min) |
| `fv_monitor.py` | Monitor — chequea el scraping cada hora y **avisa por mail** si se rompe |
| `fv_cookies.py` | Harvester de cookies de investing.com (Camoufox) |
| `fv_run.sh` | Wrapper VPN — refresca cookies + levanta gluetun + corre script |
| `gluetun-compose.yml` | Docker compose — Surfshark VPN como proxy HTTP |

> Todos los scrapers usan **`curl_cffi` con `impersonate="chrome"`** para pasar el
> anti-bot de Cloudflare (la librería `requests` ya no funciona). Ver [[Planilla Acciones Bully/contexto|Contexto]].

---

## Notas del proyecto

- [[Planilla Acciones Bully/arquitectura|Arquitectura]]
- [[Planilla Acciones Bully/stack|Stack]]
- [[Planilla Acciones Bully/changelog|Changelog]]
- [[Planilla Acciones Bully/contexto|Contexto y decisiones]]
- [[Planilla Acciones Bully/Planilla Acciones Bully|← Planilla Acciones Bully (índice)]]
