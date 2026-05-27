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

| Nombre | Ciudad | Fondo 2026 | Saldo cc |
|--------|--------|------------|----------|
| Elit | Buenos Aires | $50,000 | $8,310 a cobrar |
| New Bytes | Córdoba | $40,000 | $7,180 a cobrar |
| INVID | Mendoza | $35,000 | $5,760 a cobrar |
| Air | Rosario | $30,000 | $4,445 a cobrar |

> Los distribuidores son **Clientes** con `tipo='distribuidor'`. No son una entidad separada.

## Proveedores

| Nombre | Tipo |
|--------|------|
| Blu Studio | Estudio de Marketing |
| Imprenta Gráfica Sur | Imprenta |
| Logística Rápida SA | Logística |
| Tech Events SRL | Organización de Eventos |
| Media Digital Pro | Agencia Digital |

## Nomenclatura de secciones (nombres en la UI)

| URL | Nombre en sidebar | Sección |
|-----|------------------|---------|
| `/clientes` | Distribuidores | Principal |
| `/mercaderia/stock` | Stock Bodega | Operaciones |
| `/existencias` | Stock Distri | Operaciones |
| `/productos` | APIs Distri | Operaciones |
| `/ordenes-venta` | Órdenes de Venta | Operaciones |
| `/marketing` | Fondo | Marketing |
| `/calendario` | Calendario | Marketing |
| `/tareas` | Tareas | Marketing |

> La subsección "Importaciones" dentro de Stock Bodega se llama **"Subir Masivo"** en tabs y botón.

## Catálogo de productos — dos códigos

| Campo | Descripción | Ejemplo INVID |
|-------|-------------|---------------|
| `codigo_distribuidor` | Código interno del distribuidor | `0416990` |
| `sku` | Modelo oficial del fabricante (Gigabyte) | `GP-P550SS` |

- SKU es único **por distribuidor** (constraint 0025), no globalmente

## Branding / UI

- **Logo sidebar**: `aorus_logo_black.svg` en `layouts/default.vue`
- **Topbar**: texto "Brand ERP"
- Subtítulo distribuidores: "Mayoristas"

## Reglas de negocio

### Cuenta corriente de distribuidores
- Tabla `movimientos_cuenta`: `tipo` (FACTURA, PAGO, NOTA_CREDITO, AJUSTE), `debe_usd`, `haber_usd`
- Saldo = suma(debe) - suma(haber). Positivo = cliente debe. Negativo = cliente tiene crédito.
- El listado de distribuidores muestra el saldo de cada uno (calculado con `withSum` en el index)
- Página dedicada `/clientes/{id}/cuenta-corriente` con saldo acumulado corriente por fila

### Fondo de marketing
- Cada distribuidor tiene fondo asignado por año
- Acciones de marketing consumen el fondo (`monto_usd`)

### Tareas / Kanban
- 4 columnas: POR_HACER → EN_CURSO → READY_FOR_QA → LISTO
- Drag & drop HTML5 nativo, click → modal detalle estilo Jira

### Stock de productos
- Campo `stock` directo en `productos` — usado por APIs Distri / Stock Distri
- Tabla `stock_deposito` (modelo `StockDeposito`) — usado por Stock Bodega (`/mercaderia/stock`)
- Son independientes — no se sincronizan automáticamente

### Órdenes de Venta
- `OrdenVenta` (cabecera) + `ItemOrdenVenta` (líneas)
- Cada ítem tiene `deposito_id` nullable: de qué depósito se toma el stock
- Listas de precio 1–4 disponibles en productos

### Invoice (PDF)
- Se genera desde `/ordenes-venta/[id]` al "Generar invoice" → crea registro `Venta`
- Endpoint: `GET /api/ventas/{id}/pdf` (autenticado con Bearer)
- Preview pública: `GET /api/ventas/{venta}/preview?token=...`
- Datos de empresa en tabla `configuraciones` (claves `empresa_*` e `invoice_*`)

## TODOs pendientes

- [ ] Agregar SKUs reales a productos de Elit y Air
- [ ] Export Excel (`maatwebsite/excel` instalado, stubs 501)
- [ ] Asignación de fondo desde panel cliente (hoy solo lectura)
- [ ] Permisos granulares en sidebar (hoy todos ven todo)
- [ ] Vista/edición de Ventas directa (hoy solo se accede via orden)
- [ ] Campo `shipping_usd` editable en alguna UI (hoy default 0)
- [ ] Ingresar movimientos de cuenta corriente desde la UI (hoy solo lectura del seeder)
- [x] Módulo Cuenta Corriente por distribuidor (movimientos_cuenta, saldo en listado)
- [x] Reorganización sidebar (Operaciones + Marketing subsecciones)
- [x] Stock Bodega con tabs + buscador + filtro con/sin stock
- [x] Módulo Productos con filtros, stock, último ingreso
- [x] Módulo Existencias (tabla cruzada SKU × distribuidor)
- [x] Módulo Órdenes de Venta (cabecera + líneas + estados)
- [x] PDF Commercial Invoice

## Bugs corregidos (historial)

- `config:cache` debe correr SIEMPRE después de `optimize:clear` (PHP-FPM no lee env vars)
- `apiResource('acciones')` → `{accione}` → fix `.parameters()`
- `apiResource('proveedores')` → `{proveedore}` → fix `.parameters()`
- `->keyBy('estado')` falla con enum cast → fix: `->keyBy(fn($v) => $v->estado->value)`
- Filtros de depósito y stock en picker de órdenes no se coordinaban → unificados en un solo `.filter()`
- Nuxt: `[id].vue` coexistiendo con `[id]/` carpeta → el `.vue` actúa como layout padre. Fix: mover a `[id]/index.vue`
- API devuelve `{ data: {} }` para recursos individuales → siempre usar `c?.data ?? c` en detail pages

## Puerto confirmado

- **gigaErp: 8824** | minisaas: 8823 | DB: 3310

## Ver también

- [[gigaErp]] · [[arquitectura]] · [[changelog]] · [[memoria]]
