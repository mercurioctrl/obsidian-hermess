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
- 18 Models Eloquent (con $table explícito en `Proveedor` y `Configuracion`)
- 18 Controllers resource
- 8 API Resources
- Middleware `EnsureIsAdmin`
- Seeders: admin@gigabyte.com, clientes (Elit/New Bytes/Invid/Air), proveedor Blu Studio, configuraciones

**Frontend Nuxt 3 SPA:**
- Composables: `useApi`, `useNotification`
- Store: `auth.ts` (Pinia) con `isAdmin`, `verMontos`, `tienePermiso()`
- Layout sidebar: Dashboard, Clientes, Proveedores, Tareas, Marketing, Mercadería, Calendario, Configuración
- Componentes UI: `Modal`, `FormField`, `DataTable`, `StatsCard`, `StatusBadge`, `Toast`, `NavItem`
- 14 páginas implementadas

**Páginas implementadas:**
- `/login` — auth con Sanctum Bearer
- `/` — Dashboard con 6 KPIs + top clientes
- `/clientes` — CRUD + search + paginación
- `/clientes/[id]` — detalle + fondo de marketing con año selector
- `/tareas` — Kanban 4 columnas click-to-move
- `/proveedores` — CRUD completo
- `/marketing` — Acciones con filtros cliente/estado
- `/marketing/[id]` — detalle + adjuntos + tareas relacionadas
- `/marketing/campanas` — CRUD campañas
- `/mercaderia` — Listado de ventas
- `/mercaderia/stock` — Productos + ajuste de stock por depósito
- `/mercaderia/depositos` — Vista card de depósitos
- `/calendario` — Eventos + panel "este mes"
- `/configuracion` — CRUD etiquetas/tipos/estados (solo admin)

### Troubleshooting resuelto en deploy

- **Puerto 3308/3309 ocupados**: cambiado a 3310
- **PHP 8.3 vs 8.4**: `composer:2` requiere PHP 8.4, cambiado runtime a `php:8.4-cli`
- **SQLite en HTTP**: `.env` de `create-project` pisaba las env vars Docker; solución: `rm -f .env + config:cache` en entrypoint
- **`personal_access_tokens` faltante**: Sanctum no publicó migrations con `--no-scripts`; agregado `vendor:publish` al entrypoint
- **`proveedors` table not found**: pluralizador inglés incorrecto; agregado `$table` a `Proveedor` y `Configuracion`
- **`localhost` en frontend**: URL de API hardcodeada en build; cambiado `API_BASE_URL=/api` para funcionar desde cualquier IP de red

## 2026-05-14 — Demo data + Kanban mejorado

### DemoSeeder — datos ficticios para muestra al cliente

Se creó `database/seeders/DemoSeeder.php` simulando 3 meses de operación (Feb–May 2026):

- **Usuarios**: 2 operativos nuevos (María Gómez, Lucas Herrera) + admin existente
- **Clientes**: datos completos para los 4 distribuidores (CUIT, contacto, ciudad, `fondo_marketing_usd`)
- **Proveedores**: 4 nuevos (Imprenta Gráfica Sur, Logística Rápida SA, Tech Events SRL, Media Digital Pro)
- **Productos**: 12 (Notebooks, Monitores, Componentes, Periféricos, Almacenamiento) con stock en 2 depósitos
- **Asignaciones de fondo**: $50k/$40k/$35k/$30k por distribuidor en 2026
- **Campañas**: 1 por cliente con fechas Feb–May 2026
- **Acciones de marketing**: 15 en estados mixtos (7 Finalizadas, 4 En curso, 1 Planificada, 1 Pausada, 1 Cancelada)
- **Tareas**: 22 distribuidas en las 4 columnas Kanban (11 LISTO, 5 EN_CURSO, 2 READY_FOR_QA, 4 POR_HACER)
- **Ventas**: 13 (8 PAGADA, 4 PENDIENTE, 1 CANCELADA), todos los distribuidores con al menos 2 operaciones
- **Eventos de calendario**: 12 eventos y fechas comerciales clave
- **Etiquetas**: 8 (Urgente, Bloqueada, Follow-up, Diseño, Revisión, Q2-2026, Gaming, Workstation)

Archivos: `backend/database/seeders/DemoSeeder.php`

### Kanban — drag & drop nativo

Reemplazado el sistema click-to-move por drag & drop HTML5 nativo (sin dependencias externas):
- Cursor `grab` en cards, `grabbing` al arrastrar
- Columna destino se resalta al hover
- Card arrastrando se pone semitransparente
- Al soltar llama a `PATCH /tareas/{id}/estado` y actualiza el estado localmente

### Kanban — modal detalle estilo Jira

Al hacer clic en una card (sin arrastrar) se abre modal `2xl` con layout 2 columnas:
- **Izquierda**: ID de tarea, título editable inline, descripción textarea, etiquetas con colores
- **Derecha (sidebar)**: Estado, Prioridad, Asignado a, Creado por (read-only), Cliente, Proveedor, Deadline, Fecha de carga, botón Eliminar
- Carga datos frescos del endpoint `GET /tareas/{id}`
- `TareaResource` actualizado para incluir campo `creado_por`

Archivos: `frontend/pages/tareas/index.vue`, `backend/app/Http/Resources/TareaResource.php`, `backend/app/Http/Controllers/TareaController.php`

### Fix: SQLite en producción (config:cache)

**Síntoma**: `SQLSTATE[HY000]: General error: 1 no such table: usuarios (Connection: sqlite)`

**Causa**: PHP-FPM no puede leer variables de entorno del container. `env('DB_CONNECTION')` devolvía null → fallback a `sqlite`.

**Solución**: `docker exec gigaerp-backend php artisan config:cache` — cachea la config usando las env vars (accesibles desde artisan CLI), y PHP-FPM lee el cache estático.

**Nota**: el entrypoint ya corre `config:cache` al arrancar, pero si el container se reinicia sin reconstruir puede perder el cache. Solución permanente: agregar `config:cache` al entrypoint.

### Fix: TypeError filter is not a function (tareas)

**Causa**: `/tareas` devuelve `{ data: [], meta: {} }` pero el código asignaba el objeto completo a `tareas.value`.

**Fix**: `tareas.value = t.data ?? t`

## 2026-05-14 — Actualización de memoria y documentación

Se reescribieron los archivos de memoria de Claude y se sincronizó Obsidian para trabajo más preciso y rápido en futuras sesiones:

- **architecture_decisions.md**: tablas de reglas frontend/backend, tabla de paginación vs `get()` por módulo, tabla de relaciones TareaResource por endpoint, tabla de modal sizes, patrón Kanban drag+click con detalle del anti-conflicto
- **deploy_quirks.md**: reorganizado como checklist operativo; síntoma+causa+fix de una línea para el error SQLite; comandos de actualización sin rebuild por caso (backend / frontend)
- **project_context.md**: ficha completa con tablas de usuarios, distribuidores con ciudad y fondo, tabla de módulos/rutas, resumen numérico del DemoSeeder

Sin cambios en código. Solo documentación.
## 2026-05-14 — Debugging acciones de marketing + fixes apiResource

### Bugs encontrados y corregidos

**1. config:cache perdido → Connection: sqlite**
- Síntoma: `SQLSTATE[HY000]: no such table: usuarios (Connection: sqlite)` en todos los endpoints
- Causa: `optimize:clear` manual sin volver a cachear; el `docker-entrypoint.sh` ya tiene `config:cache` pero no alcanza si el cache se limpia en operación
- Fix permanente confirmado: `config:cache` ya estaba en el entrypoint. Fix operativo: `docker exec gigaerp-backend php artisan config:cache`

**2. apiResource pluralización española — model binding roto**
- `Route::apiResource("acciones", ...)` generaba parámetro `{accione}` (no `{accion}`)
- `Route::apiResource("proveedores", ...)` generaba `{proveedore}` (no `{proveedor}`)
- Síntoma: Resource devolvía todos los campos en `null` (modelo vacío, sin 404 ni 500)
- Diagnóstico: `php artisan route:list --path=api/X` + curl con token para ver la respuesta real
- Fix: `.parameters(["acciones" => "accion"])` y `.parameters(["proveedores" => "proveedor"])`
- Verificado: `tipos-accion/{tipos_accion}` y `estados-accion/{estados_accion}` OK (Laravel convierte snake→camel)

**3. Frontend no desenvolvía el wrapper Resource**
- `pages/marketing/[id].vue` asignaba `accion.value = a` en vez de `a?.data ?? a`
- Resultado: todos los campos del modelo eran `undefined` en la vista
- Fix: `accion.value = a?.data ?? a` + `const d = accion.value` para el `Object.assign(form, ...)`

**4. AccionMarketingResource no retornaba tareas**
- El controller cargaba `tareas` en `show()` pero el Resource no las incluía en `toArray()`
- Fix: agregado `"tareas" => $this->whenLoaded("tareas", fn() => $this->tareas->map(...))`

### Puerto confirmado
- gigaErp corre en **8824** (no 8823 — ese puerto lo ocupa minisaas)
- minisaas: 8823 | gigaErp: 8824 | bluMiniErp: 8088

Archivos modificados: `backend/routes/api.php`, `backend/app/Http/Resources/AccionMarketingResource.php`, `frontend/pages/marketing/[id].vue`
## 2026-05-14 — Dashboard rediseño + branding + pixel bar chart

### Branding

- **Logo sidebar**: reemplazado texto "gigaErp / Gigabyte" por imagen SVG `aorus_logo_black.svg` (`h-8`, 2rem)
- **Topbar**: texto "gigaErp" → "Brand ERP"
- Logos disponibles en `frontend/public/logos/`: `aorus_logo_black.svg`, `gigabyte_logo_clean.svg`

### Dashboard — rediseño completo (pages/index.vue + DashboardController.php)

**Antes**: 6 KPIs simples + tabla top clientes.  
**Ahora**: layout de 4 bloques completos:

1. **6 KPI cards** (2 filas × 3):
   - Clientes activos (+ nuevos este mes)
   - Ingresos del período (ventas PAGADAS del mes)
   - Gastos del período (AccionMarketing.monto_usd del mes)
   - Resultado del período (ingresos − gastos + % margen)
   - Cobrado en el período
   - Deuda de clientes (ventas PENDIENTES total)

2. **Pixel bar chart SVG** — Ingresos vs Gastos, últimos 12 meses:
   - Barras hechas de cuadraditos 5×5px con gap 2px (~20 filas)
   - Ingresos negro `#1A1A1A` / Gastos rojo `#C0392B`
   - Fondos casi invisibles: `#EBEBEB` / `#F5E8E8`
   - Regla crítica: `barW = PX_SIZE` para que sean cuadrados (no rectangulares)

3. **Resultado del período** (col izq): tabla ingresos/gastos/resultado del mes + margen con barra progress + acumulado anual + ticket promedio

4. **Ventas por estado** (col der): barras de distribución PAGADA/PENDIENTE/CANCELADA + top 5 clientes

### DashboardController — datos nuevos en GET /api/dashboard

Nuevos campos en `kpis`: `clientes_activos`, `clientes_nuevos_mes`, `ingresos_mes`, `ingresos_anio`, `cobrado_mes`, `pendiente_cobro`, `gastos_mes`, `gastos_anio`, `resultado_mes`, `resultado_anio`, `margen_pct`, `ticket_promedio`.

Nuevo campo `ventas_por_estado`: `{ PAGADA: {cantidad, total}, PENDIENTE: {...}, CANCELADA: {...}, total: N }`.

Nuevo campo `ultimos_12_meses`: array de 12 objetos `{ label, mes, anio, ingresos, gastos }`.

### Bug corregido — enum keyBy

`->get()->keyBy("estado")` fallaba con `"could not be converted to string"` cuando el campo tiene cast a enum.  
**Fix**: `->keyBy(fn($v) => $v->estado->value)`

### Bug corregido — SQLite (config:cache)

Después de hacer `optimize:clear` manual, el sistema caía a SQLite.  
**Fix**: `docker exec gigaerp-backend php artisan config:cache`

Archivos modificados: `backend/app/Http/Controllers/DashboardController.php`, `frontend/pages/index.vue`, `frontend/layouts/default.vue`

