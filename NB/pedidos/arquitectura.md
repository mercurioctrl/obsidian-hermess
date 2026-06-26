# Arquitectura

## Estructura general

Monorepo con dos aplicaciones separadas (repos git independientes):

```
pedidos/
├── api-rest-pedidos-laravel/    # Backend Laravel 9
│   ├── app/                     # Código Laravel
│   │   └── database/sql/        # Scripts SQL manuales (DDL legacy + features)
│   ├── docker/                  # Dockerfile, Apache, PHP config
│   └── docker-compose.yml
├── pedidos-web-app-v1/          # Frontend Nuxt 2
│   ├── app/                     # Código Nuxt
│   └── .github/workflows/       # CI/CD
└── docs/                        # Documentación cross-cutting (features grandes)
```

## Backend

### Patrón

Controllers → Services → Repositories → Models (parcialmente implementado).

En la práctica, la mayoría de la lógica está directamente en los **controllers** (144 controllers en 61+ subdirectorios). Solo existen Services y Repositories formales para módulos específicos como MakeSale, RemoveSale, ClientProfile, MercadoLibre, TotalSales, **Statistics/Lo** y **Asignacion**.

### Controllers principales

| Módulo | Controllers | Descripción |
|--------|------------|-------------|
| Order | 27 | CRUD de pedidos (OrderCreate, OrderList, OrderUpdate) |
| Statistics | 10 | Dashboards y reportes estadísticos |
| **Statistics/Lo** | **6** | **[[modulo-dashboard-lo|Dashboard Libre Opción]]** (summary, funnel, resellers, cube) |
| **Asignacion** | **1** | **[[feature-asignacion-oc|Asignación OC↔Venta]]** (5 endpoints en un controller) |
| SyncUp | 9 | Sincronización con sistemas externos |
| DownloadDocument | 6 | Descarga de documentos (PDF, Excel) |
| Addendum | 5 | Addendums de pedidos |
| Client | 5 | Gestión de clientes |
| Marketing | 5 | Fondos, acciones, movimientos |
| ShippingMethod | 1 | Métodos de envío (list, carrier, dropshipping) |
| MakeSale / RemoveSale | 2 | [[modulo-makesale|Ejecutar]] y [[modulo-removesale|revertir]] pedidos |

### Capas de soporte

- **Services/** — ShippingMethodService, ClientProfileService, ClientService, MercadoLibreService, TotalSalesService, MercadoLibreOrdersService, **LoStatisticsService**, **AsignacionService**
- **Repositories/** — ShippingMethodRepository, ClientProfileRepository, MercadoLibreRepository, TotalSalesRepository, **LoStatisticsRepository**, **AsignacionRepository**
- **Support/** — Price, TemplateMail, TokenManager, UploadFile, emails
- **Helper/** — Filter, Pagination
- **ValueObjects/** — DateRangeFilter
- **Exports/** — 9 exports Excel
- **ExternalApi/** — BcraApiExternal, VoucherApiExternal
- **Console Commands** — ProcessSalesObjectives, RefreshMercadoLibreTokens, SendWeeklyEmails, **ApplyAssignmentFifoCommand** (`asignaciones:fifo`)

### Autenticación y middleware

- **TokenAuthenticate** — JWT para endpoints de usuario (header `Authorization: Bearer`). Setea `auth_user` en `$request->attributes`.
- **PermissionMiddleware** — RBAC por endpoint
- **Rutas SyncUp** — Sin middleware; validan `?token=` contra `env('TOKEN_SYNCUP')` manualmente
- **CorsMiddleware** — Headers CORS
- **RebillMiddleware** — Middleware de refacturación

### Rutas

~245 rutas en `routes/api.php`, todas bajo `/v1`. Las rutas `syncUp/*` están fuera del middleware de auth.

### Dato: ShippingMethods

El endpoint `/v1/shippingMethods` consulta `[LO].[dbo].[mediosEnvio]` y siempre agrega un método "Retiro" hardcodeado (id 3999) al final, sin importar el `companyCode`.

### DDL legacy y migraciones

Las tablas core (pedclit/pedclil/PedProT/pedprol/etc.) **no tienen migraciones de Laravel** — viven directamente en SQL Server fuera del control de `artisan migrate`. Las extensiones nuevas (como [[feature-asignacion-oc|asignación OC]]) siguen el mismo patrón: scripts SQL manuales en `app/database/sql/` con su rollback. Aplicación por DBA o vía `php -r` con bootstrap del kernel y split por `GO`.

## Frontend

### Páginas (27)

- **Root:** orders, clients, clientsRequest, products, vouchers, comissions, chatsLO, login
- **Dashboard/** (7): ranking, heatMaps, limitesObjetivos, incentivoGigabyte, logisticPerformance
- **Marketing/** (4): actions, brands, funds, movements
- **libreOpcion/** (4): métricas, embudo, resellers, cubo OLAP — ver [[modulo-dashboard-lo]]

### Componentes (110+)

Organizados por feature: Orders (26+), Filters (19), Mkt (9), Table (9), Client (7), Report (7), Modal (4+1), Products (3), Dashboard (2), **LibreOpcion (2)**, + 17 root.

Componentes nuevos del [[feature-asignacion-oc|feature de asignación]]: `Orders/AsignacionBadge.vue`, `Modal/AsignarOCModal.vue`.

### Vuex Store (14 módulos)

orders, clients, clientsRequest, products, vouchers, comissions, dashboard, statistics, marketing, reports, chatsLO, **libreOpcion**, **asignaciones**.

### Plugins (10)

api.js (Axios wrapper, namespaces por feature), permissions.js (RBAC), firebase-messaging.js (push), apiJira.client.js, formats.js, mask.js, vee-validate.js, antd-ui.js, axios.js, vue-mixin-common-methods.js.

### publicRuntimeConfig

Configurado en `nuxt.config.js`. Hoy expone `assignmentFeatureEnabled` y `assignmentCompanies` para que el frontend gatee la columna OC sin pedir endpoints. Lectura via `this.$config.*` o `$nuxt.$config` (debug en consola).

## Base de datos

SQL Server (SQLSRV via ODBC). Cinco bases de datos:
- **NewBytes_DBF** — Datos transaccionales (pedidos, remitos, stock, clientes, agentes, **`pedclil_oc_asignacion`**)
- **NB_WEB** — Datos web (registro_stock, users) — conexión default en Laravel
- **LO** — Datos del marketplace Libre Opción (pedidosCabecera, vendedores, mediosEnvio, mediosPago, usuarios)
- **NEW_BYTES** — Remitos y ventas (MS_REMITO_CABECERA, MS_VENTAS_REMITOS)
- **CS** — Catálogo de productos (productos)

Todo se accede desde una sola conexión `sqlsrv` con cross-DB references (`[NewBytes_DBF].[dbo].[tabla]`). Ver detalles de tablas y gotchas en [[contexto#Base de datos|Contexto]].

### Vistas y triggers nuevos (NewBytes_DBF)

Del [[feature-asignacion-oc|feature de asignación OC]]:
- `vw_saldo_oc` — saldo dinámico por línea de OC.
- `vw_pedclil_estado_asignacion` — estado de cobertura por línea pendiente.
- `tg_pedclit_cestado_asignacion` — `AFTER UPDATE` que mueve asignaciones V↔C según cambio de `cestado`.

## Deploy

- **Backend:** Docker Compose → container `api-rest-pedidos-apirest-laravel` (8093:80)
- **Frontend:** PM2 (scripts en `start-example.sh` / `stop-example.sh`)
- **CI/CD:** GitHub Actions para frontend → branch `gamma` triggerea deploy via SSH
- **DB:** SQL Server externo (no containerizado)
- **DDL nuevos:** scripts manuales en `database/sql/` aplicados por DBA. Ver `database/sql/README.md`.

Ver [[stack]] para versiones completas.

## Ver también

- [[contexto]] — Reglas de negocio y gotchas
- [[modulo-makesale]] — Flujo MakeSale
- [[modulo-removesale]] — Flujo RemoveSale
- [[modulo-dashboard-lo]] — Dashboard Libre Opción
- [[feature-asignacion-oc]] — Feature de Asignación OC ↔ Venta
- [[stack]] — Dependencias y versiones

## Modelo canónico ERP

Mapeo conceptual de los nombres legacy en `NewBytes_DBF.dbo` para que nadie se pierda con la nomenclatura:

| Concepto | Tablas | Detalle |
|---|---|---|
| **Compras** (OCs a proveedores) | `pedprot` + `pedprol` + `pedproi` | cabecera (proveedor, almacén, tracking, arrivalDate) + líneas (SKU, qty, FOB unit) + **cargos extra** (camion, percepciones) |
| **Ventas** (a clientes) | `pedclit` + `pedclil` | cabecera (cliente, incoterm, forwarder, proforma) + líneas |
| **Stock** | `stocks` | Por `cCodAlm`/`ID_ALMACEN` (NO tiene `companyCode`) — buckets: `nstock`, `nstock_ingresando`, `nstock_reserva_pedidos`, `nstock_postventa`, `nstock_virtual` |
| **Linkeo compra↔venta** | `pedclil_oc_asignacion` | [[feature-asignacion-oc]] |
| **CFE Uruguay** | `FP_FactWebCliEncabezado_Uy` + `FP_FactWebCliDetalle_Uy` + `FP_DocumentosUY` + `FP_ComprobantesUY` | tipoCfe 101=eTicket / 102=NC / 103=ND, IVA 22% |
| **Forwarders** | `forwarders` | DHL, Peniel International (Miami)…, con `companyCode` |
| **Empresas** | `FP_Empresas` | 11 activas — ver [[contexto#Empresas activas (FP_Empresas)]] |

**Gotcha**: `pedproi` no es solo impuestos — guarda también cargos extra del pedido de compra (`cdescrip='camion'` $50/$200). Linkea a `pedprot.nNumPed`, NO a `pedclit`. Ver [[contexto#Gotcha: pedproi no es solo impuestos]].

## Features documentados

- [[feature-asignacion-oc|Asignación OC ↔ Venta (pedclil ↔ pedprol)]]
- [[feature-asignacion-oc-cookbook|Cookbook Asignación OC]]
- [[feature-laset-import|Laset Import Framework (companyCode=11)]] — staging para reconciliar planilla FOB con ERP
- [[feature-laset-snapshot-restore|Snapshot/Restore Laset]] — punto de restauración comp=11
- [[feature-integrar-eccn|integrarECCN]] — clasificación ECCN (control de exportación) por familia × proveedor para comp=11

## Multi-empresa

El sistema soporta **11 empresas activas** filtrando por `companyCode` (`NewBytes_DBF.dbo.FP_Empresas`). NO solo NB/NBElectric/Libreopción — también OXXEN, NBGLOBAL, MUGELLO, **LASET** (CODEMP=11, importadora uruguaya), etc. Ver [[contexto#Empresas activas (FP_Empresas)]].


## Cuenta corriente (cross-DB, base `NEW_BYTES`)

La cuenta corriente NO vive en `NewBytes_DBF` (el ERP transaccional) sino en la base legacy **`NEW_BYTES`** (módulo MS_/MC_), accedida por nombre de 3 partes sobre la misma conexión `sqlsrv`.

| | Clientes | Proveedores |
|---|---|---|
| **Movimientos** | `MC_CCORRIENTES_MOVIMIENTOS` | `MS_MOV_CTACTE_PROVEEDORES` |
| **Master** | `clientes` (NewBytes_DBF, ID_CLIENTE compartido) | `MS_PROVEEDORES` (NEW_BYTES, propio) |
| **PK movimiento** | `ID_CCMOVIMIENTO` (float, no identity → MAX+1) | `ID_MOVIMIENTO` (int, no identity → MAX+1) |
| **Clave del titular** | `ID_CLIENTE` (= `clientes.ID_CLIENTE`) | `ID_PROVEEDOR` = **`FP_Proveedores.CCODPRO`** (código legacy, NO el `Id_Proveedor` interno) |
| **Importe** | `CC_IMPORTEUSD` magnitud + signo por `TR_CODIGO` | `IMPORTE_USD` magnitud + signo por `TR_CODIGO` |
| **TR (ventas/compras)** | 24 débito / 42 crédito | 38 factura(deuda) / 40 pago / 30 NC / 32 débito |
| **Marca de import Laset** | `ID_PROCEDENCIA=99` | `USU_IDENTIFICACION='Laset'` (no hay ID_PROCEDENCIA) |

Definiciones de cada `TR_CODIGO` en `NEW_BYTES.dbo.GL_TRANSACCIONES`. El **signo** lo da el TR (importe siempre magnitud positiva). Los proveedores comp=11 no existían en `MS_PROVEEDORES` → se crean al importar (saldo 0).

**Gotcha clave**: la cta cte de proveedores keyea por **CCODPRO**, no por `Id_Proveedor`. Asus `Id_Proveedor=16679` → `CCODPRO=002605`; cargar bajo `016679` no aparece en la pantalla del proveedor. Ver [[feature-laset-cuenta-corriente|cta cte clientes]] y [[feature-laset-cuenta-corriente-proveedores|cta cte proveedores]].

### Botones de mantenimiento Laset (/syncLaset)
Patrón uniforme: **servicio idempotente** (lógica canónica, compartida con el comando CLI) + **controller `__invoke {dry_run}`** + ruta `POST /v1/laset/*` + entrada en `plugins/api.js` + botón/modal **preview→confirmar** en `pages/syncLaset.vue`. Casos: reimport, wipe-transactional, fix-marcas-comp11, relink-facturas, **ccte-import** (clientes) y **prov-ccte-import** (proveedores). Los imports de cta cte suben el xlsx (multipart) y corren el parser Python sidecar.
