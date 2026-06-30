# Módulo Tareas (tablero kanban estilo Jira)

Gestión de tareas con tablero kanban, drag & drop, detalle estilo Jira, seguimiento (watchers) y notificaciones multi-canal. Documentación técnica en repo: `arquitectura/11-modulo-tareas.md`.

**Agregado:** 2026-06-30 (entregado en PR #1, rama `feat/tareas-kanban`)

## Concepto

- Las tareas **pertenecen a un proyecto activo** y se **asignan a un usuario**.
- Código público `PREFIJO-N` (ej. `PLO-1`): prefijo del proyecto (editable) + número incremental **por proyecto**.
- **Copiable al clic** (`CodigoCopiable.vue`) y **linkeable** por URL: `/tareas/PLO-1`.
- Estados kanban: `PENDIENTE | EN_CURSO | EN_REVISION | FINALIZADO`. Prioridad: `BAJA | MEDIA | ALTA | URGENTE`.

## Base de datos (migraciones 0059–0071)

Ver [[Base de Datos]]. Tablas: `tareas`, `tarea_adjuntos`, `tarea_comentarios`, `tarea_subtareas`, `tarea_vinculos` (bidireccional), `tarea_seguidores`, `notificaciones`, `push_subscriptions`. Columnas nuevas: `proyectos.prefijo`, `usuarios.telefono`, `empleados.usuario_id` (unique, 1:1).

## Backend

- `TareaController`: index (sin paginar), store (auto-sigue creador+asignado), show / showPorCodigo, update (detecta diffs → notifica), reordenar (drag&drop), adjuntos, imágenes, comentarios, subtareas, vínculos, seguir/dejar de seguir. Ver [[Backend - API]].
- `Proyecto::derivarPrefijo`, `Tarea::getCodigoAttribute`, `Tarea::vinculadas` (ambas direcciones).
- **NotificacionService** notifica a los seguidores (menos al actor): in-app (`notificaciones`) + push, correo (`TareaCambioMail`), WhatsApp.
- **Web Push (VAPID, `minishlink/web-push`)**: `PushService`, endpoints `/push/*`, claves en `.env`. Requiere HTTPS en prod.
- **WhatsApp**: `WhatsAppService` reutiliza la Inbox API ([[Modulo WhatsApp Inbox]]); se configura en pantalla Configuración (DB).
- Búsqueda global incluye tareas (link `/tareas/{codigo}`).

## Frontend

- `pages/tareas/[[codigo]].vue` (ruta opcional `/tareas/:codigo?`): tablero con drag & drop (`vue-draggable-plus`), filtros por proyecto/etiquetas, detalle estilo Jira en 2 columnas. La **URL es la fuente de verdad** de la tarea abierta; `useHead` setea título/og.
- `RichTextEditor.vue` — **WYSIWYG con TipTap** (reemplazó a md-editor-v3); guarda HTML, imágenes por paste/botón.
- `CodigoCopiable.vue` — copia el código al portapapeles.
- **Campana** de notificaciones en topbar (no-leídas, polling 60s). Push: `public/sw.js` + `usePush.ts`.
- Panel **Seguir** (3 canales) con prompts just-in-time: pide permiso de push al activar "app", pide teléfono al activar WhatsApp. Ver [[Frontend]].

## Permisos y Personal

- Permiso `VER_SECCION_TAREAS` ([[Modulo Permisos]]).
- Vínculo **empleado ↔ usuario** ([[Modulo Personal]]): crear/vincular/desvincular usuario desde el detalle del empleado (solo admin). El usuario creado nace acotado a Tareas y sin ver saldos.

## Gotchas

- Orden en `<script setup>`: `useHead`/`watch(<ref>)` deben ir **después** de declarar el ref (si no, TDZ al montar). Ver [[Errores Comunes]].
- Si dos proyectos comparten prefijo, el código colisiona (resuelve el primero) → prefijos editables.
- Subtareas = checklist, no tareas-issue. Correo/WhatsApp fallan en silencio si no están configurados.

## Ver también

[[bluMiniErp]] · [[Base de Datos]] · [[Backend - API]] · [[Frontend]] · [[Modulo Personal]] · [[Modulo Permisos]] · [[Modulo WhatsApp Inbox]] · [[Errores Comunes]] · [[changelog]] · [[memoria]]
