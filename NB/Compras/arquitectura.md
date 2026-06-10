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

- **Provider** — El más complejo. Gestión de proveedores, órdenes de compra, ingresos (inbound), comprobantes (vouchers), distribución de impuestos
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
- Modales tipados: Provider, Warehouse, TariffPosition, Order

El detalle de orden (`Orders/Detail.vue`) recibe props `orderDetail` (respuesta del endpoint de detalle) y `order` (el registro del listado, que trae `currencyId`). Regla de cotización por moneda: ver [[contexto#Cotización según moneda del proveedor|contexto]].

### Plugins clave

- `plugins/api.js` — Wrapper `$api` con métodos tipados por dominio (orders, providerOrderInbound, tariffPosition, company)
- `plugins/formats.js` — Formateo de números/fechas
- `plugins/vue-mixin-common-methods.js` — Métodos compartidos entre componentes
- `plugins/vee-validate.js` — Validación de formularios
- `plugins/permissions.js` — Permisos globales de visibilidad (oculta columnas sensibles para `companyCode == 11` / LASET)
- `plugins/apiJira.client.js` — Integración con Jira para soporte

### Componentes reutilizables

- `Filters/` — Un componente de filtro por cada página/dominio
- `Table/` — Celdas editables inline (`EditableCell.vue`), menú contextual (`ClickRightCell.vue`)
- `Orders/` — Detalle de orden, agregar items, agregar posición arancelaria
- `Report/` — Sistema de tickets/chat de soporte

## Reglas de datos transversales

Convenciones que atraviesan varias queries y conviene tener presentes (detalle y motivos en [[contexto|Contexto y reglas]]):

- **Multi-base:** las queries joinean entre 4 bases del mismo SQL Server — `NewBytes_DBF` (maestro: `articulo`, `familias`, `stocks`, `FP_IMPUESTOS`, `FP_Empresas`…), `NB_WEB` (capa web: `usuarios_nb`, `WebArtComplement`, `marcas`, `fotos_productos`), `NEW_BYTES` (`PGM_USUARIOS`) y `PRODUCTOS` (`fotos`). Se referencian con nombre completo `[NewBytes_DBF].[dbo].[tabla]`.
- **Impuestos globales:** en `FP_IMPUESTOS`, `companyCode = NULL` = impuesto global (aplica a todas las empresas). Filtrar por empresa con `(companyCode = :cc OR companyCode IS NULL)`, nunca solo `= :cc`.
- **Búsqueda de items (`ItemRepository`):** un único `search` cubre SKU (`A.ID_PRODUCTO`), título (`A.CDETALLE`), `A.ID_ARTICULO` (exacto, sargable), marca y familia, todo **parametrizado** (reutiliza plan de SQL Server, sin inyección).

## Base de datos

SQL Server externo. No hay migraciones Laravel — el schema es gestionado fuera del proyecto. La conexión usa FreeTDS (`pdo_dblib`) por incompatibilidad del driver ODBC 18 con OpenSSL 3.0 en el contenedor Ubuntu 22.04. Servidores y gotchas de puerto en [[contexto#Infraestructura / Base de datos (gotcha importante)|contexto]].

## Ver también

- [[stack|Stack tecnológico]]
- [[changelog|Changelog]]
- [[contexto|Contexto y reglas]]
- [[memoria|Memoria del proyecto]]
