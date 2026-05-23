# Módulo: Órdenes de Venta

Pipeline para armar órdenes y generarlas como invoices. Las órdenes son la **fuente**;
las invoices son **Ventas** (reusamos la tabla `ventas` que ya existía).

## Modelo de datos

### `ordenes_venta` (migración `0027`)

| Columna | Tipo | Notas |
|---------|------|-------|
| `id` | bigint | |
| `numero` | string unique | formato `OV-0001` |
| `cliente_id` | FK → `clientes` | cascadeOnDelete |
| `usuario_id` | FK → `usuarios` nullable | quien la creó |
| `venta_id` | FK → `ventas` nullable | invoice generada (null si BORRADOR) |
| `estado` | string | enum `EstadoOrdenVenta` |
| `fecha` | date | |
| `total_usd` | decimal(12,2) | recalculado al sincronizar items |
| `notas` | text nullable | |

### `items_orden_venta` (migración `0027` + `0028`)

| Columna | Tipo | Notas |
|---------|------|-------|
| `id` | bigint | |
| `orden_venta_id` | FK → `ordenes_venta` | cascadeOnDelete |
| `producto_id` | FK → `productos` | cascadeOnDelete |
| `deposito_id` | FK → `depositos` nullable | de qué depósito sale (mig `0028`) |
| `lista_precio` | tinyint | 1..4 (cuál de las 4 listas del producto) |
| `cantidad` | int | |
| `precio_usd` | decimal(12,2) | **snapshot** del precio de la lista al momento de crear |
| `subtotal_usd` | decimal(12,2) | |

**Constraint:** `unique(orden_venta_id, producto_id)` — un SKU no se repite en la orden.

## Estados (`EstadoOrdenVenta` enum)

```
BORRADOR  → FACTURADA   (al generar invoice; crea Venta)
BORRADOR  → ANULADA     (manualmente)
BORRADOR  → eliminada   (DELETE; solo si BORRADOR)
```

Una vez `FACTURADA` o `ANULADA`, no se puede editar ni eliminar.

## Endpoints

```
GET    /api/ordenes-venta                    listado paginado (filtros: cliente_id, estado, search)
POST   /api/ordenes-venta                    crear (estado BORRADOR)
GET    /api/ordenes-venta/{id}               show con items + venta
PUT    /api/ordenes-venta/{id}               editar (422 si no es BORRADOR)
DELETE /api/ordenes-venta/{id}               eliminar (422 si FACTURADA)
PATCH  /api/ordenes-venta/{id}/anular        → ANULADA (422 si FACTURADA)
POST   /api/ordenes-venta/{id}/invoice       genera Venta, marca FACTURADA (201)
```

Las rutas estáticas (`/invoice`, `/anular`) van **antes** del `apiResource` con
`->parameters(['ordenes-venta' => 'orden_venta'])` para que el route model binding funcione.

## Generación de la invoice

`OrdenVentaController@generarInvoice` (dentro de transacción):

1. Valida que la orden esté en `BORRADOR` y tenga ítems.
2. Crea una `Venta` nueva (`VTA-XXXX`) con `cliente_id`, `total_usd`, `notas` referenciando la orden.
3. Por cada `items_orden_venta` crea un `items_venta` con `producto_id`, `cantidad`, `precio_usd`, `subtotal_usd`.
4. Actualiza la orden: `estado = FACTURADA`, `venta_id = venta.id`.

La invoice generada se ve como **HTML preview Blu-style** — ver [[invoice-preview]].

## Validación

```php
'cliente_id'           => 'required|exists:clientes,id',
'fecha'                => 'required|date',
'notas'                => 'nullable|string',
'items'                => 'required|array|min:1',
'items.*.producto_id'  => 'required|distinct|exists:productos,id',  // distinct = no repetir SKU
'items.*.deposito_id'  => 'nullable|exists:depositos,id',
'items.*.lista_precio' => 'required|integer|min:1|max:4',
'items.*.cantidad'     => 'required|integer|min:1',
```

El precio NO viene del frontend — el backend lo lee de `producto.precio_lista_{n}` y lo snapshotea.

## Frontend

### Páginas

- `pages/ordenes-venta/index.vue` — listado con DataTable, columna **Invoice** con link clickable que abre la preview en nueva tab
- `pages/ordenes-venta/nueva.vue` — wizard de creación (cabecera + builder de ítems)
- `pages/ordenes-venta/[id].vue` — detalle/edición + acciones: Guardar, Generar invoice, Anular, Eliminar

### Componente clave: `components/OrdenItems.vue`

Builder reusable de ítems. Props:
- `items` — array de ítems del form (v-model)
- `productos` — catálogo precargado (de `/api/productos/seleccionables`)
- `disabled` — read-only mode (cuando la orden no es BORRADOR)

Picker de producto: modal con buscador, cada producto muestra **4 botones (Lista 1–4 con precio)** — clickear uno agrega el ítem con esa lista preseleccionada. La columna **Depósito** del item es un select de pills con stock por depósito (auto-selecciona el primero con stock).

## Nav

`<NavItem to="/ordenes-venta" icon="lucide:file-text" label="Órdenes de Venta" />` en
`layouts/default.vue` bajo "Operaciones".

## Ver también

- [[productos]] — las 4 listas de precio que se eligen acá
- [[invoice-preview]] — qué se ve al "Ver invoice"
- [[arquitectura]] — patrón general de controllers/resources
