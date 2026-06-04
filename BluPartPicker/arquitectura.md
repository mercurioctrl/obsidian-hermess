# Arquitectura — BluPartPicker

## Flujo general

```
Invid (Excel/scraping)   Ceven (Playwright+API)   Stylus (TSV/scraping)
        │                        │                        │
  sync_invid.py           sync_ceven.py            sync_stylus.py
        └────────────────────────┼────────────────────────┘
                                 ▼
                          invid.db (SQLite)
                         /var/www/blupartpicker/
                                 │
                           api.py (FastAPI)
                        uvicorn · puerto 4444
                       blupartpicker-api.service
                                 │
                        http://10.10.10.7:4444
```

## Base de datos

### itemsRepository
Catálogo unificado. UNIQUE en `(source, codigo)`.

Campos clave: `source, codigo, producto, fabricante, nro_parte, moneda, precio_sin_iva, pct_iva, imp_interno, precio_final, precio_ars, observaciones, stock, isinstock, imagen_url, url_ficha, categoria, descripcion, created_at, updated_at`

### price_stock_history
Historial de cambios. Se inserta en cada nuevo producto y cuando cambia `precio_final`, `stock` o `isinstock`.

`source, codigo, precio, stock, isinstock, recorded_at`

### sync_log
Log de cada ejecución: `source, started_at, finished_at, status, items_total, items_new, items_updated, message`

## API — Endpoints

| Endpoint | Descripción |
|---|---|
| `GET /sources` | Estadísticas por distribuidor |
| `GET /items` | Listado paginado (filtros: source, fabricante, isinstock, q, limit, offset) |
| `GET /items/{source}/{codigo}` | Ficha completa |
| `GET /items/{source}/{codigo}/historia` | Historial precio/stock |
| `GET /sync/log` | Últimas ejecuciones |
| `GET /fabricantes` | Lista de marcas |

## Systemd

```ini
# /etc/systemd/system/blupartpicker-api.service
User=hermess · WorkingDirectory=/var/www/blupartpicker
ExecStart=python3 -m uvicorn api:app --host 0.0.0.0 --port 4444 --workers 2
Restart=always · Logs: /var/www/blupartpicker/api.log
```

## Crons

| Script | Horario |
|---|---|
| sync_invid.py | `0 */4 * * *` (00,04,08,12,16,20) |
| sync_ceven.py | `0 1,5,9,13,17,21 * * *` |
| sync_stylus.py | `0 2,6,10,14,18,22 * * *` |

---

## Ver también

- [[BluPartPicker]] — índice del proyecto
- [[resellers]] — detalles de autenticación y formatos por distribuidor
- [[stack]] — dependencias y estructura de archivos
- [[memoria]] — gotchas y convenciones de código
