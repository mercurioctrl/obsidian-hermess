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


---

## 2026-05-23

### Reorganización de docs · CLAUDE.md ≤200 líneas

Por regla del proyecto, el `CLAUDE.md` no puede pasar de 200 líneas. Se redujo
de 486 a 127 líneas, dejando solo cheatsheet (stack, comandos, reglas críticas)
y un índice de pointers a las notas de la bóveda. El detalle de arquitectura,
módulos, design system y troubleshooting **vive ahora acá en Obsidian**.

Notas nuevas creadas:
- [[troubleshooting]] — catálogo de gotchas con causa y fix
- [[modulos/ordenes-venta]] — pipeline completo Orden → Invoice
- [[modulos/invoice-preview]] — preview Blu-style + html2pdf cliente-side
- [[modulos/productos]] — 4 listas de precio + SKU per-distribuidor
- [[design-system]] — paleta, tipografía, layout, botones, cards
- [[componentes-ui]] — Modal, DataTable, FormField, StatusBadge, etc.

Memoria de Claude actualizada en `~/.claude/projects/-Users-hermess-www-gigaErp/memory/`
con 8 archivos (perfil de usuario, workflow git, deploy dance, gotchas Sanctum y
html2canvas, credenciales dev, referencia Blu ERP, regla del 200-lineas-CLAUDE).

### Invoice del listado abre en nueva tab (commit `02e5b12`)

En el listado de Órdenes de Venta, la columna Invoice muestra el `VTA-XXXX` como
link verde con ícono `external-link`. Click → abre la preview en `_blank` sin
disparar el row-click. `@click.stop` para evitar bubbling.

Archivo: `frontend/pages/ordenes-venta/index.vue`.

### Invoice preview estilo Blu (commit `001f8c8`)

Reemplaza el invoice PDF server-side de DomPDF por una **preview HTML cliente-side**
con descarga PDF vía html2pdf.js. Replica el patrón visual del presupuesto de
`erp.blustudioinc.com` que el usuario usó como referencia.

Detalles en [[modulos/invoice-preview]]. Gotchas en [[troubleshooting]].

Cambios:
- Nuevo blade `backend/resources/views/ventas/invoice-preview.blade.php`
- `VentaController@preview` acepta token Bearer o `?token=` para shareable URL
- Ruta pública `GET /api/ventas/{venta}/preview` (auth la hace el controller)
- Botón "Ver invoice" en `pages/ordenes-venta/[id].vue` junto al "Descargar PDF" viejo
- Logo AORUS embebido como PNG data URI (workaround html2canvas + SVG viewBox)
- `backend/Dockerfile`: agregado `COPY resources/` y `COPY public/logos/` (faltaban — los blades antes solo vivían en runtime vía `docker cp`)

Archivos: `backend/resources/views/ventas/invoice-preview.blade.php` (nuevo),
`backend/app/Http/Controllers/VentaController.php`, `backend/routes/api.php`,
`backend/Dockerfile`, `backend/public/logos/aorus_logo_black.png` (nuevo),
`frontend/public/logos/aorus_logo_black.png` (nuevo),
`frontend/pages/ordenes-venta/[id].vue`.

## 2026-05-26 — Cuenta corriente de distribuidores + reorganización de navegación

### Módulo Cuenta Corriente (`movimientos_cuenta`)

Nuevo módulo completo de estado de cuenta por distribuidor.

**Backend:**
- Migración `0030_create_movimientos_cuenta_table`: tabla `movimientos_cuenta` con `cliente_id`, `tipo` (enum), `referencia`, `concepto`, `fecha`, `debe_usd`, `haber_usd`, `venta_id` nullable
- Enum `TipoMovimiento`: `FACTURA`, `PAGO`, `NOTA_CREDITO`, `AJUSTE`
- Modelo `MovimientoCuenta` con relaciones a `Cliente` y `Venta`
- Controller `CuentaCorrienteController@index`: devuelve movimientos con saldo acumulado corriente + resumen (debe_usd, haber_usd, saldo_usd)
- Ruta `GET /clientes/{cliente}/cuenta-corriente`
- `ClienteController@index`: usa `withSum` para calcular saldo de cada distribuidor en una sola query
- `ClienteResource`: nuevo campo `saldo_usd` = `debe_total_usd - haber_total_usd`
- `CuentaCorrienteSeeder`: datos de fantasía para los 4 distribuidores (Elit, New Bytes, Invid, Air) con historial desde 2025-Q3; facturas, pagos, notas de crédito y ajustes

**Saldos sembrados:**

| Distribuidor | Facturado | Pagado/NC | Saldo |
|---|---|---|---|
| Elit | $104,660 | $96,350 | $8,310 |
| New Bytes | $50,705 | $43,525 | $7,180 |
| Invid | $76,670 | $70,910 | $5,760 |
| Air | $32,695 | $28,250 | $4,445 |

**Frontend:**
- `clientes/index.vue`: columna "Saldo" con color ámbar (a cobrar) / verde (a favor), botones de acción separados (fondo marketing, cuenta corriente, editar, eliminar)
- Ruta Nuxt reorganizada: `[id].vue` → `[id]/index.vue` para habilitar ruta hija sin conflicto de layout
- `clientes/[id]/index.vue`: botón "Cuenta corriente" en header
- `clientes/[id]/cuenta-corriente.vue` (nueva página): 3 cards resumen + tabla con Fecha · Tipo · Referencia · Concepto · Debe · Haber · Saldo corriente acumulado

**Fix importante:** La API devuelve `{ data: {...} }` para recursos individuales. Todos los `api.get()` de detail pages deben usar `c?.data ?? c` para desempaquetar.

Archivos: `backend/database/migrations/0030_*`, `backend/app/Enums/TipoMovimiento.php`, `backend/app/Models/MovimientoCuenta.php`, `backend/app/Http/Controllers/CuentaCorrienteController.php`, `backend/database/seeders/CuentaCorrienteSeeder.php`, `frontend/pages/clientes/[id]/cuenta-corriente.vue`

### Reorganización de sidebar y secciones

**Renombres:**
- "Mercadería" → **"Stock Bodega"** (enlaza a `/mercaderia/stock` directamente)
- "Existencias" → **"Stock Distri"**
- "Productos" → **"APIs Distri"**
- "Marketing" (sección sidebar) → **"Fondo"** (ítem de menú)
- "Importaciones" → **"Subir Masivo"**
- Subtítulo distribuidores: "Agencias, estudios y distribuidores" → **"Mayoristas"**

**Estructura sidebar nueva:**
```
Principal:    Dashboard · Distribuidores · Proveedores
Operaciones:  Stock Bodega · Stock Distri · APIs Distri · Órdenes de Venta
Marketing:    Fondo · Calendario · Tareas
Admin:        Configuración (solo admin)
```

**Stock Bodega — navegación por tabs:**
- `mercaderia/index.vue` redirige automáticamente a `/mercaderia/stock`
- Las 3 subpáginas (stock, depósitos, importaciones) tienen tabs consistentes: **Stock | Depósitos | Subir Masivo**
- Tab activo: fondo blanco con sombra sobre pill gris
- Se quitó la tabla de ventas que antes aparecía en `/mercaderia`

**Stock Bodega — buscador y filtros:**
- Buscador full-text (nombre, SKU, código distribuidor) con debounce 300ms
- Filtro **Todos / Con stock / Sin stock** (parámetros `stock=con_stock|sin_stock`)

Archivos: `frontend/layouts/default.vue`, `frontend/pages/mercaderia/index.vue`, `frontend/pages/mercaderia/stock/index.vue`, `frontend/pages/mercaderia/depositos/index.vue`, `frontend/pages/mercaderia/importaciones/index.vue`

---
