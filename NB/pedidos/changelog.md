# Changelog

Registro de cambios del proyecto, agrupado por fecha.

## 2026-04-24

Iteraciones sobre [[feature-asignacion-oc|Asignación OC ↔ Venta]] post primer merge a Development:

- feat: **`cantidad: 0` = eliminar item** — el endpoint `PUT /v1/asignaciones/lineas/{id}` ahora ignora silenciosamente items con cantidad 0 en vez de tirar 422.
- feat: **items vacíos / todos en 0 = liberar todo** — short-circuit en `reemplazarAsignacionLinea` que actúa como `DELETE`, devolviendo `liberadas` extra en el payload.
- feat: **columna Proveedor** en el modal — JOIN `vw_saldo_oc → PedProT → FP_Proveedores` en `candidatasFifo` expone `proveedor_nombre`. UI con `ellipsis: true` por nombres largos.
- feat: **columna Proforma** en el modal — `pt.CSUPROF_TEMP` propagada en `candidatasFifo` y mapeada en la fila.
- feat: **link OC clickeable** — el número de OC abre `https://compras.saftel.com/orders?currentPage=1&search={oc}&between=...&companyCode={cc}` en nueva pestaña.
- fix: **modal no auto-sugiere FIFO si ya hay vigentes** al reabrir — antes proponía cantidades de FIFO para OCs sin vigente, lo que confundía al operador (parecía que el save no había funcionado). Ahora respeta lo guardado y deja el resto en 0; el botón "Aplicar FIFO" sigue disponible para redistribuir.
- chore: rama frontend rebaseada sobre `Development` actual (incluye refactor `AsignarOcModalMejoras`: z-index modal, focus en input cantidad, estado P/S con label "Pendiente"/"Remitida"). Force-push con `--force-with-lease`.

Archivos: 
- Backend: `Asignacion/AsignacionRepository.php`, `Asignacion/AsignacionService.php`, `Asignacion/ReemplazarAsignacionRequest.php`
- Frontend: `Modal/AsignarOCModal.vue`

Branch en ambos repos: `feature/asignacion-oc-pedclil` (lista para nuevo PR).


## 2026-04-22

- feat: **[[feature-asignacion-oc|Asignación OC ↔ Venta]]** — nuevo feature end-to-end para registrar de qué OC sale cada línea de venta antes de la serialización
  - Nueva tabla `pedclil_oc_asignacion` (NewBytes_DBF), 3 índices, 2 vistas (`vw_saldo_oc`, `vw_pedclil_estado_asignacion`), 1 trigger (`tg_pedclit_cestado_asignacion`)
  - Backend: 5 endpoints HTTP (sugerencia FIFO, candidatas, estado por pedido, PUT/DELETE asignación), Service transaccional con UPDLOCK+HOLDLOCK por OC, Repository con bind params
  - Frontend: badge con 4 estados (COMPLETA/PARCIAL/DISPONIBLE/SIN_ASIGNAR), modal editable con FIFO precargado, integración en `Detail.vue` columna "OC"
  - Command CLI: `php artisan asignaciones:fifo [--branch --order --company --limit --dry-run]` — idempotente, transaccional
  - Trigger SQL maneja transición V↔C cuando `pedclit.cestado` cambia P↔S — **cero acoplamiento** con [[modulo-makesale|MakeSale]] / [[modulo-removesale|RemoveSale]]
  - Feature flag `ASSIGNMENT_FEATURE_ENABLED` + filtro `ASSIGNMENT_COMPANIES` (CSV companyCodes) + `ASSIGNMENT_ALLOW_PARTIAL`
  - Cambios mínimos colaterales: `OrderDetailDto.companyCode` y `OrderItemDto.pedclilId` agregados al getDetail
  - Documentación completa en `/docs/asignacion-oc-pedclil.md` del monorepo + `database/sql/README.md`
- docs: actualizado [[arquitectura]] con sección del feature; nuevo [[contexto|gotcha]] de driver dblib + índices filtrados
- branch: `feature/asignacion-oc-pedclil` en ambos repos (basadas en Development)

Registro de cambios del proyecto, agrupado por fecha.

## 2026-04-16

- feat: **[[modulo-dashboard-lo|Dashboard Libre Opción]]** — nueva sección completa de estadísticas exclusiva del marketplace LO
  - 6 endpoints backend: summary, funnel, byPaymentMethod, byShippingMethod, resellers, cube OLAP
  - 4 páginas frontend: métricas (KPIs + pies), embudo de conversión, ranking resellers, cubo multidimensional
  - Embudo de 5 etapas: Carritos → Pedido generado → Activos → Facturados → Entregados
  - Cubo OLAP con 7 dimensiones y 4 medidas
  - Visible solo para Administrador, Gerente General, Product Manager
- fix: **Entregados** usa `MS_VENTAS_REMITOS.ID_STATUS > 1` (no `pedclit.delivered`)
- fix: **Carritos vs cancelaciones** — los sin pedclit son carritos abandonados, no cancelaciones
- fix: **Total cancelados** = created - active (no suma de flags que se solapan)
- fix: **Motivos de cancelación** — si hay `motivoCancelacion`, se agrupa por eso sin mostrar payment; payment solo para los sin motivo
- feat: **Links clickeables** en motivos de cancelación navegan a `/orders` con filtros exactos
- feat: **Filtros OrderList** — agregados `loOnly`, `loCancelled`, `motivoCancelacion`, `mpPaymentStatus`, `mpPaymentStatusDetail`, `sinMotivo` (sin afectar existente)

Archivos backend: `Controllers/Statistics/Lo/` (6), `Services/Statistics/Lo/`, `Repositories/Statistics/Lo/`, `routes/api.php`, `OrderListRepository.php`, `OrderList.php`
Archivos frontend: `pages/libreOpcion/` (4), `store/libreOpcion.js`, `components/LibreOpcion/`, `components/Table/TabMenuLO.vue`, `components/Filters/LibreOpcion.vue`, `layouts/basic.vue`
Branch: `feature/dashboard-lo`

## 2026-04-06

- fix: **Retiro siempre visible en shippingMethods** — eliminado early return que impedía agregar "Retiro" (id 3999) cuando la query por `companyCode` no devolvía resultados de la DB
- docs: nuevas memorias de proyecto (syncUp auth, múltiples DBs, branching)

Archivos: `ShippingMethodService.php`
Branch: `hotfix/shipping-retiro-always`

## 2026-03-31

- feat: **Billing Kit Report** — nuevo reporte Excel de kits facturados (controller, service, repository, export)
- fix: nombre de cliente en reporte de kits
- feat: checks post-deploy en Gamma (GitHub Actions workflow)

Archivos: `BillingKitReportController.php`, `BillingKitReportService.php`, `BillingKitReportRepository.php`, `ExcelExportBillingKitReport.php`, `deploy-gamma.yml`

## 2026-03-25 — 2026-03-26

- fix: **ID_ARTICULO null en [[modulo-makesale|MakeSale]]/[[modulo-removesale|RemoveSale]]** — proteger queries con ISNULL para evitar SQL malformado cuando LEFT JOIN no matchea
- fix: usar `ID_Articulo` (de pedclil) en registerStock en vez de `ID_ARTICULO` (de stocks, puede ser null)
- fix: espacio en búsqueda (search)

Archivos: `MakeSaleService.php`, `RemoveSaleService.php`, `MakeSaleRepository.php`

## 2026-03-20

- feat: **Objetivos Gigabyte** — incentivo reutilizable para marca Gigabyte
- feat: objetivos de ventas (backend + frontend)
- fix: respuesta XLSX en reporte

Archivos: `incentivoGigabyte.vue`, `TabMenuDashboard.vue`

## 2026-03-18 — 2026-03-19

- feat: **Kit Report** — reporte de billing de kits
- fix: IVA en kits para sucursal 10
- fix: decompose bundle (descomposición de kits)
- fix: stock en [[modulo-removesale|RemoveSale]]
- fix: listado de productos

## 2026-03-17

- fix: **companyCode en login** — corregir query de auth con ISNULL para includeNull
- fix: **download order warehouse** — respetar `ID_ALMACEN` original del item al descargar pedido
- feat: validación básica post-deploy en Gamma
- refactor: filtro companyCode en ShippingMethods, PaymentMethods y Sellers
- feat: proforma en pedidos (PED-1325)

Archivos: `AuthRepository.php`, filtros de Sellers/Shipping/Payment en frontend

## 2026-03-16

- perf: **optimización de búsqueda de productos** — CONTAINS full-text en vez de LIKE
- perf: eliminar JOINs inutilizados en GetProducts/GetProductById
- perf: reemplazar subconsultas correlacionadas de stockInMyOrder por JOINs
- fix: restaurar LIKE en CDETALLE para substrings
- fix: urldecode en search para compatibilidad

## 2026-03-13

- hotfix: **MercadoLibre sync** — usar `unit_price` como fallback cuando `full_unit_price` no existe
- fix: restaurar JOINs de fotos y prefixar FOT.checksum

## 2026-03-12

- feat: eliminar impuesto interno al agregar a la orden
- fix: **moveItem con kits** — descomponer kits en componentes al mover, preservar precio del origen
- fix: eliminación del origen para items normales en moveItem
