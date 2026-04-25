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
