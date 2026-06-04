# Arquitectura BluPartPicker

## Visión general

```
┌───────────────────────────────────────────────────────────────────────┐
│                        MAYORISTAS                                     │
│   Invid (Excel)    Ceven (API/NetSuite)    Stylus (TSV)               │
└────────┬──────────────────┬──────────────────┬────────────────────────┘
         │                  │                  │
    sync_invid.py     sync_ceven.py      sync_stylus.py
         │            (Playwright)             │
         └──────────────────┼──────────────────┘
                            │
┌───────────────────────────────────────────────────────────────────────┐
│                        RESELLERS (37 tiendas)                         │
│                    PreciosGamer API paginada                          │
└────────────────────────────┬──────────────────────────────────────────┘
                             │
                    sync_preciosgamer.py
                    (brand oracle + category inference)
                             │
                             ▼
                      invid.db (SQLite)
                   /var/www/blupartpicker/
                             │
                         api.py (FastAPI)
                      uvicorn puerto 4444
                   blupartpicker-api.service
                             │
                     http://10.10.10.7:4444
```

## Base de datos — `invid.db`

### Tabla `itemsRepository`

Catálogo unificado. UNIQUE constraint en `(source, codigo)`.

| Columna        | Tipo | Invid | Ceven | Stylus | PreciosGamer | Notas |
|----------------|------|-------|-------|--------|--------------|-------|
| source         | TEXT | ✓ | ✓ | ✓ | ✓ | `"invid"`, `"ceven"`, `"stylus"`, `"preciosgamer_{id}"` |
| codigo         | TEXT | ✓ | ✓ | ✓ | ✓ | PK lógica por fuente |
| producto       | TEXT | ✓ | ✓ | ✓ | ✓ | |
| fabricante     | TEXT | ✓ | ✓ | ✓ | ✓ | PG: API + oráculo (87.9%) |
| nro_parte      | TEXT | ✓ | ✓ | ✓ | NULL | = codigo en Stylus |
| moneda         | TEXT | USD | USD | USD | ARS | |
| precio_sin_iva | REAL | ✓ | ✓ | ✓ | NULL | |
| pct_iva        | REAL | ✓ | NULL | ✓ | NULL | Porcentaje (ej: 21) |
| imp_interno    | REAL | ✓ | NULL | ✓ | NULL | Impuesto interno |
| precio_final   | REAL | ✓ | ✓ | ✓ | ✓ | Con IVA incluido |
| precio_ars     | TEXT | ✓ | NULL | NULL | NULL | Texto con precio pesos |
| observaciones  | TEXT | ✓ | NULL | ✓ | ✓ | Stock textual / envío |
| stock          | INT  | NULL | ✓ | ✓ | NULL | Cantidad física |
| isinstock      | INT  | ✓ | ✓ | ✓ | ✓ | 0/1 |
| imagen_url     | TEXT | parcial | ✓ | ✓ | ✓ | URL absoluta |
| url_ficha      | TEXT | ✓ | ✓ | ✓ | ✓ | Link al producto |
| categoria      | TEXT | ✓ | parcial | ✓ | ✓ | PG: inferida de descripción (92.8%) |
| descripcion    | TEXT | NULL | ✓ | NULL | NULL | HTML stripeado |
| distribuidor   | INT  | 1 | 1 | 1 | 0 | 1=mayorista, 0=reseller |
| created_at     | TEXT | ✓ | ✓ | ✓ | ✓ | ISO 8601 UTC |
| updated_at     | TEXT | ✓ | ✓ | ✓ | ✓ | ISO 8601 UTC |

### Tabla `price_stock_history`

```sql
id, source, codigo, precio, stock, isinstock, recorded_at
```

- Se inserta en cada nuevo producto (primer registro)
- Se inserta cuando cambia `precio_final`, `stock` o `isinstock`
- PreciosGamer: stock siempre NULL (la API no lo expone)

### Tabla `sync_log`

```sql
id, source, started_at, finished_at, status, items_total, items_new, items_updated, message
```

## API REST — `api.py`

**Puerto:** 4444 · **Docs:** http://10.10.10.7:4444/docs · **Framework:** FastAPI + uvicorn

| Endpoint | Descripción |
|----------|-------------|
| `GET /sources` | Estadísticas por fuente |
| `GET /items` | Listado paginado con filtros |
| `GET /items/{source}/{codigo}` | Ficha completa |
| `GET /items/{source}/{codigo}/historia` | Historial precio/stock |
| `GET /fabricantes` | Marcas con conteo — acepta `source`, `categoria`, `distribuidor` |
| `GET /categorias` | Categorías con conteo — acepta `source`, `fabricante`, `distribuidor` |
| `GET /sync/log` | Últimas ejecuciones de sync |

### Filtros de `/items`

| Parámetro | Descripción |
|-----------|-------------|
| `source` | Fuente exacta (`invid`, `ceven`, `stylus`, `preciosgamer_1091`, ...) |
| `fabricante` | Exacto, case-insensitive |
| `categoria` | Exacto, case-insensitive |
| `distribuidor` | `1` = mayorista · `0` = reseller |
| `isinstock` | `1` / `0` |
| `q` | LIKE en `producto` y `nro_parte` |
| `limit` / `offset` | Paginación (max 500) |

## Sync PreciosGamer — particularidades

**Fuente:** `https://api.preciosgamer.com/v1/sync/items-export/123`  
**Paginación:** `offset` + `limit=5000` hasta agotar resultados  
**Since:** `GET /sync/log` del último sync exitoso de cualquier `preciosgamer_*`; primer run usa `2000-01-01`

**Inferencia de categoría** (`extract_categoria()`):
1. Primera palabra del `producto` → categoría
2. Si la primera palabra es marca conocida (`KNOWN_BRANDS`) → usar la segunda
3. Si la primera palabra es `ACCESORIOS`/`ACCESORIO` → usar la tercera
4. Normalización de variantes: `AURICULARES→AURICULAR`, `MOTHERBOARD→MOTHER`, etc.
5. Abreviaciones: `PC`, `NB→NOTEBOOK`, `MB→MOTHER`, `SSD/HDD→DISCO`
6. Cobertura: **92.8%** de los 145k items

**Oráculo de marcas** (`build_brand_oracle()` + `find_brand_in_text()`):
1. Indexa las 711 marcas del repositorio con qty ≥ 2
2. Para items sin `brandDescription`, escanea palabras del producto desde la segunda
3. Saltea descriptores comunes (`GAMER`, `WIRELESS`, `RGB`, `USB`, ...)
4. Soporta marcas multipalabra (`Trust gaming`, `TP-Link`, `Cooler master`)
5. Cobertura: **87.9%** de los 145k items (69% API directa + 19% inferida)

## Systemd service

```
/etc/systemd/system/blupartpicker-api.service
User: <usuario actual>
WorkingDirectory: <path del clone>
Restart: always, RestartSec: 5s
Logs: <path del clone>/api.log
```

## Portabilidad de paths

`DB_PATH` y logs se derivan de la ubicación del archivo:
```python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "invid.db")
```

## Crons

| Script | Horario | Duración |
|--------|---------|----------|
| `sync_invid.py` | `0 */4 * * *` | ~5 min |
| `sync_ceven.py` | `0 1,5,9,13,17,21 * * *` | ~15-20 min |
| `sync_stylus.py` | `0 2,6,10,14,18,22 * * *` | ~5 min |
| `sync_preciosgamer.py` | `0 3,7,11,15,19,23 * * *` | ~10 min (1er sync) |

## Volumen actual (jun 2026)

| Fuente | Productos | Con imagen | En stock | Con cat. | Con marca | Tipo |
|--------|-----------|------------|----------|----------|-----------|------|
| invid | 1.195 | 34 (3%) | 1.195 | 953 (80%) | 1.195 | Mayorista |
| ceven | 464 | 446 (96%) | 442 | 356 (77%) | 464 | Mayorista |
| stylus | 906 | 863 (95%) | 811 | 653 (72%) | 906 | Mayorista |
| preciosgamer_* (37) | 145.108 | 141.413 (97%) | 16.300 (11%) | 134.641 (93%) | 127.535 (88%) | Resellers |
| **Total** | **147.673** | **142.756** | **18.748** | **136.603** | **130.100** | |