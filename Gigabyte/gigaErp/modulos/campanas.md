# Módulo Campañas (fusión Proyectos → Campañas)

En el release 2026-08-14 la sección **"Proyectos" se renombró a "Campañas"** y ganó una capa comercial. Sección `VER_SECCION_PROYECTOS` (key **legacy**, no cambió) → `to: '/marketing/campanas'` con `rutasExtra: ['/proyectos']`. Migs `0061–0065`, `0090`.

## Concepto

Un **Proyecto** puede tener asociada una **Campaña** (capa comercial *opcional*) vía `proyectos.campana_id` (mig 0063). La campaña agrega:
- **Líneas de cliente** `campana_clientes` (mig 0061): `cliente_id` + `presupuesto_usd` por cliente.
- Servicio **`App\Services\CampanaSync`** que centraliza el upsert Campaña ↔ Proyecto ↔ líneas (portado desde `CampanaController`), y opcionalmente agrega la campaña al calendario.

## Varias acciones por campaña + flujo de estados por tipo (2026-09-02, GIGA-51/52/53)

Antes el **tipo de acción** se definía a nivel campaña. Ahora **cada línea `campana_clientes` es una acción** con su propio tipo, presupuesto y estado:
- `tipo_id` se **movió** de `campanas` a `campana_clientes` (mig `0110`); campos de acción extra en `campana_clientes` (mig `0113`). Una campaña = **N acciones**, cada una con `presupuesto_usd` (subtotal por cliente/acción) y **total general** (`presupuesto_total_usd` en `CampanaResource`).
- **Card** de campaña muestra las N acciones; botón **+Agregar acción** desde la campaña (reusa `LineasAccionCampana.vue`, upsert por id para no perder el histórico de estado).

**Estado condicional por tipo de acción** — resolutor único **`App\Support\FlujoEstadoAccion`** (`paraTipo()` lee `tipos_accion.flujo_estado`, mig `0111`, default `GENERICO`):
- Tipo **"Publicidad digital"** → flujo `EstadoFondoCliente`: Mail enviado → Rechazó el mail → En curso → Pendiente de reporte → Reporte recibido → Pago en procesamiento → Finalizado.
- **Resto** → `EstadoAccionGenerico`: Planificada, En curso, Pausada, Finalizada, Cancelada.
- Validado en back (`CampanaController`, `AccionMarketingController`) y front (`useEstadosAccion.ts` → `opcionesPara(tipo)`, `estados_por_flujo`). Al cambiar el tipo se **limpia** el estado si no pertenece al nuevo flujo (mig `0112` limpia datos históricos fuera de flujo).

**Integración Campañas ⇄ Fondos** — service **`App\Services\CampanaFondoSync`**:
- Cada línea con presupuesto se refleja como fila en **Fondos** (`acciones_marketing`, `origen_campana=true`) — **es la misma fila**, no se duplica. `presupuesto_usd → monto_usd`.
- **Alta unificada multi-cliente**: `clientes[]` crea N líneas en una transacción (tanto desde campaña como desde Fondos con `AccionMarketingController@store`).
- Editar una acción `origen_campana` desde Fondos está **bloqueado** → redirige a editarla en la campaña. El estado sí se puede cambiar desde ambos lados (misma acción).

## Fondo por proyecto

`asignaciones_fondo.proyecto_id` (mig 0065) → el fondo de marketing ahora también se imputa por proyecto. Rutas `GET/POST /proyectos/{p}/fondo`, `DELETE /proyectos/{p}/fondo/{asignacion}` (`AsignacionFondoController@{indexProyecto,storeProyecto,destroyProyecto}`). La tabla de **Fondos** (`marketing/index.vue`) tiene **fila de total** al pie (slot `footer` de `DataTable.vue`, total sobre todas las páginas filtradas — GIGA-50).

## Calendario ligado

`eventos_calendario` gana `campana_id`/`proyecto_id`/`tarea_id` (migs 0062, 0071) y tipos de evento configurables `tipos_evento_calendario` (mig 0070, `apiResource tipos-evento-calendario`).

## Frontend

`pages/marketing/campanas/index.vue` + `[id].vue`, `pages/marketing/index.vue` (Fondos) + `[id].vue` (detalle acción). Componentes `ModalCampana.vue`, `ModalProyectoCampana.vue`, `LineasAccionCampana.vue`, `ClientesCombobox.vue`, `ProyectoTablero.vue`, `ProyectoFondo.vue`, `NotificacionesCampana` (topbar). Composable `useEstadosAccion.ts`, util `utils/lineaAccionCampana.ts`. Rutas legacy `/proyectos` siguen protegidas por el mismo permiso.

## Ver también

- [[modulos/tareas]] — las tareas cuelgan de proyectos/campañas
- [[modulos/addons]] — lanzadores externos de Marketing
- [[contexto]] — fondos de marketing por distribuidor/año
- [[changelog#2026-09-02 — Deploy cambios de Eze: flujo de estados en Campañas + calendario de trabajo en Tareas (GIGA-45→53)|changelog]]
