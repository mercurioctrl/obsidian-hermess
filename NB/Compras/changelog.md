# Changelog

Historial de cambios del proyecto Compras, basado en los commits de ambos repositorios.

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
