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
- 18 Models Eloquent (con \$table explícito en \`Proveedor\` y \`Configuracion\`)
- 18 Controllers resource
- 8 API Resources
- Middleware \`EnsureIsAdmin\`
- Seeders: admin@gigabyte.com, clientes (Elit/New Bytes/Invid/Air), proveedor Blu Studio, configuraciones

**Frontend Nuxt 3 SPA:**
- Composables: \`useApi\`, \`useNotification\`
- Store: \`auth.ts\` (Pinia) con \`isAdmin\`, \`verMontos\`, \`tienePermiso()\`
- Layout sidebar: Dashboard, Clientes, Proveedores, Tareas, Marketing, Mercadería, Calendario, Configuración
- Componentes UI: \`Modal\`, \`FormField\`, \`DataTable\`, \`StatsCard\`, \`StatusBadge\`, \`Toast\`, \`NavItem\`
- 14 páginas implementadas

**Páginas implementadas:**
- \`/login\` — auth con Sanctum Bearer
- \`/\` — Dashboard con 6 KPIs + top clientes
- \`/clientes\` — CRUD + search + paginación
- \`/clientes/[id]\` — detalle + fondo de marketing con año selector
- \`/tareas\` — Kanban 4 columnas click-to-move
- \`/proveedores\` — CRUD completo
- \`/marketing\` — Acciones con filtros cliente/estado
- \`/marketing/[id]\` — detalle + adjuntos + tareas relacionadas
- \`/marketing/campanas\` — CRUD campañas
- \`/mercaderia\` — Listado de ventas
- \`/mercaderia/stock\` — Productos + ajuste de stock por depósito
- \`/mercaderia/depositos\` — Vista card de depósitos
- \`/calendario\` — Eventos + panel "este mes"
- \`/configuracion\` — CRUD etiquetas/tipos/estados (solo admin)

### Troubleshooting resuelto en deploy

- **Puerto 3308/3309 ocupados**: cambiado a 3310
- **PHP 8.3 vs 8.4**: \`composer:2\` requiere PHP 8.4, cambiado runtime a \`php:8.4-cli\`
- **SQLite en HTTP**: \`.env\` de \`create-project\` pisaba las env vars Docker; solución: \`rm -f .env + config:cache\` en entrypoint
- **\`personal_access_tokens\` faltante**: Sanctum no publicó migrations con \`--no-scripts\`; agregado \`vendor:publish\` al entrypoint
- **\`proveedors\` table not found**: pluralizador inglés incorrecto; agregado \`\$table\` a \`Proveedor\` y \`Configuracion\`
- **\`localhost\` en frontend**: URL de API hardcodeada en build; cambiado \`API_BASE_URL=/api\` para funcionar desde cualquier IP de red

## 2026-05-14 — Demo data + Kanban mejorado

### DemoSeeder — datos ficticios para muestra al cliente

Se creó \`database/seeders/DemoSeeder.php\` simulando 3 meses de operación (Feb–May 2026):

- **Usuarios**: 2 operativos nuevos (María Gómez, Lucas Herrera) + admin existente
- **Clientes**: datos completos para los 4 distribuidores (CUIT, contacto, ciudad, \`fondo_marketing_usd\`)
- **Proveedores**: 4 nuevos (Imprenta Gráfica Sur, Logística Rápida SA, Tech Events SRL, Media Digital Pro)
- **Productos**: 12 (Notebooks, Monitores, Componentes, Periféricos, Almacenamiento) con stock en 2 depósitos
- **Asignaciones de fondo**: \$50k/\$40k/\$35k/\$30k por distribuidor en 2026
- **Campañas**: 1 por cliente con fechas Feb–May 2026
- **Acciones de marketing**: 15 en estados mixtos (7 Finalizadas, 4 En curso, 1 Planificada, 1 Pausada, 1 Cancelada)
- **Tareas**: 22 distribuidas en las 4 columnas Kanban (11 LISTO, 5 EN_CURSO, 2 READY_FOR_QA, 4 POR_HACER)
- **Ventas**: 13 (8 PAGADA, 4 PENDIENTE, 1 CANCELADA), todos los distribuidores con al menos 2 operaciones
- **Eventos de calendario**: 12 eventos y fechas comerciales clave
- **Etiquetas**: 8 (Urgente, Bloqueada, Follow-up, Diseño, Revisión, Q2-2026, Gaming, Workstation)

Archivos: \`backend/database/seeders/DemoSeeder.php\`

### Kanban — drag & drop nativo

Reemplazado el sistema click-to-move por drag & drop HTML5 nativo (sin dependencias externas):
- Cursor \`grab\` en cards, \`grabbing\` al arrastrar
- Columna destino se resalta al hover
- Card arrastrando se pone semitransparente
- Al soltar llama a \`PATCH /tareas/{id}/estado\` y actualiza el estado localmente

### Kanban — modal detalle estilo Jira

Al hacer clic en una card (sin arrastrar) se abre modal \`2xl\` con layout 2 columnas:
- **Izquierda**: ID de tarea, título editable inline, descripción textarea, etiquetas con colores
- **Derecha (sidebar)**: Estado, Prioridad, Asignado a, Creado por (read-only), Cliente, Proveedor, Deadline, Fecha de carga, botón Eliminar
- Carga datos frescos del endpoint \`GET /tareas/{id}\`
- \`TareaResource\` actualizado para incluir campo \`creado_por\`

Archivos: \`frontend/pages/tareas/index.vue\`, \`backend/app/Http/Resources/TareaResource.php\`, \`backend/app/Http/Controllers/TareaController.php\`

### Fix: SQLite en producción (config:cache)

**Síntoma**: \`SQLSTATE[HY000]: General error: 1 no such table: usuarios (Connection: sqlite)\`

**Causa**: PHP-FPM no puede leer variables de entorno del container. \`env('DB_CONNECTION')\` devolvía null → fallback a \`sqlite\`.

**Solución**: \`docker exec gigaerp-backend php artisan config:cache\` — cachea la config usando las env vars (accesibles desde artisan CLI), y PHP-FPM lee el cache estático.

**Nota**: el entrypoint ya corre \`config:cache\` al arrancar, pero si el container se reinicia sin reconstruir puede perder el cache. Solución permanente: agregar \`config:cache\` al entrypoint.

### Fix: TypeError filter is not a function (tareas)

**Causa**: \`/tareas\` devuelve \`{ data: [], meta: {} }\` pero el código asignaba el objeto completo a \`tareas.value\`.

**Fix**: \`tareas.value = t.data ?? t\`

## 2026-05-14 — Actualización de memoria y documentación

Se reescribieron los archivos de memoria de Claude y se sincronizó Obsidian para trabajo más preciso y rápido en futuras sesiones.

Sin cambios en código. Solo documentación.

## 2026-05-14 — Debugging acciones de marketing + fixes apiResource

### Bugs encontrados y corregidos

**1. config:cache perdido → Connection: sqlite**

**2. apiResource pluralización española — model binding roto**
- \`Route::apiResource("acciones", ...)\` generaba parámetro \`{accione}\`
- Fix: \`.parameters(["acciones" => "accion"])\` y \`.parameters(["proveedores" => "proveedor"])\`

**3. Frontend no desenvolvía el wrapper Resource**
- Fix: \`accion.value = a?.data ?? a\`

**4. AccionMarketingResource no retornaba tareas**
- Fix: agregado \`"tareas"\` al \`toArray()\`

## 2026-05-14 — Dashboard rediseño + branding + pixel bar chart

- Logo sidebar: \`aorus_logo_black.svg\`, topbar: "Brand ERP"
- Dashboard: 6 KPIs + pixel bar chart SVG 12 meses + resultado del período + ventas por estado
- \`DashboardController\` renovado: \`kpis\`, \`ventas_por_estado\`, \`ultimos_12_meses\`
- Bug corregido: \`->keyBy('estado')\` con enum cast → fix \`->keyBy(fn(\$v) => \$v->estado->value)\`

Archivos: \`backend/app/Http/Controllers/DashboardController.php\`, \`frontend/pages/index.vue\`, \`frontend/layouts/default.vue\`

## 2026-05-20 — Módulo Productos + Existencias + datos reales INVID/New Bytes

### Módulo Productos (\`/productos\`)

Nueva sección de catálogo con vista lista/grid, filtros distribuidor/stock, SKU, foto, precios, badge de stock.

**Concepto clave — dos códigos en productos:**
- \`codigo_distribuidor\`: código interno del distribuidor (ej. \`0416990\` en INVID)
- \`sku\`: modelo oficial del fabricante (ej. \`GP-P550SS\`) — puede estar vacío

**Migraciones agregadas:** 0020–0024 (campos precio/foto/IVA, tipo en clientes, stock/ultimo_ingreso, renombrar sku→codigo_distribuidor, agregar sku real)

### Módulo Existencias (\`/existencias\`)

Tabla cruzada SKU × distribuidor. Todos los distribuidores aparecen como columnas aunque no tengan productos.

### Datos cargados

- **INVID**: 41 productos Gigabyte con SKUs buscados en gigabyte.com
- **New Bytes**: 206 productos Gigabyte (SKU = código distribuidor)

Archivos: \`backend/app/Http/Controllers/{Producto,Existencia}Controller.php\`, \`backend/database/migrations/0020-0024\`, \`backend/database/seeders/{ProductoInvid,ProductoNewBytes,Database}Seeder.php\`, \`frontend/pages/{productos,existencias}/index.vue\`

## 2026-05-21 — Módulo Órdenes de Venta + Stock dinámico por depósito

### Módulo Órdenes de Venta (\`/ordenes-venta\`)

Nuevo módulo integrado desde \`main\` (commit b1209de):

- **Enum**: \`EstadoOrdenVenta\`
- **Modelos**: \`OrdenVenta\` (cabecera) + \`ItemOrdenVenta\` (líneas, 1:N)
- **Controller**: \`OrdenVentaController\` — index, store, show, update, destroy
- **Resource**: \`OrdenVentaResource\` con items embebidos
- **Migraciones**: \`0027_create_ordenes_venta_tables\`
- **Frontend**: listado (\`/ordenes-venta\`), nueva orden (\`/ordenes-venta/nueva\`), detalle (\`/ordenes-venta/[id]\`)
- **Componente**: \`OrdenItems.vue\` para gestión de líneas dinámicas
- **StatusBadge**: nuevos estados de orden agregados

### Migraciones de soporte para Productos

- \`0025\` — SKU único por distribuidor (constraint \`unique(sku, distribuidor_id)\`)
- \`0026\` — Listas de precio 1–4 (\`precio_lista_1\` … \`precio_lista_4\`) a la tabla productos

### Stock — columnas dinámicas por depósito (\`/mercaderia/stock\`)

Antes: columna estática "Stock total". Ahora: una columna por depósito activo.

- \`ProductoController::index\` eager-load \`stocks.deposito\`
- \`ProductoResource\` nuevo campo \`stocks_deposito: { deposito_id: cantidad }\` (via \`whenLoaded\`)
- \`ProductoResource\` nuevo campo \`stock_total\` como suma de la relación
- Frontend: \`columnas\` pasa a \`computed()\` con \`depositos.value.map(...)\` intercalado
- Celdas: verde con cantidad · rojo con 0 · \`—\` si no hay entrada para ese depósito

### Deploy de sesión

- \`optimize:clear\` sin \`config:cache\` posterior → caída a SQLite (patrón recurrente)
- Siempre: \`optimize:clear\` + \`config:cache\` en mismo comando

Archivos: \`backend/app/Enums/EstadoOrdenVenta.php\`, \`backend/app/Http/Controllers/OrdenVentaController.php\`, \`backend/app/Http/Resources/OrdenVentaResource.php\`, \`backend/app/Models/{OrdenVenta,ItemOrdenVenta}.php\`, \`backend/database/migrations/0025–0027\`, \`backend/app/Http/Controllers/ProductoController.php\`, \`backend/app/Http/Resources/ProductoResource.php\`, \`frontend/pages/ordenes-venta/\`, \`frontend/components/OrdenItems.vue\`, \`frontend/pages/mercaderia/stock/index.vue\`