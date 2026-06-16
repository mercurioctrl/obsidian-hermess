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

> Stock Bodega tiene 4 tabs: **Stock · Catálogo · Depósitos · Subir Masivo**.
> "Subir Masivo" = importaciones de stock (XLSX). "Catálogo" (`/mercaderia/catalogo`) = editar parámetros de producto.

## Catálogo de productos — códigos

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `codigo_distribuidor` | Código interno del distribuidor | `0416990` (INVID) |
| `sku` | Modelo oficial del fabricante (Gigabyte) | `GP-P550SS` |
| `item_no` | Código por ítem del catálogo GIGABYTE | `28E00-10365-1CARR` |
| `global_part` | Global Part No (modelo) | `GB-C103GP65G5 GAR1` |

- SKU es único **por distribuidor** (constraint 0025), no globalmente.

### Catálogo GIGABYTE (carga masiva)

Productos cargados desde el archivo del contacto de GIGABYTE (sin distribuidor):
- `marca=GIGABYTE`, `distribuidor_id=null`
- **`sku` = `codigo_distribuidor` = `item_no`** → permite cruzar el stock con el importador de mercadería (que matchea por sku/codigo_distribuidor)
- `nombre` = `modelo` = Global Part
- Campos propios (mig `0040`): `bu_code`, `chipset`, `item_no`, `global_part`, `link`, `ean`, `carton_box_qty`, `carton_peso_kg`, `carton_largo_mm`, `carton_ancho_mm`, `carton_alto_mm`
- **UPC NO se usa.**
- Carga: wizard `/productos/importar` o pestaña Catálogo. Detalle en [[modulos/productos#Carga masiva de catálogo GIGABYTE]].

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
- ⚠️ Para productos propios la **verdad del stock es `stock_deposito`**, NO la columna global `productos.stock` (queda desactualizada / con basura del import: `StockController@update` solo escribe `stock_deposito`, nunca la columna global).

### Stock y depósitos — reglas (2026-06-16)

- **Producto propio = `distribuidor_id IS NULL`** (creado a mano o por carga masiva de catálogo). Los productos con distribuidor van a Stock Distri / APIs Distri / Resellers y NO se mezclan. Tanto **Catálogo** (`solo_catalogo`) como **Stock Bodega** (`solo_inventario`) muestran TODOS los propios, tengan o no stock.
- **Depósito con "Stock Ilimitado"** (`depositos.stock_ilimitado`, migración `0041`): al armar orden/pre-orden con ese depósito se puede poner cualquier cantidad sin tope. Se setea en Mercadería → Depósitos. Frontend: `OrdenItems.vue` libera el tope y muestra ∞; Stock Bodega muestra ícono `lucide:infinity` en esa columna. El backend NO descuenta stock — el tope solo lo imponía el front.
- **Filtro de stock** (pestañas Todos / Con stock / Sin stock, en Catálogo y Stock Bodega), 100% sobre `stock_deposito`:
  - `con_stock` = existe `stock_deposito.cantidad > 0` en un depósito **no** ilimitado.
  - `sin_stock` = negación exacta (sin filas, todo en 0, o stock solo en depósito ilimitado).
  - **Depósito ilimitado NO cuenta como "con stock"** (el infinito no es stock real).

### Listas de precio — reglas (2026-06-16)

Las 4 listas son columnas fijas `productos.precio_lista_1..4` (no hay tabla de listas). Ver [[memoria]] (composable) y [[changelog#2026-06-16 — Listas de precio]].

- **Nombres configurables**: en la tabla `configuraciones` (claves `nombre_lista_1..4`) vía `/api/config`. Se editan en Configuración → "Listas de precio". Se muestran como "Lista N · Nombre". Composable `useListasPrecio` (`labelLista(n)`).
- **Lista por defecto del cliente** (`clientes.lista_precio_defecto`, mig `0042`): lista inicial al armar órdenes para ese cliente; overrideable por ítem.
- **Permisos de lista por usuario** (`usuarios.listas_precio` JSON, mig `0043`): qué listas puede usar cada usuario. **Admin = todas; no-admin = exactamente las asignadas; vacío/null = todas.** Los selectores muestran solo las permitidas; el backend (`OrdenVentaController`) valida 422 si se manda una no permitida. Un usuario logueado necesita re-login para ver nuevas restricciones.
- **Importación masiva por global_part**: botón Importar en Precios. El Excel/CSV se parsea en el navegador (SheetJS) y se mandan las filas como JSON a `POST /precios/importar` → esquiva la falta de PhpSpreadsheet en el container. Update por global_part sobre productos propios; solo columnas de lista con valor.

### Importaciones de stock (XLSX)

- Flujo 3 pasos: subir archivo → mapear columnas → confirmar
- `POST /api/importaciones-mercaderia/parsear` — guarda en storage, devuelve headers
- `POST /api/importaciones-mercaderia` — upsert `stock_deposito` por producto+depósito
- Trazabilidad: tabla `importaciones_mercaderia` + `items_importacion_mercaderia`
- **Lookup doble**: primero por `sku`, luego por `codigo_distribuidor` (los Excel suelen usar el segundo)
- Para el catálogo GIGABYTE el cruce funciona porque `sku`/`codigo_distribuidor` = `item_no`.

### Carga masiva del catálogo (productos, no stock)

- `POST /api/importaciones-catalogo/parsear` + `POST /api/importaciones-catalogo`
- **Upsert de productos por `item_no`** (crea/actualiza, no duplica). No toca stock.
- Parsea CSV nativo; xlsx necesita PhpSpreadsheet (ver [[troubleshooting#8. PhpSpreadsheet no instalado en el container|troubleshooting #8]]).

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

- [ ] **Limpieza data**: ~1807 productos propios (`distribuidor_id` NULL) sin inventario real — entraron sin distribuidor pero sin filas de stock, codigo_distribuidor numérico, columna global stock del import. Decidir si borrar o reasignar distribuidor. Hoy visibles en Catálogo bajo "Sin stock".
- [ ] Reconstruir imagen del backend para habilitar import xlsx (PhpSpreadsheet) — hoy solo CSV
- [ ] Cargar precios/listas al catálogo GIGABYTE (la carga masiva trae productos sin precio)
- [ ] Agregar SKUs reales a productos de Elit y Air (Ceven/Stylus ya los tienen via vincular-skus)
- [ ] Resellers: comparativa de precios entre tiendas para el mismo SKU
- [ ] Export Excel (`maatwebsite/excel` en composer.json, falta instalar en container)
- [ ] Permisos granulares en sidebar (hoy todos ven todo)
- [ ] Vista/edición de Ventas directa (hoy solo se accede via orden)
- [ ] Campo `shipping_usd` editable en alguna UI (hoy default 0)
- [ ] Anular nota de crédito (endpoint de estado ANULADA)
- [x] Depósito con "Stock Ilimitado" (mig 0041) + filtro de stock por depósito (Todos/Con/Sin) en Catálogo y Stock Bodega
- [x] Carga masiva del catálogo GIGABYTE (campos del mail) + pestaña Catálogo editable
- [x] Integración real partpicker: sync Air/Ceven/Invid/Stylus con vincular-skus
- [x] Módulo Resellers live (sin DB) con filtros
- [x] Filtro de marca default GIGABYTE en APIs Distri, Stock Distri y Resellers
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

- `mapping.*` necesario en `validate()`: con solo `mapping.item_no` se descartan las demás claves del array
- `productos.codigo_distribuidor` NOT NULL sin default → setear = item_no al crear desde catálogo
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

[[gigaErp]] · [[arquitectura]] · [[changelog]] · [[memoria]] · [[modulos/productos]]
