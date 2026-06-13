# Changelog — inventario

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
