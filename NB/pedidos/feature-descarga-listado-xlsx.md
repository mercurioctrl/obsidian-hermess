# Feature: Descarga xlsx de listados (pedidos y clientes)

**Rama:** `descargarListadoXlsx` (ambos repos) · **Fecha:** 2026-06-18

Botón (solo icono `download`, con `title="Descargar"` como tooltip) en las pestañas de **pedidos** y **clientes** que descarga un `.xlsx` del **listado actual respetando todos los filtros de la URL** — es decir, el resultado completo de la ejecución del recurso, sin paginar.

## Patrón base

Replica el mecanismo ya existente de **descarga de clientes** (`GET /v1/clients/download` → `ClientDownloadController` → `Excel::store(...)` en disco `public` → responde `{ success, path }` con `env('APP_URL').'/downloads/'.$fileName`). El front recibe el `path`, crea un `<a>` y dispara el click.

## Backend — `api-rest-pedidos-laravel`

Nuevo endpoint **`GET /v1/orders/download`**:

- `app/app/Http/Controllers/Order/OrderDownloadController.php` — invocable; `ini_set('memory_limit','1024M')`; genera `lista_pedidos-{timestamp}.xlsx`; responde `{ success, path }` (+ `warning` si se alcanza el tope de filas).
- `app/app/Services/Order/OrderDownload/OrderDownloadService.php` — **reutiliza `OrderListRepository::getOrders($filters, ['offset'=>0,'limit'=>ORDER_DOWNLOAD_MAX_ROWS])`** (método público que ya aplica filtros, calcula totales y castea `companyCode`), mapea con `OrderDto::fromArray`. `getShippingMethodsMap()` resuelve `id → nombre` del medio de envío vía `ShippingMethodRepository::getShippingMethods()` (`LO.dbo.mediosEnvio`).
- `app/app/Exports/ExcelExport/ExcelExportOrders.php` — `FromCollection` + `WithHeadings`. Columnas = tabla del front: Fecha, Pedido, Orden, Cliente, Estado, Tipo, Cotización, Percepción, $ Final, u$d Final, Factura, Medio de envío/retiro, Medio de pago, Vendedor.
- Ruta agregada en `app/routes/api.php` dentro del grupo `orders` (justo después de `Route::get('', OrderList::class)`).
- Env opcional: `ORDER_DOWNLOAD_MAX_ROWS` (default 5000), análogo a `CLIENT_DOWNLOAD_MAX_ROWS`.

> **Clientes ya tenía** la descarga (`GET /v1/clients/download`); no se tocó el backend de clientes.

### Por qué reutilizar `getOrders` sin paginar

El listado pagina con `OFFSET {offset} rows FETCH next {limit} rows only`. Como `getOrders` es público y recibe el `$pagination`, basta pasarle `offset=0` y `limit=MAX` para obtener **exactamente las mismas filas con los mismos filtros y totales** que ve el usuario — sin duplicar la query gigante (joins + subconsultas + GROUP BY de ~50 columnas).

## Frontend — `pedidos-web-app-v1`

- `components/Filters/Orders.vue` — botón solo-icono + `loadingDownload: false` en `data` + método `downloadExcelAllOrders()` (copia de `downloadExcelAllClients`: borra `itemsPerPage`, `GET orders/download` con `this.$route.query`, recibe `{success, path}`, crea `<a>` y dispara click).
- `components/Filters/Clients.vue` — el botón de descarga existente se unificó a **solo icono** (antes decía "Clientes" con `width:100px`).

## Git

| Repo | development | gamma |
|---|---|---|
| Backend | `d6c7e13` (Development) | cherry-pick `b433f53` (Gamma) |
| Frontend | `2d4ba8e` (development) | cherry-pick `64d4c9d` (gamma) |

Cherry-picks aplicaron limpios (gamma ya tenía la descarga de clientes y el `openMoreFilters` de pedidos). Identidad de commits: `Catriel <catrielmercurio@gmail.com>`.

## Deploy

- Backend: ruta nueva → `php artisan route:clear && config:clear`.
- Frontend: rebuild (`API_HOST` se bakea en build).

## Ver también

- [[arquitectura]] — patrón Controller → Service → Repository, Exports
- [[contexto]] — multi-empresa, filtros de listado
- [[changelog#2026-06-18 — Descarga xlsx de listados (pedidos y clientes)]]
