# Changelog — inventario

## 2026-06-23

Sesión profunda de **Regularización de stock**: investigación de deltas, restauración de `albprol` y diagnóstico cross-company. Rama `regularizacion-stock` (front y back, pusheadas). Ver [[modulo-regularizacion]], [[memoria]] y [[contexto]].

### Investigación del delta (item 111454 RYZEN 7 5700G)
- El delta del grid es **pura aritmética de documentos** (compra − venta − créditos − stock), no de seriales. El −412 del 5700G resultó ser una **OC física recibida y vendida pero nunca documentada** (OC **11568**, estado "P", 500 u serializadas sin `albprol`). Es el espejo-compra del caso `albclil` de ventas: sobrevive el `pedprol`, falta el `albprol`.
- **Causa estructural**: artículos **duplicados del mismo SKU entre empresas** (5700G: 113950/113147 en cc4 + 121729 en cc11). Habilita ingresos cruzados.

### Backend (ms-metadata)
- **feat**: `apply_albprol_restoration` (`regularization.py`) — restaura el `albprol` faltante desde el `pedprol` sobreviviente, como **puro asiento (cost-neutral)**: no toca stock ni costo (sin triggers, `NCOSTEPROM` almacenado, FOB usa el último albprol por fecha). Una sola cabecera canónica, **maneja parciales** (inserta faltante = pedido − documentado), idempotente, gateada por `gerencia`. Preview con **cruce de seriales** (`serialMatch`, `perfecto`, `gapFisico`). **Aplicada en prod sobre OC 11568** (14 líneas / 2470 u en cabecera 15844, 7 ítems perfectos).
- **feat**: filtro de delta **"distinto de cero"** en la grilla de stock (`stocks.py`).

### Frontend (inventario-web-app)
- **feat/UX**: la pestaña **Stock** ya **no obliga** a elegir marca/categoría/búsqueda — con solo la **empresa** carga (paginado). Filtro Delta combinable; opción "Distinto de cero". (`api.js`, `store/index.js`, `General.vue`, `ItemsStock.vue`, `itemsStock.vue`).
- **feat**: el modal de Regularización muestra el **delta real del grid vs el race neto** (`RegularizationDetail.vue`).

### Hallazgo: cc11 no serializa
- El barrido de "OC recibida sin albprol" dio falsos positivos en cc11/cc9. Razón: **cc11 prácticamente no usa el ledger de seriales** (16 de 602 artículos; 955 seriales vs 107.058 u de albprol). Su "albprol fantasma" es un **artefacto de medición**, no un error a revertir. Los deltas raros de cc11 son descuadres de **columnas de stock**, no cruces ocultos con cc4 (verificado en ambos sentidos: ni el albprol de cc11 es de cc4, ni los seriales de cc11 son items que le falten a cc4).

### Git / Ops
- Pusheado a `regularizacion-stock` en ambos repos (ms-metadata `c5ac6f9`/`a634f50`; web `3e31d70`/`db53701`), para PR con base `development`/`gamma`. `.env` y `.DS_Store` sin commitear.

## 2026-06-20

Sesión sobre `development`/`gamma` + nueva rama de funcionalidad **`catri-fine-tuning2`** (front y back, pusheada, sin mergear). Ver [[memoria]], [[contexto]] y [[modulo-precios]].

### Frontend (inventario-web-app)
- **feat**: Export **XLSX y CSV** también en la pestaña **Stock** (antes solo en Precios). Los botones (etiquetas cortas "XLSX"/"CSV") viven **dentro de la barra de filtros**, al lado de "Columnas", y emiten eventos a la página; exportan las columnas visibles. XLSX con `import('xlsx')` dinámico, CSV con BOM + `;`.
- **fix/UX**: el filtro **empresa (companyCode)** ahora se setea al `companyCode` del usuario (o **4** por defecto) **al entrar a cada pestaña**, vía `middleware/companyCode.js` (en `router.middleware`). Antes el select quedaba puesto pero los datos **sin filtrar** por una **carrera**: el watcher `immediate` de `General.vue` dispara el fetch y `updateMet` descarta el 2do fetch en vuelo (`window.__generalUpdateRunning`). Se resolvió seteando el default **antes** del fetch (middleware). Solo queda libre si se borra a mano dentro de la misma pestaña.
- **feat**: Agregada la entrada **Precios** al menú (`layouts/basic.vue`) — nunca estuvo en git (prod tenía una edición manual). Commiteada en `catri-fine-tuning` y mergeada a `development`/`gamma`.

### Backend (ms-metadata)
- **perf**: Eliminado **N+1** en `/items` y `/item` (`products.py`). `searchProducts` trae todas las imágenes en una sola query (`getImagesBulk`) en vez de abrir una conexión por producto (cada `dbconnection()` es un handshake TLS 1.0 y nunca se cierra). `GET /items?itemsPerPage=300`: **~11,5s → ~1,2s**. `getDetailProduct` pide atributos/imágenes una sola vez por artículo. Quitados los `print()` de debug.

### Git / Ops
- Mergeado `catri-fine-tuning` → `development` y `gamma` (front); en el back ya estaba contenido en `Development`/`Gamma`. Lo pendiente quedó en **`catri-fine-tuning2`** (front `983d58e`, back `6b9eeb4`), pusheada en ambos repos.
- **Gotcha git**: la rama `Development` (mayúscula) del back es la canónica (trackea `origin/Development`); borrar la `development` minúscula la dejó huérfana (macOS case-insensitive) → recuperada con `git reset --mixed origin/Development`.
- `xlsx` ya estaba en package.json; faltaba `npm install`. Los deploys necesitan `npm ci`/`npm install` o el `import('xlsx')` da 500.

Archivos: `pages/itemsStock.vue`, `pages/itemsPrices.vue`, `components/Filters/*.vue`, `middleware/companyCode.js`, `nuxt.config.js`, `layouts/basic.vue`, `core/controllers/products/products.py`.

## 2026-06-15

Más sobre la grilla de **Precios** (`/itemsPrices`), rama `catri-fine-tuning`. Commit `d1fb0e4`. Ver [[modulo-precios]] y [[competencia-partpicker-cache]].

### Frontend (inventario-web-app)
- **feat**: Columna fija **Compra-Gamer** en Resellers (siempre ese reseller, aunque no sea el más barato) + sorter + export.
- **feat**: Modal de competencia muestra **SKU** (`codigo`) y **Part #** (`nroParte`) por oferta.
- **feat**: **Título en una sola línea** con ellipsis; al hacer **hover** la fila se agranda y muestra el título completo. SKU sacado de abajo del título → **columna SKU visible por defecto**.
- **perf**: **Celdas editables lazy** (`EditablePriceCell`): muestran texto y montan el input de Ant solo al hacer click. Evita montar miles de inputs (clave con "Todo") → render/orden/scroll más fluidos. *UX:* se clickea para editar; no hay tab entre celdas.
- **perf**: La grilla pide `pricesView=1` → query liviana del backend.
- **fix**: Checkbox **"seleccionar todos"** en la cabecera no aparecía: Ant solo aplica `slots.title` si `column.title === undefined` (`lib/table/index.js`); un `title:""` lo bloqueaba → se quitó el title.

### Backend (ms-metadata)
- **perf**: `get_items_prices_grid` (query liviana, sin las subqueries pesadas de Stock) + `get_items_prices_grid_count` (`COUNT(DISTINCT)`); el endpoint las corre **en paralelo** (`ThreadPoolExecutor`) cuando `pricesView=1`. Total de la grilla ~5s → ~1,5s (y menos con paralelo). `get_items_stocks` (Stock) intacto.
- **perf**: `prewarm_catalog` en `@app.on_event("startup")` → baja el catálogo de partpicker en background al arrancar; el primer "Actualizar competencia" no espera ~30s.
- **feat**: `competition` devuelve `compragamer` por item (mejor oferta de `preciosgamer_compra-gamer`); `_build_offer` agrega `nroParte`.
- **chore**: quitado `print(con_string)` de debug en `get_items_stocks`.

Archivos: `pages/itemsPrices.vue`, `store/itemsPrices.js`, `plugins/api.js`, `components/Modal/CompetitionDetail.vue`, `components/Table/EditablePriceCell.vue`, `core/controllers/stocks/stocks.py`, `core/controllers/competition/competition.py`, `main.py`.

## 2026-06-13

Sesión de mejoras grandes a la grilla de **Precios** (`/itemsPrices`), rama `catri-fine-tuning`. Ver [[modulo-precios]].

### Frontend (inventario-web-app)
- **feat**: Columna **ID** propia anclada a la izquierda (antes el `#id` iba bajo el título; ahora el subtítulo muestra solo el SKU). Stickys: Sel · ID · SKU · Título con offsets calculados (`customCell` inline).
- **feat**: Columna **Stock** (`stockTotal` = nstock+nstock_ctrl+nstock_d1+nstock_lo) + filtro **Con stock / Sin stock / Todos** (default Con stock).
- **feat**: Columnas **Últ. ingreso / Últ. venta** (de `articulo.ULTIMO_INGRESO` / `ULTIMA_VENTA`).
- **feat**: **Orden asc/desc en todas las columnas** (client-side, sobre la página cargada).
- **feat**: **Recalcular masivo**: checkbox por fila + "todos" en cabecera; modal con un input por utilidad (PL1/PL2/MAY1/MAY2/LO1/LO2), 0=no toca, valor=suma esos puntos; aplica solo a seleccionados, secuencial con barra de progreso.
- **feat**: Tamaño de página **"Todo"** (sentinel 1.000.000) + persistencia del tamaño en localStorage.
- **feat**: **Exportar CSV** (es-AR, `;`, BOM) y **Excel .xlsx** (lib `xlsx`/SheetJS, import dinámico) de lo visible.
- **feat**: **Cache local de competencia** en localStorage: hidrata la grilla al instante y no pega solo; botón **"Actualizar competencia"** refresca lo visible y reescribe el cache (con indicador "hace X"). El detalle sigue en vivo.
- **feat**: Compactación de densidad (filas ~21px) y **altura dinámica** de la tabla midiendo `.ant-table-body` (sin franja vacía abajo).

### Backend (ms-metadata)
- **feat**: `get_items_prices` agrega `ULTIMO_INGRESO` y `ULTIMA_VENTA` (de `articulo`). OJO: `ULTIMA_COMPRA` NO existe en `articulo` (solo en `clientes`); el correcto es `ULTIMO_INGRESO`.
- **feat**: filtro de stock en `get_items_stocks`/`get_items_stocks_count` con `(ISNULL(nstock)+ISNULL(nstock_ctrl)+ISNULL(nstock_d1)+ISNULL(nstock_lo))` + columna `stockTotal` en `ItemStock`.

Archivos: `pages/itemsPrices.vue`, `store/itemsPrices.js`, `components/Filters/ItemsPrices.vue`, `plugins/api.js`, `core/controllers/stocks/stocks.py`, `core/models/models.py`, `package.json` (xlsx).

### Ops
- Se instaló `xlsx@0.18.5` en el frontend. **Tras `npm install` con el dev server corriendo hay que reiniciar `npm run dev`** (si no, webpack/HMR queda inconsistente → RuntimeError + loader infinito). Cambios sin commitear aún.

## 2026-06-12

### Frontend (inventario-web-app)
- **feat**: Señal de **tendencia** de precios (▲ subió rojo / ▼ bajó verde, tooltip con precio anterior) junto al mínimo de competencia y de resellers en la grilla, y en cada fila del modal de detalle
- **fix**: Cabeceras de la columna Título que se "metían dentro" de otras al scrollear horizontal → `<th>` sticky con estilo **inline** vía `customHeaderCell` (la CSS class no llega confiable al th en la tabla de header separada de antd)
- **fix**: Sombra del borde derecho del Título reducida a `2px/5%` (era demasiado marcada)

### Backend (ms-metadata)
- **feat**: `competition/` descarga catálogos con `tendencia=1` → cada oferta lleva `tendencia` (sube/baja/igual) + `precioAnterior`

### Deploy / Ops
- Commits `9d88670` (front) y `51fb1e9` (back) pusheados a `catri-fine-tuning`. El `.env` del backend NO se commitea (credenciales)
- Prod: sin variables `.env` nuevas; requiere salida HTTPS a `partpicker.blustudioinc.com`, `requests` instalado y permiso de escritura en `scrap_hg`. `OPENSSL_CONF` NO hace falta en prod (solo dev local)

## 2026-06-11

### Frontend (inventario-web-app)
- **feat**: Nueva sección **Precios** (`/itemsPrices`) — grilla de costos/utilidades/precios con edición inline bidireccional (utilidad→precio y precio→utilidad), código de colores del sistema legacy (naranja UNIT+PL, magenta MAY, azul LO, violeta ML+PML)
- **feat**: Columnas de **competencia**: mayoristas USD s/IVA con Δ% + semáforo, resellers ARS; carga lazy en background
- **feat**: Modal ⊕ de competencia: keywords `scrap_hg` con búsqueda en vivo (3+ chars), guardar y rematchear, lista completa de ofertas, historial de precios por fila expandible
- **feat**: Visibilidad de columnas configurable y persistida por usuario en localStorage (sobrevive logout)
- **feat**: Título como link al item en Productos (pestaña nueva, deep-link por ID)
- **fix**: Título sticky por CSS en lugar de `fixed:'left'` de antd (filas desalineadas) y `scroll.x` numérico con headers fijos (cabeceras corridas)

Archivos principales: `pages/itemsPrices.vue`, `store/itemsPrices.js`, `components/Filters/ItemsPrices.vue`, `components/Modal/CompetitionDetail.vue`, `plugins/api.js`

### Backend (ms-metadata)
- **feat**: Controller `competition/` — precios de competencia vía BluPartPicker: cache 30 min stale-while-revalidate, matching SKU exacto + `scrap_hg.search_keys` por palabra completa. Endpoints `POST /itemsCompetition`, `GET /itemsCompetition/{itemId}` (con preview `keys`), `PATCH .../searchKeys`, `GET /itemsCompetitionHistory`
- **feat**: Edición inversa de precios (`update_item_price_by_target` en `prices.py`): fijar UNIT/MAY/LO/ML deriva la utilidad ajustando solo la primera del par; ML invierte ARS+IVA→USD antes de derivar
- **fix**: Conexión a SQL Server en macOS: `OPENSSL_CONF=openssl_legacy.cnf` obligatorio (el server solo habla TLS 1.0; OpenSSL 3.x lo rechaza → error 10054 que parece firewall)

Archivos principales: `core/controllers/competition/competition.py`, `core/controllers/prices/prices.py`, `main.py`, `core/models/models.py`


## 2026-05-05

### Backend (ms-metadata)
- **hotfix**: Arreglo stock en kits (PR #263)

## 2026-04-16

### Backend (ms-metadata)
- fix: corrección en módulo de brands

## 2026-04-15

### Backend (ms-metadata)
- fix: arreglo stock syncup (sincronización de stock)

## 2026-04-29

### Frontend (inventario-web-app)
- **SNB-3913**: Cambio en la visualización de banderas en PED, INV y COM (PR #370)

## 2026-04-15

### Frontend (inventario-web-app)
- **INV-346**: Fix paginado incorrecto en pestaña de kits (PR #368)
- **INV-345**: Altura máxima en contenedor de tabla de stock para evitar scroll doble del body (PR #366)

## 2026-03-18

### Backend (ms-metadata)
- fix: corrección listado de productos
- fix: arreglo paginación en products

### Frontend (inventario-web-app)
- Refactor paginado en kits: alineado a derecha, sin scroll doble
- Refactor utilidades de control de precio: texto en shadow para campos editados, quitada línea vertical que dificultaba la vista

## 2026-03-02

### Frontend (inventario-web-app)
- **INV-343**: Al crear una categoría, se puede enviar `companyCode` (PR #362)
- **INV-342**: Al crear una marca, se puede enviar `companyCode` (PR #360)

## 2026-02-18 – 2026-02-20

### Backend (ms-metadata) — INV-BundleCostUtility
- feat: agregar costos al bundle (PR #255, #257, #259, #261)
- feat: precio por utilidad para productos individuales (INV-338)
- feat: objeto `prices` dentro del inventario de productos (INV-335, PR #252, #253)
- fix: cálculo de ganancia estipulada y precio en bundles
- fix: `ncosteprom` (costo promedio) en bundles

## Ver también

- [[inventario]] · [[arquitectura]] · [[contexto]]
