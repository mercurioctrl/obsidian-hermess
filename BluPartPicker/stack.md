# Stack e Infraestructura — BluPartPicker

## Python / Dependencias

| Paquete | Versión | Uso |
|---|---|---|
| fastapi | 0.133.1 | API REST |
| uvicorn | 0.27.1 | ASGI server |
| requests | 2.31.0 | HTTP (Invid, Stylus) |
| openpyxl | 3.1.5 | Excel Invid |
| playwright | 1.58.0 | Browser headless Ceven |
| beautifulsoup4 | 4.14.3 | Scraping Invid, Stylus |
| xlrd | 2.0.2 | (instalado, no se usa activamente) |

**Python:** 3.12.3  
**Instalar todo:** `pip install fastapi uvicorn requests openpyxl beautifulsoup4 xlrd playwright --break-system-packages && python3 -m playwright install chromium`

## Archivos del proyecto

```
/var/www/blupartpicker/
├── api.py              FastAPI app
├── sync_invid.py       Sync Invid Computers
├── sync_ceven.py       Sync Ceven (Playwright)
├── sync_stylus.py      Sync Stylus S.A.
├── invid.db            SQLite — toda la data
├── start.sh            Setup desde cero
├── README.md           Documentación de uso
└── docs/
    ├── architecture.md
    └── resellers.md
```

## Infraestructura

- **OS:** Linux Ubuntu, Python 3.12
- **Servicio:** `blupartpicker-api.service` (systemd, user hermess)
- **Puerto:** 4444
- **DB:** SQLite (sin servidor, archivo único)
- **Crons:** en crontab de hermess
- **Logs:** `*.log` en `/var/www/blupartpicker/`
