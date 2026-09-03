# Changelog

Registro de lo trabajado en el proyecto, agrupado por fecha.

---

## 2026-09-03 — Nuevo módulo Novedades (blog público por cliente)

### Novedades (rama `feat/novedades-cliente`, migración 0110)
- feat: **blog público multi-tenant por cliente** en `/n/{token}`, accesible por un **enlace secreto rotable** (capability URL, mismo modelo que las reservas tipo Calendly). **Sin login:** quien tiene el link entra. **Aislamiento total** — el cliente se resuelve **desde el token** y toda query se scopea por `cliente_id` (nunca un id entra por la URL).
- **Se alimenta solo de data existente:** `Cliente → proyectos → PruebaEjecucion (período = entrada) → HitoEjecucion (avances)` + `ProyectoAdjunto` de imagen como evidencias. **Decisión:** se publican todos los hitos (las activaciones ya son trabajo curado; `hito.estado` es texto libre sin catálogo). `categoria_servicio` agrupa como chips "por aplicación/servicio".
- **Migración 0110:** `clientes` sumó `novedades_token` (string 64, nullable, unique, `Str::random(48)`) + `novedades_publicado` (bool, default true). Sin tablas nuevas.
- **Backend:** `NovedadesPublicController@show($token)` público (`throttle:60,1`, headers `X-Robots-Tag: noindex` + `Referrer-Policy: no-referrer`); `Cliente::{asegurarNovedadesToken,regenerarNovedadesToken,novedadesLink}` + `proyectos()`; `ClienteController` asegura token en `show` y suma `novedadesRegenerarToken` + `novedadesPublicado`; `ClienteResource` expone `novedades:{token,publicado,link}`. Base del link = `config('app.novedades_url')` (env `NOVEDADES_URL`, subdominio de prod) con fallback al host del request.
- **Frontend:** `pages/n/[token].vue` (público, `layout:'auth'`, `<meta robots noindex>`, `/n` en `RUTAS_PUBLICAS`) con chips de apps que filtran y entradas por período con avances + grid de evidencias; card **"Novedades"** en `pages/clientes/[id].vue` (link + Copiar/Abrir + Regenerar + Publicar/Despublicar).
- **Verificado:** 404 sin token; armado read-only contra cliente real (8 períodos, labels ES "Septiembre 2026", apps agregadas); build frontend incluye la página; `php -l` limpio. **No** probado con imágenes reales (proyectos de prueba sin adjuntos imagen). **Es seguimiento:** NO toca finanzas. Ver [[Modulo Novedades]].
- docs: `CLAUDE.md` + `arquitectura/19-modulo-novedades.md`. Pendiente ops del subdominio de prod. Sin commitear/PR al momento de escribir esto.

Archivos: `backend/database/migrations/0110_add_novedades_token_to_clientes.php`, `backend/app/Models/Cliente.php`, `backend/app/Http/Controllers/{NovedadesPublicController,ClienteController}.php`, `backend/app/Http/Resources/ClienteResource.php`, `backend/config/app.php`, `backend/routes/api.php`, `frontend/pages/n/[token].vue`, `frontend/pages/clientes/[id].vue`, `frontend/middleware/auth.global.ts`, `CLAUDE.md`, `arquitectura/19-modulo-novedades.md`

---

## 2026-08-29 — Nuevo módulo Flota GSM (líneas prepagas)

### Flota GSM (PR #54, migración 0109)
- feat: **módulo nuevo `/flota-gsm`** para administrar **líneas SIM prepagas** y no perder números (se pierden si no se recarga cada X meses). Permiso `VER_SECCION_FLOTA_GSM` (grupo Operaciones).
- **Alta de líneas:** nombre, número, observaciones, **`meses_vigencia`** (cada cuántos meses vence) y una **lista de contactos** (nombre + email) por línea a quienes avisar.
- **Cargas + vencimiento:** botón "Carga" (fecha + monto). Al registrar se actualiza la última carga (denormalizada en `gsm_lineas`), se recalcula **`vence_el = fecha_carga + meses_vigencia`** y se muestra el estado con badge de color (rojo ≤15 días / vencida, ámbar ≤30, verde). Historial en `gsm_cargas`.
- **Avisos por email (mailer `erp@`):** (1) al registrar una carga → aviso a los contactos con monto y próximo vencimiento; (2) **15 días antes del vencimiento** → comando **`gsm:alertas-vencimiento`** (scheduler **diario 09:00**) avisa a los contactos, **una sola vez por ciclo** (`alerta_15d_enviada_at`, se rearma al cargar). ⚠️ El comando corre en el contenedor **`minisaas-scheduler`**.
- **Decisión:** es un módulo de **seguimiento** — la carga NO genera gasto ni movimiento de banco/caja (a diferencia de sueldos). Verificado E2E con token real (alta → carga → `vence_el` = fecha + N meses). Ver [[Modulo Flota GSM]].
- docs: se documentó en `CLAUDE.md` + `arquitectura/18-modulo-flota-gsm.md`.

Archivos: `backend/database/migrations/0109_create_gsm_tables.php`, `backend/app/Models/{GsmLinea,GsmCarga,GsmContacto}.php`, `backend/app/Services/GsmAlertaService.php`, `backend/app/Http/Controllers/GsmLineaController.php`, `backend/app/Console/Commands/EnviarAlertasGsm.php`, `backend/routes/{api,console}.php`, `frontend/pages/flota-gsm/index.vue`, `frontend/layouts/default.vue`, `frontend/middleware/auth.global.ts`, `frontend/pages/usuarios/index.vue`, `CLAUDE.md`, `arquitectura/18-modulo-flota-gsm.md`

---

## 2026-08-27 — Seguridad de Configuración, menú reordenable, imputación al mes contable, reservas (grilla + recordatorios), sueldos pendientes

Sesión larga, cada cambio en su propio PR desde `main`. Todo desplegado y verificado en local.

### Seguridad — Configuración solo admin + pantalla de acceso denegado (PR #44, #45)
- fix: **la sección Configuración exponía tokens/datos sensibles a usuarios comunes** (Jira/GitHub/Inbox/Mercury/AFIP, backups). `ConfiguracionController::show` ahora ramifica por rol: los no-admin reciben sólo `publicConfig()` (6 campos básicos: nombre, logo, moneda, tasa, prefijo, vigencia). El backend es la barrera real (la UI se puede saltear por API). Ícono de engranaje del sidebar gateado con `isAdmin`.
- feat: **pantalla `/acceso-denegado`** — el `middleware/auth.global.ts` manda ahí a los no-admin que entran a `/configuracion`, `/usuarios` o cualquier sección sin permiso (antes los tiraba al dashboard silenciosamente, que tampoco deberían ver). Mensaje claro + botón "Volver al inicio" al lugar correcto según el usuario (solo-empleado → `/mi-area`). Ver [[Modulo Permisos]].

### Menú lateral reordenable por drag & drop (PR #46/#47, migración 0106)
- feat: cada usuario **reordena los ítems del sidebar** arrastrándolos, dentro de su grupo (Principal/Operaciones/Administración). Botón de editar (↕) en el encabezado del primer grupo. Preferencia por usuario en `usuarios.menu_orden` (json, mig `0106`). `AuthController::actualizarMenuOrden` + `PUT /auth/menu-orden` (valida y normaliza ids). El menú de `layouts/default.vue` pasó a declarativo (`MENU_ITEMS` + `GRUPOS`); persistencia optimista con debounce en el store `auth`. Ver [[Frontend]].

### Presupuestos — filtro "Pendientes de pago" (PR #48)
- feat: toggle **"Pendientes de pago"** en el listado de presupuestos → muestra sólo los que representan deuda del cliente sin cobrar (estados **APROBADO** o **FACTURADO**). Coherente con la semántica de deuda (el CARGO en cuenta corriente nace al aprobar y se salda al cobrar). Backend `PresupuestoController::index` respeta `?pendiente_pago=1`; combina con los demás filtros y la fila de totales por moneda.

### Finanzas — imputar ingreso/cobro/gastos al mes contable + guardar fecha real (PR #49, migración 0107)
- feat: se separa la **fecha contable** (mes de imputación en las estadísticas) de la **fecha real** (cuándo ocurrió la operación). Antes el ingreso (aprobar) y el cobro (pagar) se estampaban con `now()`, cayendo en el mes del clic, no en el del presupuesto.
  - **Aprobar (CARGO)** y **Cobrar (PAGO):** `fecha = presupuesto->fecha` (imputa al mes del presupuesto); `fecha_real = now()`.
  - **Gastos:** `fecha` sigue siendo el mes de imputación (editable); `fecha_real = now()` (registro). **Sueldos:** `fecha` = día 1 del período, `fecha_real` = fecha de pago elegida en el form.
  - Migración `0107`: `fecha_real` (nullable) en `movimientos_cuenta` y `gastos`. Resources + `ProyectoController::show` la exponen. Front: cuenta corriente (`clientes/[id]`) muestra "real DD/MM" cuando difiere; modal de gasto en proyecto muestra "Fecha real de pago". El saldo del banco/caja sigue registrando la plata que entra hoy (flujo de caja real, no cambia). Sin backfill. Ver [[Reglas de Negocio]] y [[Modulo Contabilidad]].

### Reservas — editor visual de disponibilidad semanal / grilla (PR #50)
- feat: componente **`BookingWeekGrid`** — grilla de 7 días donde se pintan las franjas de disponibilidad y se guardan todas juntas, en vez de cargar reglas una por una. Backend `MiDisponibilidadController::syncReglas` + `PUT /mi-disponibilidad/reglas` (borra-y-recrea en transacción; valida `HH:MM` comparando a mano — la regla `gt` de Laravel compara **longitud** de string). Los endpoints viejos POST/DELETE siguen. Ver [[Modulo Reservas Reuniones]].

### Reservas — recordatorios al anfitrión: email + push, el día y 1h antes (PR #51, migración 0108, PR abierto)
- feat: en **Mi Disponibilidad → Configuración**, sección **"Recordatorios para mí"** con dos checkboxes: **el día** de la reunión (a la mañana) y **una hora antes**. Cada uno manda **correo** (mailer `erp@`), **push** (VAPID) e **in-app** al anfitrión.
  - Comando **`reservas:recordatorios`** agendado cada 15 min (scheduler `minisaas-scheduler`). *1h antes* dispara cuando faltan ≤60 min; *el día* dispara desde las **08:00**. Marca de envío por reserva (`recordatorio_*_enviado_at`) → **no duplica**.
  - Migración `0108`: `recordatorio_dia`/`recordatorio_1h` en `booking_configs`; `recordatorio_*_enviado_at` en `booking_reservas`. Reusa `PushService::enviarAUsuario`, `Notificacion` y `Mail::mailer('erp')`. Es para el **anfitrión** (los invitados externos ya reciben el `.ics`). Verificado E2E sembrando una reserva de prueba. Ver [[Modulo Reservas Reuniones]].

### Personal — recordatorio de sueldos pendientes del mes vencido (PR #52)
- feat: en `/staff`, tarjeta que avisa **qué empleados activos aún no cobraron el sueldo del mes vencido**. Como se paga **a mes vencido**, el período es siempre el **mes anterior**: arrancado agosto, lista a quienes no tienen registrado el SUELDO de julio, hasta que se paga. `GET /empleados/sueldos-pendientes` (declarada **antes** del apiResource): período = `now()->subMonthNoOverflow()`; activos que ya estaban en la empresa sin `PagoPersonal` tipo SUELDO de ese período; monto respeta `VER_MONTOS_SALDOS`. Card ámbar con chips por persona, o verde "todos al día". Ver [[Modulo Personal]].

### Personal — deep-link del recordatorio al form de pago precargado (PR #53, PR abierto)
- feat: al clickear un chip pendiente, abre la ficha del empleado en la pestaña **Pagos con el sueldo listo para confirmar**: tipo SUELDO, período = mes vencido, **monto = salario base**, moneda del salario, **fecha de pago = día 5 del mes en curso**, y banco/caja autoseleccionado si hay uno solo de esa moneda. El chip enlaza a `/staff/{id}?tab=pagos&sueldo=1`; `staff/[id].vue` lee `?tab`/`?sueldo` en `cargar()` y precarga `formPago`. Ver [[Modulo Personal]].

Archivos: `backend/database/migrations/{0106_add_menu_orden_to_usuarios,0107_add_fecha_real_to_movimientos_y_gastos,0108_add_recordatorios_to_booking}.php`, `backend/app/Http/Controllers/{Configuracion,Auth,Presupuesto,Gasto,Empleado,Proyecto,MiDisponibilidad}Controller.php`, `backend/app/Services/PresupuestoService.php`, `backend/app/Console/Commands/EnviarRecordatoriosReservas.php`, `backend/app/Models/{Usuario,MovimientoCuenta,Gasto,BookingConfig,BookingReserva}.php`, `backend/app/Http/Resources/{Usuario,MovimientoCuenta,Gasto}Resource.php`, `backend/routes/{api,console}.php`, `frontend/layouts/default.vue`, `frontend/stores/auth.ts`, `frontend/middleware/auth.global.ts`, `frontend/pages/{acceso-denegado,presupuestos/index,clientes/[id],proyectos/[id],mi-disponibilidad/index,staff/index,staff/[id]}.vue`, `frontend/components/BookingWeekGrid.vue`

---

## 2026-08-25 — Recuperación de clave + mailer erp@, simulador de aumentos, ajustes de comunicados

### Recuperación de contraseña + cuenta de correo del sistema (PR #43, migración 0105)
- feat: **flujo forgot/reset password** (no existía). Link "¿Olvidaste tu contraseña?" en `/login` → `/recuperar` (pide email) → email con link → `/restablecer` (nueva clave). `AuthController::forgotPassword`/`resetPassword`, rutas públicas `POST /auth/forgot-password` y `/auth/reset-password` (throttle 6/min). Tabla `password_reset_tokens` (mig 0105, token **hasheado**, expira **60 min**). Respuesta **genérica** (no filtra si el email existe) y al resetear **se cierran todas las sesiones** (`tokens()->delete()`). Frontend `pages/{recuperar,restablecer}.vue` whitelisteadas en `middleware/auth.global.ts`. Verificado E2E (forgot inserta token, reset cambia clave y permite login, inválido→422).
- feat: **mailer `erp` nuevo** = `erp@blustudioinc.com` (box.lio.red:465 SSL), **separado de `payments@`** que queda SOLO para documentos de pago/cobro. `config/mail.php` sumó el mailer `erp` + `erp_from`; vars `MAIL_ERP_*` en `docker-compose.yml`; clave real en `mini-saas/.env` (gitignored). Ver [[Stack e Infraestructura#Mail]].
- refactor: **ruteo de correos** — se movieron a `erp@` los correos que estaban mal en payments@: **reservas de reuniones** (`ReservaReunionMail` + cancelaciones `Mail::raw`) y **notificaciones de tareas** (`TareaCambioMail`). Sólo el invoice de presupuestos queda en `payments@`. ⚠️ **Gotcha:** `Mail::mailer('erp')` cambia el SMTP pero **no el From** (sigue el global payments@); con From≠usuario autenticado el server rechaza → hay que fijar `from` en el Mailable / `Mail::raw` desde `config('mail.erp_from')`. Ver [[Errores Comunes]].

### Personal — Simulador de aumentos de sueldo (PR #41)
- feat: nueva pantalla **`/staff/simulador`** (botón "Simular aumentos" en el header de Personal). Seleccionás uno o más empleados y aplicás aumentos **porcentuales o nominales** (en masa a los seleccionados o ajustando cada uno), y ves sueldo nuevo + extra/mes por empleado, totales por moneda (ARS/USD no se mezclan) y resumen de extra por mes y por año. **100% client-side** (what-if, sin persistencia ni backend). Lee `GET /empleados`, respeta `VER_MONTOS_SALDOS` (si los sueldos vienen enmascarados, muestra aviso). Montos con `fmtM`. Ver [[Modulo Personal#Simulador de aumentos]].

### Comunicados — ajustes visuales (PR #42)
- fix/style: al email de comunicación se le **sacó la barra de acento verde** superior y el **botón CTA pasó a negro** (`#1A1A1A`, como los botones primarios del sitio). Slack no tiene botones (texto), no se tocó.

Archivos: `backend/database/migrations/0105_create_password_reset_tokens_table.php`, `backend/config/mail.php`, `backend/app/Http/Controllers/AuthController.php`, `backend/app/Mail/{RecuperarPasswordMail,ReservaReunionMail,TareaCambioMail}.php`, `backend/resources/views/emails/recuperar-password.blade.php`, `backend/app/Http/Controllers/{PublicBooking,MiDisponibilidad}Controller.php`, `backend/app/Services/NotificacionService.php`, `backend/routes/api.php`, `docker-compose.yml`, `frontend/pages/{login,recuperar,restablecer}.vue`, `frontend/pages/staff/{index,simulador}.vue`, `frontend/middleware/auth.global.ts`, `mini-saas/comunicados/`, `CLAUDE.md`

---

## 2026-08-24 — Reservas: slug memorable + /agendar, gastos con IVA mixto, comunicados

Tres bloques de trabajo. Todo desplegado y verificado en local.

### Reservas — link memorable y URL `/agendar`
- feat: **slug memorable del link de reuniones** (migración `0103`). Pasó de `/reservar/{hash-64}` a **`/agendar/{slug}`** (ej: `/agendar/juan-perez`). `usuarios.booking_slug` (unique) se auto-genera del nombre (`Usuario::asegurarBookingSlug()` con `Str::slug`, desambigua `-2/-3`) y es **editable** (`PUT /api/mi-disponibilidad/slug`, valida `[a-z0-9-]`, min 3, unicidad, reserva `cancelar`). **Fallback:** `PublicBookingController::resolverAnfitrion()` matchea por `booking_slug` **o** `booking_token` → los links viejos con hash siguen andando. Trade-off aceptado: slug enumerable, pero sólo permite *pedir* reunión (como Calendly). **PR #37 (mergeado).**
- refactor: **URL pública `/reservar` → `/agendar`** (comunica mejor la acción). Rename `pages/reservar/[token].vue` → `pages/agendar/[token].vue`, whitelist del middleware y link builders del backend (show/regenerar/updateSlug/cancelUrl). La API interna `/api/reservas/*` NO cambia (no la ve el externo). Copy del kit de comunicados refuerza el verbo *agendá*. **PR #39.**
- Verificado en vivo: auto-gen desde el nombre, personalización a `juan-perez`, 422 con slug inválido/ocupado, resolución por slug y por token viejo. Ver [[Modulo Reservas Reuniones]].

### Gastos — IVA mixto (campo Exento / No gravado)
- feat: **`gastos.monto_exento`** (migración `0104`). Un mismo gasto puede tener una parte **gravada** (neto × IVA%) y una parte **exenta / no gravada** (ej: propinas), como una Factura A con ítems mixtos. **Total = neto gravado + IVA + exento**; el banco/caja descuenta el total. El **Libro IVA compras** reporta `neto` (sólo gravado), columna `exento` y `total` correctos (`ContabilidadService::libroCompras`). Forms `gastos/nuevo` + `gastos/[id]` con campo "Exento / No gravado" y total recalculado en vivo. **⚠️ Limitación:** cubre 1 alícuota gravada + exento, no dos alícuotas gravadas distintas (para eso harían falta ítems por gasto). **PR #38.** Ver [[Modulo Contabilidad]].
- fix: **al editar un gasto no se aplicaba el cambio de proyecto/tipo** — `UpdateGastoRequest` no whitelisteaba `proyecto_id` ni `tipo`, así que `validated()` los descartaba y el `update` los ignoraba. Ahora sí; además se limpia `proyecto_id` si el tipo deja de ser PROYECTO y se toca el `updated_at` del proyecto anterior y el nuevo. **PR #38.** Ver [[Errores Comunes]].
- Verificado con la factura real GE-GASTRO: neto 1.440.000 @21% + exento 174.240 → IVA 302.400, total 1.916.640; libro OK. Cambio de proyecto 1→2 persiste en DB.

### Comunicados internos
- chore: **kit de anuncio de Mi Área y Mi Disponibilidad** (`mini-saas/comunicados/`): email HTML on-brand + mensaje de Slack + 2 capturas (mockups con datos ficticios, renderizados con Chromium headless del container). URL del sistema como placeholder (`erp.blustudioinc.com`, a confirmar).

Archivos: `backend/database/migrations/{0103_add_booking_slug_to_usuarios,0104_add_monto_exento_to_gastos}.php`, `backend/app/Models/{Usuario,Gasto}.php`, `backend/app/Http/Controllers/{MiDisponibilidad,PublicBooking,Gasto,Proyecto}Controller.php`, `backend/app/Http/Requests/{Store,Update}GastoRequest.php`, `backend/app/Http/Resources/GastoResource.php`, `backend/app/Services/ContabilidadService.php`, `backend/routes/api.php`, `frontend/pages/agendar/[token].vue`, `frontend/pages/mi-disponibilidad/index.vue`, `frontend/pages/gastos/{nuevo,[id]}.vue`, `frontend/middleware/auth.global.ts`, `mini-saas/comunicados/`, `CLAUDE.md`, `arquitectura/16-modulo-reservas-reuniones.md`

---

## 2026-08-23 (tarde) — Dashboard rentabilidad, cliente clickeable, simulador de impuestos

Sesión de features frontend (backend mínimo). Desplegado y verificado en local; **sin PR aún**.

- feat: **Dashboard — tabla "Rentabilidad por Cliente (ARS)"** (`pages/index.vue`, antes de "Últimos Movimientos"). Por cliente: **Facturación · Gasto · Ganancia bruta · Impuestos · Ganancia neta** + fila de totales (`#footer` de `DataTable`). Backend `DashboardService::rentabilidadPorCliente($desde,$hasta,$impuestosTotal)`: facturación = `CARGO` ARS por cliente; gasto = gastos ARS vía `gasto → proyecto (proyectos.cliente_id)`; **impuestos = prorrateo** del total global de `ContabilidadService::liquidacion()` por participación en la facturación (aproximación: los impuestos reales son globales). Gateado por `VER_MONTOS_SALDOS`. Se eligió el enfoque "antes vs después de impuestos". Ver [[Modulo Contabilidad#Dashboard — Rentabilidad por Cliente]].
- feat: **Nombres de cliente clickeables en TODA la app** → link a `/clientes/{id}` (NuxtLink, hover verde). Aplicado en dashboard, presupuestos (listado+detalle), proyectos (card+detalle), cuenta-corriente, facturación (el controller ya trae `cliente_id`), remito detalle. En tablas/cards con navegación propia se usa `@click.stop`; en modales de confirmación queda como texto. Se agregó `cliente_id` a `ultimos_movimientos` en `DashboardService`.
- feat: **Simulador de facturas de compra (what-if)** en `pages/proyectos/[id].vue` (pestaña Ejecución, botón "Simular compras" dentro de "Impuestos estimados"). 100% client-side reactivo. Ingresás compra neta + alícuota IVA y ves comparativa **Actual vs Simulado** de cada impuesto + botón "Neutralizar IVA". Ayuda a decidir qué facturas pedir a proveedores para bajar impuestos.
- feat: **"Te queda después de impuestos"** = número que faltaba (el usuario no lo veía). Franja destacada en el bloque de impuestos + fila en el simulador. Fórmula = **Ganancia − Imp. Ganancias − IIBB** (el IVA es neutro: se cobra y se remite). Distinto del "Resultado" operativo.
- fix: **Costo real del simulador** — estaba mal: restaba el ahorro sobre el **neto** (`P − ahorro`) cuando el desembolso real es el **total** (`P + IVA`). Corregido a `(P + IVA) − ahorro`. Al 21%+35% el costo real es 65% de la compra, no 44%. Ver [[Errores Comunes]].
- feat: **Contabilidad — lista de compras incompletas con acceso a completar** (`pages/contabilidad/index.vue`). El aviso ámbar ahora **lista cada compra** con IVA a la que le faltan datos del comprobante (proveedor, fecha, monto, **qué falta** via helper `faltantesDe`) + botón **"Completar"** → `/gastos/{gasto_id}`. Las filas incompletas se resaltan en la tabla Compras. Los datos (`incompleto`, `gasto_id`) ya venían de `ContabilidadService::libroCompras()`. Ver [[Modulo Contabilidad#Compras incompletas]].

Archivos: `backend/app/Services/DashboardService.php`, `frontend/pages/index.vue`, `frontend/pages/proyectos/[id].vue`, `frontend/pages/contabilidad/index.vue`, `frontend/pages/presupuestos/{index,[id]}.vue`, `frontend/pages/proyectos/index.vue`, `frontend/pages/cuenta-corriente/index.vue`, `frontend/pages/facturacion/index.vue`, `frontend/pages/remitos/[id].vue`, `arquitectura/16-modulo-contabilidad.md`, `CLAUDE.md`

---

## 2026-08-23

- feat: **Módulo Remitos** (migración 0102). Desde `/presupuestos/{id}` → menú "Más" → **Remito** → "Generar remito": crea un remito **copiando los ítems** del presupuesto y navega a `/remitos/{id}`. **Varios remitos por presupuesto.** **Independiente del presupuesto:** editar/eliminar el remito NO lo modifica (modelo `Remito` **sin `$touches`**; `update` hace delete+recreate de `remito_items` sin tocar `items_presupuesto` — verificado en vivo). **Remito tradicional:** sólo descripción+cantidad, **sin precios**; PDF formato BLU (`PdfService::renderRemitoPdf()` + blade `pdf/remito.blade.php`, Browsershot) que **no requiere `VER_MONTOS_SALDOS`**. Numeración interna `REM-{AAAAMM}-NNN`. Tablas `remitos` + `remito_items` (`cascadeOnDelete`). Rutas CRUD + `GET /api/remitos/{id}/pdf?token=`. Frontend `pages/remitos/[id].vue` (editar fecha/ítems/observaciones) + grupo "Remito" en el menú "Más" del presupuesto. Ver [[Modulo Remitos]].
- fix/gotcha: en blades PDF el logo va con `@include('pdf._logo')` (renderiza el `<img>`), **NO** con `@include('pdf.partials.logo')` (ese sólo define `$bluLogoBase64` en el scope local del include → error 500 "Undefined variable" en el blade padre). Detectado al construir el remito. Ver [[Errores Comunes]].

Archivos: `backend/database/migrations/0102_create_remitos_tables.php`, `backend/app/Models/{Remito,RemitoItem,Presupuesto}.php`, `backend/app/Http/Controllers/RemitoController.php`, `backend/app/Http/Resources/Remito{,Item}Resource.php`, `backend/app/Services/PdfService.php`, `backend/resources/views/pdf/remito.blade.php`, `backend/routes/api.php`, `frontend/pages/remitos/[id].vue`, `frontend/pages/presupuestos/[id].vue`, `arquitectura/17-modulo-remitos.md`

---

## 2026-08-21

- feat: **Módulo Contabilidad** (PR #34 + fix #35). Nueva sección `/contabilidad`: **liquidación de impuestos del período** (IVA débito − crédito, IVA a pagar, Ganancias, IIBB, todo pesificado) + descarga del **Libro IVA** en Excel con hojas **Ventas** y **Compras**, calcado del export de *Mis Comprobantes* de ARCA. **Ventas** = comprobantes AFIP `EMITIDA`/`ACREDITADA` (facturas y NC netean; Mercury NO entra). **Compras** = gastos con `iva_monto > 0`. `ContabilidadService::liquidacion()` es la **única fuente** del cálculo (`DashboardService::impuestosResumen()` delega ahí para no desincronizar). `LibroIvaExcelService` escribe el `.xlsx` a mano (ZIP + OOXML) con **`ext-zip`** ya presente → **sin dependencias nuevas ni rebuild especial**. Rutas `GET /api/contabilidad` y `GET /api/contabilidad/libro-iva?token=` (fuera de auth, token en query). Permiso **`VER_SECCION_CONTABILIDAD`**, ícono `lucide:calculator`. Fix #35: el IVA no se resta del margen después de impuestos. Ver [[Modulo Contabilidad]].
- feat: **Datos fiscales del gasto** (migración `0101_add_datos_comprobante_to_gastos`). `gastos` sumó 7 columnas opcionales (`proveedor_nombre`, `proveedor_cuit`, `comprobante_tipo`, `comprobante_pto_vta`, `comprobante_numero`, `comprobante_fecha` indexada, `comprobante_cae`) que AFIP pide por línea en el libro de compras. Se cargan desde `FacturaCompraFields.vue` en `/gastos/nuevo` y `/gastos/[id]`, sección que se **auto-abre cuando el gasto tiene IVA > 0**. `comprobante_fecha` (≠ fecha de pago) manda en el filtro del libro cuando está cargada; si no, cae a `gastos.fecha`.
- feat: **Flecha "volver a Presupuestos" en el breadcrumb de Operación** (PR #33). En `/proyectos/[id]` el breadcrumb ganó una flecha para volver al listado de Presupuestos.

Archivos: `backend/app/Services/{ContabilidadService,LibroIvaExcelService,DashboardService}.php`, `backend/app/Http/Controllers/ContabilidadController.php`, `backend/database/migrations/0101_add_datos_comprobante_to_gastos.php`, `backend/app/Models/Gasto.php`, `frontend/pages/contabilidad/index.vue`, `frontend/components/FacturaCompraFields.vue`, `frontend/pages/gastos/{nuevo,[id]}.vue`, `arquitectura/16-modulo-contabilidad.md`

---

## 2026-08-10

- feat: **Reservas de reuniones tipo Calendly** (PR #30 base + #31 invitados). Cada usuario tiene un **link público** `/reservar/{booking_token}` (sin login) donde un externo reserva un slot, y configura su disponibilidad **self-service** en `/mi-disponibilidad`. Disponibilidad **híbrida**: reglas semanales recurrentes (`booking_reglas`) + bloqueos/extras puntuales (`booking_bloqueos`). `BookingService::slotsDisponibles()` descarta feriados, ausencias del empleado, bloqueos, reservas y pasado; `crearReserva()` revalida en transacción (**anti doble-booking**, 422). Al reservar: **email a todos los invitados + al dueño con invite `.ics`** (`IcsBuilder::invite`, múltiples `ATTENDEE`, `METHOD:REQUEST`), **evento `tipo='reserva'`** en el [[Modulo Calendario]] (color `#0A85E0`, con hora) y **notificación in-app + push** al dueño. Cancelaciones (público por `cancel_token` o dueño) liberan el slot y avisan a todos. **Invitados adicionales** (PR #31): botón "+ Agregar invitado", `booking_reservas.invitados_extra` JSON (mig 0100), `BookingReserva::todosInvitados()` deduplica por email. Nueva página pública `pages/reservar/[token].vue` (`layout: 'auth'`, whitelisteada en `middleware/auth.global.ts`); NavItem "Mi Disponibilidad" para todos. Ver [[Modulo Reservas Reuniones]].
- fix: **La regla `gt`/`lt` de Laravel compara longitud de string** (no orden) → rompía la validación de rangos horarios (`booking_reglas`/`booking_bloqueos` no se guardaban, 422 silencioso). Fix = comparar `hora_fin <= hora_inicio` a mano. Ver [[Errores Comunes]].
- docs: **`arquitectura/16-modulo-reservas-reuniones.md`** (nuevo) + secciones en `CLAUDE.md` y `arquitectura/08-errores-comunes.md` (PR #32).

Archivos: `backend/database/migrations/{0095..0100}_*`, `backend/app/Models/Booking{Config,Regla,Bloqueo,Reserva}.php`, `backend/app/Services/BookingService.php`, `backend/app/Support/IcsBuilder.php`, `backend/app/Http/Controllers/{PublicBooking,MiDisponibilidad,Calendario}Controller.php`, `backend/app/Mail/ReservaReunionMail.php`, `backend/resources/views/emails/reserva-reunion.blade.php`, `frontend/pages/{reservar/[token],mi-disponibilidad/index,mi-area/index,calendario/index}.vue`, `frontend/middleware/auth.global.ts`, `frontend/layouts/default.vue`

---

## 2026-08-07

- feat: **Días extra de vacaciones (premio)** (PR #27). Se pueden otorgar días libres extra a un empleado, cada uno con cantidad (decimal, permite 0.5), **motivo** y **fecha de vencimiento**; **suman a los días disponibles mientras no venzan**. Tabla `vacaciones_extra` (mig 0093) + modelo `VacacionExtra`. `Empleado::diasExtraVigentes()` suma solo no vencidos → `dias_disponibles = asignados + extra vigentes`. Endpoints `GET/POST/DELETE /api/empleados/{id}/vacaciones-extra` (devuelven `{items, resumen}`). Se cargan en `/staff/[id]` tab Ausencias; se ven en Mi Área con desglose `base + extra`. Ver [[Modulo Personal#Días extra de vacaciones (premio) (2026-08)]].
- feat: **Mi Área — listado de feriados del año** (PR #24). `MiAreaController` devuelve `feriados[]` del año en curso y `/mi-area` los muestra en una card al final (día+fecha, nombre, badge de tipo; pasados atenuados). Solo lectura sobre la tabla `feriados`.
- feat: **Favicon adaptativo** (PR #25). `favicon.svg` con `@media (prefers-color-scheme)` — la B de BLU se ve negra en tema claro y blanca en oscuro. Recortado al bounding box real del glyph. Fallbacks `favicon-16/32.png`, `favicon.ico` y `apple-touch-icon.png` (badge oscuro con B blanca, porque iOS no soporta transparencia adaptativa). Wireados en `nuxt.config.ts`.
- chore: **Título "Blu Erp - Gestión Empresarial"** (PR #26). Reemplaza "Mini SaaS" en el `<title>` (`nuxt.config.ts`) y en el título fallback de notificaciones push (`public/sw.js`).

Archivos: `backend/database/migrations/0093_*`, `backend/app/Models/VacacionExtra.php`, `backend/app/Http/Controllers/{EmpleadoController,MiAreaController}.php`, `backend/app/Models/Empleado.php`, `frontend/pages/{mi-area,staff/[id]}.vue`, `frontend/nuxt.config.ts`, `frontend/public/{favicon*,apple-touch-icon.png,sw.js}`

---

## 2026-08-05

- feat: **Vacaciones en días hábiles + feriados nacionales + Política de Vacaciones** (PR #23). El cálculo de vacaciones de Mi Área pasó de días corridos a **días hábiles** (política Blu): `Empleado::diasHabilesEntre()` excluye sábados, domingos y feriados. Nueva tabla `feriados` (mig 0092) + modelo `Feriado` + `FeriadosSeeder` (listado oficial **2025+2026** de argentina.gob.ar, idempotente). Los feriados también se muestran en el [[Modulo Calendario]] (evento `tipo='feriado'`, color rosa, visibles aunque se filtre por persona). En Mi Área, la nota legal se reemplazó por una card **"Política de Vacaciones"** colapsable. Ver [[Modulo Personal#Vacaciones — días hábiles + feriados]].

Archivos: `backend/database/migrations/0092_*`, `backend/app/Models/Feriado.php`, `backend/database/seeders/FeriadosSeeder.php`, `backend/app/Models/Empleado.php`, `backend/app/Http/Controllers/CalendarioController.php`, `frontend/pages/{mi-area,calendario}/index.vue`

---

## 2026-08-04

- feat: **Área de empleado — `/mi-area`** (PR #22). Vista self-service para usuarios con **empleado vinculado** (`empleados.usuario_id`): datos públicos (correo, teléfono, **dirección**, **cumpleaños**, inicio de actividades), **resumen de rol** (área, reporta a, propósito, responsabilidades desde [[Modulo People Performance|Rol & Expectativas]]), **datos bancarios** (banco, tipo cuenta, CBU/CVU, alias, titular, CUIL con copiar), y **vacaciones** por antigüedad. Campos nuevos en `empleados`: `direccion` (mig 0090), `fecha_nacimiento` + bancarios (mig 0091). `tiene_empleado` en `UsuarioResource`; login redirige a `/mi-area` si el usuario es solo-empleado; NavItem gateado. No expone sueldos. Ver [[Modulo Personal#Área de empleado y vacaciones (Mi Área) (2026-08)]].
- feat: **Breadcrumb navegable en activaciones** (PR #22). `/evidencias/[id]` con breadcrumb clickeable (`Activaciones › Cliente › Presupuesto › Proyecto › Activación N° X`), visible al ver y editar. `PruebaEjecucionController` ahora incluye `proyecto.presupuesto` y `proyecto.cliente` en el payload con eager-load (sin N+1).
- feat: **Documento W-9 (IRS)** de BLU STUDIO GROUP LLC en [[Modulo Documentos]] (PR #21). Entrada `w9` en `config/documentos.php`, solo original (sin formato BLU).

Archivos: `backend/app/Http/Controllers/{MiAreaController,EmpleadoController,PruebaEjecucionController}.php`, `backend/app/Models/Empleado.php`, `backend/app/Http/Resources/UsuarioResource.php`, `backend/database/migrations/{0090,0091}_*`, `backend/config/documentos.php`, `frontend/pages/{mi-area,staff/[id],evidencias/[id],login}.vue`, `frontend/layouts/default.vue`

---

## 2026-07-26

- fix: **Ranking de GitHub — commits contados por `committed_at` dentro del rango** (PR #19). Antes `rendimiento()` sumaba `pr->commits` atribuidos a la **fecha de apertura del PR** (`gh_created_at`), así que mover el intervalo `desde`/`hasta` casi no cambiaba el ranking (se veía el histórico). Ahora los commits del ranking (y del gráfico "Commits por desarrollador") se cuentan desde `github_commits` agrupados por `author_login` filtrando por **`committed_at`** en el rango — misma lógica que la vista detallada del dev. Líneas +/− y contadores de PR siguen a nivel PR. Aprovecha el índice `(author_login, committed_at)` (~130ms frío / ~74ms caliente). Ver [[Modulo GitHub]]
- docs: **CLAUDE.md — gastos siempre editables/eliminables** (parte del PR #19). Se corrigieron las secciones "Gastos — Edición" y "Gastos — Eliminación" que aún decían "No editables si COBRADO o FACTURADO", contradiciendo el comportamiento real tras el PR #18.
- ops: se configuró `DEEPSEEK_API_KEY` en el entorno. ⚠️ Laravel lee `env()` desde el `.env` que carga Dotenv (`/var/www/html/.env`, horneado desde `backend/.env`), **no** desde las env vars que inyecta docker-compose. La key va en `backend/.env` (gitignoreado); tras cambiarla: `config:clear` + `docker restart` (no `--force-recreate`, que revierte el `.env` en caliente). Ver [[Errores Comunes]]

Archivos: `backend/app/Services/GithubService.php` (rendimiento por `committed_at`), `CLAUDE.md`

---

## 2026-07-20

- fix: **Los gastos son siempre editables y eliminables** (PR #18) — se quitó el bloqueo que impedía registrar/editar/eliminar gastos cuando el presupuesto del proyecto estaba COBRADO o FACTURADO. Caso real: llegan costos **después** de emitida la factura y hay que imputarlos. Se eliminó `validarNoProtegido()` de `GastoController::update()`/`destroy()`; `GastoResource.editable` pasa a ser siempre `true`; se quitó el gate `puedeEditarGastos` en `proyectos/[id].vue`. Ver [[Reglas de Negocio]]
- fix: **Preselección de proyecto en forms de gasto** — pedían `/proyectos`, que oculta `propuesta`/`cancelado`, dejando el select vacío al entrar desde un proyecto en `propuesta` (y perdiendo la vinculación al guardar en edición). Ahora piden `/proyectos?estado=todos`.

Archivos: `backend/app/Http/Controllers/GastoController.php`, `backend/app/Http/Resources/GastoResource.php`, `frontend/pages/gastos/[id].vue`

---

## 2026-07-14 (continuación — People & Performance Fase 2 inicial + Calendario)

- feat: **Sección Calendario** (`/calendario`, vista mensual) que unifica **todo lo que tiene fecha y es de los usuarios**: tareas por su **deadline** (`fecha_vencimiento`, vencidas sin finalizar en rojo), **ausencias/vacaciones** por rango, **reuniones 1:1** y **objetivos** por fecha límite. Filtros por tipo y por persona. `CalendarioController` + `GET /api/calendario?desde=&hasta=`. Gateada con `VER_SECCION_CALENDARIO`. Entregado en PR #17. Ver [[Modulo Calendario]]
- feat: **Suscripción de calendario externa (feeds iCal .ics)** — cada usuario suscribe su calendario en Google/Apple/Outlook. `usuarios.calendar_token` (mig `0089`, oculto). Auth: `GET /calendario/suscripcion` + `POST …/regenerar`. Públicos por token: `GET /api/calendario/{token}/personal.ics` (solo lo suyo) y `/equipo.ics` (todo). Eventos all-day, VCALENDAR a mano. Modal "Suscribir a mi calendario" con copiar + `webcal://` + instrucciones. Solo lectura, refresh ~horas. Ver [[Modulo Calendario]]
- feat: **Reuniones 1:1 por empleado** — primer bloque de la Fase 2. Tab en la ficha con lista + modal (título/fecha/observaciones). Tabla `reuniones_uno_a_uno` (mig `0088`), `ReunionUnoAUno` + `ReunionUnoAUnoController`. Endpoints `GET/POST /empleados/{id}/reuniones-1a1`, `PUT/DELETE /reuniones-1a1/{id}`. Ver [[Modulo People Performance]]
- feat: **Ausencias con rango de fechas** — `ausencias` +`fecha_fin` opcional (mig `0087`) para vacaciones (sin `fecha_fin` = un solo día). Forms "Desde/Hasta", listado "inicio → fin · N días", validación `after_or_equal:fecha`.
- fix: **La validación de la API devolvía 500 en vez de 422** — el render de excepciones (`bootstrap/app.php`, PR #10) capturaba todo `Throwable` y, como `ValidationException` no tiene `getStatusCode()`, caía en el 500 genérico → **ningún formulario mostraba errores por campo en producción**. Ahora `ValidationException` → **422 con `errors`**. Afecta a toda la app. Ver [[Errores Comunes]]
- fix: **Pestañas de la ficha de empleado en una sola línea** — con 9 tabs se partían en dos líneas; ahora `whitespace-nowrap` + scroll horizontal (scrollbar oculta).

Todo mergeado a `main` (PRs #14, #16, #17). Migraciones nuevas: `0087`, `0088`, `0089`. ⚠️ Al desplegar correr migraciones + seeders (`RolesExpectativasSeeder`, `CompetenciasSeeder`).

Archivos: `backend/app/Http/Controllers/{Calendario,ReunionUnoAUno}Controller.php` (nuevos), `backend/app/Models/ReunionUnoAUno.php` (nuevo), `backend/bootstrap/app.php` (422), `backend/database/migrations/{0087,0088,0089}_*`, `frontend/pages/calendario/index.vue` (nuevo), `frontend/pages/staff/{[id],ausencias}.vue`, `frontend/layouts/default.vue`, `frontend/middleware/auth.global.ts`, `frontend/pages/usuarios/index.vue`

---

## 2026-07-14

- feat: **Módulo People & Performance (RRHH) sobre Personal — Fase 1 + integraciones.** Se volcaron al sistema la spec `Especificación Funcional y Técnica.docx`, la planilla de ausencias y el doc de roles/expectativas del equipo. Todo dentro de la sección Personal (`/staff`), por tabs en la ficha del empleado. Rama `feat/rrhh-ausencias-roles` (sin commitear). Ver [[Modulo People Performance]], [[Modulo Personal]], [[Backend - API]]
  - **Rol & Expectativas**: `empleados` +`area`,`reporta_a`,`proposito`,`responsabilidades`(JSON),`autonomia`,`expectativas`(JSON),`foco_desarrollo` (mig `0081`). Tab editable + `RolesExpectativasSeeder` con los 7 colaboradores reales (match nombre case/acento-insensitive, sin duplicar)
  - **Ausencias**: tabla `ausencias` (mig `0082`), `AusenciaController` CRUD, tab por empleado + vista global `staff/ausencias.vue` (fiel a la planilla, 11 motivos)
  - **Competencias**: catálogo `competencias` + pivot `empleado_competencia` (esperado vs actual 1-5) (mig `0083`), `CompetenciaController` (catálogo + sync por empleado), `CompetenciasSeeder` (8 técnicas + 10 organizacionales). Visual de puntos con anillo = nivel esperado
  - **Objetivos (OKRs)**: tabla `objetivos` (mig `0084`), `ObjetivoController`, tab con estado/prioridad/% avance/trimestre, modal alta-edición
  - **Actividad (evidencia)**: tab que conecta [[Modulo GitHub|GitHub]] (reusa `/github/desarrollador/{login}` por `github_username`) y **Jira** (nuevo `jira_account_id` mig `0086`, `/empleados/{id}/jira-issues` por JQL en vivo). Regla de la spec: evidencia, **no** métrica de evaluación
  - **Auto-vincular Jira**: botón en `/staff` → `/jira/sugerencias-empleados` (match email/nombre → exacto/único/ambiguo/sin_match) + `/jira/vincular-masivo`; preview con confirmación humana (los emails ERP `@blu.inc` no coinciden con Jira)
  - **Permisos**: la sección se gatea con `VER_SECCION_PERSONAL`; se corrigió `layouts/default.vue` para que "Personal" no quede encerrado en el bloque solo-admin (ahora `isAdmin || puedeVer('VER_SECCION_PERSONAL')`), de modo que un usuario RRHH vea solo Personal. Sueldos aparte con `VER_MONTOS_SALDOS`. Ver [[Modulo Permisos]]
  - ⚠️ Prefijos de migración `0081-0084` **duplicados** con los de GitHub — coexisten (Laravel trackea por nombre). Máx real `0086`, seguir en `0087`. Ver [[Errores Comunes]]

Archivos: `backend/database/migrations/{0081,0082,0083,0084,0086}_*`, `backend/app/Models/{Ausencia,Competencia,Objetivo,Empleado}.php`, `backend/app/Http/Controllers/{Ausencia,Competencia,Objetivo,Empleado,Jira}Controller.php`, `backend/database/seeders/{RolesExpectativas,Competencias}Seeder.php`, `backend/routes/api.php`, `frontend/pages/staff/{[id],index,ausencias}.vue`, `frontend/layouts/default.vue`, `arquitectura/15-modulo-people-performance.md` (nuevo)

- feat: **Tareas — landing con resumen de proyectos por estado.** Al entrar a `/tareas` (sin proyecto seleccionado) se muestra una **grilla de proyectos** que tienen tareas en los estados filtrados (default: pendientes + en curso); cada proyecto muestra el conteo de sus tareas por estado (pendiente / en curso / en revisión / finalizado). Seleccionar un proyecto (card o el dropdown existente) entra a su board kanban, con botón "← Todos los proyectos" para volver. Ver [[Modulo Tareas]], [[Backend - API]]
  - Backend: nuevo endpoint `GET /api/tareas/proyectos-resumen?estados=CSV` (`TareaController::proyectosResumen`) — devuelve los proyectos con ≥1 tarea en los estados filtrados, cada uno con los 4 conteos completos; **una sola query agrupada** (sin N+1), ordenado por tareas activas desc. Ruta estática **antes** de `/tareas/{tarea}`
  - Frontend: componente nuevo `components/TareasResumenProyectos.vue` (chips de filtro multi-estado persistidos + grilla de cards, colores por estado iguales al board), integrado en `pages/tareas/[[codigo]].vue`. En modo resumen ya no se cargan todas las tareas de todos los proyectos. Deep-links `/tareas/{codigo}` intactos
  - Entregado en **PR #13** (rama `feat/tareas-resumen-proyectos`, base `main`, sin mergear)
  - ⚠️ UX pendiente de decisión: el filtro de proyecto se recuerda entre sesiones (comportamiento previo) → al volver a /tareas te reencuentra en el último board, no siempre en el resumen

Archivos: `backend/app/Http/Controllers/TareaController.php` (proyectosResumen), `backend/routes/api.php`, `frontend/components/TareasResumenProyectos.vue` (nuevo), `frontend/pages/tareas/[[codigo]].vue`

---

## 2026-07-12

- fix: **Auditoría técnica — hallazgos de seguridad e integridad corregidos** (fixes "sin cambio de comportamiento"). Se analizó el documento `REPORTE_ANALISIS_TECNICO.md` (auditoría externa) verificando cada hallazgo contra el código real. Entregado en **PR #10** (rama `fix/hallazgos-reporte-seguridad`, base `feat/integracion-github`). Ver [[Errores Comunes]], [[Backend - API]], [[Modulo Permisos]]:
  - **Secretos ya no se filtran al guardar configuración:** `ConfiguracionController::update()` devolvía `$config->fresh()` completo, exponiendo `mp_access_token`/`stripe_secret_key`/`mercury_api_key`/`inbox_api_token`/`jira_api_token` en texto plano. Se extrajo `safeConfig()` reusado por `show()` **y** `update()` (enmascara y devuelve flags `*_tiene_token`). El frontend usa `jira_tiene_token` (con fallback). También cerró una fuga de `jira_api_token` que `show()` tampoco enmascaraba
  - **Bug en `GET /api/gastos-resumen`:** `resumen()` reutilizaba el mismo query builder → quedaba `WHERE moneda='ARS' AND moneda='USD'` → `total_usd` daba **0** y `por_categoria`/`por_tipo` vacíos. Fix: `(clone $query)` por agregación. Verificado en vivo: `total_usd` pasó de 0 a valor real
  - **Excepciones internas no se exponen en producción:** el handler global (`bootstrap/app.php`) devolvía `message` + clase para todo error. Ahora en prod (`debug=false`) los **500** dan mensaje genérico; los `abort(4xx,'...')` conservan su mensaje. En dev queda idéntico
  - **Bug latente resuelto — `AuthenticationException` → 401:** `useApi.ts` espera **401** para limpiar el token y redirigir a `/login`, pero el backend devolvía **500** en fallos de auth (AuthenticationException no mapea a getStatusCode) → el redirect por sesión vencida **nunca funcionaba**. Ahora devuelve 401. ⚠️ Nginx strippea `/api`, así que el renderer JSON solo se dispara con header `Accept: application/json` (que el frontend siempre manda; al testear con curl hay que incluirlo o los códigos engañan)
  - **`mysqldump` con password escapado:** `escapeshellarg()` al password del dump de backup (`BackupController`)
- feat: **Formato de montos sin cortes de línea** — espacio duro (NBSP) entre símbolo de moneda y número en `usePrivacyMode` (`$ 1.000` no se parte), + reglas CSS globales (`word-break: keep-all`, `overflow-wrap: normal`) en `app.vue`, y ajuste en `PixelBarChart`. Incluido en PR #10 (por pedido del usuario, los 3 temas van juntos)
- **Pendiente del reporte (con enfoque ya decidido):** integridad financiera (transacción atómica `DB::transaction` en create/update/destroy de gastos + validación de moneda en `update()` — ambos solo-código, sin migración ni recálculo, verificado que no afectan datos: 0 gastos con moneda desajustada), throttle de login, CORS por dominio, paginación, agregaciones a SQL, índices, tests, PHP-FPM en prod, headers de seguridad Nginx

Archivos: `backend/app/Http/Controllers/ConfiguracionController.php` (safeConfig), `backend/app/Http/Controllers/GastoController.php` (clone en resumen), `backend/bootstrap/app.php` (excepciones prod + AuthException→401), `backend/app/Http/Controllers/BackupController.php` (escapeshellarg), `frontend/pages/configuracion/index.vue` (jira_tiene_token), `frontend/composables/usePrivacyMode.ts` + `frontend/app.vue` + `frontend/components/ui/PixelBarChart.vue` (formato montos), `REPORTE_ANALISIS_TECNICO.md` (nuevo)

---

## 2026-07-11

- feat: **Integración GitHub (solo lectura, PAT)** — nuevo módulo completo. Ver [[Modulo GitHub]]. **Dashboard de rendimiento** por desarrollador (commits contados por PR, +/− líneas, PRs abiertos/mergeados/a rama destino, reviews) sobre 122 repos de BluIncStudio/New-Bytes/LibreOpción. **⚠️ Arquitectura persistencia + sync incremental (NO live):** los datos viven en la DB (`github_repos`, `github_pull_requests`, `github_pr_reviews`, `github_commits` — migraciones 0078–0085), `GithubService::sync()` (comando `github:sync`, scheduler hourly) trae solo PRs con `updated_at` nuevo; las vistas leen de la DB. Manejo de rate limit (corta y retoma). Bots excluidos. Mapeo dev→empleado con `empleados.github_username`. Permiso `VER_SECCION_GITHUB`. Entregado en **PR #9** (rama `feat/integracion-github`). Ver [[Base de Datos]], [[Backend - API]], [[Frontend]], [[Modulo Permisos]]
- feat: **Vista detallada por desarrollador** `/github/{login}` — commits **día a día** por fecha real de autoría (tabla `github_commits`, migración 0085; el sync trae los commits de cada PR y `github:backfill-commits` completa los viejos), tiles (commits, líneas, PRs aceptados=mergeados, PRs pendientes=abiertos ahora + N hoy, reviews), gráfico diario y listas de PRs pendientes/aceptados y reviews. El ranking del dashboard navega a esta página. Ver [[Modulo GitHub]]
- feat: **Facturación electrónica AFIP (ARCA)** — facturar presupuestos por AFIP además de Mercury. SOAP WSAA (TA cacheado en Redis) + WSFEv1 (CAE), Factura A/B + Notas de Crédito con QR, PDF en formato BLU, estimación de impuestos (IVA/Ganancias/IIBB) y sección **Facturación** unificada AFIP+Mercury. ⚠️ Requiere `ext-soap` (rebuild del backend). Validado end-to-end contra AFIP producción. Doc en `arquitectura/13-modulo-facturacion-afip.md`. Entregado en **PR #5** (mergeado vía #8). Ver [[Base de Datos]], [[Backend - API]], [[Modulo Permisos]]
- feat: **Módulo Documentos** — nueva sección para alojar y descargar documentos corporativos, cada uno con descarga del **Original** y de una versión con **formato BLU** (membretada, render Browsershot). Ver [[Modulo Documentos]]. Sin DB: registry curado en `config/documentos.php` + página dinámica → agregar documentos no requiere tocar frontend/rutas/permisos. `DocumentoController` (descargas fuera de `auth:sanctum` con `?token=` + permiso `VER_SECCION_DOCUMENTOS`), `PdfService::renderVistaPdf()` genérico. 5 documentos iniciales (Alta IIBB, Constancia ARCA, carta Mercury, wire Mercury 2p, constitución SRL 3p). Entregado en **PR #5** (rama `feat/documentos-empresa`). Ver [[Backend - API]], [[Frontend]], [[Modulo Permisos]]
- fix: **build del backend por composer 2.10** — la imagen `composer:2` (tag flotante) se actualizó a 2.10.1 y activa por default `policy.advisories.block`, que bloquea la resolución de `laravel/framework ^11` (advisories abiertos) → `docker compose build backend` fallaba. Fix: `config.policy.advisories.block: false` en `composer.json` (el `audit.ignore` existente no cubre este caso). Entregado en **PR #4** (rama `fix/composer-advisories-block`). Ver [[Errores Comunes]]
- ops: **permisos de la carpeta de backups + restore manual** — la carpeta `storage/app/backups` (bind-mount al host `backups/`) quedaba `root:root` → la app (`www-data`) no podía escribir y "Crear backup" fallaba silencioso. Fix: `chown www-data`. **No hay endpoint de restore**: se restauró un backup importando `database.sql` a mano en el container de MySQL. Ver [[Errores Comunes]]

Archivos: `backend/config/documentos.php` (nuevo), `backend/app/Http/Controllers/DocumentoController.php` (nuevo), `backend/app/Services/PdfService.php` (renderVistaPdf), `backend/resources/views/pdf/documentos/*.blade.php` (5), `backend/composer.json` (policy), `frontend/pages/documentos/index.vue` (nuevo)

---

## 2026-06-30

- feat: **Módulo Tareas (tablero kanban estilo Jira)** — nuevo módulo completo. Ver [[Modulo Tareas]]. Tablero con drag & drop (`vue-draggable-plus`), 4 estados, filtros por proyecto/etiquetas. Código `PREFIJO-N` (prefijo editable por proyecto) **copiable** y **linkeable** (`/tareas/PLO-1`, ruta opcional). Detalle estilo Jira en 2 columnas: descripción **WYSIWYG con TipTap** (reemplazó md-editor-v3), subtareas (checklist), tareas vinculadas (bidireccional), adjuntos, comentarios, prioridad y fechas. Migraciones 0059–0065. Ver [[Base de Datos]], [[Backend - API]], [[Frontend]]
- feat: **Seguimiento de tareas + notificaciones multi-canal** — watchers por tarea con 4 canales: **in-app** (campana en topbar con no-leídas, polling 60s), **correo** (`TareaCambioMail` por SMTP), **push de escritorio** (Web Push / VAPID con `minishlink/web-push`, service worker `public/sw.js`) y **WhatsApp** (reutiliza la Inbox API — ver [[Modulo WhatsApp Inbox]]). Alerta por cambios y comentarios a todos los seguidores menos al actor. Prompts just-in-time: pide permiso de push y teléfono al activar cada canal. Migraciones 0067–0071. `usuarios.telefono`, `PUT /api/auth/telefono`
- feat: **Vínculo Empleado ↔ Usuario del sistema** — desde el detalle del empleado (solo admin) se puede crear/vincular/desvincular un usuario. El creado desde Personal nace acotado a la sección Tareas y sin ver saldos. Migración 0066 (`empleados.usuario_id` unique). Ver [[Modulo Personal]], [[Modulo Permisos]]
- docs: nuevo `arquitectura/11-modulo-tareas.md` + refs en 02/04/06/09; README con apartado "Configuración para producción" (VAPID, MAIL_PASSWORD, APP_URL, Inbox API, HTTPS). Entregado en **PR #1** (rama `feat/tareas-kanban`)
- chore: `docker-compose.yml` mapea `VAPID_*` y `MAIL_*` a los containers **backend + scheduler** desde `mini-saas/.env` (con `${VAR:-}`). ⚠️ Al declarar default vacío, la var del container **pisa a `backend/.env`** → las claves VAPID/MAIL van en **`mini-saas/.env`**. Ver [[Stack e Infraestructura#Variables de entorno .env]] y [[Modulo Tareas]]
- chore: **mergeado todo a `main`** — PR #1 (código módulo Tareas + seguimiento + WhatsApp) y PR #2 (documentación) mergeados. Ramas `feat/tareas-kanban` y `docs/modulo-tareas` borradas. ⚠️ El clasificador de Claude Code bloquea push/merge directo a `main`; se trabajó vía PR (ver [[memoria]])
- feat: **Descargar PDF/invoice requiere permiso `VER_MONTOS_SALDOS`**. Los endpoints públicos `/presupuestos/{id}/pdf`, `/preview` y `/mercury/invoices/{id}/pdf` resuelven el usuario del token y devuelven **403** si no tiene el permiso (admin bypassa). El frontend además oculta los botones de descarga (`v-if="authStore.verMontos"`) en listado y detalle. Los documentos tienen montos → mismo criterio que el masking. Ver [[Modulo Mercury Invoicing]] y [[Modulo Permisos]]
- chore: **`mini-saas/deploy-backend.sh`** — redeploy seguro del backend en prod (docker cp + migrate + optimize:clear + restart, sin tocar .env/seeders/build). ⚠️ NO usar `start.sh` en prod (regenera backend/.env y corre build+seed). Ver [[Errores Comunes]]
- docs: documentada toda la sesión en CLAUDE.md + arquitectura (05-frontend, 08-errores-comunes, 10-medios-de-pago) y memoria de Claude. Diagnóstico clave: la app es **SPA pura**, tras rebuild el navegador sirve chunks viejos → verificar deploy server-side + Cmd+Shift+R. Ver [[Errores Comunes]]

Archivos: `backend/app/Http/Controllers/PresupuestoController.php` (pdf/preview gate), `backend/app/Http/Controllers/MercuryInvoiceController.php` (pdf gate), `frontend/pages/presupuestos/{index,[id]}.vue` (ocultar botones), `mini-saas/deploy-backend.sh` (nuevo)

---

## 2026-06-29

- feat: **Vista unificada de Operación con tabs** (`components/OperacionTabs.vue`). Presupuesto y proyecto (1:1) se presentan como una sola Operación con fases **Cotización · Ejecución · Activaciones · Cobranza**. Breadcrumb `Cliente › Operación «nombre»` + barra de tabs montada en ambos detalles. Las fases navegan entre `/presupuestos/{id}` y `/proyectos/{id}` + query `?fase=`
- feat: **Panel Cobranza** (`?fase=cobranza` en presupuesto): consolida métodos de cobro Mercury/Stripe/MercadoPago, enviar invoice y marcar cobrado, reusando los métodos existentes
- feat: **Tab Activaciones** (`?fase=activaciones` en proyecto): vista dedicada a lo ancho, **sacada del aside de Ejecución**
- feat: **Sidebar colapsable con chinche** (`layouts/default.vue`, `NavItem.vue`). Por defecto solo íconos; se expande al hover (overlay, sin empujar contenido) o queda fijo con el chinche (📌, persistido en localStorage). **Proyectos y Activaciones salen del menú** (se acceden por los tabs). Ver [[Frontend#Sidebar colapsable (2026-06-29)]]
- feat: **Filtros de listados persistentes** en localStorage (`composables/useFiltroPersistente.ts`) en presupuestos, proyectos, gastos, clientes, activaciones y staff
- feat: **Descargas de PDF en el listado de presupuestos** — columna de acciones: PDF del presupuesto siempre, y PDF del **invoice Mercury** cuando existe. Las rutas `/presupuestos/{id}/pdf` e `/mercury/invoices/{id}/pdf` validan token por query (públicas)
- feat: **Número de invoice Mercury** persistido (`mercury_invoice_number`, migración 0058) al crear/vincular/refrescar; se muestra en el listado al lado de la descarga **solo si difiere** del número de presupuesto. Descubrimiento: al crear un invoice se le manda `invoiceNumber = numero del presupuesto`, por eso los creados desde la app muestran `BLU-…`; los vinculados muestran la numeración propia de Mercury (`INV-40X`). Ver [[Modulo Mercury Invoicing]]
- ui: listado de presupuestos — número de presupuesto más chico y en una línea, título de proyecto a 2 líneas (`line-clamp-2`) con tooltip nativo, badge de estado alineado (ancho fijo del nombre), todas las celdas `align-top`
- ops: restaurada DB de **producción** desde backup local; reseteadas passwords de `admin@empresa.com` y `cmercurio@blustudioinc.com` a `admin123` para acceso local (el backup trae los users de prod con sus passwords). Whitelisteada IP de egress de dev en el token de Mercury (recordar agregar también la IP de prod)

Archivos: `frontend/components/OperacionTabs.vue` (nuevo), `frontend/components/NavItem.vue`, `frontend/layouts/default.vue`, `frontend/composables/useFiltroPersistente.ts` (nuevo), `frontend/pages/presupuestos/index.vue`, `frontend/pages/presupuestos/[id].vue`, `frontend/pages/proyectos/[id].vue`, `frontend/pages/{clientes,gastos,evidencias,proyectos,staff}/index.vue`, `backend/app/Services/MercuryInvoiceService.php`, `backend/app/Http/Controllers/MercuryInvoiceController.php`, `backend/app/Http/Resources/PresupuestoResource.php`, `backend/app/Models/Presupuesto.php`, `backend/database/migrations/0058_add_mercury_invoice_number_to_presupuestos.php`

---

## 2026-06-17

- docs: **Aclaración — el gasto de un pago de sueldo se imputa al período, no al mes en curso.** Se verificó (no era bug) que el gasto se fecha al **día 1 del mes del período** (`Carbon::create(anio,mes,1)`), nunca a `now()` ni a la fecha de pago. La confusión venía de que tanto el selector "Período" del form como el Dashboard ("Gastos del Período") defaultean al mes actual. Documentado en [[Errores Comunes#El gasto de un pago de sueldo aparece en el mes en curso (no es bug)]] y [[Modulo Personal#Comportamiento de pagos, gasto vinculado y saldo (⚠️ desde migración 0057)]]. Solo cambios de documentación (CLAUDE.md, arquitectura 06/08, memoria)

---

## 2026-06-16

- feat: **Presupuestos — columnas Gasto y Ganancia + fila de totales.** En `/presupuestos`, a la derecha de Total se agregaron **Gasto** (rojo) y **Ganancia** (verde/rojo según signo). Nuevo método `Presupuesto::gastosConvertidos()` suma los gastos del proyecto asociado convertidos a la moneda del presupuesto (misma lógica que `Proyecto::rentabilidad`). `PresupuestoResource` expone `gastos_monto` y `ganancia` (respetan `VER_MONTOS_SALDOS`). Ver [[Backend - API#Presupuestos]] y [[Reglas de Negocio]]
- feat: **Fila de totales al pie del listado de presupuestos**, agrupada **por moneda** (ARS/USD separados, no se mezclan), sumando Total/Gasto/Ganancia sobre **todo el set filtrado** (no solo la página). El controller `index` calcula con `(clone $query)->get()` y los devuelve via `->additional(['totales' => ...])`. Se agregó un slot `#footer` a [[Componentes UI|DataTable.vue]]. Reacciona a todos los filtros (estado, etiqueta, cliente, mes, año, búsqueda) → permite ver "cuánto entró, cuánto gasté, cuánto gané" por período
- feat: **Personal — los pagos de sueldo ahora generan un gasto vinculado.** Decisión de diseño: un pago de personal **ES un gasto**. `EmpleadoController::registrarPago` crea un `Gasto` (tipo OPERATIVO, categoría **"Sueldos"** via `firstOrCreate`, fechado al primer día del período) que es la **única fuente del descuento de saldo** (evita doble conteo); el pago guarda `gasto_id`. Al eliminar el pago se borra el gasto y se devuelve el saldo. Ver [[Modulo Personal#Comportamiento de pagos, gasto vinculado y saldo (⚠️ desde migración 0057)]]
- feat: **Pagos de personal con período mes/año** (`<input type="month">` en el form) separado de la fecha real de pago — el gasto se fecha al período elegido y aparece en `/gastos` y Dashboard de ese mes. El dropdown banco/caja se filtra por moneda (debe coincidir, 422 si no)
- feat: **Nuevos tipos de pago**: además de SUELDO/BONO/AGUINALDO ahora hay **ADELANTO, COMISION, OTRO** (enum alterado en migración 0057). Historial muestra período + 6 badges de color; resumen dinámico por tipo presente
- db: Migración 0057 — `pagos_personal` + `periodo_mes` (tinyint), `periodo_anio` (smallint), `gasto_id` (FK→gastos `nullOnDelete`); enum `tipo` ampliado. Categoría "Sueldos" agregada al `CategoriaGastoSeeder`

Archivos: `backend/app/Models/Presupuesto.php` (gastosConvertidos), `backend/app/Http/Controllers/PresupuestoController.php` (totales + eager-load gastos), `backend/app/Http/Resources/PresupuestoResource.php` (gastos_monto, ganancia), `backend/app/Models/PagoPersonal.php` (campos + relación gasto), `backend/app/Http/Controllers/EmpleadoController.php` (registrarPago/eliminarPago con gasto vinculado), `backend/database/migrations/0057_add_periodo_gasto_to_pagos_personal.php`, `backend/database/seeders/CategoriaGastoSeeder.php`, `frontend/components/ui/DataTable.vue` (slot footer), `frontend/pages/presupuestos/index.vue` (columnas + totales), `frontend/pages/staff/[id].vue` (período, tipos, filtro moneda, historial)

---

## 2026-04-16

- fix: **Envío WhatsApp — mensajes con links correctos.** Se intentó usar `mediaBase64` y `mediaUrl` para enviar archivos como adjuntos nativos de WhatsApp, pero el worker del bot no procesa media (solo texto). Se revirtió a mensajes de texto con links:
  - **ARCHIVO:** `"Hola {nombre}, te envío {titulo}\n\n{publicUrl}"`
  - **ENLACE:** `"Hola {nombre}, te comparto {titulo}\n\n{urlDirecta}"` (con `https://` asegurado). Antes usaba el redirect via public token; ahora manda la URL directa del enlace
- fix: **APP_URL corregida a `http://localhost:8823`** — antes era `http://localhost` (sin puerto), generaba URLs rotas en los links compartidos por WhatsApp. El problema estaba en 3 capas: (1) `docker-compose.yml` hardcodeaba `APP_URL: http://localhost` overrideando el `.env` de Laravel; (2) PHP-FPM no hereda env vars del container igual que CLI; (3) Nginx pasaba `Host: $host` que no incluye el puerto
- infra: `docker-compose.yml` ahora usa `APP_URL: ${APP_URL:-http://localhost:8823}` (configurable desde `.env` de compose con fallback correcto)
- infra: `nginx/default.conf` cambiado `proxy_set_header Host $host` → `$http_host` en la location `/api/` para que Laravel vea el puerto en `url()`. Ver [[Stack e Infraestructura#Nginx - Ruteo]]
- feat: **Open Graph preview con logo Blu en links compartidos por WhatsApp.** `servirArchivoPublico` ahora detecta crawlers por User-Agent (WhatsApp, Facebook, Telegram, Slack, LinkedIn) y devuelve HTML con `og:title`, `og:image` (logo Blu) y `og:description` en vez del archivo. Usuarios reales siguen recibiendo el archivo/redirect normal. Ver [[Modulo WhatsApp Inbox#Compartir adjuntos por WhatsApp]]
- discovery: **Deploy backend con `docker cp` no basta si PHP-FPM tiene opcache activo.** `optimize:clear` limpia caches de Laravel pero no el opcache de PHP. Hay que reiniciar el container con `docker restart minisaas-backend`. Ver [[Errores Comunes]] y [[Stack e Infraestructura#Comandos de deploy]]
- discovery: **El bot de WhatsApp (Inbox API) no soporta media** — acepta `mediaBase64`/`mediaUrl`/`mimetype`/`filename` en el request y responde `success:true`, pero el worker solo procesa el campo `mensaje`. Para enviar archivos como adjuntos nativos de WhatsApp, hace falta arreglar el worker del bot. Ver [[Modulo WhatsApp Inbox#Servicio externo (Inbox API) — referencia completa]]

Archivos: `backend/app/Http/Controllers/ProyectoController.php` (enviarAdjuntoWhatsApp simplificado + servirArchivoPublico con OG tags + import Log), `docker-compose.yml` (APP_URL configurable), `nginx/default.conf` ($http_host)

---

## 2026-04-15

- feat: **Teléfonos múltiples por cliente** — un cliente puede tener N teléfonos con código de área, nombre de contacto y tipo (`WHATSAPP` default, `LLAMADA`, `FIJO`). Card "Teléfonos" en el aside de `pages/clientes/[id].vue`, debajo del card Estado (no en el modal de edición). Ver [[Base de Datos#cliente_telefonos]] y [[Backend - API#Clientes]]
- db: Migración 0053 — crea `cliente_telefonos` (`cliente_id`, `codigo_area`, `numero`, `etiqueta`)
- db: Migración 0054 — rename `etiqueta` → `nombre` y agrega `tipo` (string, default `WHATSAPP`). La migración 0053 quedó con forma vieja porque se iteró en la misma sesión
- feat: Endpoints dedicados **fuera** del `update` del cliente — `POST /api/clientes/{id}/telefonos` y `DELETE /api/clientes/{id}/telefonos/{telefono}`. Se deliberó la alternativa de sincronizar desde el body del update y se descartó: más simple, menos acoplamiento, y permite tocar teléfonos sin editar el cliente. Las rutas están registradas **antes** de `apiResource('clientes', …)` para no colisionar con `{cliente}`. Ver [[Errores Comunes#Rutas especificas despues de apiResource colisionan con id]]
- feat: `ClienteTelefono` con `$touches = ['cliente']` para mantener el `updated_at` del cliente fresco al tocar teléfonos. `ClienteController::index/show` eager-loadea `telefonos`, `ClienteResource` siempre los expone
- ux: Primera iteración puso el card dentro del bloque Información y también un form en el modal de edición. Se movió por feedback: **"debería aparecer como un módulo más, similar al de adjuntos en proyectos"** y después **"ponelo en el aside, abajo del de estado"**. Patrón final replica el de "Enlaces y Archivos" de proyecto — header + botón "+ Agregar" que toggleaea un mini-form, lista con ícono por tipo, X para borrar visible en hover

**Integración WhatsApp Inbox API + compartir adjuntos de proyecto (misma fecha):**

- feat: **Nueva integración WhatsApp via Inbox API externa** — un servicio tipo cola (worker + SQLite) al que se le postea `{ token, telefono, mensaje }` y un cliente de WhatsApp Web se encarga del envío cada 10s con reintentos. Ver [[Modulo WhatsApp Inbox]]
- db: Migración 0055 — `configuracion.inbox_api_url` e `inbox_api_token`. Configurables desde el card "Integración WhatsApp (Inbox API)" en `pages/configuracion/index.vue`. Mismo patrón que Mercury/MP/Stripe: el token nunca se devuelve al frontend, solo flag `inbox_tiene_token`
- feat: **Compartir adjuntos de proyecto por WhatsApp** — botón verde (`lucide:message-circle`) en hover junto a cada adjunto del card "Enlaces y Archivos" en `pages/proyectos/[id].vue`. Visible solo si el cliente tiene al menos un teléfono con `tipo=WHATSAPP`. Modal con checkboxes listando los contactos WhatsApp del cliente (todos pre-seleccionados)
- db: Migración 0056 — `proyecto_adjuntos.public_token` (varchar(80), unique, nullable). Método `ProyectoAdjunto::asegurarPublicToken()` genera `bin2hex(random_bytes(32))` (64 chars hex) on-demand y lo persiste. La seguridad del link compartido se basa únicamente en la imposibilidad de adivinar el token
- feat: **Ruta pública fuera de auth** — `GET /api/archivos/publico/{token}` → `ProyectoController::servirArchivoPublico`. Si `tipo=ENLACE` hace `redirect()->away()`, si `tipo=ARCHIVO` devuelve el file con `Content-Disposition: inline`. Sin expiración, sin rate limiting — si hay que invalidar un link compartido, `UPDATE proyecto_adjuntos SET public_token = NULL WHERE id = X`
- feat: **Endpoint de envío** — `POST /api/proyectos/{proyecto}/adjuntos/{adjunto}/enviar-whatsapp` con body `{ telefono_ids[] }`. Valida pertenencia al cliente del proyecto, genera/reutiliza el `public_token`, arma el mensaje `"Hola {nombre}, te ha enviado el archivo {titulo} - {url}"`, normaliza el número con `preg_replace('/\D+/', '', codigo_area.numero)` y postea por cada contacto al `inbox_api_url` con `Http::timeout(15)`. Errores individuales no rompen el loop — se acumulan en `fallidos[]`. Response: `{ url, enviados[], fallidos[] }` — el frontend muestra toast con contadores
- infra: `ProyectoController::show` ahora eager-loadea `presupuesto.cliente.telefonos` para que el frontend tenga los contactos WhatsApp disponibles sin request extra

Archivos: migraciones 0053/0054/0055/0056, `app/Models/ClienteTelefono.php` (nuevo), `app/Models/Cliente.php` (relación), `app/Models/ProyectoAdjunto.php` (método `asegurarPublicToken`), `app/Models/Configuracion.php` (fillable), `app/Http/Controllers/ClienteController.php` (store/update/show eager-load + endpoints agregarTelefono/eliminarTelefono), `app/Http/Controllers/ProyectoController.php` (eager-load telefonos, endpoints `enviarAdjuntoWhatsApp` y `servirArchivoPublico`, imports de `Http`/`Configuracion`/`ClienteTelefono`), `app/Http/Controllers/ConfiguracionController.php` (hide + flag `inbox_tiene_token`, validación URL, guard contra token vacío), `app/Http/Resources/ClienteResource.php` (expone telefonos), `routes/api.php` (rutas `/clientes/{id}/telefonos`, `/proyectos/{id}/adjuntos/{adj}/enviar-whatsapp`, `/archivos/publico/{token}` **fuera de auth**), `frontend/pages/clientes/[id].vue` (card Teléfonos en aside + CRUD inline), `frontend/pages/clientes/nuevo.vue` (revertido — no lleva teléfonos en el form de creación), `frontend/pages/configuracion/index.vue` (card Integración WhatsApp), `frontend/pages/proyectos/[id].vue` (botón WhatsApp + modal contactos + computed `whatsappContactos`)

---

## 2026-04-14

- feat: **Integración Mercury Invoicing API completa** — facturación electrónica USD desde el ERP usando la API de Accounts Receivable de Mercury. Cubre los 3 caminos: listado, creación desde presupuesto, y embebido del link de pago en el email. Ver [[Modulo Mercury Invoicing]] y [[Medios de Pago#Mercury Invoicing API (desde 2026-04-14)]]
- db: Migración 0049 — `clientes.mercury_customer_id` (uuid del customer en Mercury, persistido tras find-or-create)
- db: Migración 0050 — `presupuestos.mercury_invoice_id` / `mercury_invoice_slug` / `mercury_invoice_status` / `mercury_invoice_tasa_cambio` / `mercury_invoice_created_at` (referencia + auditoría del invoice creado)
- db: Migración 0051 — `presupuestos.mercadopago_payment_url` y `presupuestos.stripe_payment_url` (antes los links se generaban on-the-fly y eran ephemeral; ahora se persisten para reusarlos en el modal de envío)
- feat (Fase 1 — backend foundations): nuevo `app/Services/MercuryInvoiceService.php` envuelve toda la lógica HTTP. Nuevo `MercuryInvoiceController` con 7 endpoints. Ver [[Backend - API#Mercury Invoicing — endpoints (desde 2026-04-14)]]
- feat (Fase 2 — listado): `/mercury` ahora tiene **tabs** "Cuenta" e "Invoices". Tab Invoices lazy-load, tabla cursor-based con status badges
- feat (Fase 3 — crear desde presupuesto): botón "Crear invoice Mercury" en `/presupuestos/[id]` cuando `!mercury_invoice_id`. Modal con conversión ARS→USD
- feat (Fase 4 — payment links en email): modal "Enviar invoice por email" con sección "Métodos de pago a incluir" (Mercury/Stripe/MP)
- feat: **Vincular invoice Mercury existente** y **adjuntar PDF Mercury al email**
- ux: **Reorganización del action bar de presupuestos** — máximo 2 CTAs + dropdown "Más"
- feat: **Tracking de usuario creador en activaciones e hitos** — `created_by` nullable (migración 0052)

---

## 2026-04-13

- feat: **Envío de invoice por email** desde detalle de presupuesto
- infra: Configurado SMTP `box.lio.red:465` SSL
- refactor: **Migración DomPDF → Spatie Browsershot + Chromium headless** para PDFs de presupuesto

---

## 2026-04-08

- feat: Filtros de mes, año y cliente en listados de presupuestos, proyectos y activaciones

---

## 2026-03-30

- feat: Descripcion IA de activaciones escalada segun cantidad de hitos
- fix: Actualizar dominio `blu.inc` -> `blustudioinc.com` en invoice

---

## 2026-03-29

- feat: Campo `realizado` en gastos para indicar si el pago al acreedor fue cancelado
- feat: Checkbox read-only de gastos realizados en listado de presupuestos

---

## 2026-03-27

- fix: PDF presupuesto — corregir scroll en html2canvas
- ui: Remover boton eliminar del listado de activaciones

---

## 2026-03-25

- feat: Eliminar activaciones requiere credenciales admin
- feat: Mostrar estado del proyecto en listado de presupuestos

---

## 2026-03-22

- feat: IVA en gastos (0 / 10.5 / 21 / 27%)
- feat: Etiquetas de colores visibles en listado de proyectos
- feat: Orden de presupuestos y proyectos por `updated_at` DESC con touch automatico
- feat: Dashboard mejorado con 6 KPIs, tooltips, filtro por periodo
- feat: Edicion de gastos con restriccion por estado de presupuesto
- feat: Modal de detalle de gasto en vista de proyecto
- feat: Boton eliminar gastos desde listado y vista de proyecto

---

## 2026-03-21

- feat: PDF de activaciones sobre hoja membretada Blu con TCPDF+FPDI

---

## Ver tambien

- [[Backend - API]] - Endpoints modificados
- [[Reglas de Negocio]] - Reglas de dominio agregadas
- [[Errores Comunes]] - Bugs descubiertos y resueltos
- [[memoria]] - Convenciones y feedback acumulado
