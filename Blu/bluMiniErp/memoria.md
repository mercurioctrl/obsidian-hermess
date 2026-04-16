# Memoria del Proyecto

Consolidacion de la memoria persistente de Claude para este proyecto. Organizada por tipo.

Ultima sincronizacion: 2026-04-16 (iteración: WhatsApp links fix, OG preview, APP_URL fix, opcache gotcha)

---

## Feedback (patrones tecnicos)

Lecciones aprendidas y correcciones del usuario. Estas guian el comportamiento de desarrollo.

### Docker
- **Local vs servidor:** En local, docker corre desde `mini-saas/`. En servidor Ubuntu necesita `sudo`. `git pull` puede fallar por backups con permisos root
- **Frontend rebuild:** Siempre usar `--no-cache` y reiniciar nginx despues para resolver nueva IP del container. Ver [[Stack e Infraestructura#Comandos de deploy]]
- **APP_URL en docker-compose.yml (2026-04-16):** La variable `APP_URL` hardcodeada en `docker-compose.yml` overrideaba el `.env` de Laravel. Ahora usa `${APP_URL:-http://localhost:8823}` (configurable). PHP-FPM lee de `.env` de Laravel, no de env vars del container — ambos deben tener el puerto
- **Nginx $http_host (2026-04-16):** La location `/api/` pasa `proxy_set_header Host $http_host` (con puerto) en vez de `$host`. Sin esto, `url()` de Laravel genera URLs sin el puerto 8823
- **Deploy + opcache (2026-04-16):** `docker cp` + `optimize:clear` no limpia el opcache de PHP-FPM. Siempre `docker restart minisaas-backend` después de copiar archivos PHP

### PHP / Laravel
- **env() vs config():** Nunca usar `env()` directo en controllers. PHP-FPM no hereda env vars del container. Registrar en `config/services.php` y leer con `config()`. Ver [[Errores Comunes#env no lee variables de entorno del container en PHP-FPM]]
- **Gasto.categoria:** Es string plano, NO relacion Eloquent. Nunca usar `with('categoria')`
- **RolUsuario:** Es enum casteado. Comparar con `RolUsuario::ADMIN`, no con string ni `->value`. Ver [[Backend - Modelos#Usuario]]
- **Rutas apiResource:** Las rutas especificas (`/gastos/categorias`) deben registrarse ANTES del `apiResource`. Ver [[Errores Comunes#Rutas especificas despues de apiResource colisionan con id]]
- **Laravel 11 sin `config/mail.php`:** El skeleton de este repo no incluye `config/mail.php`. Hay que crearlo a mano para que el Mail facade funcione. Ver [[Errores Comunes#Laravel 11 sin config mail php por default]] y [[Stack e Infraestructura#Mail SMTP]]

### Frontend / Vue
- **Modal:** Siempre usar `v-model`, nunca `v-if` + `@close`. Ver [[Frontend#Componentes UI]]
- **useApi.delete con body:** Usar `{ data: {...} }`, no `{ body: {...} }`
- **useApi errores:** Los catch reciben Error estandar. Usar `e.message`, no `e?.data?.message`

### Action bar — jerarquía visual
**Patrón canónico (2026-04-14, por feedback explícito del usuario):** En pantallas de detalle (presupuesto, proyecto, etc.), el action bar tiene como máximo `[Editar] [⋯ Más] | [CTA outline] [CTA primary]` — máximo 2 CTAs visibles + 1 dropdown único "Más" agrupado por sección con headers tipográficos. Ver [[Frontend#Action bar de pantallas de detalle]].

**Reglas:**
- **Defaultear** features nuevas al menú "Más", no a botones visibles. Solo ascender a CTA si es transición de estado del flujo principal.
- **Máximo 2 CTAs primarios** simultáneos. Si hay 3 transiciones posibles, la menos común va al menú.
- Usar headers de sección dentro del dropdown cuando hay 4+ items para dar jerarquía visual.
- En mobile, ocultar labels de Editar/Más con `hidden sm:inline`.

**Why del usuario:** Llegó a haber 9-10 botones visibles en el detalle de presupuesto y se volvió "difícil de usar, demasiado a la vista y confuso". La consolidación bajo un menú único con headers por sección hace las acciones secundarias descubribles sin abrumar la vista.

**Anti-patrones:** spawn-ear botones nuevos por cada feature, múltiples dropdowns coexistiendo, esconder transiciones de estado en el menú, botones del mismo color/peso visual que los CTAs primarios para acciones secundarias.

### Convenciones de API

#### Query params sin caracteres no-ASCII
**Regla:** En query params (URL del API), usar siempre nombres ASCII. Ejemplo concreto: filtro de año va como `?anio=2026`, no `?año=2026`.

**Por que:** Aunque PHP moderno soporta keys UTF-8 en `$_GET`, el encoding URL (`a%C3%B1o`) introduce un punto de fragilidad innecesario: depende de que cada cliente HTTP encode bien, que el servidor decode bien, y que cualquier proxy/log intermedio no rompa los bytes. Es trivial evitarlo usando ASCII.

**Como aplicar:**
- En el state del frontend podes mantener nombres descriptivos en español (`filtroAño`, `filtroMes`) para legibilidad
- Al serializar a `URLSearchParams`, traducir a ASCII: `params.set('anio', String(filtroAño.value))`
- En el backend, leer con `$request->anio` / `$request->filled('anio')`
- Aplica tambien a otros campos potenciales: usar `descripcion` no `descripción`, etc.

---

## Proyecto (features y decisiones)

### Infraestructura
- **Docker entrypoint:** `docker-entrypoint.sh` recrea `storage/framework` dirs en cada arranque. Resuelve "valid cache path" error. Ver [[Stack e Infraestructura#Entrypoint del backend]]
- **Storage uploads:** Volumen `uploads_storage` + symlink en Dockerfile. PDFs en `pdf_storage`. Ver [[Stack e Infraestructura#Volumenes Docker]]
- **Backup/Restore:** Scripts bash `backup.sh` y `restore.sh` para backup completo (DB, PDFs, uploads, .env)

### Listados - filtros de fecha y cliente
**Convención (2026-04-08):** Los listados de **presupuestos**, **proyectos** y **activaciones** soportan filtros de mes, año y cliente. Default = mes/año actual; cada filtro tiene opción "Todos" para deshabilitarlo.

**Por que:** El usuario trabaja por períodos mensuales. Sin default al mes actual los listados se llenaban de histórico irrelevante.

**Patrón:**
- Backend usa `whereMonth(...)` + `whereYear(...)` con `$request->filled(...)`
- Param wire es `anio` (no `año`) — ver sección de query params ASCII arriba
- Frontend: dos dropdowns separados de mes (1-12) y año (rango actual+1 hasta -5)
- Cargar lista de clientes con `api.get('/clientes?activo=true&per_page=200')`, normalizar `cli?.data ?? cli ?? []`
- Watch sobre cada filtro → refetch

**Columna de fecha por entidad** (importante para futuros reportes/dashboards/exports):
- **Presupuestos** → `presupuestos.fecha` (PresupuestoController::index)
- **Proyectos** → `proyectos.fecha_inicio` (ProyectoController::index)
- **Activaciones / pruebas_ejecucion** → `pruebas_ejecucion.periodo_desde` (PruebaEjecucionController::index)

Ojo: para activaciones se filtra por `periodo_desde`, así que activaciones sin período no aparecen cuando hay filtro de mes/año.

**Cliente en activaciones:** la cadena de relaciones es `PruebaEjecucion → proyecto → presupuesto.cliente_id`. El controller usa `whereHas('proyecto.presupuesto', fn($q) => $q->where('cliente_id', ...))`.

### Presupuestos
- **Edicion:** Editables en cualquier estado excepto COBRADO/FACTURADO. Moneda editable. Movimientos CC se actualizan al guardar. Ver [[Reglas de Negocio#Presupuestos - Flujo de estados]]
- **Suscripciones:** Renovacion automatica mensual. Campos: `es_suscripcion`, `suscripcion_inicio`, `suscripcion_meses`, `suscripcion_frecuencia`. Scheduler `monthlyOn(1,'03:00')`
- **Etiquetas:** Etiquetas de colores asignables desde presupuesto y proyecto. Pivot migraciones 0044-0045. Filtrable en ambos listados. Ver [[Reglas de Negocio#Etiquetas de Presupuestos]]
- **Dominio invoice:** PDF de presupuesto usa `blustudioinc.com` (cambio desde `blu.inc` el 2026-03-30)

### Gastos
- **Cotizacion e IVA:** Cada gasto registra tasa_cambio (BCRA) e IVA (0/10.5/21/27%). Monto final = subtotal + IVA. Migracion 0047. Ver [[Reglas de Negocio#IVA en Gastos]]
- **Edicion:** Editables desde listado y proyecto. Proteccion por estado presupuesto COBRADO/FACTURADO. Campo `editable` en GastoResource. Ver [[Reglas de Negocio#Gastos - Proteccion por estado de presupuesto]]
- **Campo realizado:** Indica si el pago al acreedor fue cancelado. Toggle PATCH, desmarcar requiere admin. Migracion 0048. Ver [[Reglas de Negocio#Gastos - Campo realizado]]

### Proyectos
- **Adjuntos:** Enlaces y archivos adjuntos por proyecto. Upload a `storage/public`. Max 10MB. Ver [[Backend - API#Proyectos]]
- **Jira multi-board:** Multiples tableros Jira por proyecto. Tabla `proyecto_jira_boards`. Las columnas `jira_project_key/name` ya NO existen en proyectos
- **Orden por actividad:** Presupuestos y proyectos ordenados por `updated_at` DESC. Touch automatico al modificar hijos

### Activaciones
- **Copiar:** Copiar activaciones entre proyectos del mismo cliente. Periodo opcional. Estructura copiada, datos de ejecucion vacios
- **Eliminacion:** Requiere credenciales admin. Modal email+password. Backend valida rol ADMIN
- **PDFs activaciones:** TCPDF+FPDI sobre membretada Blu (portrait A4). Plantilla en `storage/app/templates/membretada.pdf`
- **PDFs presupuestos (2026-04-13):** Migrados de DomPDF a **Spatie Browsershot + Chromium headless**. Entry point único `PdfService::renderPresupuestoPdf()` — lo usan tanto `/api/presupuestos/{id}/pdf` como `PresupuestoInvoiceMail`. Blade canónico: `pdf/presupuesto-preview.blade.php` (el mismo que renderiza `/preview` HTML). Dockerfile instala chromium + libs + Node 20 + puppeteer global. Ver [[Stack e Infraestructura#Browsershot - renderizado de PDFs de presupuesto]]
- **DeepSeek IA:** Descripciones automaticas con DeepSeek API. Config en `services.php`. Campos `descripcion_ia` y `descripcion_ia_cant_hitos`. Frontend muestra "Desactualizada" si cambia la cantidad de hitos
- **DeepSeek longitud escalada (2026-03-30):** Longitud variable segun cantidad de hitos — ≤5 hitos: 2-3 oraciones / `max_tokens: 300`; 6-15 hitos: 3-5 oraciones / `max_tokens: 500`; +15 hitos: 5-7 oraciones / `max_tokens: 700`. Prompt dice "cubriendo todas las actividades listadas" (NO "breve") para evitar omisiones del modelo
- **Tracking de creador (2026-04-14):** Nueva columna `created_by` (nullable) en `pruebas_ejecucion` y `hitos_ejecucion` (migración 0052). El detalle de activación muestra "Creada por X" + columna "Creado por" en la tabla de hitos. Los PDFs/preview no exponen el dato. `update()` reconcilia hitos por `id` en lugar de borrar+recrear, preservando el `created_by` original de los existentes. Los registros previos a la migración quedan en `NULL` (aparecen como "—") y pueden backfillearse con un `UPDATE` manual si hace falta. Ver [[changelog#2026-04-14]]

### Integraciones
- **MercadoPago:** Access token + banco vinculado. Movimientos via `/v1/payments/search`. Sync saldo manual. Conversion USD->ARS. Limitaciones API (balance 403, movements requiere permisos especiales). **Desde 2026-04-14:** `init_point` se persiste en `presupuestos.mercadopago_payment_url`. Ver [[Medios de Pago#MercadoPago]]
- **Stripe:** Secret key + banco vinculado. Montos en centavos. Checkout Sessions. Conversion moneda. **Desde 2026-04-14:** `url` del Checkout Session se persiste en `presupuestos.stripe_payment_url`. Ver [[Medios de Pago#Stripe]]
- **Mercury Invoicing (2026-04-14):** API de Accounts Receivable de Mercury para facturar USD. Solo cuentas con plan que incluye Invoicing. Servicio único `MercuryInvoiceService`. 8 endpoints en `MercuryInvoiceController` (incluye `/link` para vincular invoices existentes y filtro `?status=` en `index`). Mercury solo opera en USD — para presupuestos ARS hay conversion ARS→USD con tasa BCRA persistida. **IP whitelist por token** (las IPs egress de dev y prod son distintas). PDF descargable via `/ar/invoices/{id}/pdf` (no documentado pero existe). URLs derivadas del slug: `/invoice/{slug}` (vista hosteada) y `/pay/{slug}` (landing de pago). El modal de envío permite **vincular invoices Mercury existentes** (picker filtrado por Unpaid con warning de cliente mismatch) y **adjuntar el PDF de Mercury** al email como segundo attachment (`PresupuestoInvoiceMail` recibe 3er arg `bool $attachMercuryPdf`, fallback con warning si la descarga falla). Ver [[Modulo Mercury Invoicing]] y [[Medios de Pago#Mercury Invoicing API (desde 2026-04-14)]]
- **Conversion monedas:** Dolar oficial BCRA venta (dolarapi.com). USD->ARS multiplica, ARS->USD divide

### Mail SMTP y envío de invoices
**Añadido (2026-04-13):** El proyecto envía mails transaccionales vía SMTP de BluStudio. Config completa en [[Stack e Infraestructura#Mail SMTP]].

**Contexto de la decisión:**
- Transporte: SMTP directo a `box.lio.red:465` SSL, remitente `payments@blustudioinc.com`
- BCC automático a la misma cuenta via `MAIL_PAYMENTS_BCC` → el equipo de pagos tiene copia de todo
- `MAIL_PASSWORD` queda vacía en el `.env` commiteado — cada entorno la setea a mano. Decisión explícita del usuario para no trackear la password
- Por ahora solo se usa para **invoices de presupuestos** (endpoint `POST /api/presupuestos/{id}/enviar-invoice`). El día de mañana habrá otras cuentas para otros tipos de mails — cuando lleguen, agregar un segundo mailer en `config/mail.php` (`mailers.notifications`, etc.) en lugar de pisar el SMTP de pagos

**"Se acuerda el mail":** cuando el usuario envía un invoice con un email, el endpoint actualiza `cliente.email` si difiere. La próxima vez el modal viene precargado con ese valor. La persistencia vive en la ficha del cliente, no en una tabla aparte de historial.

**Patrón canónico de Mailable con PDF:** Ver `app/Mail/PresupuestoInvoiceMail.php`. Delega la generación del PDF al servicio central (`app(PdfService::class)->renderPresupuestoPdf($presupuesto)`) y adjunta los bytes **in-memory** — no se toca filesystem. Desde el 2026-04-13 el PDF se renderiza con Browsershot/Chromium en lugar de DomPDF, pero la interfaz del Mailable no cambió. Reutilizar este patrón para cualquier Mailable futuro con adjunto (un servicio dedicado que devuelve bytes, el Mailable solo adjunta).

**Payment links en el email (2026-04-14):** El `PresupuestoInvoiceMail` ahora recibe un segundo argumento `$paymentLinks` (array `mercury|stripe|mercadopago` → URL). Los URLs vienen del modal de envío (sección "Métodos de pago a incluir") y se renderizan como botones full-width en el body del email, cada uno con su color de marca. El controller (`enviarInvoice`) los recibe en el body del POST como flags opcionales (`mercury_pay_url`, `stripe_payment_url`, `mercadopago_payment_url`). Para que el modal del frontend pueda pre-marcar los checkboxes, los links se persisten en el presupuesto cuando se generan (no son ephemeral). Ver [[Modulo Mercury Invoicing]].

**Fix del `\Log::error` (2026-04-13):** El catch del `enviarInvoice` usaba `\Log::error(...)` sin FQN, que en Laravel 11 no resuelve (no hay alias `\Log` global). Cuando `Mail::to(...)` lanzaba un error real, el propio catch crasheaba con "Class Log not found", enmascarando la causa. Siempre usar `\Illuminate\Support\Facades\Log::error(...)` o agregar `use Illuminate\Support\Facades\Log;` al tope. Ver [[Errores Comunes#Log facade sin FQN completo falla en Laravel 11]].

### Clientes — Teléfonos múltiples (2026-04-15)
Un cliente puede tener N teléfonos con `nombre` de contacto, `codigo_area`, `numero` y `tipo` (`WHATSAPP` default, `LLAMADA`, `FIJO`). Migraciones 0053/0054, modelo `ClienteTelefono` con `$touches = ['cliente']`. Ver [[Base de Datos#cliente_telefonos]] y [[Backend - Modelos#ClienteTelefono]].

**Decisiones de diseño:**
- **Endpoints dedicados, no sync desde update del cliente.** Hay un `POST /api/clientes/{id}/telefonos` y `DELETE /api/clientes/{id}/telefonos/{telefono}`, registrados ANTES del `apiResource('clientes', …)` para no colisionar con `{cliente}`. Descartamos la alternativa de aceptar el array en el body del update del cliente porque era más complejo (sync/reconcile por id), acoplaba cambios, y forzaba editar el cliente entero para agregar un teléfono.
- **UI en el aside, no en el modal de edición.** Primera iteración puso el card dentro del bloque Información + un form en el modal de edición. Por feedback del usuario en la misma sesión (*"debería aparecer como un módulo más, similar al de adjuntos en proyectos"* y después *"ponelo en el aside, abajo del de estado"*) terminó replicando el patrón visual de "Enlaces y Archivos" de proyecto, viviendo en la columna derecha de `pages/clientes/[id].vue`.
- **`nuevo.vue` NO lleva el form de teléfonos.** Se carga después desde el detalle. Mantener el form de creación simple.

**Caso de uso principal:** enviar adjuntos de proyecto al cliente por WhatsApp. Ver sección siguiente.

### WhatsApp Inbox API y compartir adjuntos (2026-04-15)
Integración con un servicio externo tipo cola para enviar WhatsApp. Ver [[Modulo WhatsApp Inbox]] para la documentación completa.

**Contexto:**
- El usuario tiene su propia infraestructura — un servicio que corre detrás de ngrok, con un cliente de WhatsApp Web activo y una SQLite como cola. Se le postea `{ token, telefono, mensaje }`, se encola, y un worker lo envía cada 10s con reintentos hasta 5 veces. NO es la API oficial de WhatsApp Business.
- La URL del ngrok **puede cambiar** — por eso `inbox_api_url` es configurable desde el UI (`configuracion.inbox_api_url`, migración 0055). El token también se edita desde el UI y nunca viaja al frontend en el GET.

**Flow del caso de uso "compartir adjunto por WhatsApp":**
1. En el card "Enlaces y Archivos" de un proyecto, cada adjunto muestra en hover un botón verde (`lucide:message-circle`) **solo si el cliente tiene algún teléfono con `tipo=WHATSAPP`**. El computed `whatsappContactos` filtra desde `proyecto.cliente.telefonos` — requiere que `ProyectoController::show` eager-loadee `presupuesto.cliente.telefonos` (está en el controller).
2. Modal con checkboxes, todos pre-seleccionados.
3. Backend genera `bin2hex(random_bytes(32))` (64 chars hex) si el adjunto no tiene `public_token`, lo persiste (migración 0056), y arma la URL `/api/archivos/publico/{token}`.
4. Para cada teléfono, normaliza el número con `preg_replace('/\D+/', '', codigo_area.numero)` y postea al Inbox API con mensaje `"Hola {nombre}, te ha enviado el archivo {titulo} - {url}"`. Errores individuales se acumulan en `fallidos[]` — no rompen el loop.
5. Toast con contadores.

**La ruta pública `/api/archivos/publico/{token}` está fuera de `auth:sanctum`.** La seguridad se basa **únicamente** en la imposibilidad de adivinar el token. No hay expiración, no hay rate limiting, no hay firma. Para invalidar un link compartido, `UPDATE proyecto_adjuntos SET public_token = NULL WHERE id = X`. Si esto genera un problema de abuso, agregar throttling al middleware o agregar `public_token_expires_at`.

**Gotchas / próximos pasos:**
- El mensaje incluye el link en claro. Asumir que puede ser reenviado en WhatsApp — si el archivo es sensible, el usuario tiene que borrarlo del proyecto o invalidar el token.
- El mismo patrón (config de URL/token + `Http::post` al Inbox API) se puede reutilizar para otros flows de envío (ej: invoices, presupuestos, activaciones). Cuando llegue, extraer la llamada HTTP a un servicio dedicado (`WhatsAppService::enviar($telefono, $mensaje)`) en vez de duplicar.
- Si el token de Inbox API cambia, el `update` de `ConfiguracionController` unset-ea `inbox_api_token` cuando viene vacío — así se puede editar solo la URL sin reingresar el token. Mismo patrón que Mercury/MP/Stripe.

### Otros
- **Busqueda global:** Buscador en topbar. GET `/api/busqueda?q=`. Busca en clientes, presupuestos, proyectos, gastos. Max 5 por tipo. Ver [[Frontend#Busqueda global]]
- **Bancos y Cajas:** Transferencias, retiros, historial movimientos. Tabla `movimientos_banco_caja`. Proteccion admin para eliminar/ajustar saldo. Ver [[Reglas de Negocio#Bancos y Cajas - Saldo automatico]]
- **Dashboard multimoneda:** 6 KPI cards con tooltips info. Cobros MP/Stripe multimoneda
- **Freelance:** Tipo contrato FREELANCE agregado a empleados (migracion 0028). Ver [[Modulo Personal#Tipo de contrato]]

---

## Ver tambien

- [[changelog|Changelog]] - Registro de commits recientes
- [[Reglas de Negocio]] - Reglas de dominio
- [[Errores Comunes]] - Bugs conocidos
- [[Backend - API]] - Endpoints del sistema
