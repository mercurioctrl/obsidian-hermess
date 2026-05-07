# bully — API + Fair Value Scraper

Backend Python de la [[Planilla Acciones Bully/Planilla Acciones Bully|Planilla Acciones Bully]].
Sirve opciones financieras desde yfinance y fair values scrapeados de investing.com Pro.

**API pública:** `https://api.bully.lio.red/options`
**Repo:** `/var/www/bully/bully`
**Última sincronización:** 2026-05-04

---

## Componentes

| Archivo | Rol |
|---|---|
| `app.py` | Flask API — endpoint `/options` |
| `fv2.py` | Scraper batch — 129 tickers → SQL Server |
| `fv_watcher.py` | Watcher incremental — rellena nuevos tickers (cron cada 5 min) |
| `fv_cookies.py` | Harvester de cookies de investing.com (Camoufox) |
| `fv_run.sh` | Wrapper VPN — refresca cookies + levanta gluetun + corre script |
| `gluetun-compose.yml` | Docker compose — Surfshark VPN como proxy HTTP |

---

## Notas del proyecto

- [[Planilla Acciones Bully/arquitectura|Arquitectura]]
- [[Planilla Acciones Bully/stack|Stack]]
- [[Planilla Acciones Bully/changelog|Changelog]]
- [[Planilla Acciones Bully/contexto|Contexto y decisiones]]
- [[Planilla Acciones Bully/Planilla Acciones Bully|← Planilla Acciones Bully (índice)]]
