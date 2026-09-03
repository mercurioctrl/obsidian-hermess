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

## Calendario de trabajo + fechas de trabajo (2026-09-02, GIGA-46/47/48)

Sobre el kanban se sumó una **vista calendario** dentro de `/tareas` (toggle kanban/calendario) que muestra **qué se trabajó cada día** y **cuánto duró** cada tarea, con **los mismos filtros** que el tablero.

- **Sesiones de trabajo**: `TareaController@calendario` recorre el `TareaHistorialEstado` y arma sesiones — **abre** cuando la tarea entra en una columna marcada `es_trabajo` (en curso) y **cierra** cuando entra en una `es_cierre` (en revisión / listo). Si vuelve a "en curso" en días posteriores, se abre una **nueva** sesión. Columnas marcadas en mig `0105` (`es_trabajo`/`es_cierre`) y `0114` (`es_finalizada`).
- **Fechas de trabajo editables** en la card de detalle (`fecha_inicio_trabajo` / `fecha_fin_trabajo`, mig `0106`), guardado inline vía `PATCH` `TareaController@actualizarFechasTrabajo`. Sólo el responsable.
- **Preset de inicio**: setear una fecha de inicio **futura** deja la tarea "programada" (`inicio_trabajo_aplicado_en=NULL`, badge "Programado") y la proyecta **punteada** en el calendario para organizar la semana. Al llegar el día pasa **automáticamente** a "en curso": inmediato si la fecha es ≤ hoy, o de madrugada vía el command `AplicarInicioTrabajoTareas` (scheduler). Lógica en `TareaEstadoService` (`cambiar(..., porPreset:true)`).
- **La fecha de fin NO se presetea**: la tarea se **extiende** en el calendario hasta que el responsable la arrastra a finalizado o completa el campo de fin. Al finalizar (`es_finalizada`) deja de extenderse y se muestra **tachada** (`line-through`) en el calendario.
- El **calendario original** (`/calendario`) **se desvinculó de las tareas** (ya no muestra sus deadlines): sólo fechas comerciales, efemérides, eventos y campañas. El deadline se sigue viendo desde el kanban.

## Notificaciones

Cada acción (asignación, cambio de estado, comentario, mención, deadline) dispara el motor `TareaNotificador` → in-app + email + push. Ver [[modulos/notificaciones]].

## Frontend

Página `pages/tareas/index.vue` (tablero + toggle calendario) y `pages/tareas/[id].vue` (detalle). Componentes: `TareasCalendarioSesiones` (vista calendario/Gantt de sesiones), `TareaChecklist`, `TareaComentarios`, `TareaSeguidores`, `TareaRelacionadas`, `TareaEnlaces`, `TareaEtiquetasSelector`, `TareaHistorialEstados`, `TareaBadgeDeadline`, `TareaBadgeAprobacion`. Selectores reutilizables `SelectorUsuario` / `SelectorUsuarioMulti` / `SelectorPais`.

Enlaces/comentarios/adjuntos guardan **inline** (Enter / auto-subida, sin paso "agregar" obligatorio) y el enlace **conserva su nombre** (backend resuelve el `<title>` real si no se da uno). *Nota: en `TareaEnlaces.vue` todavía queda visible el botón "+".*

## Ver también

- [[modulos/solicitudes]] — las tareas nacen muchas veces de una Solicitud aprobada
- [[modulos/notificaciones]] — motor de avisos disparado por eventos de tarea
- [[modulos/campanas]] — una tarea puede colgar de un proyecto/campaña
- [[arquitectura]] · [[changelog#2026-09-02 — Deploy cambios de Eze: flujo de estados en Campañas + calendario de trabajo en Tareas (GIGA-45→53)|changelog]]
