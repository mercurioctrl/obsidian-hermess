# Módulo Requerimientos

Segundo tab del **portal del cliente** (mismo enlace secreto que [[Modulo Novedades]], resuelto por el
**mismo `novedades_token`**): un **tablero tipo Trello** donde el cliente **carga requerimientos fácil**.
**Sin login**, **aislamiento total** — el cliente se resuelve DESDE el token y todo se scopea por `cliente_id`.

La página pública `/n/{token}` tiene **tabs** "Novedades" + "Requerimientos"; cada tab con su flag
(`novedades_publicado` / `requerimientos_habilitado`), ambos bajo el único token del cliente.

**Reparto de control:**
- **Cliente (público):** Trello completo sobre **tarjetas** (crear/editar/mover/borrar + drag).
- **Equipo (interno):** además gestiona **columnas** y **convierte un requerimiento en una Tarea** interna
  (módulo [[Modulo Tareas]]).

En desarrollo 2026-09-03 (rama `feat/requerimientos-cliente`, PR #56, migración 0111). Es **seguimiento/intake**:
NO toca finanzas (igual que [[Modulo Flota GSM]] y [[Modulo Novedades]]).

## Modelo de datos (migración 0111)

`clientes` sumó `requerimientos_habilitado` (bool, default true).

**`req_columnas`** (kanban configurable por cliente): `cliente_id` (FK cascade), `nombre`, `color` (hex),
`orden`, `es_final` (marca "Hecho"). Columnas por defecto (sembradas por
`Cliente::asegurarTableroRequerimientos()`): Solicitado · En análisis · En progreso · Hecho.

**`req_tarjetas`** (cards): `cliente_id`, `req_columna_id` (FK cascade), `titulo`, `descripcion`,
`prioridad` (BAJA/MEDIA/ALTA), `orden`, `origen` (CLIENTE/EQUIPO), `tarea_id` (FK nullOnDelete → tareas,
si se convirtió), `created_by` (null si la creó el cliente).

## Backend

- **`RequerimientoService`** (`app/Services/`): `board(Cliente, $incluirTarea)`, `reordenar(Cliente, $columnas)`
  (scopeado por `cliente_id`), `siguienteOrden($colId)`.
- **`RequerimientosPublicController`** (PÚBLICO, resuelto por `novedades_token` + `requerimientos_habilitado`,
  `throttle:120,1`, headers noindex): `show`/`storeTarjeta`/`updateTarjeta`/`destroyTarjeta`/`reordenar`.
  Cada mutación valida `tarjeta.cliente_id === cliente.id`. **Al crear el cliente una tarjeta → `notificarEquipo()`**:
  avisa a admins activos con in-app (`Notificacion`, url `/requerimientos/{cliente_id}`) + push VAPID
  (`PushService::enviarAUsuario`), best-effort. Ver [[Modulo Tareas]] (misma infra de notificaciones).
- **`RequerimientoController`** (interno): `index` (clientes con `total`+`pendientes`), `board(Cliente)`
  (columnas + tarjetas + `proyectos`), CRUD de columnas (`destroyColumna` sólo si vacía), tarjetas
  (`origen=EQUIPO`), y **`convertirEnTarea`** (body `proyecto_id` del cliente + `asignado_a`) → crea `Tarea`
  (numero auto por su `booted`) y setea `tarjeta.tarea_id`; 422 si ya convertida.
- **`ClienteController::requerimientosHabilitado`** (toggle) + `ClienteResource` expone `requerimientos:{habilitado}`.

### Rutas
```
# PÚBLICO (throttle:120,1) — novedades_token
GET/POST/PUT/DELETE  /api/requerimientos/{token}[/tarjetas[/{tarjeta}]] , /reordenar

# auth:sanctum (interno)
GET    /api/requerimientos                              (landing)
GET    /api/requerimientos/cliente/{cliente}            (board + proyectos)
POST   /api/requerimientos/cliente/{cliente}/{columnas|columnas-reordenar|tarjetas|reordenar}
PUT/DELETE /api/requerimientos/columnas/{columna}       (DELETE 422 si tiene tarjetas)
PUT/DELETE /api/requerimientos/tarjetas/{tarjeta}
POST   /api/requerimientos/tarjetas/{tarjeta}/convertir (body: proyecto_id, asignado_a)
PUT    /api/clientes/{cliente}/requerimientos/habilitado
```

## Frontend

- **`components/RequerimientosBoard.vue`** — kanban con **`vue-draggable-plus`** (ya instalado, lo usa Tareas).
  Props `columnas` + `interno`; copia local para el drag, `@end` emite `reordenar`; quick-add + modal de
  edición (título/descripción/prioridad/eliminar + "convertir en tarea" si `interno`); columnas configurables
  sólo con `interno`.
- **`pages/n/[token].vue`** — portal público con **tabs** (carga `/novedades` + `/requerimientos` en paralelo).
- **`pages/requerimientos/index.vue`** (landing: clientes con ≥1 tarjeta) + **`[id].vue`** (board interno +
  modal convertir, con select de proyectos del board + asignado desde `/staff`).
- Sección `/requerimientos` con **`VER_SECCION_REQUERIMIENTOS`** (sidebar + `middleware/auth.global.ts` +
  catálogo en [[Frontend|usuarios]]) — gating **solo frontend**. Ver [[Modulo Permisos]].
- **`pages/clientes/[id].vue`** — la card del aside pasó a **"Portal del cliente"**: un link secreto único
  (Copiar/Abrir/Regenerar) + toggles **Novedades** y **Requerimientos** (+ "Ver tablero").

## Herramientas de la tarjeta (2026-09-05, migración 0112, PR #58)

La tarjeta tiene las mismas herramientas que una [[Modulo Tareas|Tarea]] interna, usables por el
cliente (público, por token) y el equipo:
- **Comentarios** (`req_comentarios`): hilo cliente↔equipo. El cliente sólo borra los `origen=CLIENTE`.
- **Adjuntos** (`req_adjuntos`): subir archivo o pegar **enlace**; si es enlace, el backend trae el
  `<title>`/`og:title` (`RequerimientoService::fetchTitulo`, timeout 5s) con **guarda anti-SSRF**
  (`urlSegura`: sólo http/https, bloquea localhost/hosts internos/IPs privadas). Archivos servidos por
  token público (`GET /api/requerimientos/adjuntos/{token}`, patrón [[Modulo WhatsApp Inbox|adjuntos por token]]).
- **Checklist** (`req_subtareas`): subtareas con barra de progreso.
- **Fecha límite** (`req_tarjetas.fecha_limite`): chip en la tarjeta (rojo vencida / ámbar ≤3 días).

Todo se serializa dentro de cada tarjeta del board (sin fetch extra). 15 rutas de sub-recursos
(par público-por-token / interno). Frontend: `RequerimientosBoard.vue` con modal rico (guardado
inmediato de sub-recursos) + badges en la cara de la tarjeta; elige endpoint según props `token`/`interno`.

## Limitaciones / futuro

- Columnas configurables **sólo por el equipo** (el cliente mueve tarjetas, no gestiona columnas).
- Adjuntos hasta 10 MB. `fetchTitulo` best-effort (si el sitio no responde, queda la URL).
- Notificación sólo **in-app + push** (sin email). El landing lista sólo clientes con ≥1 tarjeta.
- La conversión a Tarea es **one-way** (no sincroniza estado ni comentarios/adjuntos tarea↔tarjeta después).

## Ver también

- [[Modulo Novedades]] — comparten portal y `novedades_token` (tabs del mismo enlace)
- [[Modulo Tareas]] — destino de "convertir en tarea" + misma infra de notificaciones
- [[Modulo Permisos]] · [[Frontend]] · [[Backend - API]] · [[Base de Datos]]
- [[changelog#2026-09-03]]
