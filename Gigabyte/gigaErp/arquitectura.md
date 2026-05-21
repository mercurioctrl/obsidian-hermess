
# Arquitectura — gigaErp

## Estructura de directorios

```
gigaErp/
├── backend/          ← Laravel 11 (PHP 8.4)
│   ├── app/
│   │   ├── Enums/            ← RolUsuario, EstadoTarea, PrioridadTarea, EstadoVenta
│   │   ├── Http/Controllers/ ← 20 resource controllers
│   │   ├── Http/Resources/   ← 8 API resources
│   │   ├── Models/           ← 18 Eloquent models
│   │   └── Services/
│   ├── database/
│   │   ├── migrations/       ← 0001–0024
│   │   └── seeders/          ← DatabaseSeeder + DemoSeeder + ProductoInvidSeeder + ProductoNewBytesSeeder
│   └── routes/api.php        ← todo dentro de auth:sanctum
├── frontend/         ← Nuxt 3 SPA (ssr: false)
│   ├── components/ui/        ← Modal, FormField, DataTable, StatsCard, StatusBadge, Toast
│   ├── composables/          ← useApi, useNotification
│   ├── layouts/              ← default (sidebar+topbar), auth
│   ├── middleware/           ← auth.global.ts (global, no usar definePageMeta)
│   ├── pages/                ← routing por archivos
│   │   ├── productos/index.vue   ← catálogo con grid/lista/filtros/stock
│   │   └── existencias/index.vue ← tabla cruzada SKU × distribuidor
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
Eager loads: distribuidor
```

Campos por producto: `id, nombre, codigo_distribuidor, sku, marca, precio, precio_oferta, iva, precio_final, foto_principal, distribuidor_id, distribuidor{id,nombre}, activo, stock, ultimo_ingreso`

### Dos códigos en Producto

| Campo | Descripción | Lookup key en seeder |
|-------|-------------|---------------------|
| `codigo_distribuidor` | Código interno del distribuidor | ✅ (updateOrCreate) |
| `sku` | SKU real del fabricante (Gigabyte) | solo almacenado, no es PK |

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

## Paginación vs colección por módulo

| Módulo | Backend | Frontend — leer con |
|--------|---------|---------------------|
| Clientes, Ventas, Acciones, Productos | `paginate(20/50)` | `res.data` + `res.meta` |
| Tareas, Etiquetas, Tipos, Estados | `get()` | `res.data ?? res` |
| Existencias | `get()` agrupado | `res.distribuidores` + `res.items` (sin wrapper data) |

## API Resources — relaciones cargadas

### ProductoResource
| Endpoint | Relaciones cargadas |
|----------|-------------------|
| `index()` | `distribuidor` |
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

### Distribuidores = Clientes con `tipo='distribuidor'`
No hay tabla separada para distribuidores. Campo `tipo` en `clientes`.
Productos se vinculan con `distribuidor_id` (FK → `clientes.id`).

### stock en tabla productos (no en stock_deposito)
El módulo Productos usa campo `stock` directo. El módulo Mercadería legacy usa `stock_deposito`.
Ambos coexisten — el campo `stock` en Producto es independiente del stock por depósito.

### Migración de datos en seeders, no en migraciones
La migración 0022 solo agrega la columna `stock`. El llenado inicial va en los seeders
(los productos no existen cuando corre la migración en fresh install).

## Modelos y relaciones principales

```
Usuario ─────── tareas (asignado_usuario_id / creado_por_id)
Cliente ─┬────── tareas · acciones_marketing · campanas
(=Dist.) ├────── asignaciones_fondo · eventos_calendario
         ├────── ventas
         └────── productos (via distribuidor_id)
Proveedor ────── tareas (proveedor_id / asignado_proveedor_id)
AccionMarketing ─┬─── tareas · accion_adjuntos
Campana ──────── acciones_marketing
Producto ─┬───── stock_deposito · items_venta
Deposito ──────── stock_deposito
Venta ─────────── items_venta
```

## Permisos

- `ADMIN`: acceso total
- `OPERATIVO`: array JSON `permisos` en el modelo (`VER_MONTOS`, `VER_SECCION_CLIENTES`, etc.)

## Ver también

- [[gigaErp]] · [[stack]] · [[changelog]] · [[contexto]] · [[memoria]]
