# Operación — partPicker

Cómo correr el proyecto en una máquina limpia, de dónde sale el stock, y cómo reconstruir la base desde el respaldo de SQL Server. Ver [[partPicker]] y [[specs-y-armador]].

## Setup en máquina limpia

El repo se clona sin lo gitignoreado (`venv/`, `.env`, `scraper.db`, `buildcores-db/`, `skus.json`).

- **Python 3.12** (no 3.14). `python3 -m venv venv`.
- **NO** usar `pip install -r requirements.txt`: conflicto de `pyee` entre `playwright`/`pyppeteer` (que el scraper no usa). Instalar solo:
  `undetected-chromedriver selenium beautifulsoup4 lxml python-dotenv flask pymssql requests` + `setuptools<81`
  (`uc 3.5.5` importa `distutils`, removido en 3.12 → lo provee `setuptools`).
- **Chrome:** `/usr/bin/google-chrome` v152 + `DISPLAY=:1`. `uc 3.5.5` funciona con Chrome 152 y pasa Cloudflare. Headful, no headless.
- **.env:** destino SQL Server `db-nb-massql-dev.blu.net.ar:4444`, DB `PRODUCTOS`, user `cmercurio`. Credenciales solo en el `.env` (no en la bóveda).

> **Gotcha buffering:** correr siempre con `-u` → `./venv/bin/python -u scraper.py > scraper.log 2>&1`. Sin `-u`, el log queda vacío y el monitor no muestra progreso (lee `scraper.log`, detecta el proceso con `pgrep -f scraper.py`).

## Origen del stock (dato clave)

"En stock" = existe fila en **`NewBytes_DBF.dbo.stocks`** con **`nstock > 0`** para **cualquier** almacén (`ID_ALMACEN`), vinculado `stocks.ID_ARTICULO = id_interno`.

- NO es `CS.dbo.productos.stock_cliente` (ése es el catálogo web/marketplace LO, da otra cifra).
- La familia PC de cada artículo sale de `NewBytes_DBF.dbo.articulo.ID_FAMILIA`, que es el mismo id que `category_mapping.category_id` (3=PROCESADORES, 1=MEMORIAS, 23=PLACA DE VIDEO, 14/37/70=MOTHER ASUS/GIGABYTE/ASROCK, etc.). `category_mapping` da el `pcpp_category`.

## Reconstruir scraper.db desde SQL Server

El respaldo en `PRODUCTOS` tiene 5 tablas: `skus`, `matches`, `product_specs`, `spec_definitions`, `category_mapping` (con las columnas de migración `spec_def_id` y `nombre_es`). **NO** tiene `products`, `items`, `categories`, `brands`.

- Script `rebuild_db.py` (en el repo): copia las 5 tablas preservando `spec_definitions.id` (a los que apunta `spec_def_id`). Deja `products` vacío (lo repuebla la Fase 1) e `items`/`categories`/`brands` vacías (rompe solo la pestaña "SKUs pendientes" del monitor).

## Scrape dirigido a in-stock

Para actualizar solo los in-stock sin re-indexar todo: `prep_instock_items.py` puebla `items`+`categories` con los in-stock componentes-PC sin match y deja `progress.phase='search'` → `python scraper.py` corre solo la **Fase 4** sobre ellos.

## Match manual — ojo

El botón de match manual del monitor scrapea con requests/BS4 y **Cloudflare lo bloquea**: crea el `match` pero deja el producto **sin specs**. Completar con Chrome: `scrape_one.py` (corre `phase3` sobre los matches sin specs).

## Sync a SQL Server

`sync_sqlserver.py` no se dispara solo. Upsert idempotente fila por fila (commit cada 100): re-actualiza las ~26k existentes para insertar unas pocas nuevas → **lento** (varios min por unos cientos de registros nuevos). Pendiente: optimizarlo para tocar solo lo nuevo/cambiado o usar `executemany`.

## Cobertura actual de componentes PC en stock (2026-09-02)

De **344** componentes de PC en stock: **233 con specs (68%)**, **228 con specs de compatibilidad (66%)**.

| Categoría | In-stock | Con specs | % |
|---|---:|---:|---:|
| video-card | 30 | 27 | 90% |
| cpu | 44 | 38 | 86% |
| internal-hard-drive | 29 | 19 | 66% |
| memory | 31 | 20 | 65% |
| motherboard | 80 | 51 | 64% |
| power-supply | 37 | 23 | 62% |
| case | 47 | 28 | 60% |
| cpu-cooler | 46 | 27 | 59% |

Hueco (111 sin specs): no están en PCPartPicker o el Part# no coincidió exacto. Subir cobertura → buscar por nombre/modelo, aflojar criterio, o clonar `buildcores-db/`.

## Ver también

- [[partPicker]] — índice
- [[specs-y-armador]] — esquema de tablas y reglas del armador
- [[changelog]]
