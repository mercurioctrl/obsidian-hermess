# Módulo Solicitudes

Cola de pedidos que **piden convertirse en Tarea**. Alguien carga una solicitud (título, descripción, prioridad, cliente, deadline) y un responsable la aprueba (convirtiéndola en [[modulos/tareas|Tarea]]) o la rechaza con motivo. Sección `VER_SECCION_SOLICITUDES` (`/solicitudes`). Migs `0077`, `0085`, `0086`, `0109`.

## Modelo

`Solicitud` (tabla `solicitudes`): `titulo`, `descripcion`, `prioridad` (default `MEDIA`), `cliente_id`, `deadline`, `fecha_carga`, `estado` (default `PENDIENTE`), `creado_por_id`, `tarea_id` (la tarea resultante), `resuelto_por_id`, `resuelto_en`, `motivo_rechazo`. Relación many-to-many con clientes vía `solicitud_cliente` (mig `0109`).

## Flujo

- `apiResource solicitudes` (CRUD).
- `POST /solicitudes/{s}/convertir` → crea la Tarea completando proyecto/asignación/deadline y linkea `tarea_id`.
- `POST /solicitudes/{s}/rechazar` → guarda `motivo_rechazo`.
- **Acción por email sin login**: `GET|POST /solicitudes/{s}/accion/{usuario}/{accion}` con `middleware('signed')` (URL firmada + expiración). GET *aprobar* ejecuta directo; GET *rechazar* muestra un form blade para escribir el motivo, POST confirma. Controlador `SolicitudController@accionEmail`.

## Permisos de edición/borrado (2026-09-02, GIGA-45)

Antes **cualquier** usuario autenticado podía borrar o editar la solicitud de otro. Ahora `update`/`destroy` pasan por el gate `SolicitudController@puedeGestionar`: **el autor (`creado_por_id`) o quien tiene `VALIDAR_SOLICITUDES`** (+ admin por bypass). El solicitante, si se confundió o ya no la necesita, puede editar el título (p. ej. poner "borrar") en vez de eliminarla.

> **Nota / deuda:** el spec (ERP.pdf) pedía que **borrar** fuera **sólo** de "Vale"/validador — no del autor. Hoy el autor todavía puede borrar la propia; se dio por **cumplido igual** por ahora. Fix pendiente = sacar `creado_por_id` del gate de `destroy` (dejarlo sólo en `update`).

Mails: `SolicitudCreadaMail`, `SolicitudResueltaMail`; blades en `resources/views/notificaciones/solicitud*.blade.php`.

## Ver también

- [[modulos/tareas]] — destino de una solicitud aprobada
- [[modulos/notificaciones]] — avisos de creación/resolución
- [[changelog#2026-09-02 — Deploy cambios de Eze: flujo de estados en Campañas + calendario de trabajo en Tareas (GIGA-45→53)|changelog]]
