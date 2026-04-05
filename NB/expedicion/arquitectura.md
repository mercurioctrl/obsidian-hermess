# Arquitectura — Expedición

## Diagrama general

```
┌─────────────────────┐     HTTP (axios)     ┌──────────────────────────┐
│  Frontend (Nuxt 2)  │ ──────────────────── │   API REST (Slim 4)      │
│  localhost:4149      ��                      │   localhost:8084/v1      │
│                      │                      │                          │
│  pages/ → store/     │     JSON + JWT       │  Controller → Service    │
│  store/ → plugins/   │ ◄────────────────── │  Service → Repository    │
│  plugins/api.js      │                      │  Repository → SQL Server │
└─────────────────────┘                      └──────────────────────────┘
                                                       │
                                              ┌────────┴────────┐
                                              │   SQL Server     │
                                              │  190.210.23.108  │
                                              │  Bases: NB_WEB,  │
                                              │  NEW_BYTES,      │
                                              │  NewBytes_DBF    │
                                              └──────────��──────┘

Servicios externos (llamados desde el backend):
  ├── MS Envíos (tracking, etiquetas ZPL, cotizaciones)
  ├── MS Comprobantes (facturación, tipos de voucher)
  └── Postventa (info de seriales, procesamiento de pases)
```

## Backend — Arquitectura en capas

### Bootstrap (app/src/App/App.php)

Secuencia de inicialización:
```
DotEnv → Container (Pimple) → ErrorHandler → Middlewares → CORS
→ Database (PDO/SQL Server) → Services → Repositories → Routes → NotFound
```

Entry point: `app/public/index.php` → `App.php`

### Flujo de un request

```
Request HTTP
  → Apache (mod_rewrite → public/index.php)
    → Slim Routing Middleware
      → PermissionMiddleware (valida JWT, extrae user)
        → Controller (recibe request, delega a service)
          → Service (lógica de negocio, validaciones)
            → Repository (queries SQL crudos, PDO)
              → SQL Server
            ← datos
          ← datos procesados + DTOs
        ← JsonResponse
      ← HTTP Response
```

### Patrón de dominio (ejemplo: Passes)

```
App/Routes/PassesRoute.php          → define GET/PATCH /passes
App/Service/ServicePasses.php       → registra passes_service en container
App/Repositories/PassesRepository.php → registra passes_repository en container

Controller/Passes/Passes.php        → __construct($container, "passes_service")
Service/Passes/PassesService.php    → recibe PassesRepository, lógica de negocio
Repository/Passes/PassesRepository.php → queries SQL, extends BaseRepository
```

### DI Container (Pimple)

- Services registrados como `{dominio}_service` (ej: `passes_service`, `shipment_list_service`)
- Repositories como `{dominio}_repository`
- Controllers resuelven service por string key: `new Base($container, "passes_service")`
- DB accesible como `$container["db"]` (PDO wrapper con logging)

### Middleware de permisos

| Middleware | Valida | HTTP si falla |
|-----------|--------|---------------|
| PermissionMiddleware | `user.expedicion > 0` (JWT válido) | 401 |
| ItemMiddleware | `user.exp_items > 0` | 403 |
| OrderMiddleware | `user.exp_upload_serials > 0` | 403 |

### Base de datos

- DSN: `sqlsrv:Server=HOST,PORT;Database=NB_WEB;TrustServerCertificate=yes;Encrypt=no`
- Credenciales via `$_SERVER["DB_USER"]` y `$_SERVER["DB_PASS"]` (no `$_ENV`)
- Queries frecuentes con LEFT JOIN cross-database: `NB_WEB.dbo.*`, `NEW_BYTES.dbo.*`, `NewBytes_DBF.dbo.*`
- PDO wrapper custom (`MyPdo`) con logging de queries via Monolog
- Paginación: OFFSET/FETCH en SQL Server

### Traits reutilizados

| Trait | Uso |
|-------|-----|
| ValidateDataTrait | 40+ métodos estáticos de validación (tipo, formato, rango). Throws Exception con mensaje en español |
| FormatDate | Formateo de fechas (dmY, Ymd, YmdHis, etc.) |
| ConvertDataTrait | Conversión de arrays a cláusulas SQL IN |
| DetectDataTrait | Detección de browser/device |

### Support (integraciones externas)

| Clase | Servicio | Auth |
|-------|----------|------|
| Envios.php | MS Envíos (tracking, etiquetas, cotización) | Bearer token |
| MSComprobantes.php | Facturación (vouchers, padron AFIP) | Bearer token |
| Postventa.php | Info seriales, procesar pases | Bearer token |
| TokenManager.php | JWT propio (HS256, secret hardcodeado) | — |
| Api.php | HTTP client fluent (cURL) | Configurable |
| Zpl.php | Generación de etiquetas ZPL para impresoras Zebra | — |

---

## Frontend — Arquitectura Nuxt 2

### Flujo de datos

```
Page (monta componentes, lee store)
  → Store action (dispatch)
    → plugins/api.js (método por dominio)
      → @nuxtjs/axios ($axios.$get/$post)
        → API REST backend
      ← response.data (auto-unwrapped)
    ← commit mutation al store
  ← reactividad Vue actualiza UI
```

### API Plugin (plugins/api.js)

Cliente centralizado inyectado como `$api`. Métodos agrupados por dominio:

```javascript
$api.passes.getDetail(id)
$api.providers.postSerialsByItem(orderId, itemId, data)
$api.shipments.getTracking(pedido)
$api.orders.dispatch(pedido, data)
$api.refund.getDetail(pedido)
$api.stock.setItemById(data)
$api.trackingOrders.drop(form)
$api.company.getCompanies(params)
```

### Vuex Store

- Módulos por dominio: `passes`, `providers`, `shipments`, `pickUp`, `stock`, `refund`, `vouchers`, `trackingOrders`, `reports`
- Patrón común en cada módulo:
  - `state`: lista de items, pagination config, loading flags, cancelToken
  - `mutations`: SET_*, DELETE_*, SET_ROW_* (SCREAMING_SNAKE_CASE)
  - `actions`: fetch con cancel token, error handling via `$messageAlert`
  - `getters`: column definitions para a-table (Ant Design)
- Root store: `company` selector, `pendings` polling (cada 5 min), smart dispatcher `getGeneralUpdate(route)`

### Permisos en frontend

```javascript
// middleware/exp-permissions.js
expRoutes = [
  { name: "pickUp",    permission: "expPickUp",    useBiggerItemsPerPage: true },
  { name: "shipments", permission: "expShipment",  useBiggerItemsPerPage: true },
  { name: "providers", permission: "expEntry" },
  { name: "passes",    permission: "expPasses" },
  { name: "stock",     permission: "expStock" },
  { name: "refund",    permission: "expRefund" },
  { name: "vouchers",  permission: "expVoucher" },
  { name: "trackingOrders", permission: "expTracking" },
]

// En templates:
v-if="$can('expPickUp')"
```

### Layout y UI

- Layout principal: `layouts/basic.vue` — header con menú horizontal filtrado por permisos + badges de pendings
- Patrón de página: tabla (a-table) + filtros + modales de detalle
- Theming: Less variables globales (`@azul: #304794`, `@verde`, `@rojo`, etc.) en `assets/less/colors.less`
- Utilidades CSS custom tipo Tailwind: `.flex-center`, `.fs-12`, `.mb-15`, `.modal-xl`

---

## Docker

```yaml
# docker-compose.yml
services:
  apirest:
    build: ./docker/Dockerfile    # Ubuntu 22.04 + PHP 8.3 + Apache + ODBC 18
    container_name: expedition-api-rest
    ports: 8084:80
    volumes:
      - ./app/:/var/www/app       # código montado como volumen
      - ./docker/php/php.ini:/etc/php/8.3/apache2/conf.d/99-custom.ini
```

### Particularidades del Dockerfile

- ODBC Driver 18 (ARM64 compatible) con OpenSSL config reducida (`SECLEVEL=0`, `MinProtocol=TLSv1`) para conectar a SQL Server legacy
- Extensiones `sqlsrv` y `pdo_sqlsrv` instaladas via PECL
- Apache con `mod_rewrite` habilitado, DocumentRoot en `/var/www/app/public`
- Cron para limpieza de logs Apache y app

## CI/CD

- GitHub Action: `.github/workflows/deploy-gamma.yml`
- Trigger: merge de PR a branch Gamma
- Deploy: SSH a servidor de staging (`/var/www/gamma_expedicion/api-rest-expedicion`)
- Post-deploy: crea PR automático Gamma → Development + notificación Slack

---

## Ver también

- [[NB/expedicion/stack|Stack]] — Versiones exactas de cada tecnología
- [[NB/expedicion/contexto|Contexto]] — Dominios de negocio y estado actual
- [[NB/expedicion/documentacion|Documentación]] — Cómo levantar y operar
- [[NB/expedicion/memoria|Memoria]] — Decisiones de arquitectura y gotchas
- [[NB/expedicion/changelog|Changelog]] — Qué cambió y cuándo
