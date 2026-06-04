# Stack — BluPartPicker

## Runtime

- **Python 3** (probado en 3.12 y 3.14)
- **SQLite** — `invid.db`, ~147k rows, sin servidor
- **FastAPI** — API REST, puerto 4444, CORS abierto GET
- **uvicorn** — ASGI server
- **systemd** — service `blupartpicker-api`
- **cron** — 4 jobs (invid, ceven, stylus, preciosgamer), desfasados por hora

## Dependencias Python

```
fastapi          # API REST
uvicorn          # ASGI server
requests         # HTTP para Invid, Stylus, PreciosGamer
openpyxl         # Excel de Invid
playwright       # Browser para Ceven (Akamai bypass)
beautifulsoup4   # Scraping catálogo Invid y Stylus
```

## Syncs

| Script | Fuente | Técnica | Duración |
|--------|--------|---------|----------|
| `sync_invid.py` | Invid | Excel + scraping | ~5 min |
| `sync_ceven.py` | Ceven | Playwright + NetSuite API | ~15-20 min |
| `sync_stylus.py` | Stylus | TSV latin-1 + scraping | ~5 min |
| `sync_preciosgamer.py` | PreciosGamer | API REST paginada | ~10 min (1er sync) |

## APIs externas

| API | Auth | Notas |
|-----|------|-------|
| PreciosGamer | Ninguna | `https://api.preciosgamer.com/v1/sync/items-export/123` |
| Invid | Session cookie | Login por form |
| Stylus | Session cookie | Login por form |
| Ceven | Playwright session | Akamai bloquea requests directos |

## Hosts probados

- Ubuntu 22.04 LTS
- Ubuntu 26.04 "resolute" (Python 3.14, libs Chromium `t64`, Playwright override `ubuntu24.04-x64`)

---

## Ver también

- [[BluPartPicker]] — índice
- [[arquitectura]] — cómo se conectan los componentes