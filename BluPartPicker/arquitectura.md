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
                      invid.db (SQLite, WAL)
                   /var/www/blupartpicker/
                          ▲
         dolarapi.com ──→ sync_exchange_rates.py (cada 30 min)
                             │
                         api.py (FastAPI)
                      uvicorn puerto 4444
                   blupartpicker-api.service
                             │
                     http://10.10.10.7:4444
```

## Base de datos — `invid.db`

SQLite en WAL mode (`PRAGMA journal_mode=WAL` persistido en el archivo).

### Tabla `itemsRepository`

Catálogo unificado. UNIQUE constraint en `(source, codigo)`.

| Columna        | Tipo | Invid | Ceven | Stylus | PreciosGamer | Notas |
|----------------|------|-------|-------|--------|--------------|-------|
| source         | TEXT | ✓ | ✓ | ✓ | ✓ | `"invid"`, `"ceven"`, `"stylus"`, `"preciosgamer_{id}"` |
| codigo         | TEXT | ✓ | ✓ | ✓ | ✓ | PK lógica por fuente |
| producto       | TEXT | ✓ | ✓ | ✓ | ✓ | |
| fabricante     | TEXT | ✓ | ✓ | ✓ | ✓ | PG: API + oráculo (87.9%) |
| nro_parte      | TEXT | ✓ | ✓ | ✓ | NULL | = codigo en Stylus |
| moneda         | TEXT | USD | USD | USD | ARS | Siempre "USD" o "ARS", nunca "US$" |
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

### Tabla `exchange_rates`

Tipos de cambio USD/ARS. Actualizada cada 30 min desde `dolarapi.com/v1/dolares`.

```sql
id, casa TEXT UNIQUE, nombre TEXT, compra REAL, venta REAL, source_updated_at TEXT, fetched_at TEXT
```

| `casa` | Descripción |
|--------|-------------|
| `oficial` | Dólar oficial bancario |
| `mayorista` | Dólar mayorista — usado por importadores. **Default de la API** para conversión USD→ARS. |
| `blue` | Dólar informal |
| `bolsa` | Dólar bolsa (MEP) |
| `contadoconliqui` | CCL |
| `cripto` | Dólar cripto |
| `tarjeta` | Dólar tarjeta |

### Índices

```sql
idx_items_distribuidor      ON itemsRepository(distribuidor)
idx_items_source            ON itemsRepository(source)
idx_items_isinstock         ON itemsRepository(isinstock)
idx_items_categoria_lower   ON itemsRepository(LOWER(categoria))
idx_items_fabricante_lower  ON itemsRepository(LOWER(fabricante))
idx_items_dist_cat          ON itemsRepository(distribuidor, LOWER(categoria))  ← más usado
idx_items_dist_fab          ON itemsRepository(distribuidor, LOWER(fabricante))
idx_items_orden             ON itemsRepository(fabricante, producto)

idx_psh_source_codigo       ON price_stock_history(source, codigo)
idx_psh_recorded_at         ON price_stock_history(recorded_at)
```

## API REST — `api.py` (v2.1.0)

**Puerto:** 4444 · **Docs:** http://10.10.10.7:4444/docs · **Framework:** FastAPI + uvicorn

| Endpoint | Descripción |
|----------|-------------|
| `GET /sources` | Estadísticas por fuente |
| `GET /items` | Listado paginado con filtros y conversión de moneda |
| `GET /items/{source}/{codigo}` | Ficha completa |
| `GET /items/{source}/{codigo}/historia` | Historial precio/stock |
| `GET /fabricantes` | Marcas con conteo — acepta `source`, `categoria`, `distribuidor` |
| `GET /categorias` | Categorías con conteo — acepta `source`, `fabricante`, `distribuidor` |
| `GET /exchange-rates` | Tipos de cambio USD/ARS actuales (7 casas) |
| `GET /sync/log` | Últimas ejecuciones de sync |

### Filtros de `/items`

| Parámetro | Default | Descripción |
|-----------|---------|-------------|
| `source`, `fabricante`, `categoria`, `distribuidor`, `isinstock`, `q` | — | Filtros estándar |
| `moneda_out` | — | `ARS` o `USD` — agrega `precio_convertido` en la moneda elegida |
| `tc` | `mayorista` | Casa de cambio: `mayorista` \| `blue` \| `oficial` \| `bolsa` \| `cripto` \| `tarjeta` |
| `precio_min` / `precio_max` | — | Rango sobre `precio_convertido` (requiere `moneda_out`) |
| `sort_by` | — | `precio` \| `fabricante` \| `producto` \| `updated_at` |
| `sort_dir` | `asc` | `asc` \| `desc` |
| `limit` / `offset` | 50 / 0 | Paginación (max 500) |

**Conversión inline SQL:**
```sql
CASE WHEN moneda = 'USD' THEN precio_final * {tc_venta} ELSE precio_final END  -- moneda_out=ARS
CASE WHEN moneda = 'USD' THEN precio_final ELSE precio_final / {tc_venta} END  -- moneda_out=USD
```

**Caché en memoria (por worker uvicorn):**
- `/categorias`, `/fabricantes`: TTL 5 min
- Tipo de cambio activo: TTL 5 min
- Se invalida sola al expirar; sin lógica de invalidación explícita

## Sync PreciosGamer — particularidades

**Inferencia de categoría** (`extract_categoria()`): primera palabra → categoría, con skip de marcas y abreviaciones. **92.8% cobertura.**

**Oráculo de marcas** (`build_brand_oracle()` + `find_brand_in_text()`): indexa 711 marcas del repo (qty≥2), busca en texto de descripción, soporta marcas multipalabra. **87.9% cobertura total.**

## Crons

| Script | Horario | Duración |
|--------|---------|----------|
| `sync_invid.py` | `0 */4 * * *` | ~5 min |
| `sync_ceven.py` | `0 1,5,9,13,17,21 * * *` | ~15-20 min |
| `sync_stylus.py` | `0 2,6,10,14,18,22 * * *` | ~5 min |
| `sync_preciosgamer.py` | `0 3,7,11,15,19,23 * * *` | ~10 min (1er sync) |
| `sync_exchange_rates.py` | `*/30 * * * *` | <5 seg |

## Volumen actual (jun 2026)

| Fuente | Productos | Con imagen | En stock | Con cat. | Con marca | Tipo |
|--------|-----------|------------|----------|----------|-----------|------|
| invid | 1.195 | 34 (3%) | 1.195 | 953 (80%) | 1.195 | Mayorista |
| ceven | 464 | 446 (96%) | 442 | 356 (77%) | 464 | Mayorista |
| stylus | 906 | 863 (95%) | 811 | 653 (72%) | 906 | Mayorista |
| preciosgamer_* (37) | 145.108 | 141.413 (97%) | 16.300 (11%) | 134.641 (93%) | 127.535 (88%) | Resellers |
| **Total** | **147.673** | **142.756** | **18.748** | **136.603** | **130.100** | |

---

## Ver también

- [[BluPartPicker]] — índice del proyecto
- [[resellers]] — auth, formatos y gotchas por fuente
- [[contexto]] — decisiones de diseño y casos de uso
- [[changelog]] — historial de cambios
