# Arquitectura

## Estructura general

Monorepo con dos aplicaciones separadas (repos git independientes):

```
pedidos/
├── api-rest-pedidos-laravel/    # Backend Laravel 9
│   ├── app/                     # Código Laravel
│   ├── docker/                  # Dockerfile, Apache, PHP config
│   └── docker-compose.yml
└── pedidos-web-app-v1/          # Frontend Nuxt 2
    ├── app/                     # Código Nuxt
    └── .github/workflows/       # CI/CD
```

## Backend

### Patrón

Controllers → Services → Repositories → Models (parcialmente implementado).

En la práctica, la mayoría de la lógica está directamente en los **controllers** (144 controllers en 61+ subdirectorios). Solo existen Services y Repositories formales para módulos específicos como MakeSale, RemoveSale, ClientProfile, MercadoLibre, TotalSales y **Statistics/Lo**.

### Controllers principales

| Módulo | Controllers | Descripción |
|--------|------------|-------------|
| Order | 27 | CRUD de pedidos (OrderCreate, OrderList, OrderUpdate) |
| Statistics | 10 | Dashboards y reportes estadísticos |
| **Statistics/Lo** | **6** | **[[modulo-dashboard-lo|Dashboard Libre Opción]]** (summary, funnel, resellers, cube) |
| SyncUp | 9 | Sincronización con sistemas externos |
| DownloadDocument | 6 | Descarga de documentos (PDF, Excel) |
| Addendum | 5 | Addendums de pedidos |
| Client | 5 | Gestión de clientes |
| Marketing | 5 | Fondos, acciones, movimientos |
| ShippingMethod | 1 | Métodos de envío (list, carrier, dropshipping) |
| MakeSale / RemoveSale | 2 | [[modulo-makesale|Ejecutar]] y [[modulo-removesale|revertir]] pedidos |

### Capas de soporte

- **Services/** — ShippingMethodService, ClientProfileService, ClientService, MercadoLibreService, TotalSalesService, MercadoLibreOrdersService, **LoStatisticsService**
- **Repositories/** — ShippingMethodRepository, ClientProfileRepository, MercadoLibreRepository, TotalSalesRepository, **LoStatisticsRepository**
- **Support/** — 6 clases utilitarias: Price, TemplateMail, TokenManager, UploadFile, emails
- **Helper/** — Filter, Pagination
- **ValueObjects/** — DateRangeFilter
- **Exports/** — 9 exports Excel (billing, stock, clientes, facturas, kits)
- **ExternalApi/** — BcraApiExternal, VoucherApiExternal
- **Console Commands** — ProcessSalesObjectives, RefreshMercadoLibreTokens, SendWeeklyEmails

### Autenticación y middleware

- **TokenAuthenticate** — JWT para endpoints de usuario (header `Authorization: Bearer`)
- **PermissionMiddleware** — RBAC por endpoint
- **Rutas SyncUp** — Sin middleware; validan `?token=` contra `env('TOKEN_SYNCUP')` manualmente
- **CorsMiddleware** — Headers CORS
- **RebillMiddleware** — Middleware de refacturación

### Rutas

~240 rutas en `routes/api.php`, todas bajo `/v1`. Las rutas `syncUp/*` están fuera del middleware de auth.

### Dato: ShippingMethods

El endpoint `/v1/shippingMethods` consulta `[LO].[dbo].[mediosEnvio]` y siempre agrega un método "Retiro" hardcodeado (id 3999) al final, sin importar el `companyCode`.

## Frontend

### Páginas (27)

- **Root:** orders, clients, clientsRequest, products, vouchers, comissions, chatsLO, login
- **Dashboard/** (7): ranking, heatMaps, limitesObjetivos, incentivoGigabyte, logisticPerformance
- **Marketing/** (4): actions, brands, funds, movements
- **libreOpcion/** (4): métricas, embudo, resellers, cubo OLAP — ver [[modulo-dashboard-lo]]

### Componentes (110+)

Organizados por feature: Orders (26), Filters (19), Mkt (9), Table (9), Client (7), Report (7), Modal (4), Products (3), Dashboard (2), **LibreOpcion (2)**, + 17 root.

### Vuex Store (13 módulos)

orders, clients, clientsRequest, products, vouchers, comissions, dashboard, statistics, marketing, reports, chatsLO, **libreOpcion**.

### Plugins (10)

api.js (Axios wrapper), permissions.js (RBAC), firebase-messaging.js (push), apiJira.client.js, formats.js, mask.js, vee-validate.js, antd-ui.js, axios.js, vue-mixin-common-methods.js.

## Base de datos

SQL Server (SQLSRV via ODBC). Cuatro bases de datos:
- **NewBytes_DBF** — Datos transaccionales (pedidos, remitos, stock, clientes, agentes)
- **NB_WEB** — Datos web (registro_stock, users) — conexión default en Laravel
- **LO** — Datos del marketplace Libre Opción (pedidosCabecera, vendedores, mediosEnvio, mediosPago, usuarios)
- **NEW_BYTES** — Remitos y ventas (MS_REMITO_CABECERA, MS_VENTAS_REMITOS)
- **CS** — Catálogo de productos (productos)

Ver detalles de tablas y gotchas en [[contexto#Base de datos|Contexto]].

## Deploy

- **Backend:** Docker Compose → container `api-rest-pedidos-apirest-laravel` (8093:80)
- **Frontend:** PM2 (scripts en `start-example.sh` / `stop-example.sh`)
- **CI/CD:** GitHub Actions para frontend → branch `gamma` triggerea deploy via SSH
- **DB:** SQL Server externo (no containerizado)

Ver [[stack]] para versiones completas.

## Ver también

- [[contexto]] — Reglas de negocio y gotchas
- [[modulo-makesale]] — Flujo MakeSale
- [[modulo-removesale]] — Flujo RemoveSale
- [[modulo-dashboard-lo]] — Dashboard Libre Opción
- [[stack]] — Dependencias y versiones
