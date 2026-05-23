# Contexto — gigaErp

## Negocio

Sistema interno de gestión para la marca **Gigabyte** (hardware IT).
Usuarios: equipo de marketing/administración de Gigabyte.
Moneda: USD exclusivamente.

## Usuarios

| Email | Pass | Rol | Permisos extra |
|-------|------|-----|----------------|
| `admin@gigabyte.com` | `admin123` | ADMIN | todos |
| `maria.gomez@gigabyte.com` | `demo1234` | OPERATIVO | VER_MONTOS |
| `lucas.herrera@gigabyte.com` | `demo1234` | OPERATIVO | — |

## Distribuidores (Clientes con tipo='distribuidor')

| Nombre | Ciudad | Fondo 2026 | Productos cargados |
|--------|--------|------------|-------------------|
| Elit | Buenos Aires | $50,000 | — |
| New Bytes | Córdoba | $40,000 | 206 productos |
| INVID | Mendoza | $35,000 | 41 productos |
| Air | Rosario | $30,000 | — |

> Los distribuidores son **Clientes** con `tipo='distribuidor'`. No son una entidad separada.

## Proveedores

| Nombre | Tipo |
|--------|------|
| Blu Studio | Estudio de Marketing |
| Imprenta Gráfica Sur | Imprenta |
| Logística Rápida SA | Logística |
| Tech Events SRL | Organización de Eventos |
| Media Digital Pro | Agencia Digital |

## Catálogo de productos — dos códigos

| Campo | Descripción | Ejemplo INVID | Ejemplo NB |
|-------|-------------|---------------|------------|
| `codigo_distribuidor` | Código interno del distribuidor | `0416990` | `GP-P550SS` |
| `sku` | Modelo oficial del fabricante (Gigabyte) | `GP-P550SS` | `GP-P550SS` |

- SKU es único **por distribuidor** (constraint 0025), no globalmente

## Branding / UI

- **Logo sidebar**: `aorus_logo_black.svg` en `layouts/default.vue`
- **Topbar**: texto "Brand ERP"
- Logos en `frontend/public/logos/`: `aorus_logo_black.svg`, `gigabyte_logo_clean.svg`
- `gigabyte_logo_clean.svg` embebido como base64 en el PDF de invoice

## Reglas de negocio

### Fondo de marketing
- Cada distribuidor tiene fondo asignado por año
- Acciones de marketing consumen el fondo (`monto_usd`)

### Tareas / Kanban
- 4 columnas: POR_HACER → EN_CURSO → READY_FOR_QA → LISTO
- Drag & drop HTML5 nativo, click → modal detalle estilo Jira

### Stock de productos
- Campo `stock` directo en `productos` — usado por Productos/Existencias
- Tabla `stock_deposito` (modelo `StockDeposito`) — usado por `/mercaderia/stock`

### Órdenes de Venta
- `OrdenVenta` (cabecera) + `ItemOrdenVenta` (líneas)
- Cada ítem tiene `deposito_id` nullable: de qué depósito se toma el stock
- Picker de productos en la orden filtra por depósito + stock (filtros combinados)
- Al agregar un producto: pills de depósito con stock disponible, auto-selecciona primer depósito con stock
- Listas de precio 1–4 disponibles en productos

### Invoice (PDF)
- Se genera desde `/ordenes-venta/[id]` al "Generar invoice" → crea registro `Venta`
- El PDF se descarga con el botón "Descargar PDF" en el banner verde de la orden
- Endpoint: `GET /api/ventas/{id}/pdf` (autenticado con Bearer)
- Formato: Commercial Invoice con logo, seller, buyer, payment terms, incoterm, bank details, firma
- Datos de empresa en tabla `configuraciones` (claves `empresa_*` e `invoice_*`)
- `shipping_usd` en la tabla ventas (default 0)

### Dashboard
- Ingresos = ventas PAGADA
- Gastos = AccionMarketing.monto_usd
- Solo USD

## Datos demo cargados

| Seeder | Entidad | Cantidad |
|--------|---------|----------|
| DemoSeeder | Productos legacy (stock por depósito) | 12 |
| DemoSeeder | Ventas | 13 (8 PAGADA · 4 PENDIENTE · 1 CANCELADA) |
| DemoSeeder | Tareas | 22 |
| DemoSeeder | Acciones de marketing | 15 |
| ProductoInvidSeeder | Productos Gigabyte INVID | 41 |
| ProductoNewBytesSeeder | Productos Gigabyte New Bytes | 206 |

## Configuraciones en DB (tabla configuraciones)

| Clave | Valor default |
|-------|---------------|
| `empresa_nombre` | Gigabyte |
| `empresa_direccion` | 123 Main St, Miami, FL 33101 |
| `empresa_ciudad_pais` | Miami, FL — USA |
| `empresa_telefono` | +1 (305) 000-0000 |
| `empresa_email` | sales@company.com |
| `empresa_web` | www.company.com |
| `invoice_payment_terms` | Net 30 |
| `invoice_incoterm` | FCA Miami |
| `invoice_banco_nombre` | Bank of America |
| `invoice_banco_cuenta` | 000-000000-00 |
| `invoice_banco_aba` | 026009593 |
| `invoice_banco_swift` | BOFAUS3N |
| `invoice_banco_direccion` | 100 N Tryon St, Charlotte, NC 28255 |
| `invoice_firma_nombre` | Authorized Representative |
| `invoice_firma_titulo` | Sales Manager |

> Todos estos valores se leen en tiempo real al generar el PDF. Editar en la sección Configuración.

## TODOs pendientes

- [ ] Agregar SKUs reales a productos de Elit y Air
- [ ] Export Excel (`maatwebsite/excel` instalado, stubs 501)
- [ ] Asignación de fondo desde panel cliente (hoy solo lectura)
- [ ] Permisos granulares en sidebar (hoy todos ven todo)
- [ ] Vista/edición de Ventas directa (hoy solo se accede via orden)
- [ ] Campo `shipping_usd` editable en alguna UI (hoy default 0)
- [x] Módulo Productos con filtros, stock, último ingreso
- [x] Módulo Existencias (tabla cruzada SKU × distribuidor)
- [x] Módulo Órdenes de Venta (cabecera + líneas + estados)
- [x] Stock con columnas dinámicas por depósito en `/mercaderia/stock`
- [x] Selección de depósito por ítem en órdenes de venta
- [x] Filtros complementarios depósito + stock en picker de orden
- [x] PDF Commercial Invoice con dompdf (barryvdh/laravel-dompdf)

## Bugs corregidos (historial)

- `config:cache` debe correr SIEMPRE después de `optimize:clear` (PHP-FPM no lee env vars)
- `apiResource('acciones')` → `{accione}` → fix `.parameters()`
- `apiResource('proveedores')` → `{proveedore}` → fix `.parameters()`
- `->keyBy('estado')` falla con enum cast → fix: `->keyBy(fn($v) => $v->estado->value)`
- Filtros de depósito y stock en picker de órdenes no se coordinaban → unificados en un solo `.filter()`

## Puerto confirmado

- **gigaErp: 8824** | minisaas: 8823 | DB: 3310

## Ver también

- [[gigaErp]] · [[arquitectura]] · [[changelog]] · [[memoria]]
