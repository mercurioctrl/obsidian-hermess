# Contexto — gigaErp

## Negocio

Sistema interno de gestión para la marca **Gigabyte** (hardware IT).
Usuarios: equipo de marketing/administración de Gigabyte.
Moneda: USD exclusivamente.

## Usuarios

| Email | Pass | Rol | Permisos extra |
|-------|------|-----|----------------|
| `admin@gigabyte.com` | `admin123` | ADMIN | todos |
| `carolina.lagos@gigabyte.com` | `demo1234` | OPERATIVO | aprobaciones + VER_MONTOS |
| `martin.fierro@gigabyte.com` | `demo1234` | OPERATIVO | VER_MONTOS |
| `julia.mendez@gigabyte.com` | `demo1234` | OPERATIVO | — |

## Distribuidores (Clientes con tipo='distribuidor')

| Nombre | Ciudad | Fondo 2026 | Saldo cc | Línea de crédito |
|--------|--------|------------|----------|-----------------|
| Elit | Buenos Aires | $50,000 | $8,310 a cobrar | $30,000 |
| New Bytes | Córdoba | $40,000 | $7,180 a cobrar | $20,000 |
| Invid | Mendoza | $35,000 | $5,760 a cobrar | $40,000 |
| Air | Rosario | $30,000 | $4,445 a cobrar | $12,000 |

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
| `/marketing` | Fondos | Marketing |
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
- **Patrón filtros**: todas las páginas envuelven filtros en `bg-white rounded-xl border border-[#E8E8E3] p-4`

## Reglas de negocio

### Cuenta corriente de distribuidores

- Tabla `movimientos_cuenta`: `tipo` (FACTURA, PAGO, NOTA_CREDITO, AJUSTE), `debe_usd`, `haber_usd`
- Saldo = suma(debe) - suma(haber). Positivo = cliente debe. Negativo = cliente tiene crédito.
- El listado de distribuidores muestra el saldo de cada uno (calculado con `withSum` en el index)
- Página dedicada `/clientes/{id}/cuenta-corriente` con saldo acumulado corriente por fila
- Click en fila del listado → va directo a cuenta corriente (no a la ficha)

### Línea de crédito

- Campo `linea_credito_usd` nullable en `clientes`
- Solo admins pueden editar (botón lápiz visible solo con `authStore.isAdmin`)
- Cada cambio genera registro en `historial_linea_credito` con monto anterior, nuevo, usuario y notas
- La cuenta corriente muestra barra de utilización (saldo / línea); roja si >90%

### Nota de crédito

- Entidad `NotaCredito` con ítems de texto libre (`NotaCreditoItem`) — no usa productos del catálogo
- Numeración: NC-0001, NC-0002...
- Al crear: se asienta automáticamente un movimiento `NOTA_CREDITO` (haber) en `movimientos_cuenta`
- Preview pública: `GET /api/notas-credito/{id}/preview?token=...` — mismo patrón que invoices
- Desde cuenta corriente: crear NC manual con ítems libres
- Desde orden de venta (FACTURADA): crear NC pre-llenada con ítems de la orden, editable para parciales

### Fondo de marketing

- Cada distribuidor tiene fondo asignado por año
- Acciones de marketing consumen el fondo (`monto_usd`)

### Tareas / Kanban

- 4 columnas: POR_HACER → EN_CURSO → READY_FOR_QA → LISTO
- Drag & drop HTML5 nativo, click → modal detalle estilo Jira

### Stock de productos — dos sistemas independientes

- Campo `stock` directo en `productos` — usado por APIs Distri / Stock Distri
- Tabla `stock_deposito` (modelo `StockDeposito`) — usado por Stock Bodega (`/mercaderia/stock`)
- Son independientes — no se sincronizan automáticamente
- Las importaciones XLSX actualizan `stock_deposito` (no el campo `stock`)

### Importaciones de stock (XLSX)

- Flujo 3 pasos: subir archivo → mapear columnas → confirmar
- `POST /api/mercaderia/importaciones/parsear` — guarda en storage, devuelve headers
- `POST /api/mercaderia/importaciones/procesar` — upsert `stock_deposito` por producto+depósito
- Trazabilidad: tabla `importaciones_mercaderia` + `items_importacion_mercaderia`
- **Lookup doble**: primero por `sku`, luego por `codigo_distribuidor` (los Excel suelen usar el segundo)

### Órdenes de Venta — flujo de estados

```
BORRADOR → APROBADA → FACTURADA
    ↓           ↓
  ANULADA    ANULADA
```

- Solo usuarios con permiso `aprobaciones` pueden aprobar
- Solo desde APROBADA se puede generar invoice (FACTURADA)
- Desde FACTURADA se puede emitir nota de crédito total o parcial

### Invoice (PDF)

- Se genera desde `/ordenes-venta/[id]` al "Generar invoice" → crea registro `Venta`
- Endpoint: `GET /api/ventas/{id}/pdf` (autenticado con Bearer)
- Preview pública: `GET /api/ventas/{venta}/preview?token=...`
- Datos de empresa en tabla `configuraciones` (claves `empresa_*` e `invoice_*`)

## TODOs pendientes

- [ ] Agregar SKUs reales a productos de Elit y Air
- [ ] Export Excel (`maatwebsite/excel` instalado, stubs 501)
- [ ] Permisos granulares en sidebar (hoy todos ven todo)
- [ ] Vista/edición de Ventas directa (hoy solo se accede via orden)
- [ ] Campo `shipping_usd` editable en alguna UI (hoy default 0)
- [ ] Anular nota de crédito (endpoint de estado ANULADA)
- [x] Nota de crédito desde cuenta corriente (texto libre)
- [x] Nota de crédito desde orden facturada (pre-llenada, editable para parciales)
- [x] Línea de crédito por distribuidor con historial de cambios
- [x] Validación stock en picker de órdenes
- [x] Importaciones masivas de stock desde XLSX con mapeo de columnas
- [x] Módulo Cuenta Corriente por distribuidor
- [x] Reorganización sidebar
- [x] Estado APROBADA en órdenes + permisos configurables
- [x] PDF Commercial Invoice + preview Blu-style

## Bugs corregidos (historial)

- `config:cache` debe correr SIEMPRE después de `optimize:clear` (PHP-FPM no lee env vars)
- `apiResource` pluralización española → fix `.parameters()`
- `->keyBy('estado')` falla con enum cast → fix: `->keyBy(fn($v) => $v->estado->value)`
- Filtros de depósito y stock en picker no se coordinaban → unificados
- Nuxt `[id].vue` + carpeta `[id]/` → mover a `[id]/index.vue`
- API devuelve `{ data: {} }` para recursos individuales → siempre usar `c?.data ?? c`
- Solo primer usuario visible en Configuración → `UsuarioResource::collection` devuelve `{ data: [] }` → `res?.data ?? res`
- `authStore` en template → inicializar en `<script setup>`, no dentro de funciones
- Filtros Stock Bodega sin card wrapper → agregado `bg-white rounded-xl border p-4`
- Sidebar "Fondo" → "Fondos"

## Puerto confirmado

- **gigaErp: 8824** | minisaas: 8823 | DB: 3310

## Ver también

[[gigaErp]] · [[arquitectura]] · [[changelog]] · [[memoria]]
