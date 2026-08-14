# Módulo Solicitudes

Cola de pedidos que **piden convertirse en Tarea**. Alguien carga una solicitud (título, descripción, prioridad, cliente, deadline) y un responsable la aprueba (convirtiéndola en [[modulos/tareas|Tarea]]) o la rechaza con motivo. Sección `VER_SECCION_SOLICITUDES` (`/solicitudes`). Migs `0077`, `0085`, `0086`.

## Modelo

`Solicitud` (tabla `solicitudes`): `titulo`, `descripcion`, `prioridad` (default `MEDIA`), `cliente_id`, `deadline`, `fecha_carga`, `estado` (default `PENDIENTE`), `creado_por_id`, `tarea_id` (la tarea resultante), `resuelto_por_id`, `resuelto_en`, `motivo_rechazo`.

## Flujo

- `apiResource solicitudes` (CRUD).
- `POST /solicitudes/{s}/convertir` → crea la Tarea completando proyecto/asignación/deadline y linkea `tarea_id`.
- `POST /solicitudes/{s}/rechazar` → guarda `motivo_rechazo`.
- **Acción por email sin login**: `GET|POST /solicitudes/{s}/accion/{usuario}/{accion}` con `middleware('signed')` (URL firmada + expiración). GET *aprobar* ejecuta directo; GET *rechazar* muestra un form blade para escribir el motivo, POST confirma. Controlador `SolicitudController@accionEmail`.

Mails: `SolicitudCreadaMail`, `SolicitudResueltaMail`; blades en `resources/views/notificaciones/solicitud*.blade.php`.

## Ver también

- [[modulos/tareas]] — destino de una solicitud aprobada
- [[modulos/notificaciones]] — avisos de creación/resolución
- [[changelog#2026-08-14 — Deploy release colaboración (Tareas 2.0, Solicitudes, Minutas, Notificaciones+Push, Campañas)|changelog]]
