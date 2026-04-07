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

En la práctica, la mayoría de la lógica está directamente en los **controllers** (138 controllers en 61 subdirectorios). Solo existen 4 Services y 3 Repositories formales — el patrón se aplicó para módulos específicos como MakeSale, RemoveSale, ClientProfile, MercadoLibre y TotalSales.

### Controllers principales

| Módulo | Controllers | Descripción |
|--------|------------|-------------|
| Order | 27 | CRUD de pedidos (OrderCreate, OrderList, OrderUpdate) |
| Statistics | 10 | Dashboards y reportes estadísticos |
| SyncUp | 9 | Sincronización con sistemas externos |
| DownloadDocument | 6 | Descarga de documentos (PDF, Excel) |
| Addendum | 5 | Addendums de pedidos |
| Client | 5 | Gestión de clientes |
| Marketing | 5 | Fondos, acciones, movimientos |
| ShippingMethod | 1 | Métodos de envío (list, carrier, dropshipping) |
| MakeSale / RemoveSale | 2 | [[modulo-makesale|Ejecutar]] y [[modulo-removesale|revertir]] pedidos |

### Capas de soporte

- **Services/** — ShippingMethodService, ClientProfileService, ClientService, MercadoLibreService, TotalSalesService, MercadoLibreOrdersService
- **Repositories/** — ShippingMethodRepository, ClientProfileRepository, MercadoLibreRepository, TotalSalesRepository
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

~234 rutas en `routes/api.php`, todas bajo `/v1`. Las rutas `syncUp/*` están fuera del middleware de auth.

### Dato: ShippingMethods

El endpoint `/v1/shippingMethods` consulta `[LO].[dbo].[mediosEnvio]` y siempre agrega un método "Retiro" hardcodeado (id 3999) al final, sin importar el `companyCode`.

## Frontend

### Páginas (23)

- **Root:** orders, clients, clientsRequest, products, vouchers, comissions, chatsLO, login
- **Dashboard/** (7): ranking, heatMaps, limitesObjetivos, incentivoGigabyte, logisticPerformance
- **Marketing/** (4): actions, brands, funds, movements

### Componentes (101)

Organizados por feature: Orders (26), Filters (18), Mkt (9), Table (8), Client (7), Report (7), Modal (4), Products (3), Dashboard (2), + 17 root.

### Vuex Store (12 módulos)

orders, clients, clientsRequest, products, vouchers, comissions, dashboard, statistics, marketing, reports, chatsLO.

### Plugins (10)

api.js (Axios wrapper), permissions.js (RBAC), firebase-messaging.js (push), apiJira.client.js, formats.js, mask.js, vee-validate.js, antd-ui.js, axios.js, vue-mixin-common-methods.js.

## Base de datos

SQL Server (SQLSRV via ODBC). Tres bases de datos:
- **NewBytes_DBF** — Datos transaccionales (pedidos, remitos, stock, clientes, agentes)
- **NB_WEB** — Datos web (registro_stock, users) — conexión default en Laravel
- **LO** — Datos de logística (mediosEnvio)

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
- [[stack]] — Dependencias y versiones
