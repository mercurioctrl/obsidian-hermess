## 2026-05-18 — Frontend

Merges a `development` (pull de hoy):

- fix: **etiquetas se borran al agregar producto** (PED-1358) — las etiquetas de la orden desaparecían al agregar un nuevo artículo; relacionado con flag "Mostrar en Orden". `Detail.vue`.
- feat: **comentario de factura** (PED-1363) — se puede agregar un comentario al generar la factura. `Detail.vue` + `CloseSale.vue` (170 líneas modificadas).
- fix: **liquidación — moneda mostrada** (PED-1359) — en LASET (`companyCode=11`) los medios de pago en pesos no debían verse. Refactor usa permiso `.can('viewPesos')` en vez de hardcodear divisas. `CloseSale.vue` + `plugins/api.js`.
- feat: **filtro en selector de forwarders** (PED-1361) — al escribir en el selector de forwarders/condición de venta en el detalle de OC, ahora filtra. Mejoras de tipografía y padding. `Detail.vue`.

Archivos: `app/components/Orders/CloseSale.vue`, `app/components/Orders/Detail.vue`, `app/layouts/basic.vue`, `app/plugins/api.js`.

Ramas nuevas recibidas (aún sin mergear a `development`): `PED-1362-comentario-factura`, `PED-1365-api-refactor`, `LAW-69-api-ped-refactor`.


## 2026-05-13

- feat: **nuevo medio de pago id=21 con comportamiento de pago diferido** — funciona igual que el id=16 (pago diferido): verifica crédito disponible del cliente antes de liquidar y autoriza directo a status 2 (autorizado pendiente de preparar).
  - Archivos: `Services/Liquidate/LiquidateServices.php` (constante `DEFERRED_PAYMENT_21 = 21`, condición en `verifyPaymentDeferred`), `Services/Liquidate/CreateOrder.php` (mapa `payment()` y condición en `authorization()`)
  - Rama: `deve-fix-linea-creidto-laset` (basada en `Development`, pusheada a origin)

# Changelog

Registro de cambios del proyecto, agrupado por fecha.

## 2026-04-25

Continuación de iteraciones sobre [[feature-asignacion-oc|Asignación OC ↔ Venta]]:

- feat: **modo solo lectura para pedidos remitidos** — el modal se puede abrir con `pedclit.cestado='S'` pero todo queda deshabilitado (inputs, checkboxes, botones de acción). Alerta info arriba, botón cambia de ✏️ a 👁️ en `Detail.vue`, footer solo "Cerrar". Acepta asignaciones en estado `'V'` o `'C'` (consumidas por el trigger). Genera filas huérfanas para OCs cuyo saldo ya se agotó y no vienen en `candidatasFifo`.
- feat: **persistencia del checkbox "costo seleccionado" en DB** — nueva columna `pedclil_oc_asignacion.costo_seleccionado BIT NOT NULL DEFAULT 0`. Reemplaza localStorage (que era por-browser). Ahora portable entre máquinas. Camino: PUT items incluyen flag → `ReemplazarAsignacionRequest` valida → service propaga → `insertAsignacion` graba → `asignacionesDeLinea` devuelve → modal precarga.
- feat: **extender duración de sesión JWT a 60 días** — `.env backend` `JWT_EXPIRATION_TIME="now + 60 days"`; `nuxt.config.js` `refreshToken.maxAge = 60 * 60 * 24 * 60`. Rationale: evitar relogins operativos frecuentes. Rotar `JWT_SIGNATURE_KEY` si hay filtración.
- infra: scripts SQL nuevos `database/sql/2026_04_25_001_{add,drop}_costo_seleccionado.sql` — idempotentes, con `USE [NewBytes_DBF]; GO` y `sys.columns + sys.tables` en lugar de `INFORMATION_SCHEMA`.
- gotcha: **SSMS pegar apply+drop en la misma ventana los ejecuta a ambos** → la columna apareció y desapareció, rompiendo `asignacionesDeLinea` con *"Invalid column name 'costo_seleccionado'"*. Fix: tratar cada script como archivo separado.
- gotcha: `SET IMPLICIT_TRANSACTIONS ON` (default en algunas sesiones SSMS) produce warning cosmético "ROLLBACK TRANSACTION sin BEGIN TRANSACTION" en los DDL. Ignorar, o `SET IMPLICIT_TRANSACTIONS OFF;` arriba del script.

Archivos:
- Backend: `Asignacion/AsignacionRepository.php` (SELECT + INSERT con `costo_seleccionado`), `Asignacion/AsignacionService.php` (propagación), `Http/Requests/Asignacion/ReemplazarAsignacionRequest.php` (validación), `database/sql/2026_04_25_001_*.sql`, `.env` (JWT_EXPIRATION_TIME).
- Frontend: `Modal/AsignarOCModal.vue` (prop `readOnly`, filas huérfanas, checkbox persistido, footer condicional), `Orders/Detail.vue` (ícono dinámico edit/eye, `:read-only="!isPending"`), `nuxt.config.js` (refreshToken maxAge).
- Docs: `docs/asignacion-oc-pedclil.md`, `CLAUDE.md`.

**Deploy**:
- Frontend: commit de `nuxt.config.js` ya pusheado a `feature/asignacion-oc-pedclil` (4a36d6c). El resto de cambios aún sin committear.
- Backend: editar `.env` en el servidor + `config:clear` + correr `2026_04_25_001_add_costo_seleccionado.sql` en SQL Server (solo el apply, no el drop).

## 2026-04-24

Iteraciones sobre [[feature-asignacion-oc|Asignación OC ↔ Venta]] post primer merge a Development:

- feat: **`cantidad: 0` = eliminar item** — el endpoint `PUT /v1/asignaciones/lineas/{id}` ahora ignora silenciosamente items con cantidad 0 en vez de tirar 422.
- feat: **items vacíos / todos en 0 = liberar todo** — short-circuit en `reemplazarAsignacionLinea` que actúa como `DELETE`, devolviendo `liberadas` extra en el payload.
- feat: **columna Proveedor** en el modal — JOIN `vw_saldo_oc → PedProT → FP_Proveedores` en `candidatasFifo` expone `proveedor_nombre`. UI con `ellipsis: true` por nombres largos.
- feat: **columna Proforma** en el modal — `pt.CSUPROF_TEMP` propagada en `candidatasFifo` y mapeada en la fila.
- feat: **link OC clickeable** — el número de OC abre `https://compras.saftel.com/orders?currentPage=1&search={oc}&between=...&companyCode={cc}` en nueva pestaña.
- fix: **modal no auto-sugiere FIFO si ya hay vigentes** al reabrir — antes proponía cantidades de FIFO para OCs sin vigente, lo que confundía al operador (parecía que el save no había funcionado). Ahora respeta lo guardado y deja el resto en 0; el botón "Aplicar FIFO" sigue disponible para redistribuir.
- chore: rama frontend rebaseada sobre `Development` actual (incluye refactor `AsignarOcModalMejoras`: z-index modal, focus en input cantidad, estado P/S con label "Pendiente"/"Remitida"). Force-push con `--force-with-lease`.

**Tercera tanda de iteraciones (misma fecha, flujo "Guardar con costo" + UX del dropdown):**

- feat: **título dinámico del modal** — `{branch} - {order} - {id_articulo} - {nombre_producto} (Asignar línea de compra)`. Requiere `articulo.cDetalle` (LEFT JOIN en `pedclilInfo`).
- feat: **checkbox por fila en columna Costo** — permite seleccionar qué OCs usar para el cálculo del costo promedio. Estado persiste en `localStorage['asignarOC.costoTildados.{pedclilId}']` entre aperturas del modal.
- feat: **bloque "Costo promedio ponderado"** debajo de los alerts — fórmula `Σ(costo × cantidad) / Σ(cantidad)` sobre filas tildadas con cantidad > 0. Si hay una sola fila muestra "Costo seleccionado: X"; si son múltiples, "Costo promedio ponderado (N OCs · X u): Y".
- feat: **botón "Guardar con costo"** en footer custom del modal — además de persistir la asignación OC, hace `PATCH /v1/orders/addItem` con `costForSale = promedio ponderado`. `Detail.vue::onAsignacionGuardada` escucha `saved: { conCosto }` y refresca el detalle si aplica.
- feat: **tag "ASIGNADA"** (violeta) en el dropdown de Costo de `Detail.vue` — heurística: compara `Math.round(costForSale * 100) / 100 === store.getters['asignaciones/costoPonderadoPorLinea'](...)`. Requiere que `asignacionesDeLinea` traiga `costo` (JOIN a `pedprol.nPreDiv`).
- fix: **redondeo consistente (bug 139,73 vs 139,72)** — `toLocaleString` y `toFixed` dan resultados distintos en bordes tipo `139.725`. Reemplazado por `Math.round((x + Number.EPSILON) * 100) / 100` en modal Y store, para que match exacto sea posible.
- feat: **dropdown de Costo rediseñado** en `Detail.vue` — cada opción es `precio (monospace, verde) + meta (bandera + proveedor · depósito)` con tags semánticos (ACTUAL / PROMEDIO / ASIGNADA). `dropdown-match-select-width=false` + `minWidth: 320px` para que entre todo. Tabular-nums alinea los precios como columna.
- feat: **endpoint `pedclilInfo` extendido** — ahora retorna `producto_nombre`, `id_almacen`, `lista_precio`, `npreunit` (para armar el PATCH de addItem) y se propagan en el payload de `sugerirFifo`.
- infra: **`selectedPrice` del PATCH `/orders/addItem`** debe ser `pedclil.npreunit` (precio unitario real), NO `listaPrecio` (código de lista). El backend valida `> 0` — mandar 0 tira *"No se permite un precio menor o igual a 0"*.

Archivos:
- Backend: `Asignacion/AsignacionRepository.php` (+3 JOINs en `pedclilInfo`, +costo en `asignacionesDeLinea`), `Asignacion/AsignacionService.php` (propaga campos nuevos).
- Frontend: `Modal/AsignarOCModal.vue`, `Orders/Detail.vue` (método `costoVieneDeAsignacion`, slot de costo rediseñado, handler `onAsignacionGuardada`), `store/asignaciones.js` (+getter `costoPonderadoPorLinea`).
- Docs: `docs/asignacion-oc-pedclil.md`, `CLAUDE.md`.

**Segunda tanda de iteraciones (misma fecha, nuevas features de contexto en el modal):**

- feat: **columna Costo** en el modal — `pedprol.nPreDiv` joineado por `nNumPed + cRef` en `candidatasFifo`. Formato `es-AR` con 2 decimales. Width del modal pasó a 900px.
- feat: **endpoint `/v1/asignaciones/stock-almacenes`** (GET) + método `AsignacionRepository::stockPorAlmacen` → stock físico del SKU por depósito (JOIN `stocks + FP_Almacen`, filtra `deleted_at IS NULL` y `nstock > 0 OR reservado > 0`).
- feat: **endpoint `/v1/asignaciones/comprometido`** (GET) + métodos `pedidosPendientesPorArticulo` y `remitosSinFacturarPorArticulo` → devuelve `{pedidos, remitos}` del mismo SKU (pedidos = `pedclit.cestado='P'` misma company; remitos = `albclit.lfacturado=0`). Top 50 de cada uno.
- feat: **bloques de contexto en el modal** — chips de stock por depósito debajo de la tabla + `a-collapse` con dos paneles (órdenes pendientes / remitos sin facturar) que el operador puede expandir para ver qué compromete el SKU. Contexto read-only **fuera** del `<a-table>` editable (patrón [[feedback_modal_contexto_vs_edicion|separar edición de contexto]] — ver memoria local).
- docs: [[feature-asignacion-oc-cookbook|cookbook]] actualizado con receta nueva "Agregar bloque de contexto al modal", queries SQL de stock/compromisos, curls ejecutables. [[feature-asignacion-oc|feature note]] lista 7 endpoints (antes 5). Memoria local cross-sesión actualizada con schema de `stocks`/`FP_Almacen`/`albclit`/`clientes` (hay dos PKs: `ccodcli` vs `ID_CLIENTE` según tabla).

Archivos (cambios working-tree, aún sin commit):
- Backend: `Asignacion/AsignacionRepository.php`, `Asignacion/AsignacionService.php`, `Asignacion/AsignacionController.php`, `routes/api.php`
- Frontend: `Modal/AsignarOCModal.vue`, `plugins/api.js`
- Docs: `docs/asignacion-oc-pedclil.md`, `CLAUDE.md`

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

## 2026-05-12

- fix: **arreglo join albclitshipping** — corregido JOIN en `OrderListRepository.php` relacionado a la tabla de shipping por albarán de cliente.
- feat: **cupón Libre Opción** — lógica de aplicación de cupones en pedidos LO. Archivos: `OrderRepository.php`, `UnprocessedOrdersRepository.php`, `OrderService.php`.
- fix: **`salespersonId` ahora actualiza también `ccodage`** — al hacer PATCH `/v1/clients/{id}/params`, además de guardar en `ID_VENDEDOR`, se actualiza `ccodage = RIGHT('00'+ISNULL(valor,''),2)`. Regla de negocio: `ccodage` debe mantenerse sincronizado con `ID_VENDEDOR` en `NewBytes_DBF.dbo.clientes`. Archivo: `Services/Client/ClientParametersService.php`.
- fix: **removida restricción `ncosteprom > 0`** en `GetProducts` (`ProductRepository.php`) — artículos con costo promedio en 0 o NULL ahora aparecen en el listado. La restricción impedía buscar artículos recién cargados sin costo.

Archivos: `Services/Client/ClientParametersService.php`, `Repositories/Product/ProductRepository.php`, `Repositories/Order/OrderList/OrderListRepository.php`, `Repositories/Order/OrderRepository.php`

Rama: `hotfix-salesperson-and-ncostreprom-ccodage` (basada en `Development`, pusheada a origin)

## 2026-05-14

Sesión de **descubrimiento + scaffolding del [[feature-laset-import|Laset Import Framework]]** (companyCode=11). Branch `lasetImportFramework` creada en ambos repos basada en `Development`/`development` recién sincronizadas.

- discovery DB: identificadas las 11 empresas activas en `FP_Empresas` (no solo NB/NBElectric/LO como decía el `CLAUDE.md`). Laset = CODEMP 11, importadora uruguaya con `defaultIncoterms=14`.
- discovery ERP: mapeo canónico **compras = `pedprot` + `pedprol` + `pedproi`**, **ventas = `pedclit` + `pedclil`**, **stock = `stocks`** (filtrado por almacén — no tiene `companyCode`). `pedclil_oc_asignacion` linkea ambos. Estado actual companyCode=11: 386 compras + 363 ventas + 179 CFE Uy + 84 forwarders + 158 cargos extra ya migrados.
- gotcha confirmado: **`pedproi` no es solo impuestos** — guarda también cargos extra del pedido de compra (`cdescrip='camion'` $50/$200). Linkea a `pedprot.nNumPed`, NO a `pedclit`.
- gotcha confirmado: tabla `rebates` (12 rows) + `NewTable` (0 rows) son **huérfanas** — restos de intento abandonado del 2025-11-01. Sin `companyCode`. NO usar.
- discovery CFE Uruguay: las 4 tablas `FP_*_Uy` (Encabezado, Detalle, Documentos, Comprobantes) son **la mitad downstream de Laset ya implementada** — emiten CFE uruguayos con IVA 22% en DOL a clientes LATAM. 179 facturas + 1411 líneas con adendas que confirman beneficiario "Laset Sociedad Anonima".
- creadas tablas staging: **`laset_import_batches`** (cabecera por carga, 9 cols) + **`laset_import_staging`** (1 fila por fila de Excel, 67 cols crudas en NVARCHAR lossless + 8 cols de matching con CHECK enum). En `NewBytes_DBF.dbo`. 5 índices: batch, sku, customer_invoice, vendor_invoice, status.
- scripts DDL versionados: `2026_05_14_001_create_laset_import_staging.sql` + drop simétrico. Aplicados al SQL Server.
- regla cero del feature: **NUNCA modificar tablas ERP existentes** (`pedprot`/`pedprol`/`pedproi`/`pedclit`/`pedclil`/`stocks`/`FP_*`/`forwarders`). Solo lectura via JOIN; toda metadata de matching vive en `laset_import_staging.matched_*`.
- bug menor recuperado: `git branch -D development` en backend (case-insensitive macOS) borró también `Development`. Recuperado con `git reset --hard origin/Development`.
- documentación: `docs/laset-import-framework.md` (nuevo, 250+ líneas), sección "Laset Import Framework" agregada al `CLAUDE.md` del repo.

Archivos: `docs/laset-import-framework.md`, `api-rest-pedidos-laravel/app/database/sql/2026_05_14_001_{create,drop}_laset_import_staging.sql`, `api-rest-pedidos-laravel/app/database/sql/README.md` (entrada nueva), `CLAUDE.md`.

Branch: `lasetImportFramework` (ambos repos, basada en development/Development sincronizadas).

Próximo paso: cargador PHP que parsee `docs/laser.xlsx` y popule la staging, después reconciliación.

### 2026-05-14 — continuación (matching agregado + plan migración)

Después de cargar las 3007 filas a staging en la sesión previa, esta jornada se cerró con la reconciliación, el matching agregado y la decisión de migración.

- **Reconciliación implementada** (DB views, read-only sobre ERP):
  - `vw_laset_planilla_compras` / `vw_laset_planilla_ventas` — agregado staging por SKU.
  - `vw_laset_erp_compras` / `vw_laset_erp_ventas` / `vw_laset_erp_stock` — agregado ERP por id_articulo + comp=11 + almacenes Laset.
  - `vw_laset_sku_bridge` — UNION articulo + alias.
  - `vw_laset_reconciliation` — vista maestra con deltas y bridge_status.
- **Bridge SKU descubierto**: `articulo.ID_PRODUCTO` (varchar) = SKU del fabricante, `articulo.ID_ARTICULO` (int) = PK interna. Cobertura inicial 620/739 (84%) directa.
- **Tabla `laset_sku_alias`** creada (en `NewBytes_DBF.dbo`) para persistir normalizaciones automáticas + decisiones manuales. Bridge view refactorizado a UNION articulo + alias. Script `database/sql/2026_05_14_003_create_laset_sku_alias.sql`.
- **Normalizaciones fuzzy aplicadas** (sku planilla → ID_Articulo):
  - `auto:trim` (newlines/whitespace trailing — ej. `'MAG255FE20\n'`)
  - `auto:nospace`, `auto:nohyphen`, `auto:hyph2sp`, `auto:sp2hyph`, `auto:alnum` (paréntesis, mayúsculas)
  - `auto:split-slash` (ej. `'PBE120GS25SSDR / PE000775'` → matchea por la parte izquierda)
  - `auto:last-word` (ej. `'NC Apoyo precio 100-100000593WOF'` → matchea última palabra)
  - 14 SKUs huérfanos recuperados con normalizaciones.
- **5 services marcados** automáticamente con `source='service'` (`Fondos Laset`, `PRINTING FEE`, `Transporte aereo`, `Flete Carga Bonded Fastmark`, `RMA %`).
- **Aggregate matching aplicado** vía tabla tmp + UPDATE FROM JOIN (evitando dblib segfault con UPDATE loops). Categorías:
  - MATCHED (planilla=ERP exact) = 536 filas
  - PARTIAL (discrepancias) = 1860 filas
  - DELTA_ONLY (ERP vacío) = 65 filas
  - NO_BRIDGE = 147 filas
  - IGNORED (basura+services) = 399 filas
- **Decisión clave de negocio (usuario)**: **planilla = fuente de verdad** para comp=11. El ERP comp=11 actual es ex-carga-fallida (146 SKUs con `ERP > Planilla` por duplicación de ~10× en casos como `Ajuste precio A520MAPRO` plC=280 / erpC=2260, 214 con `Planilla > ERP` por undercount).
- **PARTIAL promovido a MATCHED** (score=90) + DELTA_ONLY promovido a MATCHED (score=80). **Total importable: 2461 filas** (82%).
- **Plan de migración 3 fases acordado**:
  - **A**: alta de los 100 SKUs huérfanos en `articulo` por equipo catálogo (CSV en `docs/laset_orphan_skus.csv` + `.md`).
  - **B**: DELETE de filas ERP comp=11 sin contraparte en planilla. REGLA CRÍTICA: `WHERE companyCode = 11` SIEMPRE. Otras companies intocables.
  - **C**: INSERT de las 2461 MATCHED a pedprot/pedprol/pedproi/pedclit/pedclil + pedclil_oc_asignacion.
- **Gotchas técnicos catalogados** (ver [[memoria]] y [[feature-laset-import#10. Gotchas]]):
  - PhpSpreadsheet inviable >15 min → preprocesar con Python+openpyxl en host
  - dblib segfault con UPDATE loops → tabla tmp + UPDATE FROM JOIN
  - dblib no auto-castea DECIMAL → INT en tmp para scores
  - SQL Server 2012 — sin `CREATE OR ALTER VIEW`, sin `DROP VIEW IF EXISTS`
  - `pedprot.sitio=0` vs `pedprol.sitio=NULL` → joinear solo por `nNumPed`
  - macOS case-insensitive: `git branch -D development` puede romper `Development`
- **Scripts SQL versionados (database/sql/)**:
  - `2026_05_14_001_create_laset_import_staging.sql` (+drop) — tablas staging
  - `2026_05_14_002_create_laset_reconciliation_views.sql` (+drop) — vistas
  - `2026_05_14_003_create_laset_sku_alias.sql` (+drop) — alias + refactor bridge
- **Backend**: `LasetImportStagingCommand`, `scripts/laset_xlsx_to_json.py`.
- **Docs**: `docs/laset-import-framework.md` actualizado a v2 (sección 7 decisiones, 8 plan migración, gotchas técnicos), `docs/laset_orphan_skus.{csv,md}` generados.

Próximo: fase A (equipo catálogo), portar aggregate-match a artisan command, diseñar fase B+C.

### 2026-05-14 (PM) — Laset Fase B ejecutada + discovery Fase C

**Fase B aplicada**: DELETE total ERP companyCode=11 — 7822 filas borradas.

| Tabla | Filas borradas |
|---|---:|
| `pedprot` | 386 |
| `pedprol` | 1349 |
| `pedproi` | 31 |
| `pedclit` | 363 |
| `pedclil` | 1847 |
| `albprot` | 526 |
| `albprol` | 1205 |
| `albclit` | 331 |
| `albclil` | 1746 |
| `pedclil_oc_asignacion` | 38 |

- **Decisión**: `DELETE total + re-INSERT` en lugar de row-level matching, porque el matching staging↔ERP es agregado por SKU (no fila-a-fila).
- **Backups in-DB** en `NewBytes_DBF.dbo.laset_phase_b_backup_*` (10 tablas) — mantener hasta validar Fase C. Permiten rollback con INSERT FROM SELECT.
- **Aislamiento verificado**: snapshot pre/post por company. Otras companies (4/9/etc) intactas.
- **Script**: `database/sql/2026_05_14_004_phase_b_delete_comp11.sql` con backups + JOINs compuestos `(cnumped, cnumsuc)` + pre-check assertions con `THROW`.

**Bug crítico atrapado en revisión SQL pre-ejecución**: el script inicial usaba `WHERE cnumped IN (SELECT cnumped FROM pedclit WHERE companyCode=11)` que habría borrado 5 ventas legítimas de NB (cnumped 10338002, 10338022, 10338027 colisivos entre comp=11 y comp=4). PK efectiva de pedclit es `(cnumped, cnumsuc)` — uq_pedclit. Refactorizado a `DELETE x FROM x JOIN pedclit t ON t.cnumped=x.cnumped AND t.cnumsuc=x.cnumsuc WHERE t.companyCode=11`. Misma corrección aplicada a pedclil/albclit/albclil. `pedprot.nNumPed` y `albprot.nnumalb` sí son únicos globalmente, esos OK.

**Otro bug detectado**: conteo inicial `albprot=370` era falso (subselect cruzado mal armado `nnumalb IN nNumPed`). Conteo real `WHERE companyCode=11`: **526 filas** (rango 2026-03-02 → 2026-05-12). De los 526, 369 con pedprot padre + 157 "remitos huérfanos" (compras directas sin OC).

**Pre-check assertions**: pedido explícito del usuario — antes de cada DELETE, batch separado con `DECLARE @bad INT; SELECT @bad = COUNT(*) ... WHERE …; IF @bad > 0 THROW 50001, [ABORT], 1; GO`. El loader PHP propaga la excepción y aborta antes de tocar nada. Defense in depth.

**Discovery Fase C** (no implementada todavía):
- Schema mapeado de las 6 tablas a poblar: pedprot 34 cols (`id_pedprod` IDENTITY, `nNumPed` manual desde MAX+1=13219), pedclit 78 cols (`id` IDENTITY, `cnumped` manual desde MAX+1=10459501, `ccodcli` NOT NULL), pedprol 25, pedclil 42, pedproi 16 (`lcalcuauto` NOT NULL), pedclil_oc_asignacion 19.
- Agrupación: 2461 filas MATCHED → 417 pedprot únicas (por proveedor+vendor_pi+vendor_invoice) + 396 pedclit únicas (por razon_social+customer_pi+customer_invoice). Total ≈ 4078 INSERTs.
- **Bloqueante de mapping resuelto**: tabla maestra moderna es **`FP_Proveedores`** (no `proveedo`, que tiene `cnompro` vacío para Laset). Match staging.proveedor → FP_Proveedores comp=11 estricto: **25/28 OK**, 3 a auto-crear.
- Match clientes: 50/56 OK con `clientes WHERE companyCode=11`, 6 a auto-crear.
- Match SKUs: 806/820 OK vía `articulo.ID_PRODUCTO`, 14 bloqueados (Fase A pendiente).
- **Regla confirmada por usuario**: proveedores y clientes **NUNCA se comparten entre companies**. Si pedprot/pedclit comp=11 referencia un ccodpro/ccodcli de otra company, es data sucia de la ex-carga-fallida (varios ejemplos detectados: ccodpro 002300/000847/001130 = NB comp=4; ccodcli 096117 MASTER COMPUTERS = comp=4).

**Decisiones tomadas con usuario para implementación Fase C**:
- Forma: artisan command PHP `laset:import-fase-c` con `--dry-run / --limit / --chunk`.
- FKs faltantes: auto-crear `FP_Proveedores`/`clientes` mínimos con `companyCode=11`.
- Idempotencia: `WHERE match_status=MATCHED AND matched_pedprot_nnumped IS NULL`. Filas IMPORTED se skipean.

**Pendiente** (próxima sesión): implementar el comando, dry-run, ejecución real.

**Memoria nueva** (local + bóveda):
- [[feedback_pedclit_pk_compuesta]] — PK efectiva `(cnumped, cnumsuc)`, no usar IN sobre cnumped.
- [[feedback_pre_check_assertions_destructivos]] — Patrón THROW antes de DELETE destructivos.
- [[project_erp_master_tables_fp]] — FP_Proveedores moderna vs proveedo legacy + regla nunca-compartido.

**Scripts SQL**:
- `database/sql/2026_05_14_004_phase_b_delete_comp11.sql` (+ esqueleto rollback simétrico).

### 2026-05-14 (noche) — Laset Fase C ejecutada + fix almacenes + reset stocks

**Fase C ejecutada completa**: 2439 filas staging IMPORTED → ERP comp=11.

| Tabla | Insertadas |
|---|---:|
| FP_Proveedores | +3 (auto-create) |
| clientes | +6 (auto-create) |
| pedprot | 506 |
| pedclit | 392 |
| pedprol | 2439 |
| pedclil | 2439 |
| pedclil_oc_asignacion | 2439 |
| **TOTAL INSERTs** | **8224** |

- Comando: `php artisan laset:import-fase-c [--dry-run] [--limit=N] [--chunk=50]`. Idempotencia via `WHERE match_status='MATCHED' AND matched_pedprot_nnumped IS NULL`.
- Ejecución gradual: --limit=10 (validación), --limit=100, --limit=500, sin limit. dblib aguantó las transacciones grandes sin segfault.
- IDs generados: nNumPed 13219→13632, cnumped 10459501→10459887.

**Bug almacenes Laset detectado y arreglado** (corregido por usuario: *"los de laset no pueden estar nunca en SAF"*):
- Mapping inicial mappeaba BONDED-FASTMARK→SAF (almacén de NB comp=4). 3 pedprot mal asignados.
- Mapping intermedio "fix" creó otro bug peor: asumió URU/ASI no existían y los puso en IDs 17/18, pero ya existían como ID 14/15 → 110+53 pedclil con ID_ALMACEN huérfano.
- Mapping final correcto: DOM=9, BON=11 (consolida BONDED-*), GRI=10, URU=14, ASI=15. Todos verificados en `FP_Almacen WHERE companyCode=11`.
- Las 3 columnas relacionadas deben coordinarse SIEMPRE: `pedprot.cCodAlm`+`warehousesId`, `pedclit.ccodalm`+`ID_ALMACEN`, `pedclil.ID_ALMACEN`.

**Reset stocks comp=11** (corregido por usuario: *"lo anterior debías sacarlo, si al pisarlo con lo de la planilla ya te ds el stock"*):
- 286 filas reseteadas a 0 con DOBLE FILTRO: `articulo.companyCode=11 AND stocks.cCodAlm IN (almacenes Laset)`.
- 302 filas con articulo.companyCode=4 (NB) en almacenes Laset PRESERVADAS (17 unidades, items compartidos físicamente).
- Backup en `laset_phase_b_backup_stocks` (incluye snapshot de articulo_companyCode).

**Identidad contable post-reset**:
- Saldo neto agregado comp=11: compras=101517, ventas=101517, **saldo=0** ✓
- Por SKU global: **657/657 cuadran (100%)** ✓
- Por (SKU, almacén): **1059/1090 cuadran (97%)**. Las 31 discrepancias restantes son **cross-warehouse normal** del ERP (compra en X, venta desde Y, neto SKU=0).

**Memorias nuevas** (local + bóveda):
- [[memoria#Doble filtro company del item + del almacén]] — para `stocks` y otras tablas sin companyCode propio.
- [[memoria#Almacenes Laset reales]] — DOM/BON/GRI/URU/ASI; SAF NO es de Laset.

**Backups in-DB activos** (mantener hasta validar B+C en producción):
- `laset_phase_b_backup_*` (10 tablas, Fase B)
- `laset_phase_b_backup_stocks` (Fase reset stocks)

### 2026-05-15 — Replicación a producción: runbook + scripts + comandos versionados

**Objetivo**: dejar todo listo para replicar Fase B+C en producción de manera segura y documentada.

**Generados**:

| Archivo | Tipo | Qué hace |
|---|---|---|
| `app/Console/Commands/LasetAggregateMatchCommand.php` | Artisan | `php artisan laset:aggregate-match [--dry-run]`. Porta el script ad-hoc `/tmp/aggregate_match2.php` con regla planilla=verdad. Tabla tmp + UPDATE FROM JOIN single-statement (evita dblib segfault). |
| `app/scripts/laset_reset_stocks.php` | Script PHP | Reset stocks comp=11 con doble filtro (item+almacén). Backup automático en `laset_phase_b_backup_stocks`. Pre-checks con THROW. Soporta `--dry-run`. |
| `app/scripts/laset_pre_flight_prod.php` | Script PHP | Read-only. 9 secciones: objetos del feature, conteos comp=11 vs baseline dev, actividad reciente, FP_Almacen IDs, snapshot otras companies, MAX(IDs), staging actual, stocks doble filtro, checklist GO/NO-GO. |
| `app/scripts/laset_post_flight_validation.php` | Script PHP | Read-only. Verifica backups in-DB, conteos esperados, identidad SKU global ≥99%, almacenes válidos, doble filtro stocks. Exit code 0/1 para CI. |
| `docs/laset-import-runbook-prod.md` | Doc | Runbook 11 pasos: pre-requisitos, backup DBA, ventana, DDL, carga planilla, aggregate match, Fase B+C, reset stocks, validación, rollback parcial/full, limpieza final. |

**Validación dry-run de los nuevos comandos en dev**:

```
laset:aggregate-match --dry-run
  925 combinaciones SKU → MATCHED 820 / UNMATCHED 100 / IGNORED 5
  MATCHED/100=614, /90=10, /80=10

laset_reset_stocks.php --dry-run
  Filas con doble filtro (item comp=11 + almacén Laset): 286
  Filas a PRESERVAR (item NO comp=11 en almacén Laset): 302 (17 unidades)
```

Coincide con lo aplicado manualmente en la sesión 2026-05-14.

**Actualizado**:
- `CLAUDE.md` (raíz proyecto): sección "Artisan Commands" con los 3 comandos Laset.
- Runbook: referencias a los nuevos artisan commands en lugar de scripts ad-hoc.

**Para correr en producción** (resumen):
1. Pre-flight (read-only) → coordinar surprises
2. Backup full DBA + ventana de mantenimiento
3. DDL 001/002/003 (si falta)
4. `php artisan laset:import-staging` (carga planilla)
5. `php artisan laset:aggregate-match` (NUEVO)
6. Service aliases manuales (si pre-flight detectó)
7. DDL 004 Fase B (con pre-checks THROW)
8. `php artisan laset:import-fase-c` (gradual: --limit=10/100/500/sin limit)
9. `laset_reset_stocks.php` (NUEVO)
10. Post-flight validation
11. Cierre + monitoreo 7-14 días + dropear backups in-DB

Doc canónico: [`docs/laset-import-runbook-prod.md`](repo)

---

### 2026-05-15 (cont.) — Laset Fase D (remitos + pedproi + stock) + fix defecto Fase C

**Hallazgo**: Fase C había creado solo las órdenes comp=11 (pedprot/pedprol +
pedclit/pedclil), sin remitos ni pedproi ni stock. Se implementó **Fase D**.

**Generado**:

| Archivo | Tipo | Qué hace |
|---|---|---|
| `app/Console/Commands/LasetImportFaseDCommand.php` | Artisan | `laset:import-fase-d [--dry-run --limit --chunk]`. Crea albprot/albprol/albclit/albclil + pedproi camion + stock compra(+)/venta(−) sobre órdenes comp=11 existentes. Fechas de documento respetadas. Idempotente. Pre-check de aislamiento (THROW si ID_Articulo del delta no es comp=11). |
| `database/sql/2026_05_15_001_reset_stock_comp11.sql` (+drop) | SQL | Paso 0 Fase D: reset stock comp=11 en almacén Laset, doble filtro articulo.companyCode=11, backup `laset_phase_b_backup_stocks`. |
| `database/sql/2026_05_15_002_fix_fasec_articulo_comp11.sql` (+drop) | SQL | Fix defecto Fase C: remap 5 SKUs con gemelo comp=11, backup + pre-check THROW. |
| `docs/laset_fasec_skus_sin_comp11.csv` | CSV | 39 SKUs sin artículo comp=11 para Fase A (catálogo), con impacto por SKU. |

**Defecto de Fase C detectado por el pre-check de Fase D**: `resolveMasters`
resolvía SKU→ID_ARTICULO sin filtrar companyCode → 56 pedprol + 56 pedclil de
órdenes comp=11 apuntaban a 44 artículos NB (comp=4).

**Fix**: (1) `resolveMasters` ahora filtra `articulo.companyCode=11`;
(2) SQL `2026_05_15_002` **aplicado en dev** — 8 pedprol + 8 pedclil remapeadas
a los gemelos comp=11, backups 56+56, articulo y otras companies intactas;
(3) 39 SKUs restantes → Fase A catálogo.

**Dry-run Fase D**: albprot=506, albprol=2439, albclit=392, albclil=2439,
pedproi=111, registro_stock=2439, stock neto=0.

**Estado**: Fase D BLOQUEADA hasta Fase A (39 SKUs) + re-bind Fase C. Ver
[[feature-laset-import#12. Sesión 2026-05-15 (cont.) — Fase D + fix defecto Fase C]].

---

### 2026-05-15 (cont. 2) — Laset Fase D pasada 1 ejecutada + snapshot/restore

**Fix Fase C aplicado**: SQL `2026_05_15_002` remapeó 8 pedprol + 8 pedclil
(5 SKUs con gemelo comp=11) a sus artículos comp=11. Backups 56+56.

**Fase D pasada 1 ejecutada en dev** (`laset:import-fase-d --skip-bloqueadas`):
493 albprot + 1454 albprol + 111 pedproi + 379 albclit + 2155 albclil + 2155
registro_stock. Stock 672/672 = delta. Difirió 15+15 órdenes (39 SKUs → Fase A).

Tres fixes en el camino (todos atajados por guards, sin data corrupta):
- Consolidación de líneas de remito por artículo (PK albclil = (ID_Articulo,
  ID_NROREMCLI_ENC); norma ERP confirmada en backups).
- UPSERT de stock (INSERT fila mínima si el combo no existía; ~64% faltaban).
- Set de almacenes Laset desde `FP_Almacen WHERE companyCode=11` (no
  hardcodear; URU/ASI reales = 14/15, no 17/18). Corrige reset SQL + comando.

Guards nuevos: ASSERT rollback si queda stock sin aplicar; auto-auditoría
remitos reales vs plan.

Identidad `compras − ventas − stock = 0` verificada: 684/721 = 0, los 37 ≠ 0
100% explicados por órdenes diferidas (cierran en pasada 2).

**Snapshot/Restore unificado** (reversibilidad total del proceso):
| Archivo | Qué |
|---|---|
| `app/Support/LasetSnapshotRegistry.php` | Registro único del alcance comp=11 (14 tablas, incl. cross-DB NB_WEB.registro_stock) |
| `app/Console/Commands/LasetSnapshotCommand.php` | `laset:snapshot {tag}` (--dry-run/--drop) |
| `app/Console/Commands/LasetRestoreCommand.php` | `laset:restore {tag}` (--dry-run/--force), IDENTITY_INSERT + trigger off/on, pre-check vs manifiesto |
| `database/sql/2026_05_15_003_create_laset_snapshot_manifest.sql` (+drop) | Tabla manifiesto |

Probado end-to-end: daño simulado (borrar albclil/pedproi, stocks=99999,
registro_stock) → `laset:restore` → estado bit-idéntico, identidad igual,
trigger rehabilitado. Punto `postPasada1` creado (15949 filas, 14 tablas).
Gotcha: `DISABLE/ENABLE TRIGGER` no admite prefijo de DB → `sp_executesql`
en contexto NewBytes_DBF.

**Workflow**: `laset:snapshot <tag>` ANTES de cada proceso/sesión →
si algo sale mal `laset:restore <tag> --force`. Ver
[[feature-laset-snapshot-restore]].
