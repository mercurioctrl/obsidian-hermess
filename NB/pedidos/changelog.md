
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
