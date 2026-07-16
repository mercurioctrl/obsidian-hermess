# Módulo Calendario

Sección propia (`/calendario`, ítem en el sidebar) que **unifica en una vista mensual todo lo que tiene fecha y es de los usuarios**. Cross-cutting: junta datos de [[Modulo People Performance]] (ausencias, 1:1, objetivos) y de [[Modulo Tareas]] (deadlines). Entregado 2026-07-14 (PR #17). Doc técnico del repo: `arquitectura/15`.

## Qué muestra

| Tipo | Origen | Fecha usada |
|------|--------|-------------|
| **Tarea** | `tareas.fecha_vencimiento` (deadline), asignada a un usuario | día de vencimiento; **vencida sin finalizar → roja** |
| **Ausencia** / **Vacaciones** | `ausencias` (rango `fecha → fecha_fin`) | cada día del rango; "Vacaciones" = motivo, color propio |
| **Reunión 1:1** | `reuniones_uno_a_uno.fecha` | ese día |
| **Objetivo** | `objetivos.fecha_fin` (fecha límite) | ese día |

Filtros por **tipo** (chips de color) y por **persona**. Navegación de mes + "Hoy". Grilla lunes-primero, 42 días.

## Backend

`CalendarioController` (`app/Http/Controllers/CalendarioController.php`):
- `GET /api/calendario?desde=&hasta=` — array plano de eventos normalizados (`tipo, titulo, fecha, fecha_fin, persona, estado?, url, meta`). Método privado `agregarEventos($desde,$hasta,$soloUsuarioId?)` centraliza la agregación (con filtro por persona cuando aplica).

## Suscripción externa (feeds iCal .ics)

Cada usuario puede suscribir su calendario en **Google / Apple / Outlook** (solo lectura, refresh ~horas, no push):
- `usuarios.calendar_token` (mig `0089`, hex 48, unique, **oculto** en respuestas — está en `$hidden`).
- Auth: `GET /api/calendario/suscripcion` (genera/devuelve token) · `POST /api/calendario/suscripcion/regenerar` (rota = revoca URLs).
- **Feeds públicos** (fuera de `auth:sanctum`, auth por el token en la URL, patrón como `archivos/publico`):
  - `GET /api/calendario/{token}/personal.ics` — solo lo del usuario (tareas asignadas + ausencias/1:1/objetivos de su **empleado vinculado** por `empleado.usuario_id`).
  - `GET /api/calendario/{token}/equipo.ics` — todo el equipo.
  - Ventana: −3 a +12 meses. Eventos **all-day** (`DTSTART/DTEND;VALUE=DATE`, DTEND exclusivo = +1 día), UID estable `{tipo}-{id}@blu-minierp`. VCALENDAR generado a mano (escape + fold RFC 5545).
- Frontend `pages/calendario/index.vue`: modal "Suscribir a mi calendario" con las 2 URLs (personal/equipo), copiar, link `webcal://` e instrucciones por plataforma + regenerar token. Las URLs se arman con `window.location.origin` (no dependen del host del backend).

## Permisos

Gateado con **`VER_SECCION_CALENDARIO`** (sidebar + `middleware/auth.global.ts` + `SECCIONES_DISPONIBLES` del editor de usuarios). Admin lo ve directo. Ver [[Modulo Permisos]].

## Ver también

- [[Modulo People Performance]] — fuente de ausencias/1:1/objetivos
- [[Modulo Tareas]] — fuente de tareas con deadline
- [[Modulo Permisos]] — `VER_SECCION_CALENDARIO`
- [[Backend - API]] · [[Base de Datos]]
