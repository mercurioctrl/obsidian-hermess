# Arquitectura — gigaErp

## Estructura de directorios

```
gigaErp/
├── backend/          ← Laravel 11 (PHP 8.4)
│   ├── app/
│   │   ├── Enums/            ← RolUsuario, EstadoTarea, PrioridadTarea, EstadoVenta, EstadoOrdenVenta
│   │   ├── Http/Controllers/ ← 21 resource controllers
│   │   ├── Http/Resources/   ← 9 API resources
│   │   ├── Models/           ← 20 Eloquent models
│   │   └── Services/
│   ├── database/
│   │   ├── migrations/       ← 0001–0029
│   │   └── seeders/          ← DatabaseSeeder + DemoSeeder + ProductoInvidSeeder + ProductoNewBytesSeeder
│   └── routes/api.php        ← todo dentro de auth:sanctum
├── frontend/         ← Nuxt 3 SPA (ssr: false)
│   ├── components/
│   │   ├── ui/               ← Modal, FormField, DataTable, StatsCard, StatusBadge, Toast
│   │   └── OrdenItems.vue    ← gestión de líneas en órdenes de venta (con picker por depósito)
│   ├── composables/          ← useApi, useNotification
│   ├── layouts/              ← default (sidebar+topbar), auth
│   ├── middleware/           ← auth.global.ts (global, no usar definePageMeta)
│   ├── pages/
│   │   ├── productos/index.vue         ← catálogo con grid/lista/filtros/stock
│   │   ├── existencias/index.vue       ← tabla cruzada SKU × distribuidor
│   │   ├── ordenes-venta/index.vue     ← listado de órdenes
│   │   ├── ordenes-venta/nueva.vue     ← crear orden con líneas dinámicas
│   │   └── ordenes-venta/[id].vue      ← detalle, edición y descarga de PDF
│   ├── public/logos/         ← aorus_logo_black.svg, gigabyte_logo_clean.svg
│   └── stores/               ← auth.ts (Pinia)
├── nginx/default.conf        ← /api/* y /storage/* → backend:9000, /* → frontend:3000
└── docker-compose.yml        ← 6 servicios: db, redis, backend, scheduler, frontend, nginx
```

## Patrones de backend

- Resource controllers: `index / store / show / update / destroy`
- Respuestas con Resource: wrap `{ data: {} }` automático
- Colecciones paginadas: `{ data: [], meta: { total, per_page, current_page, last_page } }`
- Colecciones sin paginar (`get()`): `{ data: [] }` sin `meta`
- Rutas estáticas **siempre antes** del `apiResource`

## Módulo Productos — `GET /api/productos`

```
Filtros: ?search=X &distribuidor_id=N &stock=con_stock|sin_stock &activo=1
Pagina: 50 por página
Eager loads: distribuidor, stocks.deposito
```

Campos por producto: `id, nombre, codigo_distribuidor, sku, marca, precio, precio_oferta, iva, precio_final, precio_lista_1..4, foto_principal, distribuidor_id, distribuidor{id,nombre}, activo, stock, stocks_deposito{deposito_id:cantidad}, stock_total, ultimo_ingreso`

### Endpoint seleccionables — `GET /api/productos/seleccionables`

Endpoint sin paginación para los modales de selección de productos. Devuelve solo campos necesarios para el picker:

```php
// ProductoController::seleccionables()
Producto::with('stocks')->get()->map(fn($p) => [
    'id', 'nombre', 'sku', 'codigo_distribuidor', 'foto_principal',
    'precio_lista_1'..'precio_lista_4',
    'stock' => stocks.sum('cantidad'),
    'stocks_deposito' => { deposito_id: cantidad, ... }
])
```

No pagina — carga hasta 60 en el picker con `.slice(0, 60)` en el frontend.

### Dos códigos en Producto

| Campo | Descripción | Lookup key en seeder |
|-------|-------------|---------------------|
| `codigo_distribuidor` | Código interno del distribuidor | ✅ (updateOrCreate) |
| `sku` | SKU real del fabricante (Gigabyte) | solo almacenado, no es PK |

### stocks_deposito en ProductoResource

```php
// Solo presente cuando se carga la relación stocks.deposito
'stocks_deposito' => $this->whenLoaded('stocks', fn() =>
    $this->stocks->mapWithKeys(fn($s) => [$s->deposito_id => (int) $s->cantidad])->toArray()
),
'stock_total' => $this->whenLoaded('stocks', fn() => (int) $this->stocks->sum('cantidad'), (int) $this->stock),
```

## Módulo Existencias — `GET /api/existencias`

Endpoint no-resource (solo `index`). Agrupa todos los productos con SKU no-null por SKU.

```json
{
  "distribuidores": [{ "id": N, "nombre": "..." }],
  "items": [{
    "sku": "GV-N1030D4-2GL",
    "nombre": "...",
    "marca": "Gigabyte",
    "foto_principal": "...",
    "precio": 111.38,
    "precio_final": 123.07,
    "stock": { "1": 45, "2": null },
    "stock_total": 45
  }]
}
```

- `stock[dist_id] = N` → tiene el producto, N unidades
- `stock[dist_id] = 0` → tiene el producto, sin unidades
- `stock[dist_id] = null` → no vende ese producto
- **Todos** los distribuidores (tipo=distribuidor) aparecen como columnas, aunque no tengan productos

## Módulo Órdenes de Venta — `GET /api/ordenes-venta`

```
Pagina: estándar
Modelos: OrdenVenta (cabecera) → ItemOrdenVenta (líneas, FK: orden_venta_id)
Enum: EstadoOrdenVenta
Resource: OrdenVentaResource (incluye items embebidos)
```

Las órdenes usan las listas de precio 1–4 del modelo Producto (migración 0026).

### Depósito por ítem de orden (migración 0028)

Cada `ItemOrdenVenta` puede tener un `deposito_id` nullable, indicando de qué depósito se toma el stock.

```php
// ItemOrdenVenta: $fillable incluye 'deposito_id'
// belongsTo: Deposito
// En OrdenVentaResource → items:
'deposito_id'     => $i->deposito_id,
'deposito_nombre' => $i->deposito?->nombre,
```

En el picker (`OrdenItems.vue`), el usuario puede:
1. Filtrar por depósito (dropdown) → solo muestra productos disponibles en ese depósito
2. Ver pills de depósito por producto (si está en varios, elegir el origen)
3. El depósito elegido se guarda como `deposito_id` en el ítem

**Coerción de tipos importante**: el select HTML devuelve string, pero las keys de `stocks_deposito` son enteros. Siempre usar `Number(filtroDeposito.value)` y fallback `p.stocks_deposito?.[String(depId)]`.

## Módulo Invoice PDF — `GET /api/ventas/{id}/pdf`

Flujo completo: OrdenVenta → [Generar Invoice] → Venta → [Descargar PDF]

```
OrdenVenta (estado BORRADOR) 
  → POST /ordenes-venta/{id}/invoice 
  → crea Venta (VTA-XXXX) 
  → OrdenVenta queda FACTURADA
  
Venta
  → GET /ventas/{id}/pdf
  → dompdf genera Commercial Invoice
  → retorna binary PDF
```

### Descarga de PDF en frontend

`useApi` solo retorna JSON. Para binarios se usa `fetch()` nativo con Bearer token:

```ts
const resp = await fetch(`/api/ventas/${venta_id}/pdf`, {
  headers: { Authorization: `Bearer ${authStore.token}` },
})
const blob = await resp.blob()
const url = URL.createObjectURL(blob)
// crear <a> temporal, click, revocar URL
```

### Invoice PDF — estructura

Generado con `barryvdh/laravel-dompdf:^2.2` desde `resources/views/ventas/invoice.blade.php`.

Secciones del Commercial Invoice:
- **Header**: Logo base64 + título "COMMERCIAL INVOICE" + número `INV-{YEAR}-{N}` + fecha
- **Seller/Buyer**: dos columnas, datos desde `$config['empresa_*']` y `$venta->cliente`
- **Terms bar**: Payment Terms · Incoterm · Currency · Items count
- **Items table**: header negro, filas con SKU/descripción/qty/precio unitario/subtotal
- **Totals**: Subtotal / Shipping (oculto si = 0) / Total USD
- **Bank Details** + **Authorized Signature**: dos cajas lado a lado
- CSS `page-break-inside: avoid` en todos los bloques principales (dompdf pagination fix)

### Logo en PDF (dompdf)

dompdf no puede cargar URLs externas. El SVG del logo se embebe como base64 data URI directamente en el Blade template:

```html
<img src="data:image/svg+xml;base64,{base64_encoded_svg}" alt="Gigabyte" />
```

### Configuraciones de invoice (tabla `configuraciones`)

Claves sembradas por migración 0029 con `firstOrCreate`:

| Clave | Uso en PDF |
|-------|-----------|
| `empresa_nombre`, `empresa_direccion`, `empresa_ciudad_pais` | Bloque Seller |
| `empresa_telefono`, `empresa_email`, `empresa_web` | Bloque Seller |
| `invoice_payment_terms`, `invoice_incoterm` | Terms bar |
| `invoice_banco_nombre`, `invoice_banco_cuenta`, `invoice_banco_aba`, `invoice_banco_swift`, `invoice_banco_direccion` | Bank Details |
| `invoice_firma_nombre`, `invoice_firma_titulo` | Authorized Signature |

### Campo shipping_usd (migración 0029)

`ventas.shipping_usd DECIMAL(10,2) DEFAULT 0` — se muestra en el PDF solo si > 0. No tiene UI de edición todavía (siempre 0 en la práctica).

## Vista Stock por depósito — `/mercaderia/stock`

La tabla genera columnas dinámicas según los depósitos activos en `GET /api/depositos`:

```ts
const columnas = computed(() => [
  { key: 'sku', label: 'SKU' },
  { key: 'nombre', label: 'Nombre' },
  ...depositos.value.map((d) => ({ key: `dep_${d.id}`, label: d.nombre })),
  { key: 'total', label: 'Total' },
  { key: 'unidad', label: 'Unidad' },
  { key: 'acciones', label: '' },
])
```

Cada celda de depósito lee `row.stocks_deposito?.[d.id]`.

## Paginación vs colección por módulo

| Módulo | Backend | Frontend — leer con |
|--------|---------|---------------------|
| Clientes, Ventas, Acciones, Productos, Órdenes de Venta | `paginate(20/50)` | `res.data` + `res.meta` |
| Tareas, Etiquetas, Tipos, Estados | `get()` | `res.data ?? res` |
| Existencias | `get()` agrupado | `res.distribuidores` + `res.items` (sin wrapper data) |

## API Resources — relaciones cargadas

### ProductoResource
| Endpoint | Relaciones cargadas |
|----------|-------------------|
| `index()` | `distribuidor`, `stocks.deposito` |
| `show()` | `stocks.deposito` |

### AccionMarketingResource
| Endpoint | Relaciones cargadas |
|----------|-------------------|
| `index()` | `cliente`, `tipo`, `estado`, `campana`, `creadoPor` |
| `show()` | todo lo anterior + `adjuntos`, `tareas` |

### TareaResource
| Endpoint | Relaciones |
|----------|-----------|
| `index()` | `cliente`, `proveedor`, `asignadoUsuario`, `etiquetas` |
| `show()` | todo lo anterior + `asignadoProveedor`, `accion`, `creadoPor` |

## apiResource — pluralización española (BUG CONOCIDO)

| apiResource | Parámetro generado | Fix aplicado |
|------------|-------------------|-------------|
| `acciones` | `{accione}` ❌ | `.parameters(['acciones' => 'accion'])` |
| `proveedores` | `{proveedore}` ❌ | `.parameters(['proveedores' => 'proveedor'])` |
| `productos` | `{producto}` ✅ | OK sin fix |
| `ordenes-venta` | verificar con route:list | aplicar fix si es necesario |

**Síntoma**: Resource devuelve campos en `null` sin 404 ni 500.
**Diagnóstico**: `php artisan route:list --path=api/X`.

## Enum en colecciones — bug keyBy

`->get()->keyBy('estado')` falla con enum cast. **Fix**: `->keyBy(fn($v) => $v->estado->value)`

## Dashboard — estructura GET /api/dashboard

```json
{
  "kpis": { "clientes_activos", "ingresos_mes", "gastos_mes", "resultado_mes", "cobrado_mes", "pendiente_cobro" ... },
  "ventas_por_estado": { "PAGADA": { "cantidad": N, "total": N }, ... },
  "top_clientes": [{ "id", "nombre", "total_ventas" }],
  "ultimos_12_meses": [{ "label": "MAY", "mes": 5, "anio": 2026, "ingresos": N, "gastos": N }]
}
```

## Pixel Bar Chart SVG (pages/index.vue)

```ts
const PX_SIZE = 5   // barW = PX_SIZE para cuadrados perfectos
const PX_GAP  = 2
const CHART_H = 140
const MAX_PX  = 20  // filas de cuadraditos por barra
```

## Decisiones de diseño

### `config:cache` obligatorio (PHP-FPM)
`env()` devuelve null en PHP-FPM. Fix: `docker exec gigaerp-backend php artisan config:cache`
**Patrón**: después de cada `optimize:clear`, siempre ejecutar `config:cache`.

### Distribuidores = Clientes con `tipo='distribuidor'`
No hay tabla separada para distribuidores. Campo `tipo` en `clientes`.
Productos se vinculan con `distribuidor_id` (FK → `clientes.id`).

### Dos tablas de stock coexisten
- `stock` directo en tabla `productos`: usado por módulos Productos y Existencias
- `stock_deposito` (via `StockDeposito` model): usado por `/mercaderia/stock`
- Son independientes — no se sincronizan automáticamente

### Migración de datos en seeders, no en migraciones
La migración solo agrega columnas. El llenado inicial va en los seeders.

## Modelos y relaciones principales

```
Usuario ─────── tareas (asignado_usuario_id / creado_por_id)
Cliente ─┬────── tareas · acciones_marketing · campanas
(=Dist.) ├────── asignaciones_fondo · eventos_calendario
         ├────── ventas
         ├────── ordenes_venta
         └────── productos (via distribuidor_id)
Proveedor ────── tareas (proveedor_id / asignado_proveedor_id)
AccionMarketing ─┬─── tareas · accion_adjuntos
Campana ──────── acciones_marketing
Producto ─┬───── stock_deposito · items_orden_venta
Deposito ──────── stock_deposito · items_orden_venta (nullable)
Venta ─────────── items_venta (generada desde OrdenVenta)
OrdenVenta ────── items_orden_venta
```

## Permisos

- `ADMIN`: acceso total
- `OPERATIVO`: array JSON `permisos` en el modelo (`VER_MONTOS`, `VER_SECCION_CLIENTES`, etc.)

## Ver también

- [[gigaErp]] · [[stack]] · [[changelog]] · [[contexto]] · [[memoria]]
