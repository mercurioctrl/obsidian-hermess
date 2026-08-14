# Módulo Tareas (2.0)

Tablero Kanban de tareas de marketing, ampliado en el release de colaboración (2026-08-14, migs `0064–0091`) con colaboración completa. Sección `VER_SECCION_TAREAS` (`/tareas`), detalle en `/tareas/[id]`.

## Capacidades

| Feature | Backend | Rutas |
|---------|---------|-------|
| Kanban por columnas | `ColumnaTarea` (`es_inicio` mig 0076), `Tarea` | `PATCH /tareas/{t}/estado` |
| **Subtareas** (checklist) | `Subtarea` (mig 0067) | `/tareas/{t}/subtareas`, `/subtareas/{s}/toggle`, `.../reordenar` |
| **Comentarios + menciones** | `TareaComentario` (migs 0074, 0084), `Support\MencionParser` | `/tareas/{t}/comentarios`, `DELETE /comentarios/{c}` |
| **Adjuntos** (S3) | `TareaAdjunto` (mig 0075), disco `tarea_adjuntos` | `/tareas/{t}/adjuntos` |
| **Enlaces** externos | `TareaEnlace` (mig 0083) | `/tareas/{t}/enlaces` |
| **Seguidores** (watchers) | `TareaSeguidor` (mig 0078) | `/tareas/{t}/seguidores` |
| **Relaciones** entre tareas | `TareaRelacion` (mig 0069) | `/tareas/{t}/relaciones`, `DELETE .../{relacionada}` |
| **Historial de estados** | `TareaHistorialEstado` (mig 0066) | expuesto en el resource |
| Etiquetas | `Etiqueta` (descripción mig 0081) | `POST /tareas/{t}/etiquetas` |

`Tarea` gana además: `numero` correlativo visible tipo `#123` (mig 0068), `proyecto_id` + `color` (mig 0064), `pais` (mig 0091).

## Notificaciones

Cada acción (asignación, cambio de estado, comentario, mención, deadline) dispara el motor `TareaNotificador` → in-app + email + push. Ver [[modulos/notificaciones]].

## Frontend

Página `pages/tareas/index.vue` (tablero) y `pages/tareas/[id].vue` (detalle). Componentes: `TareaChecklist`, `TareaComentarios`, `TareaSeguidores`, `TareaRelacionadas`, `TareaEnlaces`, `TareaEtiquetasSelector`, `TareaHistorialEstados`, `TareaBadgeDeadline`, `TareaBadgeAprobacion`. Selectores reutilizables `SelectorUsuario` / `SelectorUsuarioMulti` / `SelectorPais`.

## Ver también

- [[modulos/solicitudes]] — las tareas nacen muchas veces de una Solicitud aprobada
- [[modulos/notificaciones]] — motor de avisos disparado por eventos de tarea
- [[modulos/campanas]] — una tarea puede colgar de un proyecto/campaña
- [[arquitectura]] · [[changelog#2026-08-14 — Deploy release colaboración (Tareas 2.0, Solicitudes, Minutas, Notificaciones+Push, Campañas)|changelog]]
