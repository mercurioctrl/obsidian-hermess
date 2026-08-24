# Feature: Estadísticas por lista de precio

Sección nueva del dashboard (**pestaña "Estadísticas por lista"**, `/dashboard/estadisticasPorLista`) que muestra métricas por lista de precio (A–S): facturación, costo, ganancia, rentabilidad %, **retorno sobre costo** y clientes, con gráficos y desglose mensual.

Rama: `feature/estadisticas-lista-precio` (backend y frontend). Implementado 2026-08-24.

## Objetivo

Ver cuánto rinde cada lista de precio y **cuál conviene vender** — no solo en volumen (facturación) sino en eficiencia. La métrica clave es **rentabilidad sobre costo** (`ganancia ÷ costo`), que mide el rendimiento *dólar por dólar* de lo invertido, sin el sesgo del volumen facturado (una lista que factura mucho no "gana" solo por tamaño).

## Backend

- **Endpoint:** `GET /v1/statistics/priceListStatistics`
- **Patrón:** Controller → Service → Repository
  - `Http/Controllers/Statistics/PriceListStatistics.php`
  - `Services/PriceListStatistics/PriceListStatisticsService.php`
  - `Repositories/PriceListStatistics/PriceListStatisticsRepository.php`
- **Params:** `companyCode` (default 4 = NB) + `year` (default año actual), **o** un rango `from`/`to` (YYYY-MM-DD) que tiene prioridad sobre el año.
- **Query base:** universo de pedidos remitidos — `pedclit A` (`cestado='s'`, `lanula<>1`, `companyCode`), join `pedclil B` con `listaPrecio` no nula, join `albclit rem` (`ntipoalb>1`), join `MS_REMITO_DETALLE_GANANCIA_ENLACE ga` para el costo. Facturación = Σ `npreunit·ncanped`; ganancia = facturación − Σ `costo·ncanped`. Agrupa por `listaPrecio × año × mes`.
- **Clientes por lista:** `COUNT(DISTINCT ccodcli)` en el mismo universo.
- **Costo y retorno sobre costo** se derivan en el service: `costo = facturación − ganancia`, `returnOnCost = ganancia / costo · 100`. No requiere query extra.
- **Respuesta:** `{ appliedFilters, summary:[{priceList,total,cost,profit,profitability,returnOnCost,clients}], monthly:[{priceList,year,month,total,profit}] }`.

## Frontend

- **Página:** `pages/dashboard/estadisticasPorLista.vue` (Chart.js / vue-chartjs).
- **Menú:** item "Estadísticas por lista" en `components/Table/TabMenuDashboard.vue`.
- **Store:** `store/dashboard.js` → state/mutation/action/getter `priceListStats`; el action parsea el `between` global (`DD-MM-YYYY_DD-MM-YYYY`) a `from`/`to`.
- **UI:** KPIs (facturación, rentabilidad, rentabilidad %, clientes) + torta de facturación por lista + barras de rentabilidad $ + **barras de rentabilidad sobre costo (%)** + torta de clientes + línea de evolución mensual + tabla de detalle.
- **Filtro de fecha:** respeta el rango global del dashboard (`between`); si no hay, usa el selector de año de la sección (fallback). Elegir un año limpia el rango.
- Colores por lista reusando el getter `colors` del store.

## Gotchas

- **Punto flotante:** los KPIs se muestran con `toFixed(2)` porque sumar floats ya redondeados reintroduce error (ej. `14.271.363,489999998`).
- **vue-chartjs `Line`:** importar como `Line as LineChart` — `<Line>` colisiona con el elemento SVG reservado `<line>` en Vue 2 (Vue warn "reserved HTML elements as component id: Line").
- **Laset (companyCode 11) devuelve vacío:** los pedidos de Laset no cargan `listaPrecio` en `pedclil` (import FOB), así que el reporte queda sin datos para comp=11. Tiene sentido para empresas que usan listas (NB=4, NBE=9).
- El driver `pdo_sqlsrv` local devuelve strings → cast a float/int en PHP.

## Ver también

- [[decision-listas-precios-nombradas]] — listas de precio nombradas y extensibles por companyCode
- [[relacion-tablas-ped-alb]] — pedclit / pedclil / albclit / albclil
- [[changelog]] — entrada 2026-08-24
