# Arquitectura

## Visión general

Monorepo con dos repositorios Git independientes. El código fuente de ambos vive dentro de `app/`.

```
compras/
├── api-rest-compras-laravel/    # API REST (Laravel 9)
│   ├── app/                     # Código Laravel
│   ├── docker/                  # Dockerfile + config Apache/PHP
│   └── docker-compose.yml
└── compras-web-app-v1-/         # Frontend (Nuxt 2)
    └── app/                     # Código Nuxt
```

## API — Patrón Controller → Service → Repository

Cada dominio sigue una estructura de 4 capas:

| Capa | Ubicación | Responsabilidad |
|------|-----------|-----------------|
| Controller | `app/Http/Controllers/{Domain}/` | Recibe request, delega a service. Invocables (single-action) |
| Service | `app/Services/{Domain}/` | Lógica de negocio |
| Repository | `app/Repositories/{Domain}/` | Queries a SQL Server (SQL crudo, `DB::select`) |
| DTO | `app/Dto/{Domain}/` | Transformación de datos |

### Dominios principales

- **Provider** — El más complejo. Gestión de proveedores, órdenes de compra, ingresos (inbound), comprobantes (vouchers), cuenta corriente, distribución de impuestos
- **TariffPosition** — Posiciones arancelarias. Búsqueda interna, sincronización con API externa, gestión de prefijos de impuestos (`tariffTax`)
- **Warehouse** — CRUD de depósitos
- **Forwarder** — CRUD de despachantes de aduana
- **Categories** — Categorías de productos (listado + edición)
- **Items** — Productos/ítems para las órdenes. Búsqueda unificada (ver abajo)
- **Auth** — Login JWT custom con `PermissionMiddleware`

### Autenticación

JWT custom (no Sanctum en runtime). `PermissionMiddleware` valida el token via `TokenManager` y verifica que el usuario tenga permiso `compras > 0`. El usuario decodificado se inyecta en `$request->attributes`.

### Archivos transversales

- `Helper/Filter.php` — Filtrado genérico de queries
- `Helper/Pagination.php` — Paginación estándar
- `Support/TokenManager.php` — Encode/decode JWT (firebase/php-jwt)

## Frontend — Nuxt 2 con Vuex

### Estructura de páginas

Cada página corresponde a un módulo de negocio con su propio store Vuex:

| Página | Store | Descripción |
|--------|-------|-------------|
| `orders.vue` | `orders.js` | Órdenes de compra |
| `providers.vue` | `providers.js` | Proveedores |
| `providerOrderInbound.vue` | `providerOrderInbound.js` | Ingresos de mercadería |
| `providerVoucher.vue` | `providerVoucher.js` | Comprobantes de compra |
| `warehouses.vue` | `warehouses.js` | Depósitos |
| `forwarders.vue` | `forwarders.js` | Despachantes |
| `categories.vue` | `categories.js` | Categorías |
| `tariffPosition.vue` | `tariffPosition.js` | Posiciones arancelarias |
| `tariffTax.vue` | `tariffTax.js` | Impuestos arancelarios |
| `dashboard.vue` | — | Dashboard principal |

### Sistema de modales

El store raíz (`store/index.js`) gestiona un sistema de modales dinámicos con soporte para:
- Múltiples modales simultáneos con z-index gestionado
- Minimizar/maximizar
- Arrastre (drag) via `components/Modal/Draggable.vue`
- Modales tipados: `OrderDetail`, `ProviderOrderInboundDetail`, `ProviderCurrentAccount` (renderizados en `layouts/basic.vue` por `modal.type`)

Se abre con `this.$store.dispatch('addModal', { title, id, type, props })`. ⚠️ El binding `:status` en `basic.vue` toleraba solo modales con `props.orderDetail`; se hizo tolerante (`modal.props.orderDetail ? ... : ''`) para soportar modales sin orderDetail (ej. cuenta corriente).

El detalle de orden (`Orders/Detail.vue`) recibe props `orderDetail` (respuesta del endpoint de detalle) y `order` (el registro del listado, que trae `currencyId`). Regla de cotización por moneda: ver [[contexto#Cotización según moneda del proveedor|contexto]].

⚠️ **z-index:** los modales draggables arrancan en 999 e **incrementan** al enfocar. Un `a-modal` de Ant anidado dentro de un Detail (ej. modal de seriales) necesita `:z-index` alto (se usa `10000`) o queda detrás del modal contenedor.

### Detalle de Órdenes vs Ingresos (no confundir)

Hay **dos componentes Detail casi idénticos**:

- `components/Orders/Detail.vue` → vista **Órdenes** (modal type `OrderDetail`). Tiene filas resumen **Cotización** (`type:'resumen'`) **y Cotización fiscal** (`type:'resumenfiscal'`); columnas Subtotal/Subtotal Final en u\$d **y** \$. Muestra el **SKU** (`articulo.ID_PRODUCTO`) inline junto al nombre del producto, en otro color (oculto para LASET, que tiene columna SKU dedicada). Incluye botón de **eliminar ítem** (`canDeleteOrderItem`/`deleteOrderItem`). Reglas de display de cotización en pesos: ver [[contexto#Cotización en pesos (currencyQuote === 1) — display|contexto]].
- `components/ProviderOrderInbound/Detail.vue` → vista **Ingresos** (modal type `ProviderOrderInboundDetail`; son órdenes ya remitidas). Solo fila **Cotización**. ⚠️ Su `name:` interno también es `'OrderDetail'` (colisión confusa, no es el de Órdenes).

`orderDetail.numPed` = `PedProT.nNumPed` (id de orden). `record.id` del ítem = `ID_ARTICULO`.

Ambos endpoints de detalle devuelven **`currencyId`** (ej. `PSO`/`DOL`) y las cotizaciones, **todo desde `PedProT`** (cabecera del pedido): `currencyId`←`PedProT.cCodDiv`, `currencyQuote`←`PedProt.nValDiv`, `currencyFiscalQuote`←`PedProt.nvaldiv_FISCAL`. En el **ingreso** originalmente salían de `albprot` (daba id numérico `1`) — corregido el 2026-06-30 para tomarlos del pedido. El front elige cuál cotización mostrar según moneda (`currencyQuoteComputed`): pesos→fiscal, dólares→quote. Ver [[contexto#Cotización única en el header del detalle (COM-320, 2026-07-02)|contexto]].

### Agregar ítem a una orden / selector de IVA

En `Orders/AddItem.vue`, el buscador usa `/v1/items` (cada ítem trae `iva` = `articulo.ivaCompra`). Al agregar, el `price.iva` arranca con ese valor (PATCH a `/providerOrder/{n}`), que se guarda en `PedProL.nivaserv`. El selector de IVA en el detalle ofrece 0 / 10.5 / 21. Ver [[contexto#IVA por defecto del artículo al agregar ítem|contexto]].

### Eliminar línea de una orden pendiente

`DELETE /v1/providerOrder/{orderId}/item/{itemId}` → `ProviderOrderDeleteItem` (controller invokable) → `DeleteOrderItemService::delete` → `DeleteOrderItemRepository`. Valida `PedProT.cEstado = 'P'` (si no → 400), hard-delete de la línea en `PedProl` + su `PedProlSuggested` por `nNumPed`+`ID_Articulo` (0 filas → 404), y recalcula la distribución (`DistributionCalculatorService::recalculateDistribution`). En el front lo dispara el tacho de `Orders/Detail.vue` (`deleteOrderItem`). **Ojo:** el `DELETE /providerOrder/{orderId}` (sin `/item`) es otro endpoint distinto: `DistributeTaxesDelete`, borra impuestos distribuidos de `pedproi`. Ver [[contexto#Eliminar línea de orden pendiente (2026-07-20)|contexto]].

### Filtros de listados

Cada listado tiene su `components/Filters/{Dominio}.vue`. Los filtros escriben en `$route.query` (via `handleChange`) y el store reenvía toda la query como params al endpoint (`GET /v1/...`).

- **Órdenes** filtra por: estado, depósito, empresa, nro proforma, nro factura, **SKU** (`articulo.ID_PRODUCTO`), **ID interno** (`articulo.ID_ARTICULO`) y **serial**. Ingresos tiene además serializado y marca, y también SKU / ID interno / serial.
- **Filtro de Empresa**: al entrar a cualquier pestaña arranca en `$auth.user.companyCode || 4`; solo libre si se limpia a mano (las 9 Filters). Ver [[contexto#Filtro de Empresa (companyCode) por defecto en pestañas|contexto]].
- **Filtros que tocan líneas/seriales** (SKU, ID interno, serial) se aplican con condiciones que **solo se concatenan al WHERE cuando el filtro está presente** (el de serial es un `EXISTS` sobre `ST_DETALLE_STOCK`), para no penalizar el listado general. El `count()` de Órdenes usa `COUNT(DISTINCT nnumped)` para no inflar la paginación con los joins a líneas. Ver [[contexto#Filtro por serial — Órdenes e Ingresos|contexto]].
- **Columna "Serializado" (Sí/No)** en Órdenes e Ingresos: `fullSerialized` = `COUNT(líneas) == COUNT(serialized=1)`.

### Seriales de ingreso

En el detalle de Ingreso, los productos serializados (`record.serializedAmount > 0`) muestran un menú contextual (clic derecho) "Ver seriales" que abre un `a-modal` con los números de serie.

Flujo: `$api.providerOrderInbound.getSerials(numPed, ID_ARTICULO)` → `GET /v1/providerOrderInbound/{orderId}/serials/{itemId}` → `ProviderOrderInboundSerials` (controller) → `ProviderOrderInboundDetailService::getSerials` → `ProviderOrderInboundRepository::getSerials` → lee `NEW_BYTES.dbo.ST_DETALLE_STOCK` (col `SERIAL`) join `articulo` por `cRef`, filtrando `ID_COMPRA = nNumPed` + `ID_ARTICULO`.

### Cuenta corriente de proveedores

Desde el listado de Proveedores, el ícono 👁️ (columna "Cta Cte") abre el modal `components/Provider/CurrentAccount.vue` (type `ProviderCurrentAccount`) con la cuenta corriente del proveedor.

Flujo: `$api.providers.getCurrentAccount(providerCode, {from,to,search,currentPage,itemsPerPage})` → `GET /v1/providers/{providerCode}/currentAccount` → `ProviderCurrentAccount` (controller) → `ProviderCurrentAccountService` → `ProviderCurrentAccountRepository` + `ProviderCurrentAccountDto`.

El repo lee el ledger oficial **`NEW_BYTES.dbo.MS_MOV_CTACTE_PROVEEDORES`** (movimientos del proveedor por `ID_PROVEEDOR = CCODPRO`, excluyendo anulados), toma el tipo desde `GL_TRANSACCIONES.TR_NOMBRE`, el importe de `IMPORTE_USD` (+ `COTIZACION` → pesos) y aplica el signo según `TR_CODIGO` (suman 38/32; restan 30/40/128/44). Devuelve movimientos paginados + saldos `balanceUsd` / `balancePeso`. Incluye pagos (es un ledger). Reglas y gotchas en [[contexto#Cuenta corriente de proveedores (ledger MS_MOV_CTACTE_PROVEEDORES)|contexto]].

> La v1 armaba la cuenta corriente desde `FACPROT`/`FACPROL` — **descartada** en el refactor 2026-06-24.

### Exportación XLSX/CSV

Util `app/utils/tableExport.js` (SheetJS `xlsx`): `exportTable(columns, rows, filename, format)`. Cada columna puede ser `{title|header, dataIndex}` (toma `row[dataIndex]`, listados) o `{header, value(row)}` (valor calculado). Genera xlsx/csv en el browser (`XLSX.writeFile`).

- **Listados** (Órdenes/Ingresos): los botones viven en `components/Filters/*.vue` y emiten `@export`; la página re-consulta el endpoint con `route.query` + `itemsPerPage` alto (baja **todo lo filtrado**) y exporta con las columnas visibles.
- **Detalle de orden:** `components/Orders/Detail.vue` (`exportItems`) exporta `newItems` (sin filas resumen) con subtotales calculados como los slots.

Detalle y decisiones en [[contexto#Exportación de tablas (XLSX/CSV) — 2026-06-26|contexto]].

### Plugins clave

- `plugins/api.js` — Wrapper `$api` con métodos tipados por dominio (orders, providerOrderInbound, **providers**, tariffPosition, company)
- `plugins/formats.js` — Formateo de números/fechas (`formatNum`)
- `plugins/vue-mixin-common-methods.js` — Métodos compartidos entre componentes (`mixinInputOnlyNumber`, `mixinObjCompare`, etc.)
- `plugins/vee-validate.js` — Validación de formularios
- `plugins/permissions.js` — Permisos globales de visibilidad (oculta columnas sensibles para `companyCode == 11` / LASET)
- `plugins/apiJira.client.js` — Integración con Jira para soporte

### Componentes reutilizables

- `Filters/` — Un componente de filtro por cada página/dominio
- `Table/` — Celdas editables inline (`EditableCell.vue`, `EditableCell2.vue` con prop `currency`), menú contextual (`ClickRightCell.vue`)
- `Orders/` — Detalle de orden, agregar items, agregar posición arancelaria
- `ProviderOrderInbound/` — Detalle de ingreso (ver arriba)
- `Provider/` — `CurrentAccount.vue` (modal de cuenta corriente)
- `Report/` — Sistema de tickets/chat de soporte

## Reglas de datos transversales

Convenciones que atraviesan varias queries y conviene tener presentes (detalle y motivos en [[contexto|Contexto y reglas]]):

- **Multi-base:** las queries joinean entre varias bases del mismo SQL Server — `NewBytes_DBF` (maestro/ERP: `PedProT`/`PedProL` compras, `albprot`/`albprol` ingresos-remitos, `FACPROT`/`FACPROL` comprobantes de compra, `articulo`, `FP_Almacen`, `FP_PROVEEDORES`, `FP_IMPUESTOS`, `FP_Empresas`, `FP_TiposDocumentosCobro`…), `NB_WEB` (capa web), `NEW_BYTES` (`ST_DETALLE_STOCK` seriales, `ST_*_DESPACHOS_*`) y `PRODUCTOS`. Se referencian con nombre completo `[Base].[dbo].[tabla]`.
- **Compras vs ingresos:** orden = `PedProT.nNumPed` (líneas en `PedProL`). Ingreso/remito = `albprot.nnumalb` (líneas en `albprol`), vinculado por `albprot.nNumPed = PedProT.nNumPed`.
- **Comprobantes de compra (`FACPROT`/`FACPROL`):** los usa el listado `providerVoucher`. Cabecera `FACPROT` (key `IDFACPROT`; trae los **importes en 0**) + líneas `FACPROL` (join por `CSERIE` + `CNUMFAC`). `FACPROT.companyCode` está **100% NULL** → derivar del proveedor. (Ya **no** se usan para la cuenta corriente.)
- **Cuenta corriente de proveedores (`NEW_BYTES.dbo.MS_MOV_CTACTE_PROVEEDORES`):** ledger de movimientos. `ID_PROVEEDOR` = `CCODPRO`. `IMPORTE_USD` siempre positivo; dirección por `TR_CODIGO` (diccionario `GL_TRANSACCIONES`, columna `TR_NOMBRE`). `FECHA_MOV` = float YYYYMMDD. `COTIZACION` → pesos. `ANULADO` 'SI'/'NO'. Mapeo de signo en [[contexto#Cuenta corriente de proveedores (ledger MS_MOV_CTACTE_PROVEEDORES)|contexto]].
- **`articulo` tiene dos ids:** `ID_ARTICULO` (numérico, el `item.id` del front) y `cRef` (string, el `cref` que usan PedProL/albprol/`ST_DETALLE_STOCK`). No son lo mismo. El proveedor: `ID_PROVEEDOR` (num) y `CCODPRO` (código, **único**, el que usan PedProT/albprot/FACPROT).
- **Seriales:** `NEW_BYTES.dbo.ST_DETALLE_STOCK`, col `SERIAL`, key `ID_COMPRA = PedProT.nNumPed` + `cref = articulo.cRef` (no tiene vínculo directo al ingreso/`nnumalb`). `serializedAmount` = COUNT de esas filas. `serialized` (1/0) por línea está en `PedProL`. El filtro por serial de los listados se hace con `EXISTS` sobre esta tabla (solo cuando se usa).
- **Depósito:** `FP_Almacen` mapea `ID_ALMACEN` (num) ↔ `CCODALM` (char3) ↔ `cnombre`. `PedProT` guarda `warehousesId`+`cCodAlm`; `albprot` solo `ccodalm`. SAFcom = id 2 / 'SAF' (ver [[contexto#companyCode 4 (NB) y depósito SAFcom|contexto]]).
- **Impuestos globales:** en `FP_IMPUESTOS`, `companyCode = NULL` = impuesto global (aplica a todas las empresas). Filtrar con `(companyCode = :cc OR companyCode IS NULL)`, nunca solo `= :cc`.
- **Búsqueda de items (`ItemRepository`):** un único `search` cubre SKU (`A.ID_PRODUCTO`), título (`A.CDETALLE`), `A.ID_ARTICULO` (exacto, sargable), marca y familia, todo **parametrizado** (reutiliza plan de SQL Server, sin inyección). Devuelve también `iva` (= `A.ivaCompra`) para el default del selector de IVA.

## Base de datos

SQL Server externo. No hay migraciones Laravel — el schema es gestionado fuera del proyecto. La conexión usa FreeTDS (`pdo_dblib`) por incompatibilidad del driver ODBC 18 con OpenSSL 3.0 en el contenedor Ubuntu 22.04. Servidores y gotchas de puerto en [[contexto#Infraestructura / Base de datos (gotcha importante)|contexto]].

## Ver también

- [[stack|Stack tecnológico]]
- [[changelog|Changelog]]
- [[contexto|Contexto y reglas]]
- [[memoria|Memoria del proyecto]]
