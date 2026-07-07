# Changelog

Historial de cambios del proyecto Compras, basado en los commits de ambos repositorios.

## 2026-07-02

- feat (front, **COM-320**): **Moneda y cotización única en el header del detalle** de Orden e Ingreso. Consume los campos de divisa que se agregaron en la API (`currencyId`, `currencyQuote`, `currencyFiscalQuote`). Se muestra **una sola** fila "Cotización" según el caso: **pesos** (`currencyId === 'PSO'`) → usa `currencyFiscalQuote` (porque `currencyQuote` queda fijo en 1); **dólares** → usa `currencyQuote`. Nuevo computed `currencyQuoteComputed` / `isProviderInPesos` que unifica el cálculo de subtotales. Archivos front: `Orders/Detail.vue`, `ProviderOrderInbound/Detail.vue`, `Modal/Draggable.vue`, `layouts/basic.vue`, `pages/providerOrderInbound.vue`. Commits `877b288`, `02af31f`, `44252b7`, `fabad7e`. **Estado: mergeado a `gamma` (PRs #283/#285), pendiente de `development`.** Ver [[contexto#Cotización única en el header del detalle (COM-320, 2026-07-02)|contexto]].

## 2026-06-30

- feat: **Columna "Pedido" (remitos / `inboundIds`) en el listado de Órdenes** (COM-444). El API concatena los `nnumalb` de `NewBytes_DBF.dbo.albprot` por pedido vía `STUFF(... FOR XML PATH(''))` y los expone en `ProviderOrderDto.inboundIds`; el front agrega la columna con botones que navegan a la pestaña Ingresos filtrando por `nNumAlb` (`store/orders.js`, `pages/orders.vue`). PRs API #409/#410, front #281.
- fix: **Moneda y cotizaciones del Ingreso ahora desde `PedProt`** (rama `arreglos-divisa`, PRs #411–#414). `providerOrderInbound`: `currencyId` ← `PedProt.ccoddiv` (código `PSO`/`DOL`, antes `albprot.ccoddiv` devolvía el id numérico `1`); `currencyQuote` ← `PedProt.nValDiv`; nuevo `currencyFiscalQuote` ← `PedProt.nvaldiv_FISCAL`. DTO `ProviderOrderInboundDetailDto` actualizado. Ver [[contexto#Moneda y cotizaciones del Ingreso vienen de PedProt (2026-06-30)|contexto]].
- fix: **Recurso `items` ya no oculta artículos con `ocultarDeNb = 1`** (rama `quitar-filtro-ocultarDeNb-items`, PRs #415/#416). Ese flag es para la tienda web; en compras se deben poder buscar/ingresar. Se quitó `AND ocultarDeNb <> 1` del listado y del `count` (`ItemRepository`). Síntoma: buscar `104495` (Ducky One 2 SF White) no traía nada.
- fix: **Ingresos duplicados en el listado de `providerOrderInbound`** (rama `fix-ingresos-duplicados`, commit `e845061`). El `GROUP BY` incluía `albprol.nnumalb` (nullable por LEFT JOIN) además de `albprot.nnumalb` → cada remito salía 2 veces (uno con total real, otro con total 0/NULL). Se quitó `albprol.nnumalb` del GROUP BY. Además `count()` pasó de `COUNT(albprot.nnumalb)` a `COUNT(DISTINCT albprot.nnumalb)` (antes contaba filas del join → páginas de más). Ver [[contexto#Duplicados en listado de Ingresos (GROUP BY nullable) (2026-06-30)|contexto]].
- infra: el `.env` de la API se apuntó a **`10.10.10.47:1433`** con user **`cmercurio`** (entorno **saftel** / `compras.saftel.com`, companyCode 4). Ver [[contexto#Infraestructura / Base de datos (gotcha importante)|contexto]].

## 2026-06-29

- feat: **`currencyId` en los detalles** de Órdenes e Ingresos. El detalle de orden (`GET /v1/providerOrder/{id}`) ahora devuelve `currencyId` desde `PedProT.cCodDiv`; el de ingreso (`GET /v1/providerOrderInbound/{id}`) desde `albprot.ccoddiv` (ej. `PSO`/`DOL`), además de `currencyQuote`. Commits API `0c8249a`, `dc8240b` (`ProviderOrderDetailRepository`/`ProviderOrderDetailDto`, `ProviderOrderInboundRepository::getDetail`/`ProviderOrderInboundDetailDto`).
- infra: la DB dev `db-nb-dev.blu.net.ar:41433` se cayó; se repuntó el `.env` a **`10.10.10.47:1433`** (mismas credenciales `fcallipo`/`NB_WEB`). Ver [[contexto#Infraestructura / Base de datos (gotcha importante)|contexto]].

## 2026-06-26

- feat: **Export XLSX / CSV** (frontend, dep nueva **SheetJS `xlsx`**). Ver [[arquitectura#Exportación XLSX/CSV|arquitectura]] y [[contexto#Exportación de tablas (XLSX/CSV)|contexto]].
  - Botones XLSX/CSV en la línea de filtros de **Órdenes** e **Ingresos** que bajan **todo lo filtrado** (re-consultan el endpoint con los mismos filtros pero `itemsPerPage` alto, no solo la página visible). Reusan las columnas visibles del listado.
  - Botones en el **detalle de la orden** (barra arriba de la tabla de items) para exportar la tabla de items (`newItems`, excluye filas resumen). Subtotales calculados igual que en pantalla; para LASET omite columnas en `$`.
  - Util reutilizable `app/utils/tableExport.js` (`exportTable(columns, rows, filename, format)`): columnas por `dataIndex` o por función `value`. Commit front `b1a01c2`.

## 2026-06-24

- refactor: **La cuenta corriente de proveedores ahora lee el ledger oficial `NEW_BYTES.dbo.MS_MOV_CTACTE_PROVEEDORES`** en vez de armarse desde `FACPROT`/`FACPROL` (esa fue la primera versión, descartada). El recurso (`GET v1/providers/{providerCode}/currentAccount`) toma los movimientos del proveedor (`ID_PROVEEDOR = CCODPRO`), excluye anulados (`ANULADO <> 'SI'`), el tipo desde `GL_TRANSACCIONES.TR_NOMBRE`, importe en `IMPORTE_USD` (+ `COTIZACION` → pesos), fecha desde `FECHA_MOV` (float YYYYMMDD). Débito/crédito por `TR_CODIGO`: **suman 38, 32; restan 30, 40, 128, 44**. Saldos `balanceUsd`/`balancePeso`. Se mantuvo la forma de respuesta → **el front no cambió**. Detalle en [[contexto#Cuenta corriente de proveedores (ledger MS_MOV_CTACTE_PROVEEDORES)|contexto]]. Commit API `14b208d`. Archivos: `ProviderCurrentAccountRepository.php`, `ProviderCurrentAccountDto.php`.

## 2026-06-22

> Sigue en `catri-fine-tunning`. La rama ya se mergeó a `development` (PRs #274, #276) y a `gamma`; el último commit (SKU inline) entra limpio.

### Cuenta corriente de proveedores (feature nueva — backend + frontend)

- feat: **Endpoint** `GET v1/providers/{providerCode}/currentAccount` — devuelve los comprobantes (`FACPROT`) del proveedor como movimientos de cuenta corriente, con filtros de fecha (`from`/`to`) y búsqueda, paginación y **saldos separados en u\$d y \$** (controller `ProviderCurrentAccount` → `ProviderCurrentAccountService` → `ProviderCurrentAccountRepository` + `ProviderCurrentAccountDto`). Reglas de cálculo en [[contexto#Cuenta corriente de proveedores (2026-06-22)|contexto]].
- feat: **Modal en Proveedores** — ícono 👁️ (columna "Cta Cte") en cada fila del listado abre un modal draggable con cabecera de saldos + tabla de movimientos (débitos/créditos), filtros de fecha/búsqueda y paginación (`components/Provider/CurrentAccount.vue`, `$api.providers.getCurrentAccount`, registro en `layouts/basic.vue`, columna en `store/providers.js`).
- fix: **`providerVoucher` deriva el `companyCode` del proveedor** (`ISNULL(FACPROT.companyCode, FP_Proveedores.companyCode)`), porque en `FACPROT` está **100% NULL** → antes el filtro de empresa nunca matcheaba; ahora ~36k comprobantes caen en empresa 4.

### Detalle de orden

- feat: **SKU junto al nombre del producto** en el detalle de orden, inline y en otro color (magenta), para identificarlo claro. Oculto para LASET (que ya tiene columna SKU dedicada) (`Orders/Detail.vue`).

### Git / merges

- La feature "eliminar ítem de una orden de compra" (otra rama, PR #273) entró a `development`/`gamma` y tocó `Orders/Detail.vue`. Se resolvió el conflicto con el SKU inline **combinando ambos**: nombre + SKU agrupados a la izquierda (`.product-title-group`) y el botón de eliminar a la derecha, vía `flex-between`. Tras mergear `development` dentro de `catri-fine-tunning` (commit `a5d4b57`), el merge a `development` y a `gamma` quedó limpio.

Commits: API `dcc1b6e` · Front `79f47df`, `a891afe`, merge `a5d4b57`.
Archivos: `app/Http/Controllers/Provider/ProviderCurrentAccount.php`, `app/Services/Provider/Provider/ProviderCurrentAccountService.php`, `app/Repositories/Provider/Provider/ProviderCurrentAccountRepository.php`, `app/Dto/Provider/ProviderCurrentAccountDto.php`, `app/Repositories/Provider/ProviderOrder/ProviderVoucherRepository.php`, `app/routes/api.php`, `components/Provider/CurrentAccount.vue`, `pages/providers.vue`, `store/providers.js`, `plugins/api.js`, `layouts/basic.vue`, `components/Orders/Detail.vue`

## 2026-06-20

> Rama de funcionalidad **`catri-fine-tunning`** (ambos repos, pusheada a origin). Aún **no mergeada** a development. Ver [[contexto#Filtro de Empresa (companyCode) por defecto en pestañas|contexto]].

- feat: **IVA por defecto del artículo al agregar un ítem.** El buscador de productos (`/v1/items`) ahora devuelve `articulo.ivaCompra` como `iva` (`ItemRepository` + `ItemDto`); al agregar un ítem a una orden el selector de IVA arranca con ese valor en vez de 0 (sigue editable). El detalle ya caía a `ISNULL(PL.nivaserv, AR.ivaCompra)` (API + `Orders/AddItem.vue`).
- ui: **Desplegable de búsqueda de productos más legible** — título destacado, metadata (categoría · marca · SKU · stock) en línea aparte, mejor contraste y espaciado. Antes el `line-height: 0` aplastaba la 2da línea (`Orders/AddItem.vue`).
- feat: **Filtros nuevos en el listado de Órdenes**: SKU (`articulo.ID_PRODUCTO`), ID interno (`articulo.ID_ARTICULO`) y **serial**. El de serial usa un `EXISTS` sobre `NEW_BYTES.dbo.ST_DETALLE_STOCK` (`ID_COMPRA = pedprot.nNumPed`) que **solo se agrega al WHERE cuando se usa** (sin impacto de rendimiento si no se filtra). `count()` pasó a `COUNT(DISTINCT nnumped)` con joins a `pedprol`/`articulo` para no inflar la paginación (API `ProviderOrderRepository` + `Filters/Orders.vue`).
- feat: **Filtro por serial en Ingresos** — `EXISTS` correlacionado con la línea del ingreso (`albprol.ID_ARTICULO` ↔ artículo del `cref` del serial). Se habilitó el param `serial` en el controller (`$request->only`). Los filtros SKU / ID interno ya existían en Ingresos; se alineó el wording al de Órdenes (API `ProviderOrderInboundRepository` + controller + `Filters/ProviderOrderInbound.vue`).
- feat: **Columna "Serializado" (Sí/No) en el listado de Órdenes** — `fullSerialized` calculado con la misma lógica que Ingresos (`COUNT(líneas) = COUNT(serialized=1)`). ⚠️ Una orden **sin líneas** da "Sí" (0=0), heredado de Ingresos (API `ProviderOrderRepository`/`ProviderOrderDto` + `pages/orders.vue` + `store/orders.js`).
- ui: **Filtros de Órdenes compactados** (anchos 110-150px, placeholders cortos) para que los 8 entren en una sola línea, manteniendo `flex-wrap` (`Filters/Orders.vue`).
- feat/fix: **Filtro de Empresa (companyCode) por defecto en todas las pestañas** — al entrar a CUALQUIER pestaña arranca en `Number($auth.user.companyCode) || 4` (default 4 si el usuario no tiene empresa asignada). Antes quedaba en null para usuarios sin empresa. Solo queda libre si se limpia a mano. Aplicado a las **9** `components/Filters/*.vue` (Orders, ProviderOrderInbound, Categories, Providers, Forwarders, Warehouses, ProviderVoucher, TariffTax, TariffPosition).
- infra: el `.env` de la API quedó apuntando a la DB **`10.10.10.47:1433`** (user `fcallipo`, DB `NB_WEB`). Ver [[contexto#Infraestructura / Base de datos (gotcha importante)|contexto]].

Commits: API `0446aa2`, `8458e8d` · Front `f427c83`, `3e8214b`.
Archivos: `app/Repositories/Items/ItemRepository.php`, `app/Dto/Item/ItemDto.php`, `app/Repositories/Provider/ProviderOrder/ProviderOrderRepository.php`, `app/Dto/Provider/ProviderOrderDto.php`, `app/Repositories/Provider/OrderInbound/ProviderOrderInboundRepository.php`, `app/Http/Controllers/Provider/ProviderOrderInbound.php`, `components/Orders/AddItem.vue`, `components/Filters/*.vue`, `pages/orders.vue`, `store/orders.js`

## 2026-06-10

> Cambios en working tree (aún sin commitear/mergear al cierre de la sesión).

- fix: `tariffTax?companyCode=X` no devolvía los impuestos **globales** (IVA, Ganancias, Retenciones, etc., cargados con `companyCode NULL`). El filtro `companyCode = :cc` descarta los NULL en SQL Server. Cambiado a `(companyCode = :companyCode OR companyCode IS NULL)` para incluirlos (API — `TariffTaxPrefixRepository`). Ver [[contexto#Impuestos globales (NULL = todas las empresas)|regla de impuestos globales]].
- perf/feat: Búsqueda unificada de items (`/v1/items?search=`). Ahora un solo término encuentra por SKU (`ID_PRODUCTO`), título (`CDETALLE`), `id_articulo`, marca y familia. Query **parametrizada** (named binds) → reutiliza el plan de ejecución de SQL Server y elimina la inyección SQL que había por interpolación de strings (API — `ItemRepository`).
- feat: En el detalle de orden, la **cotización** queda no editable cuando el proveedor opera en pesos (`currencyId = 'PSO'`); solo la *cotización fiscal* es editable. En otra moneda (USD) la cotización sigue editable. Nuevo computed `isProviderInPesos` (Frontend — `Orders/Detail.vue`).

Archivos: `app/Repositories/TariffPosition/TaxesName/TariffTaxPrefixRepository.php`, `app/Repositories/Items/ItemRepository.php`, `components/Orders/Detail.vue`

### Ingresos: ver seriales + ajustes de cotización en pesos (working tree)

- feat: **Ver seriales en Ingresos** — clic derecho sobre un producto serializado en el detalle de un Ingreso → "Ver seriales (N)" → modal con los números de serie. Back: nuevo endpoint `GET /v1/providerOrderInbound/{nNumPed}/serials/{ID_ARTICULO}` (controller `ProviderOrderInboundSerials` → service → repo que lee `NEW_BYTES.dbo.ST_DETALLE_STOCK` por `ID_COMPRA` + `cref`). Se agregó `serializedAmount` por ítem al detalle del ingreso. Front: `$api.providerOrderInbound.getSerials`, menú contextual (`a-dropdown` trigger contextmenu) + `a-modal` en `ProviderOrderInbound/Detail.vue`. Ver [[arquitectura#Detalle de Órdenes vs Ingresos (no confundir)|arquitectura]].
- fix: En el detalle de **Ingreso**, la fila resumen "Cotización" no mostraba **Subtotal Final** (la `percepcion` venía `undefined` → `subtotalFinal + undefined = NaN`, y `NaN >= 0` es false). Guard con `Number(orderDetail.percepcion) || 0` (`ProviderOrderInbound/Detail.vue`).
- feat: Detalle en **pesos** (`currencyQuote === 1`): el **Costo** muestra `$` en vez de `u$d` (prop `currency` en `Table/EditableCell2.vue`, antes hardcodeado), se corrigieron las clases de color `.dolar`/`.peso` que estaban invertidas, y la fila **Cotización fiscal** ya no multiplica subtotales por la cotización fiscal — solo muestra el valor. Además se muestra la cotización / cotización fiscal en la columna "Cant." cuando la orden no es editable (remitida) (`Orders/Detail.vue`). Ver [[contexto#Cotización en pesos (currencyQuote === 1) — display|regla de display]].
- ui: Columna **Fecha** del listado de Órdenes en una sola línea (`white-space: nowrap` + fuente 12px) para que la hora no caiga abajo (`pages/orders.vue`).
- data: Limpieza en SQL Server (prod): `companyCode IS NULL` → **4 (NB)** en `PedProT` (78) y `albprot` (11.914); depósito **SAFcom** (`warehousesId=2` / `ccodalm='SAF'`) donde faltaba para `companyCode=4` (PedProT 10.319, albprot 3), **sin pisar** 7 filas con depósito distinto a propósito (DE1, Miami, DOM, 006). Ver [[contexto#companyCode 4 (NB) y depósito SAFcom|contexto]].

Archivos (esta sesión): `app/Http/Controllers/Provider/ProviderOrderInboundSerials.php`, `app/Repositories/Provider/OrderInbound/ProviderOrderInboundRepository.php`, `app/Services/Provider/OrderInbound/ProviderOrderInboundDetailService.php`, `app/routes/api.php`, `components/ProviderOrderInbound/Detail.vue`, `components/Orders/Detail.vue`, `components/Table/EditableCell2.vue`, `pages/orders.vue`, `plugins/api.js`

## 2026-03-11

- feat: Despachos temporales y serialización de datos (API)
- Merge de rama `laset-compras-temp-despacho`

## 2026-03-05

- fix: Arreglo en generación de proforma (API)

## 2026-03-04

- feat: Agregar campo `finalPrice` en órdenes (API)
- fix: COM-285 — Revisión de funcionalidad que no andaba correctamente (API)

## 2026-03-03

- fix: Hotfix para query incompleta en stock de warehouse inbound (API)
- fix: Hotfix para inserción con datos incorrectos en tabla de stocks (API)
- fix: Completar columnas faltantes en INSERT de stocks y castear `companyCode` en `ListCategoriesDto` (API)

## 2026-02-24

- refactor: COM-284 — Ajustar visibilidad del selector de depósito cuando la orden está pendiente y no hay `amountEntered` (Frontend)

## 2026-02-02

- refactor: COM-283 — Cambiar "IVA" por "Impuestos" en el listado de órdenes (Frontend)
- refactor: COM-279 — Filtro de `companyCode` en proveedores dentro de crear orden + selector de empresa (Frontend)
- mejora: COM-280 — Agregar logo de empresa para identificación rápida (Frontend)
- refactor: COM-277 — Selector de empresa en alta/edición de proveedores (Frontend)
- refactor: COM-281 — Usuario autenticado homologado (API)
- fix: Cálculo de `taxAmount` en órdenes de proveedor (API)
- refactor: COM-278 — Modificar proveedor incorporando `companyCode` (API)

## 2026-01-29 — 2026-01-30

- fix: Arreglo `companyCode` en autenticación (API)
- fix: Corregir cálculo de `totalFinal` en listado de órdenes (API)
- feat: `companyCode` en patch de proveedor (API)
- refactor: COM-277 — Alta/Edición de proveedores con selector de empresa (Frontend)
- refactor: Logo de empresa al lado del proveedor, mejora de navegación y anchos de tabla (Frontend)
- fix: COM-271 — No agregar productos sin cantidad al hacer ingreso parcial (Frontend)

## 2026-01-26 — 2026-01-27

- fix: Resolución de conflictos gamma → dev (Frontend)
- refactor: COM-201 — Atributo `warehousesId` asociado a órdenes (Frontend)
- refactor: COM-222 — Cambiar posición del buscador en modal de orden de compra (Frontend)
- fix: COM-198 — Eliminar país del detalle de orden mostraba NaN (Frontend)

---

Ver también: [[arquitectura|Arquitectura]] · [[stack|Stack]] · [[contexto|Contexto y reglas]]
