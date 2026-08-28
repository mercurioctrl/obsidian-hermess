# Módulo Reservas de Reuniones (link público tipo Calendly)

Cada **usuario del ERP** tiene un **link público compartible y memorable** (`/agendar/{slug}`, ej: `/agendar/juan-perez`) donde una persona externa (sin login) reserva un espacio de reunión entre los slots que el usuario preconfigura **self-service**. Al confirmarse: email a todas las partes con invite `.ics`, evento en el [[Modulo Calendario]] y notificación in-app/push al dueño.

> PRs: #30 (base) + #31 (invitados adicionales) + #32 (docs). Migraciones `0095`–`0100`. Mergeado a `main` el 2026-08-10.
> **2026-08-24:** #37 (slug memorable, migración `0103`) + #39 (URL pública `/reservar` → `/agendar`).

## Modelo de datos

Todo cuelga de `usuarios.id` (no de `empleados`), para que aplique también a admins sin ficha.

| Tabla | Campos clave |
|-------|--------------|
| `usuarios.booking_slug` (0103) | string(60) unique. **Slug memorable** del link (`/agendar/juan-perez`). Auto-gen del nombre (`asegurarBookingSlug()`, `Str::slug` + desambigua `-2/-3`), **editable** por el usuario |
| `usuarios.booking_token` | string(64) unique, `$hidden`. Lazy: `Usuario::asegurarBookingToken()`. Ahora **fallback** de links viejos con hash |
| `booking_configs` (0096) | `usuario_id` (unique), `activo`, `duracion_minutos`, `buffer_minutos`, `dias_anticipacion`, `titulo`, `descripcion`, `ubicacion` |
| `booking_reglas` (0097) | `usuario_id`, `dia_semana` (0=Dom..6=Sáb), `hora_inicio`, `hora_fin` — horarios semanales recurrentes |
| `booking_bloqueos` (0098) | `tipo` (`bloqueo` día/rango · `extra` slot puntual), `fecha`, `hora_inicio?`, `hora_fin?`, `motivo?` |
| `booking_reservas` (0099) | `fecha`, `hora_inicio/fin`, `invitado_nombre/email/notas`, `invitados_extra` JSON (0100), `estado`, `cancel_token`, `uid_ics` |

Modelos: `BookingConfig`, `BookingRegla`, `BookingBloqueo`, `BookingReserva`. `BookingReserva::todosInvitados()` = principal + extras deduplicado por email.

## Backend

- **`app/Services/BookingService.php`** — `slotsDisponibles()` genera slots de reglas semanales + extras, descartando **feriados**, **ausencias** del empleado vinculado, bloqueos, reservas y horarios pasados; acota a `dias_anticipacion`. `crearReserva()` revalida en **transacción** → anti doble-booking (422). Todo en TZ `America/Argentina/Buenos_Aires`.
- **`app/Support/IcsBuilder.php`** — helper `.ics` reutilizable (esc/fold + `invite()` con múltiples `ATTENDEE`, `METHOD:REQUEST`). El [[Modulo Calendario]] lo usa; su `respuestaIcs` ahora emite VEVENT con hora para las reservas.
- **`PublicBookingController`** (público) + **`MiDisponibilidadController`** (self-service, opera sobre `auth()->user()`). **`resolverAnfitrion($ref)`** resuelve al dueño por `booking_slug` **o** `booking_token` (fallback de links viejos).
- **`ReservaReunionMail`** + blade `emails/reserva-reunion`: email a cada invitado (saludo personalizado) + al dueño, con `.ics` adjunto. **Se envía por el mailer `erp@`** (`Mail::mailer('erp')`, no payments@); el Mailable/`Mail::raw` fija el `from` en `erp@`. Ver [[Stack e Infraestructura#Mail]].

## Endpoints

**Públicos** (fuera de `auth:sanctum`, seguridad por token en la URL):
```
GET  /api/reservas/cancelar/{cancelToken}   (DEBE ir antes de /{token})
GET  /api/reservas/{token}                  (info anfitrión + slots)
POST /api/reservas/{token}                  (crea reserva; invitados_extra[] opcional)
```

**Self-service** (`auth:sanctum`):
```
GET/PUT /api/mi-disponibilidad
PUT     /api/mi-disponibilidad/slug            (personaliza el slug; valida [a-z0-9-], min 3, unicidad; 422 si ocupado/reservado)
POST    /api/mi-disponibilidad/regenerar-token
POST|DELETE /api/mi-disponibilidad/reglas[/{regla}]
PUT     /api/mi-disponibilidad/reglas            (syncReglas: reemplaza TODAS las reglas de una vez; lo usa la grilla visual)
POST|DELETE /api/mi-disponibilidad/bloqueos[/{bloqueo}]
DELETE  /api/mi-disponibilidad/reservas/{reserva}   (el dueño cancela; avisa a todos)
```

## Al confirmar / cancelar

- **Emails** a todos los invitados (principal + extras) y al dueño, con **invite `.ics`** para aceptar y agregar al calendario. Cada envío en try/catch (si el SMTP falla, no rompe la reserva).
- **Notificación in-app + push** al dueño (`Notificacion` + `PushService`, `url` `/mi-disponibilidad`).
- **Evento en el [[Modulo Calendario]]** como `tipo='reserva'` (color `#0A85E0`, con hora) + en los feeds `.ics`.
- **Cancelación** (pública por `cancel_token` o del dueño) libera el slot y avisa por email a todos los invitados.

## Frontend

- **`pages/agendar/[token].vue`** — PÚBLICA (`layout: 'auth'`, whitelisteada por prefijo `/agendar` en `middleware/auth.global.ts`). Flujo: elegir día → horario → datos + **"+ Agregar invitado"** → confirmar. Cancelación vía `?cancelar=<token>`. (Antes `/reservar`; renombrada en #39.)
- **`pages/mi-disponibilidad/index.vue`** — editor del **slug personalizable** (prefijo del dominio + input + Guardar), link (copiar/regenerar/toggle activo), config, horarios semanales, excepciones y próximas reuniones (badge `+N` de invitados extra + cancelar).
- **Accesos:** NavItem "Mi Disponibilidad" en el sidebar (sin permiso, para todo usuario) + tarjeta en `/mi-area`.

### Editor visual de horarios / grilla semanal (PR #50, 2026-08-27)

- Componente **`components/BookingWeekGrid.vue`** — grilla de 7 días con **click-and-drag para pintar/borrar franjas** de disponibilidad, en vez del alta manual de rangos uno por uno. La página `mi-disponibilidad` tiene toggle Lista/Calendario (grilla).
- Guarda el **set completo** con **`PUT /mi-disponibilidad/reglas`** → `MiDisponibilidadController::syncReglas()` (**delete + recreate en una transacción**; valida `HH:MM` con regex y compara `hora_fin <= hora_inicio` a mano). Los endpoints POST/DELETE de reglas individuales siguen existiendo.

## Recordatorios al anfitrión (PR #51, migración 0108, 2026-08-27)

El anfitrión puede optar por recibir recordatorios de **sus** reuniones (no los invitados: ellos ya reciben el `.ics`).

- **Config:** en Mi Disponibilidad, sección **"Recordatorios para mí"** con dos checkboxes en `booking_configs`: **`recordatorio_dia`** (el día, a la mañana) y **`recordatorio_1h`** (una hora antes). `MiDisponibilidadController` los expone y valida.
- **Envío:** comando **`reservas:recordatorios`** (en `routes/console.php`, scheduler `everyFifteenMinutes`). Manda **correo (`erp@`) + push (VAPID) + in-app** al dueño. *1h antes* dispara cuando faltan ≤60 min; *el día* dispara desde las **08:00**.
- **Anti-duplicado:** `booking_reservas.recordatorio_dia_enviado_at` / `recordatorio_1h_enviado_at` (mig `0108`) marcan el envío → cada recordatorio se manda una sola vez.
- Reusa `PushService::enviarAUsuario`, `Notificacion` y `Mail::mailer('erp')` (mismo patrón que el aviso de nueva reserva). Un fallo de SMTP no corta el resto.
- ⚠️ El **scheduler** corre en el contenedor `minisaas-scheduler` (`php artisan schedule:work`); al deployar hay que copiar el comando + `console.php` ahí y reiniciarlo.

## Gotchas

- El link público se arma con `request()->getSchemeAndHttpHost()` (host real del request), NO con `config('app.url')` (que es `http://localhost`).
- **⚠️ Validación de horas:** la regla `gt:campo` de Laravel compara **longitud** de string, no orden → rompía la validación de rangos horarios. Comparar `hora_fin <= hora_inicio` a mano. Ver [[Errores Comunes]].

## Ver también

- [[Modulo Calendario]] — donde aparecen las reservas como eventos con hora
- [[Modulo Personal]] — `/mi-area` enlaza a Mi Disponibilidad; las ausencias bloquean slots
- [[Modulo Tareas#Web Push]] — mismo `PushService`/notificaciones in-app
- [[Errores Comunes]] — gotcha de la regla `gt` con horas
- [[Backend - API]] · [[Base de Datos]]
