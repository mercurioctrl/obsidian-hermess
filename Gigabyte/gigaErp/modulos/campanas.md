# Módulo Campañas (fusión Proyectos → Campañas)

En el release 2026-08-14 la sección **"Proyectos" se renombró a "Campañas"** y ganó una capa comercial. Sección `VER_SECCION_PROYECTOS` (key **legacy**, no cambió) → `to: '/marketing/campanas'` con `rutasExtra: ['/proyectos']`. Migs `0061–0065`, `0090`.

## Concepto

Un **Proyecto** puede tener asociada una **Campaña** (capa comercial *opcional*) vía `proyectos.campana_id` (mig 0063). La campaña agrega:
- `tipo_id` → tipos de campaña configurables (mig 0090).
- **Líneas de cliente** `campana_clientes` (mig 0061): `cliente_id` + `presupuesto_usd` por cliente.
- Servicio **`App\Services\CampanaSync`** que centraliza el upsert Campaña ↔ Proyecto ↔ líneas (portado desde `CampanaController`), y opcionalmente agrega la campaña al calendario.

## Fondo por proyecto

`asignaciones_fondo.proyecto_id` (mig 0065) → el fondo de marketing ahora también se imputa por proyecto. Rutas `GET/POST /proyectos/{p}/fondo`, `DELETE /proyectos/{p}/fondo/{asignacion}` (`AsignacionFondoController@{indexProyecto,storeProyecto,destroyProyecto}`).

## Calendario ligado

`eventos_calendario` gana `campana_id`/`proyecto_id`/`tarea_id` (migs 0062, 0071) y tipos de evento configurables `tipos_evento_calendario` (mig 0070, `apiResource tipos-evento-calendario`).

## Frontend

`pages/marketing/campanas/index.vue` + `[id].vue`, componentes `ModalProyectoCampana.vue`, `ProyectoTablero.vue`, `ProyectoFondo.vue`, `NotificacionesCampana` (topbar). Rutas legacy `/proyectos` siguen protegidas por el mismo permiso.

## Ver también

- [[modulos/tareas]] — las tareas cuelgan de proyectos/campañas
- [[contexto]] — fondos de marketing por distribuidor/año
- [[changelog#2026-08-14 — Deploy release colaboración (Tareas 2.0, Solicitudes, Minutas, Notificaciones+Push, Campañas)|changelog]]
