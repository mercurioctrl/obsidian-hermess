# Arquitectura — gigaErp

## Estructura de directorios

\`\`\`
gigaErp/
├── backend/          ← Laravel 11 (PHP 8.4)
│   ├── app/
│   │   ├── Enums/            ← RolUsuario, EstadoTarea, PrioridadTarea, EstadoVenta, EstadoOrdenVenta
│   │   ├── Http/Controllers/ ← 21 resource controllers
│   │   ├── Http/Resources/   ← 9 API resources
│   │   ├── Models/           ← 20 Eloquent models
│   │   └── Services/
│   ├── database/
│   │   ├── migrations/       ← 0001–0027
│   │   └── seeders/          ← DatabaseSeeder + DemoSeeder + ProductoInvidSeeder + ProductoNewBytesSeeder
│   └── routes/api.php        ← todo dentro de auth:sanctum
├── frontend/         ← Nuxt 3 SPA (ssr: false)
│   ├── components/
│   │   ├── ui/               ← Modal, FormField, DataTable, StatsCard, StatusBadge, Toast
│   │   └── OrdenItems.vue    ← gestión de líneas en órdenes de venta
│   ├── composables/          ← useApi, useNotification
│   ├── layouts/              ← default (sidebar+topbar), auth
│   ├── middleware/           ← auth.global.ts (global, no usar definePageMeta)
│   ├── pages/
│   │   ├── productos/index.vue         ← catálogo con grid/lista/filtros/stock
│   │   ├── existencias/index.vue       ← tabla cruzada SKU × distribuidor
│   │   ├── ordenes-venta/index.vue     ← listado de órdenes
│   │   ├── ordenes-venta/nueva.vue     ← crear orden con líneas dinámicas
│   │   └── ordenes-venta/[id].vue      ← detalle y edición
│   ├── public/logos/         ← aorus_logo_black.svg, gigabyte_logo_clean.svg
│   └── stores/               ← auth.ts (Pinia)
├── nginx/default.conf        ← /api/* y /storage/* → backend:9000, /* → frontend:3000
└── docker-compose.yml        ← 6 servicios: db, redis, backend, scheduler, frontend, nginx
\`\`\`

## Patrones de backend

- Resource controllers: \`index / store / show / update / destroy\`
- Respuestas con Resource: wrap \`{ data: {} }\` automático
- Colecciones paginadas: \`{ data: [], meta: { total, per_page, current_page, last_page } }\`
- Colecciones sin paginar (\`get()\`): \`{ data: [] }\` sin \`meta\`
- Rutas estáticas **siempre antes** del \`apiResource\`

## Módulo Productos — \`GET /api/productos\`

\`\`\`
Filtros: ?search=X &distribuidor_id=N &stock=con_stock|sin_stock &activo=1
Pagina: 50 por página
Eager loads: distribuidor, stocks.deposito
\`\`\`

Campos por producto: \`id, nombre, codigo_distribuidor, sku, marca, precio, precio_oferta, iva, precio_final, precio_lista_1..4, foto_principal, distribuidor_id, distribuidor{id,nombre}, activo, stock, stocks_deposito{deposito_id:cantidad}, stock_total, ultimo_ingreso\`

### Dos códigos en Producto

| Campo | Descripción | Lookup key en seeder |
|-------|-------------|---------------------|
| \`codigo_distribuidor\` | Código interno del distribuidor | ✅ (updateOrCreate) |
| \`sku\` | SKU real del fabricante (Gigabyte) | solo almacenado, no es PK |

### stocks_deposito en ProductoResource

\`\`\`php
// Solo presente cuando se carga la relación stocks.deposito
'stocks_deposito' => $this->whenLoaded('stocks', fn() =>
    $this->stocks->mapWithKeys(fn($s) => [$s->deposito_id => (int) $s->cantidad])->toArray()
),
'stock_total' => $this->whenLoaded('stocks', fn() => (int) $this->stocks->sum('cantidad'), (int) $this->stock),
\`\`\`

## Módulo Existencias — \`GET /api/existencias\`

Endpoint no-resource (solo \`index\`). Agrupa todos los productos con SKU no-null por SKU.

\`\`\`json
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
\`\`\`

- \`stock[dist_id] = N\` → tiene el producto, N unidades
- \`stock[dist_id] = 0\` → tiene el producto, sin unidades
- \`stock[dist_id] = null\` → no vende ese producto
- **Todos** los distribuidores (tipo=distribuidor) aparecen como columnas, aunque no tengan productos

## Módulo Órdenes de Venta — \`GET /api/ordenes-venta\`

\`\`\`
Pagina: estándar
Modelos: OrdenVenta (cabecera) → ItemOrdenVenta (líneas, FK: orden_venta_id)
Enum: EstadoOrdenVenta
Resource: OrdenVentaResource (incluye items embebidos)
\`\`\`

Las órdenes usan las listas de precio 1–4 del modelo Producto (migración 0026).

## Vista Stock por depósito — \`/mercaderia/stock\`

La tabla genera columnas dinámicas según los depósitos activos en \`GET /api/depositos\`:

\`\`\`ts
const columnas = computed(() => [
  { key: 'sku', label: 'SKU' },
  { key: 'nombre', label: 'Nombre' },
  ...depositos.value.map((d) => ({ key: \`dep_\${d.id}\`, label: d.nombre })),
  { key: 'total', label: 'Total' },
  { key: 'unidad', label: 'Unidad' },
  { key: 'acciones', label: '' },
])
\`\`\`

Cada celda de depósito lee \`row.stocks_deposito?.[d.id]\`.

## Paginación vs colección por módulo

| Módulo | Backend | Frontend — leer con |
|--------|---------|---------------------|
| Clientes, Ventas, Acciones, Productos, Órdenes de Venta | \`paginate(20/50)\` | \`res.data\` + \`res.meta\` |
| Tareas, Etiquetas, Tipos, Estados | \`get()\` | \`res.data ?? res\` |
| Existencias | \`get()\` agrupado | \`res.distribuidores\` + \`res.items\` (sin wrapper data) |

## API Resources — relaciones cargadas

### ProductoResource
| Endpoint | Relaciones cargadas |
|----------|-------------------|
| \`index()\` | \`distribuidor\`, \`stocks.deposito\` |
| \`show()\` | \`stocks.deposito\` |

### AccionMarketingResource
| Endpoint | Relaciones cargadas |
|----------|-------------------|
| \`index()\` | \`cliente\`, \`tipo\`, \`estado\`, \`campana\`, \`creadoPor\` |
| \`show()\` | todo lo anterior + \`adjuntos\`, \`tareas\` |

### TareaResource
| Endpoint | Relaciones |
|----------|-----------|
| \`index()\` | \`cliente\`, \`proveedor\`, \`asignadoUsuario\`, \`etiquetas\` |
| \`show()\` | todo lo anterior + \`asignadoProveedor\`, \`accion\`, \`creadoPor\` |

## apiResource — pluralización española (BUG CONOCIDO)

| apiResource | Parámetro generado | Fix aplicado |
|------------|-------------------|-------------|
| \`acciones\` | \`{accione}\` ❌ | \`.parameters(['acciones' => 'accion'])\` |
| \`proveedores\` | \`{proveedore}\` ❌ | \`.parameters(['proveedores' => 'proveedor'])\` |
| \`productos\` | \`{producto}\` ✅ | OK sin fix |
| \`ordenes-venta\` | verificar con route:list | aplicar fix si es necesario |

**Síntoma**: Resource devuelve campos en \`null\` sin 404 ni 500.
**Diagnóstico**: \`php artisan route:list --path=api/X\`.

## Enum en colecciones — bug keyBy

\`->get()->keyBy('estado')\` falla con enum cast. **Fix**: \`->keyBy(fn(\$v) => \$v->estado->value)\`

## Dashboard — estructura GET /api/dashboard

\`\`\`json
{
  "kpis": { "clientes_activos", "ingresos_mes", "gastos_mes", "resultado_mes", "cobrado_mes", "pendiente_cobro" ... },
  "ventas_por_estado": { "PAGADA": { "cantidad": N, "total": N }, ... },
  "top_clientes": [{ "id", "nombre", "total_ventas" }],
  "ultimos_12_meses": [{ "label": "MAY", "mes": 5, "anio": 2026, "ingresos": N, "gastos": N }]
}
\`\`\`

## Pixel Bar Chart SVG (pages/index.vue)

\`\`\`ts
const PX_SIZE = 5   // barW = PX_SIZE para cuadrados perfectos
const PX_GAP  = 2
const CHART_H = 140
const MAX_PX  = 20  // filas de cuadraditos por barra
\`\`\`

## Decisiones de diseño

### \`config:cache\` obligatorio (PHP-FPM)
\`env()\` devuelve null en PHP-FPM. Fix: \`docker exec gigaerp-backend php artisan config:cache\`
**Patrón**: después de cada \`optimize:clear\`, siempre ejecutar \`config:cache\`.

### Distribuidores = Clientes con \`tipo='distribuidor'\`
No hay tabla separada para distribuidores. Campo \`tipo\` en \`clientes\`.
Productos se vinculan con \`distribuidor_id\` (FK → \`clientes.id\`).

### Dos tablas de stock coexisten
- \`stock\` directo en tabla \`productos\`: usado por módulos Productos y Existencias
- \`stock_deposito\` (via \`StockDeposito\` model): usado por \`/mercaderia/stock\`
- Son independientes — no se sincronizan automáticamente

### Migración de datos en seeders, no en migraciones
La migración solo agrega columnas. El llenado inicial va en los seeders.

## Modelos y relaciones principales

\`\`\`
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
Deposito ──────── stock_deposito
Venta ─────────── (sin items por ahora)
OrdenVenta ────── items_orden_venta
\`\`\`

## Permisos

- \`ADMIN\`: acceso total
- \`OPERATIVO\`: array JSON \`permisos\` en el modelo (\`VER_MONTOS\`, \`VER_SECCION_CLIENTES\`, etc.)

## Ver también

- [[gigaErp]] · [[stack]] · [[changelog]] · [[contexto]] · [[memoria]]