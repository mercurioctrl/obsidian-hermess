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
---

## 2026-06-04 — Sesión 3: Exchange rates + conversión de precios + optimización DB

### Tabla `exchange_rates` + sync automático
- Nueva tabla en SQLite: `casa`, `nombre`, `compra`, `venta`, `source_updated_at`, `fetched_at`
- 7 tipos de cambio: `oficial`, `mayorista`, `blue`, `bolsa`, `contadoconliqui`, `cripto`, `tarjeta`
- `sync_exchange_rates.py`: fetch desde `dolarapi.com/v1/dolares` (sin auth), upsert por `casa`
- Cron: `*/30 * * * *` (cada 30 min, sin log en sync_log por ser operación trivial)
- Endpoint: `GET /exchange-rates` — devuelve las 7 casas ordenadas por relevancia

### API v2.1.0 — conversión de precios y filtros nuevos en `/items`
- `moneda_out=ARS|USD`: convierte `precio_final` al vuelo usando el TC activo → agrega campo `precio_convertido`
- `tc=mayorista|blue|oficial|...`: elige la casa de cambio (default: `mayorista`)
- `precio_min` / `precio_max`: filtra por precio convertido (requiere `moneda_out`)
- `sort_by=precio|fabricante|producto|updated_at` + `sort_dir=asc|desc`
- La conversión es inline SQL: `CASE WHEN moneda='USD' THEN precio_final * {tc} ELSE precio_final END`
- Mayoristas devuelven ARS reales; resellers (PreciosGamer, ARS) se mantienen o convierten a USD

### Optimización SQLite para 147k items
- WAL mode activado (`PRAGMA journal_mode=WAL`) — permite reads concurrentes durante writes de sync
- Pragmas por conexión en `get_db()`: `cache_size=-51200` (50MB), `temp_store=MEMORY`, `mmap_size=134217728` (128MB)
- 8 índices: `distribuidor`, `source`, `isinstock`, `LOWER(categoria)`, `LOWER(fabricante)`, `(distribuidor, LOWER(categoria))`, `(distribuidor, LOWER(fabricante))`, `(fabricante, producto)`
- Caché en memoria por worker (dict con TTL 5 min): `/categorias`, `/fabricantes` y tipos de cambio

### Fix crítico: Invid moneda `US$` → `USD`
- El Excel de Invid entrega `moneda="US$"`, no `"USD"`
- La expresión SQL `CASE WHEN moneda='USD'` no matcheaba → 1.195 items sin conversión
- Fix: normalización en `parse_excel()` al momento del parseo
- Backfill manual: `UPDATE itemsRepository SET moneda='USD' WHERE moneda='US$' AND source='invid'` (1.195 filas)

Archivos modificados: `api.py`, `sync_invid.py`, `sync_exchange_rates.py` (nuevo), `docs/architecture.md`, `README.md`
---

## 2026-06-04 — Sesión 4: PreciosGamer — source por nombre, modelo 48h, fixes

### Source por nombre de reseller
- El source se generaba como `preciosgamer_{resellerId}` (ej: `preciosgamer_1061`)
- Cambiado a slug del nombre real: `preciosgamer_venex`, `preciosgamer_libre-opcion`, etc.
- `_source_slug(name)`: lowercase + guiones, sin caracteres especiales
- Migración de DB: 145.108 rows en `itemsRepository`, `price_stock_history` y `sync_log`

### Modelo de sync: DELETE + INSERT, ventana 48h
- Antes: upsert acumulativo — los items viejos se quedaban indefinidamente
- Ahora: `DELETE FROM itemsRepository WHERE source LIKE 'preciosgamer_%'` antes de cada insert
- `since` fijo = ahora - 48h (antes dependía del sync_log)
- Así la tabla siempre muestra solo los items actualizados en las últimas 48h
- `price_stock_history` no se toca (mantiene historial completo)

### sku → nro_parte
- PreciosGamer agregó campo `sku` a su API (puede ser NULL)
- Mapeado a `nro_parte` en `normalize()` y en el UPDATE de `upsert_products()`
- Ejemplos: `AC-HUEHU-B1`, `25246`, NULL

### start.sh corregido
- Faltaban crons de `sync_preciosgamer.py` y `sync_exchange_rates.py`
- Faltaba el primer sync de ambos scripts en el setup inicial
- Sin esto, `exchange_rates` nunca se creaba y la conversión de precios no funcionaba en server nuevo

### Operacional
- Ceven tuvo timeouts de login en 3 ejecuciones de cron consecutivas (08:00, 12:00, 04:00) — transitorio
- Manual run funcionó OK: 466 items, 462 procesados
- Commit `7e34d62` pusheado a main


## 2026-06-18 — Matching de productos (`oracular_sku`) + consola de curación

Feature grande: agrupar items de distintas fuentes que son el mismo producto físico, con UI para curar. Ver [[matching-productos]].

### Pipeline de matching (`match_products.py`, no destructivo)
- Tablas nuevas: `product_groups`, `item_oracular_map` (+ columna espejo `oracular_sku`), `manual_matches`, `match_candidates`. No tocan `itemsRepository`.
- Niveles por precisión decreciente: 1 deterministas (EAN/nro_parte/nombre+marca con filtro de promiscuidad) · 1.5 alias de marca · 3b adjudicados · 2/3a fuzzy IDF-Jaccard con vetos (spec/variant/marca/token-raro) · 4 imagen (opt-in) · auditoría que deja en NULL los conflictos.
- Cobertura ~63-65%. Precisión > cobertura (sin evidencia → NULL).

### Adjudicación con LLM (Haiku) a escala
- 2 pasadas de agentes Haiku (workflow) sobre 2.482 clusters → veredictos a `manual_matches`.
- 3 redes de seguridad sobre las decisiones del LLM (vetos deterministas + audit + token-raro). Aprendizaje: al nivel de precisión exigido la ganancia neta del LLM sobre el determinista es chica; el valor fue eliminar errores duros y dejar corpus durable.

### API + frontend
- Endpoints: `GET /groups`, `GET /groups/{oracular_sku}` (comparador), `GET /candidates`, `POST /match` (curación, único endpoint de escritura; CORS ahora GET+POST). `/items` ahora trae `oracular_sku`.
- `gen_candidates.py` → cola `match_candidates` (~15.8k candidatos).
- Consola de curación en `/ui` (`frontend/index.html`, vanilla JS): navegar matcheados + revisar candidatos (Mismo/Distinto/Saltar). API v2.2.0.

Archivos: `match_products.py`, `gen_candidates.py`, `frontend/index.html`, `api.py`, `ejemplo_comparar.sh`.


## 2026-06-25 — Auth por API Key + Swagger completo

### Sistema de autenticación (`feat/api-auth`)

Diseño: API Key estática en header `X-Api-Key`. CORS sigue abierto — cualquier frontend puede consumirla, pero necesita la key. Sin OAuth ni DB externa, mínima fricción.

**Tablas nuevas en `invid.db`** (creadas automáticamente al iniciar `api.py`):
- `api_keys(key PK, user_name, email, active, plan, note, created_at)` — `active=0` → 403
- `api_usage(id, key, endpoint, method, ip, ts)` — log de requests, escritura async en batch cada 5s

**Variables de entorno:**
- `AUTH_REQUIRED=0` (default) → API pública, sin romper deploy existente
- `AUTH_REQUIRED=1` + `ADMIN_KEY=<secret>` → activa validación en producción

**Endpoints `/admin/*`** (requieren `X-Api-Key: <ADMIN_KEY>`):
- `POST /admin/keys` — crear key (token_urlsafe(32), devuelve la key una sola vez)
- `GET /admin/keys` — listar todas
- `PATCH /admin/keys/{key}` — activar/desactivar, cambiar plan
- `GET /admin/keys/{key}/usage?days=30` — consumo por endpoint en ventana de N días

### Swagger v2.3.0 documentado

- 5 grupos de endpoints con tags: Catálogo · Comparador · Curación · Referencia · Admin
- Botón **Authorize** en Swagger UI via `APIKeyHeader` security scheme
- Docstrings completos en cada endpoint: campos de respuesta, ejemplos, errores (401/403/404)
- `Field()` con descriptions en todos los campos de modelos Pydantic
- Descripción general de la API con sección de autenticación y sección de matching

### Runbook de producción (`docs/runbook.md`)

Nuevo archivo con el proceso completo documentado:
- Mapa visual del pipeline (syncs → matching → API → curación)
- Comandos exactos para corrida manual completa
- Verificación funcional (queries SQLite + curl)
- Tabla de crons activos, nota de hueco del matching (no está en cron)
- Troubleshooting rápido por síntoma

Archivos: `api.py`, `docs/architecture.md`, `docs/runbook.md`, `.claude/CLAUDE.md`



## 2026-07-17 — Ceven: rotación de credenciales + prueba del importador

### Credenciales de Ceven rotadas
- El importador (`sync_ceven.py`) fallaba en login: el sitio devolvía "Correo electrónico o contraseña incorrectos".
- Diagnóstico con Playwright + screenshot confirmó que las credenciales viejas (`mrebreg@nb.com.ar` / `Nb20262026`) habían sido dadas de baja/rotadas del lado del distribuidor.
- Nuevas credenciales validadas y actualizadas en `sync_ceven.py:22-23`: `jdebello@nb.com.ar` / `Rmfrb001!`.

### Prueba end-to-end del importador
- Corrida completa OK: **513 items · 59 nuevos · 454 actualizados** · 343 entradas de historial.
- Catálogo bajó los 514 productos en batches de 100; mapeo de las 26 categorías completo.
- Estado en DB (`source=ceven`): 587 items · 563 con precio · 554 en stock · 443 con categoría.

### Aprendizaje: el loop de categorías es frágil
- Una corrida previa cortó con `Page.evaluate: TypeError: Failed to fetch` en la categoría 16/26 (throttling transitorio de Akamai por la ráfaga de requests).
- El loop de categorías **no tiene retry**: una sola falla aborta todo el sync y descarta los 514 items ya bajados (el upsert es posterior al mapeo). El reintento manual pasó sin problemas.
- Pendiente sugerido: agregar retry con backoff a las requests de categorías. Ver [[resellers#Ceven]].

Archivos: `sync_ceven.py` (credenciales, sin commitear al cierre de la sesión).
