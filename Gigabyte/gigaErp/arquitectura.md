# Arquitectura — gigaErp

## Estructura de directorios

```
gigaErp/
├── backend/          ← Laravel 11 (PHP 8.4)
│   ├── app/
│   │   ├── Enums/            ← RolUsuario, EstadoTarea, PrioridadTarea, EstadoVenta
│   │   ├── Http/Controllers/ ← 18 resource controllers
│   │   ├── Http/Resources/   ← 8 API resources
│   │   ├── Models/           ← 18 Eloquent models
│   │   └── Services/
│   ├── database/
│   │   ├── migrations/       ← 0001–0019
│   │   └── seeders/          ← DatabaseSeeder + DemoSeeder (demo 3 meses)
│   └── routes/api.php        ← todo dentro de auth:sanctum
├── frontend/         ← Nuxt 3 SPA (ssr: false)
│   ├── components/ui/        ← Modal, FormField, DataTable, StatsCard, StatusBadge, Toast
│   ├── composables/          ← useApi, useNotification
│   ├── layouts/              ← default (sidebar+topbar), auth
│   ├── middleware/           ← auth.global.ts (global, no usar definePageMeta)
│   ├── pages/                ← routing por archivos
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

## Paginación vs colección por módulo

| Módulo | Backend | Frontend — leer con |
|--------|---------|---------------------|
| Clientes, Ventas, Acciones, Productos | `paginate(20)` | `res.data` + `res.meta` |
| Tareas, Etiquetas, Tipos, Estados | `get()` | `res.data ?? res` |

## API Resources — relaciones cargadas

### AccionMarketingResource
| Endpoint | Relaciones cargadas | Campos retornados |
|----------|--------------------|--------------------|
| `index()` | `cliente`, `tipo`, `estado`, `campana`, `creadoPor` | id, titulo, monto_usd, fecha_inicio/fin, cliente, tipo, estado, campana, created_at |
| `show()` | todo lo anterior + `adjuntos`, `tareas` | todo lo anterior + adjuntos[], tareas[] |

### TareaResource
| Endpoint | Relaciones |
|----------|-----------|
| `index()` | `cliente`, `proveedor`, `asignadoUsuario`, `etiquetas` — sin `creadoPor` |
| `show()` | todo lo anterior + `asignadoProveedor`, `accion`, `creadoPor` |

> `creado_por` solo disponible al abrir el modal de detalle, no en el Kanban.

## apiResource — pluralización española (BUG CONOCIDO)

Laravel singulariza en inglés. Con nombres en español puede generar parámetros incorrectos:

| apiResource | Parámetro generado | Parámetro correcto | Estado |
|------------|-------------------|-------------------|--------|
| `acciones` | `{accione}` ❌ | `{accion}` | ✅ Corregido con `.parameters()` |
| `proveedores` | `{proveedore}` ❌ | `{proveedor}` | ✅ Corregido con `.parameters()` |
| `tipos-accion` | `{tipos_accion}` → camelCase `$tiposAccion` | ✓ coincide | OK |
| `estados-accion` | `{estados_accion}` → camelCase `$estadosAccion` | ✓ coincide | OK |

**Síntoma**: Resource devuelve todos los campos en `null` (no hay 404 ni 500).
**Diagnóstico**: `php artisan route:list --path=api/X` + curl autenticado al endpoint.
**Fix**: `Route::apiResource('X', XController::class)->parameters(['X' => 'param']);`
**Regla**: al crear cualquier `apiResource` en español, verificar inmediatamente el parámetro con `route:list`.

## Enum en colecciones — bug keyBy

Cuando un modelo tiene `$casts = ['estado' => MiEnum::class]` y se hace `->get()->keyBy('estado')`, Laravel castea el campo a enum y el keyBy falla con *"could not be converted to string"*.

**Fix**: `->keyBy(fn($v) => $v->estado->value)`

## Dashboard — estructura GET /api/dashboard

```json
{
  "kpis": {
    "clientes_activos", "clientes_nuevos_mes",
    "ingresos_mes", "ingresos_anio",
    "cobrado_mes", "pendiente_cobro",
    "gastos_mes", "gastos_anio",
    "resultado_mes", "resultado_anio",
    "margen_pct", "ticket_promedio",
    "acciones_activas", "tareas_pendientes", "tareas_en_curso"
  },
  "ventas_por_estado": {
    "PAGADA":    { "cantidad": N, "total": N },
    "PENDIENTE": { "cantidad": N, "total": N },
    "CANCELADA": { "cantidad": N, "total": N },
    "total": N
  },
  "top_clientes": [{ "id", "nombre", "total_ventas" }],
  "ultimos_12_meses": [{ "label": "MAY", "mes": 5, "anio": 2026, "ingresos": N, "gastos": N }]
}
```

- `ingresos` = ventas con `estado = PAGADA`
- `gastos` = `AccionMarketing.monto_usd`
- `top_clientes` filtra solo ventas PAGADAS del año

## Pixel Bar Chart SVG — implementación (pages/index.vue)

```ts
const PX_SIZE = 5   // CRÍTICO: barW debe igualar PX_SIZE para cuadrados (no rectángulos)
const PX_GAP  = 2
const PX_STEP = 7
const CHART_H = 140
const MAX_PX  = 20  // filas de cuadraditos
```

Colores: ingresos `#1A1A1A` / `#EBEBEB` vacío · gastos `#C0392B` / `#F5E8E8` vacío.
SVG font-size: `6` unidades SVG (escala con viewBox — a pantallas más anchas, se ve más grande).
Layout: viewBox `0 0 770 {CHART_H+26}`, slot 60px/mes, bar1 at `i*60+23`, bar2 at `i*60+31`.

## Decisiones de diseño

### `config:cache` obligatorio (PHP-FPM)
`env()` devuelve null en PHP-FPM sin cache. El `docker-entrypoint.sh` corre `config:cache` al arrancar.
Si el cache se pierde (por `optimize:clear` manual): `docker exec gigaerp-backend php artisan config:cache`.

### `$table` explícito en modelos españoles
`Proveedor` → `protected $table = 'proveedores'`
`Configuracion` → `protected $table = 'configuraciones'`

### PHP 8.4 en runtime
`composer:2` usa PHP 8.4 al resolver dependencias. Runtime: `php:8.4-cli`.

### Kanban — drag & drop + modal Jira
- HTML5 DnD nativo sin dependencias
- Click → `GET /tareas/{id}` → modal `2xl`
- Anti-conflicto: `draggingId` con `setTimeout 50ms` en `onDragEnd`

### Branding
- Sidebar logo: `frontend/public/logos/aorus_logo_black.svg` → `class="h-8 w-auto"` (2rem)
- Topbar: `<span class="text-sm text-[#9B9B93]">Brand ERP</span>`

## Modelos y relaciones principales

```
Usuario ─────── tareas (asignado_usuario_id / creado_por_id)
Cliente ─┬────── tareas · acciones_marketing · campanas
         ├────── asignaciones_fondo · eventos_calendario
         └────── ventas
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
