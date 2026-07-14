# Changelog

Registro de lo trabajado en el proyecto, agrupado por fecha.

---

## 2026-07-14

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
