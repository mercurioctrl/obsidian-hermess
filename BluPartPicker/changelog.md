# Changelog — BluPartPicker

## 2026-06-04 — Sesión 2: PreciosGamer + API v2

### Nuevo importador: PreciosGamer (`sync_preciosgamer.py`)
- Integra 37 resellers de retail vía `https://api.preciosgamer.com/v1/sync/items-export/123`
- Cada reseller como source independiente: `preciosgamer_{resellerId}`
- Campo `distribuidor=0` para distinguirlos de los mayoristas
- Paginación automática por `offset`/`limit=5000`; `since` se calcula del último sync exitoso
- 145.108 items en el primer sync (~10 min); syncs siguientes <1 min

### Inferencia de categoría (`extract_categoria()`)
- Primera palabra de la descripción → categoría (ej. `MOUSE`, `MEMORIA`, `NOTEBOOK`)
- Si es una marca conocida (`KNOWN_BRANDS`), usar la segunda palabra
- Si es `ACCESORIOS`, saltar dos palabras para llegar a la categoría real
- Normalización de variantes: `AURICULARES→AURICULAR`, `MOTHERBOARD→MOTHER`, `NB→NOTEBOOK`, etc.
- Cobertura final: **92.8%** de 145k items

### Oráculo de marcas (`build_brand_oracle()`)
- Indexa las 711 marcas del repositorio propio (qty ≥ 2) como diccionario
- Para items sin `brandDescription` de la API, busca la marca en el texto de la descripción
- Soporta marcas multipalabra (`Trust gaming`, `TP-Link`, `Western Digital`)
- Blacklist de marcas basura (`Cpu`, `Sin definir`, etc.)
- Cobertura final: **87.9%** — el oráculo mejora solo a medida que llegan nuevas marcas de otros distribuidores

### API v2 — nuevos filtros y endpoints
- `GET /items?categoria=MOUSE` — filtro por categoría (exacto, case-insensitive)
- `GET /categorias` — nuevo endpoint: lista de categorías con conteo, acepta `source`, `fabricante`, `distribuidor`
- `GET /fabricantes` mejorado — ahora acepta `categoria` y `distribuidor` como filtros
- Swagger actualizado con descripción completa de mayoristas vs resellers
- Cron agregado: `0 3,7,11,15,19,23 * * *` (desfasado 3h de Invid)

### Documentación
- `README.md` reescrito con tabla de fuentes, endpoints y filtros completos
- `docs/architecture.md` actualizado con diagrama, tabla de columnas y volumen actual
- Notas Obsidian y memoria sincronizadas

---

## 2026-06-04 — Sesión 1

### Refactor portabilidad
- `api.py` + `sync_*.py`: `DB_PATH` y logs usan `BASE_DIR = os.path.dirname(os.path.abspath(__file__))`
- `start.sh`: `WORKDIR` desde la ubicación del script, `User=$(id -un)` en systemd, bootstrap pip, fallback Playwright Ubuntu 26.04

### `start.sh` probado y validado en este host
- Invid ✓ · Stylus ✓ · Ceven ✓
- API verificada: 2.565 productos, 3 fuentes

---

## 2026-06-03

### Nuevo distribuidor: Stylus
- `sync_stylus.py` — 906 productos, TSV latin-1 por marca + scraping catálogo
- Login: `POST /login.php`, cron `0 2,6,10,14,18,22 * * *`

### Columna `categoria` agregada a todos los distribuidores

### Repositorio Git
- `git@github.com:BluIncStudio/bluPartPicker.git` (privado), rama `main`

### Bóveda Obsidian configurada

---

## 2026-06-02

### Invid + Ceven + API FastAPI (v1)
- `itemsRepository`, `price_stock_history`, `sync_log`
- Endpoints: sources, items, historia, sync/log, fabricantes
- systemd service `blupartpicker-api.service`

---

## Ver también

- [[BluPartPicker]] — índice del proyecto
- [[arquitectura]] — estado actual del sistema
- [[contexto]] — motivación y decisiones de diseño