# Changelog — gigaErp

## 2026-05-14

### Scaffold completo del proyecto

Se construyó el proyecto desde cero en una sesión de trabajo.

**Infraestructura:**
- Docker Compose con 6 servicios (db, redis, backend, scheduler, frontend, nginx)
- Dockerfile backend multi-stage: `composer:2` (build) → `php:8.4-cli` (runtime)
- Dockerfile frontend: Node 20 multi-stage con build estático
- Nginx proxy: `/api/*` → backend:8000, `/*` → frontend:3000
- Puerto público: 8824

**Backend Laravel 11:**
- 4 Enums: `RolUsuario`, `EstadoTarea`, `PrioridadTarea`, `EstadoVenta`
- 19 migraciones numeradas (0001–0019)
- 18 Models Eloquent
- 18 Controllers resource
- 8 API Resources

**Frontend Nuxt 3 SPA:**
- Composables: `useApi`, `useNotification`
- Store: `auth.ts` (Pinia)
- 14 páginas implementadas

## 2026-05-14 — Demo data + Kanban mejorado

- DemoSeeder con 3 meses de datos ficticios
- Kanban drag & drop HTML5 nativo
- Modal detalle de tarea estilo Jira
- Fix SQLite/config:cache
- Fix TypeError filter en tareas

## 2026-05-14 — Debugging acciones + Dashboard + branding

- Fix apiResource pluralización española (.parameters())
- Fix Resource wrapper en frontend
- Dashboard: 6 KPIs + pixel bar chart SVG 12 meses
- Logo AORUS sidebar, "Brand ERP" topbar

## 2026-05-20 — Módulo Productos + Existencias + datos reales

- Módulo Productos (/productos): catálogo con grid/lista/filtros/stock
- Módulo Existencias (/existencias): tabla cruzada SKU × distribuidor
- Datos INVID (41 productos) y New Bytes (206 productos) cargados
- Migraciones 0020–0024: precio/foto/IVA, tipo en clientes, stock, sku

## 2026-05-21 — Módulo Órdenes de Venta + Stock dinámico por depósito

- Módulo OrdenVenta (cabecera + líneas): index, nueva, detalle/edición
- Enum EstadoOrdenVenta, OrdenVentaResource con items embebidos
- Migraciones 0025 (SKU único por distribuidor), 0026 (listas de precio 1–4), 0027 (tablas orden)
- Vista /mercaderia/stock: columnas dinámicas por depósito activo
- ProductoResource: campos stocks_deposito y stock_total via whenLoaded

Archivos: `backend/app/Enums/EstadoOrdenVenta.php`, `backend/app/Http/Controllers/OrdenVentaController.php`, `backend/app/Http/Resources/OrdenVentaResource.php`, `backend/app/Models/{OrdenVenta,ItemOrdenVenta}.php`, `frontend/pages/ordenes-venta/`, `frontend/components/OrdenItems.vue`, `frontend/pages/mercaderia/stock/index.vue`

## 2026-05-23 — Filtros de stock + depósito por ítem + Commercial Invoice PDF

### Filtros complementarios en picker de Órdenes de Venta

El selector de productos en órdenes de venta tenía los filtros de depósito y stock como dos `.filter()` independientes que no se coordinaban. Rediseñados como un único filtro combinado:

- Depósito seleccionado → el filtro de stock aplica sobre ESE depósito específico
- Sin depósito → el filtro de stock aplica sobre el stock total del producto
- `Number(filtroDeposito.value)` para evitar coerción de tipo en claves del objeto `stocks_deposito`
- `seleccionables()` endpoint ahora incluye `stocks_deposito: {deposito_id: cantidad}` y `stock` (eager load relación `stocks`)

### Selección de depósito por ítem de orden

Cada línea de orden ahora guarda de qué depósito se toma el stock:

- **Migración 0028**: columna `deposito_id` nullable en `items_orden_venta` (FK → depositos, nullOnDelete)
- `ItemOrdenVenta::$fillable` actualizado + relación `deposito()`
- `OrdenVentaController`: acepta `deposito_id` en validación, lo persiste en `sincronizarItems()`; eager load `items.deposito` en todos los endpoints
- `OrdenVentaResource`: expone `deposito_id` y `deposito_nombre` en cada ítem
- **Frontend picker**: pills de depósito por producto con stock en paréntesis, auto-selecciona el primer depósito con stock o el filtro activo; `depositosPicker` reactive map
- Columna "Depósito" agregada a la tabla de ítems de la orden

### PDF Commercial Invoice

Endpoint `GET /api/ventas/{id}/pdf` que genera PDF descargable via dompdf (ya instalado en el container).

**Blade template** (`resources/views/ventas/invoice.blade.php`):
- Logo Gigabyte SVG embebido como base64 (sin dependencias de filesystem externo)
- Número de invoice formateado `INV-{AÑO}-{XXXX}` desde `venta.numero`
- Bloque Seller: datos de empresa desde tabla `configuraciones` (`empresa_nombre`, `empresa_direccion`, etc.)
- Bloque Buyer: nombre, email, teléfono, dirección del cliente
- Barra de términos: Payment Terms, Incoterm, Currency, cantidad de ítems
- Tabla de ítems con header negro: SKU · Description · Qty · Unit Price · Total
- Totales: Subtotal / Shipping / Total USD
- Bank Details: Banco, ABA/Routing, SWIFT, Account #, Dirección del banco
- Authorized Signature: línea + nombre + título
- `page-break-inside: avoid` en todos los bloques principales (terms bar, tabla, totals, banco, firma)

**Migración 0029**:
- Campo `shipping_usd` (decimal, default 0) en tabla `ventas`
- Config keys sembradas: `empresa_direccion`, `empresa_ciudad_pais`, `empresa_telefono`, `empresa_email`, `empresa_web`, `invoice_payment_terms`, `invoice_incoterm`, `invoice_banco_*`, `invoice_firma_*`

**Frontend**: botón "Descargar PDF" en banner verde de invoice generada (en `/ordenes-venta/[id]`). Usa `fetch()` nativo con token Bearer, descarga como blob y dispara `<a download>`.

Archivos: `backend/app/Http/Controllers/{ProductoController,VentaController,OrdenVentaController}.php`, `backend/app/Http/Resources/OrdenVentaResource.php`, `backend/app/Models/{ItemOrdenVenta,Venta}.php`, `backend/database/migrations/0028-0029`, `backend/resources/views/ventas/invoice.blade.php`, `backend/routes/api.php`, `frontend/components/OrdenItems.vue`, `frontend/pages/ordenes-venta/[id].vue`, `frontend/pages/ordenes-venta/nueva.vue`
