# Changelog — inventario

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
