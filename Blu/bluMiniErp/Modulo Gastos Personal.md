# Módulo Gastos de Personal

Rendición de **reembolsos** del empleado: desde el **Área de empleado** ([[Modulo Personal|/mi-area]])
el empleado carga los gastos que tuvo de su bolsillo (taxi, insumos, etc.) adjuntando la **evidencia**
(imagen o PDF: ticket, captura). Quedan **PENDIENTE** hasta que un admin los **aprueba** o **rechaza**
(con motivo).

Es **intake/seguimiento** — como [[Modulo Requerimientos]], [[Modulo Novedades]] y [[Modulo Flota GSM]],
**NO toca finanzas**: no genera un `Gasto` real ([[Reglas de Negocio|flujo de caja]]) ni descuenta de
ningún banco/caja ni impacta saldos. Es un registro para reembolsar aparte (ej. junto al sueldo).

Desarrollado 2026-09-05 (rama `feat/gastos-personal`, PR #60, migración 0113).

## Modelo de datos (migración 0113)

**`gastos_empleado`**
- `empleado_id` (FK → `empleados`, cascade) · `usuario_id` (FK → `usuarios`, nullOnDelete — quién lo cargó)
- `descripcion` (500) · `monto` (decimal 12,2) · `moneda` (ARS/USD) · `fecha` (date del gasto)
- `categoria` (100, nullable, texto libre)
- `estado` (`PENDIENTE` | `APROBADO` | `RECHAZADO`, default PENDIENTE) · `motivo_rechazo` (500, nullable)
- `revisado_por` (FK → `usuarios`, nullOnDelete) · `revisado_at` (timestamp) · timestamps
- índice `(empleado_id, estado)`

**`gasto_empleado_adjuntos`** (evidencias)
- `gasto_empleado_id` (FK cascade) · `nombre` (300) · `path` (disco `public`, `gastos-empleado/{id}/…`)
- `mime_type` · `size` · `public_token` (64, unique — capability token, patrón [[Modulo WhatsApp Inbox|adjuntos por token]])

Estados como constantes del modelo: `GastoEmpleado::PENDIENTE|APROBADO|RECHAZADO`.

## Backend

- **Modelos** `GastoEmpleado` (rel. `empleado`, `usuario`, `revisor`, `adjuntos`) y `GastoEmpleadoAdjunto`
  (`asegurarPublicToken()`). **`GastoEmpleadoResource`** expone `monto` **sin enmascarar** (es el gasto
  propio del empleado, no un saldo de la empresa → no usa `VER_MONTOS_SALDOS`, ver [[Modulo Permisos]]);
  cada adjunto trae `es_imagen` + `url` = `/api/gastos-personal/adjuntos/{token}`.
- **`MiGastoController`** (self-service, `auth:sanctum`): resuelve el empleado con
  `request()->user()->empleado` (403 si el usuario no tiene ficha). CRUD **sólo sobre lo propio**
  (`propio()`), **editable sólo en `PENDIENTE`** (`editable()` → 422 si ya se resolvió). Adjuntos
  `mimes:jpg,jpeg,png,webp,gif,pdf|max:10240`. Al crear **notifica a los admins** (in-app `Notificacion`
  + push `PushService`, ver [[Modulo Tareas]]).
- **`GastoPersonalController`** (admin, gate **real** `abort_unless(tienePermiso('VER_SECCION_PERSONAL'))`):
  `index` (consolidado, filtros `?estado`/`?empleado_id`, `PENDIENTE` primero, `additional(pendientes)`),
  `empleado(Empleado)` (para el tab de `/staff/{id}`), `aprobar`/`rechazar` (rechazar exige `motivo`;
  setean `revisado_por/at` y **notifican al empleado**), `servirAdjunto(token)` **fuera de auth**
  (capability token, `inline`).

### Rutas
```
# PÚBLICO (capability token) — sirve la evidencia
GET    /api/gastos-personal/adjuntos/{token}

# Empleado (auth) — self-service en Mi Área
GET/POST           /api/mis-gastos
PUT/DELETE         /api/mis-gastos/{gasto}              (sólo PENDIENTE)
POST/DELETE        /api/mis-gastos/{gasto}/adjuntos[/{adjunto}]   (multipart: archivo — imagen/pdf, 10MB)

# Admin (auth + gate VER_SECCION_PERSONAL)
GET    /api/gastos-personal?estado=&empleado_id=
GET    /api/empleados/{empleado}/gastos
POST   /api/gastos-personal/{gasto}/aprobar
POST   /api/gastos-personal/{gasto}/rechazar           (body: motivo)
```
⚠️ El prefijo `/gastos-personal` **no colisiona** con `/gastos` en el middleware del front: el matcher
usa `path === prefijo || path.startsWith(prefijo + '/')`. Ver [[Modulo Permisos]].

## Frontend

- **`components/MisGastos.vue`** — embebido en `pages/mi-area/index.vue` ([[Modulo Personal]]). Lista con
  badge de estado + miniaturas de evidencia; modal de carga/edición. En **nuevo** acumula archivos y los
  sube tras crear el gasto (necesita el id); en **edición** sube/borra al instante. Muestra `motivo_rechazo`
  si fue rechazado. Editar/borrar sólo mientras `PENDIENTE`.
- **`components/GastosPersonalPanel.vue`** — panel admin reutilizable, prop `empleadoId?`:
  sin prop → consolidado (`/gastos-personal`, filtros de estado + buscador de empleado); con prop → por
  empleado (`/empleados/{id}/gastos`). Aprobar / Rechazar (modal de motivo) sobre las tarjetas `PENDIENTE`.
- **`pages/gastos-personal/index.vue`** — sección consolidada. NavItem en **Administración** + prefijo en
  `middleware/auth.global.ts`, gateados por `VER_SECCION_PERSONAL` (gating de sección **solo frontend**, pero
  el backend valida de verdad los endpoints de aprobación).
- **`pages/staff/[id].vue`** — tab **"Gastos"** que monta `<GastosPersonalPanel :empleado-id="Number(id)" />`.

Montos con `fmtM(monto, moneda, 2)` de `usePrivacyMode` (respeta el modo privado, ver [[Frontend]]).

## Limitaciones / futuro

- **No es un `Gasto`:** si en el futuro se quisiera que al aprobar impacte contabilidad, habría que generar
  un `Gasto` real (con `banco_caja_id`) en `aprobar()` — hoy deliberadamente NO lo hace ([[Modulo Contabilidad]]).
- Evidencias hasta 10 MB (jpg/png/webp/gif/pdf). Notificación sólo in-app + push (sin email).
- El empleado sólo edita/borra en `PENDIENTE`; tras resolverse queda de sólo lectura.

## Ver también

- [[Modulo Personal]] — vive dentro del Área de empleado (`/mi-area`) + tab en `/staff/{id}`
- [[Modulo Permisos]] — gate `VER_SECCION_PERSONAL` · [[Modulo Tareas]] — misma infra de notificaciones
- [[Backend - API]] · [[Base de Datos]] · [[Frontend]]
- [[changelog#2026-09-05 — Gastos de personal (rendición de reembolsos con evidencia)]]
