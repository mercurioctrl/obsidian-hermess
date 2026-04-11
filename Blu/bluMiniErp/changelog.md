# Changelog

Registro de lo trabajado en el proyecto, agrupado por fecha.

---

## 2026-04-08

- feat: Filtros de mes, año y cliente en listados de presupuestos, proyectos y activaciones. Default al mes/año actual con opción "Todos" para deshabilitar cada filtro. Ver [[memoria#Listados - filtros de fecha y cliente]] y [[Backend - API#Presupuestos]]
- refactor: Listado de proyectos migrado de filtrado client-side a fetch server-side con query params (consistente con presupuestos y activaciones)
- convención: Param wire usa `anio` (ASCII) en lugar de `año` para evitar fragilidad de encoding URL/PHP. State frontend mantiene nombres en español. Ver [[memoria#Query params sin caracteres no-ASCII]]

Campos de fecha por listado:
- Presupuestos → `presupuestos.fecha`
- Proyectos → `proyectos.fecha_inicio`
- Activaciones → `pruebas_ejecucion.periodo_desde`

Archivos: `PresupuestoController.php`, `ProyectoController.php`, `PruebaEjecucionController.php`, `presupuestos/index.vue`, `proyectos/index.vue`, `evidencias/index.vue`

## 2026-03-30

- feat: Descripcion IA de activaciones escalada segun cantidad de hitos. ≤5 hitos -> 2-3 oraciones (`max_tokens: 300`), 6-15 hitos -> 3-5 oraciones (`max_tokens: 500`), +15 hitos -> 5-7 oraciones (`max_tokens: 700`). Prompt dice "cubriendo todas las actividades listadas" (no "breve") para evitar omisiones del modelo. Ver [[Reglas de Negocio]] y [[Backend - API#DeepSeek]]
- fix: Actualizar dominio `blu.inc` -> `blustudioinc.com` en invoice (PDF de presupuestos)
- docs: Reglas de longitud escalada DeepSeek en CLAUDE.md

Archivos: `PruebaEjecucionController.php`, `presupuesto-preview.blade.php`, `CLAUDE.md`

## 2026-03-29

- feat: Campo `realizado` en gastos para indicar si el pago al acreedor fue cancelado (migracion 0048). Toggle con PATCH, desmarcar requiere credenciales admin. Ver [[Reglas de Negocio#Gastos - Campo realizado]]
- feat: Checkbox read-only de gastos realizados en listado de presupuestos. Eager-load `proyecto.gastos` en index
- feat: Color diferente para estado COBRADO vs APROBADO en [[Frontend]] (StatusBadge)
- fix: Dashboard — meses duplicados en grafico de ingresos/gastos

Archivos principales: `GastoController.php`, `GastoResource.php`, `Gasto.php`, `presupuestos/index.vue`, `StatusBadge.vue`, `DashboardService.php`

## 2026-03-27

- fix: PDF presupuesto — corregir scroll en html2canvas para exportacion completa
- ui: Remover boton eliminar del listado de activaciones (solo desde detalle)

Archivos: `presupuesto-preview.blade.php`, `evidencias/index.vue`

## 2026-03-25

- feat: Eliminar activaciones requiere credenciales admin (modal email+password). Ver [[Reglas de Negocio#Operaciones que requieren credenciales admin]]
- feat: Mostrar estado del proyecto en listado de presupuestos

Archivos: `PruebaEjecucionController.php`, `presupuestos/index.vue`, `evidencias/[id].vue`

## 2026-03-22

- feat: IVA en gastos (0 / 10.5 / 21 / 27%). Migracion 0047. Ver [[Reglas de Negocio#IVA en Gastos]]
- feat: Etiquetas de colores visibles en listado de proyectos. Ver [[Reglas de Negocio#Etiquetas de Presupuestos]]
- feat: Orden de presupuestos y proyectos por `updated_at` DESC con touch automatico
- feat: Dashboard mejorado con 6 KPIs, tooltips, filtro por periodo
- feat: Edicion de gastos con restriccion por estado de presupuesto (COBRADO/FACTURADO bloquea)
- feat: Modal de detalle de gasto en vista de proyecto
- feat: Boton eliminar gastos desde listado y vista de proyecto
- ui: Reducir tamano de texto en tabla gastos del proyecto, quitar columna categoria
- docs: Documentar edicion de gastos, proteccion por estado y error de rutas apiResource
- fix: `env()` -> `config()` en BackupController. Ver [[Errores Comunes#env no lee variables de entorno del container en PHP-FPM]]
- fix: nowrap en columnas numericas de gastos

Archivos principales: `GastoController.php`, `GastoResource.php`, `gastos/nuevo.vue`, `gastos/[id].vue`, `proyectos/[id].vue`, `presupuestos/index.vue`, `DashboardService.php`

## 2026-03-21

- feat: PDF de activaciones sobre hoja membretada Blu con TCPDF+FPDI (portrait A4). Ver [[Stack e Infraestructura#Plantilla PDF membretada]]
- fix: Agregar tcpdf y fpdi al composer.json para produccion
- fix: Asegurar dirs templates y temp en Dockerfile y entrypoint

Archivos: `PruebaEjecucionController.php`, `Dockerfile`, `docker-entrypoint.sh`, `composer.json`

---

## Ver tambien

- [[Backend - API]] - Endpoints modificados
- [[Reglas de Negocio]] - Reglas de dominio agregadas
- [[Errores Comunes]] - Bugs descubiertos y resueltos
- [[memoria]] - Convenciones y feedback acumulado
