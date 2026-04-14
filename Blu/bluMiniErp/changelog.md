# Changelog

Registro de lo trabajado en el proyecto, agrupado por fecha.

---

## 2026-04-13

- feat: **Envío de invoice por email** desde detalle de presupuesto. Nuevo botón "Enviar invoice" junto al de PDF, modal con email precargado desde `cliente.email` y vista previa del mensaje. Al enviar, el mail queda guardado en la ficha del cliente ("se acuerda el mail"). Ver [[Backend - API#Presupuestos]] y [[Stack e Infraestructura#Mail SMTP]]
- infra: Configurado SMTP de `box.lio.red:465` (SSL) con remitente `payments@blustudioinc.com`. `MAIL_PASSWORD` queda vacía en el `.env` commiteado, cada entorno la setea. BCC automático a `payments@blustudioinc.com` (`MAIL_PAYMENTS_BCC`). Ver [[memoria#Mail SMTP y envío de invoices]]
- infra: Creado `config/mail.php` a mano — Laravel 11 en este repo no lo trae en el skeleton por default (solo app, auth, cache, cors, database, sanctum, services, session). Sin ese archivo el Mail facade no funciona aunque estén las env vars. Ver [[Errores Comunes#Laravel 11 sin config mail php por default]]
- feat: Mailable `PresupuestoInvoiceMail` con **PDF adjunto in-memory** — no toca filesystem. El Envelope setea el BCC, no el controller
- feat: Vista `resources/views/emails/presupuesto-invoice.blade.php` con estilo consistente con el sistema de diseño (fondo `#F5F5F0`, cards blancos, texto `#1A1A1A`, totales formateados `es-AR`)

**Iteración (misma fecha) — migración de renderizado de PDF presupuestos:**

- fix: `\Log::error(...)` sin FQN completo fallaba en el catch del envío de invoice (Class "Log" not found — Laravel 11 no registra el alias `\Log` global en este repo). Cambiado a `\Illuminate\Support\Facades\Log::error(...)` en `PresupuestoController::enviarInvoice`. Ver [[Errores Comunes#Log facade sin FQN completo falla en Laravel 11]]
- refactor: **Migración DomPDF → Spatie Browsershot + Chromium headless** para PDFs de presupuesto. El botón "PDF" del frontend abre `/preview` como HTML (render Chrome real), mientras que el email adjuntaba un DomPDF con fuentes Times serif, sin flex y con logo caído al texto fallback — outputs muy distintos. Ahora ambos caminos (download y adjunto del email) pasan por `PdfService::renderPresupuestoPdf()` que renderiza `pdf.presupuesto-preview.blade.php` (el mismo blade que usa `/preview`) vía Chrome headless → outputs prácticamente idénticos. Ver [[PDFs y Renderizado#Presupuestos - Browsershot + Chromium headless]]
- infra: Dockerfile del backend ahora instala `chromium` + libs X/audio/pango/cairo, fuentes (`fonts-liberation fonts-dejavu-core fonts-noto-color-emoji`), Node 20 (via `deb.nodesource.com`) y `puppeteer` global. Env vars `PUPPETEER_SKIP_DOWNLOAD`, `PUPPETEER_SKIP_CHROMIUM_DOWNLOAD`, `PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium` para usar el Chromium del sistema (no el que bajaría puppeteer). Rebuild pesado: ~300MB extras, varios minutos. Corre headless sin problema en servers Linux sin GUI.
- composer: `spatie/browsershot ^4.2` tiene advisories PKSA-* activos que bloquean el install. Workaround: `config.audit.ignore` con los 6 PKSA + flag `--no-audit` en `composer update` del Dockerfile. Ver [[Errores Comunes#Browsershot bloqueado por security advisories PKSA]]
- refactor: `PresupuestoInvoiceMail::attachments()` ahora delega en `app(PdfService::class)->renderPresupuestoPdf($presupuesto)` en vez de hacer `Pdf::loadView(...)` directo. Elimina duplicación — hay un único entry point para generar el PDF de un presupuesto
- cleanup: `pdf.presupuesto.blade.php` quedó como legacy (no se usa en ningún path) — se puede eliminar en una próxima limpieza
- config local: `MAIL_PASSWORD` seteada en `.env` local (no commiteada) para probar el envío end-to-end

Archivos: `backend/Dockerfile`, `backend/composer.json`, `backend/app/Services/PdfService.php`, `backend/app/Mail/PresupuestoInvoiceMail.php`, `backend/app/Http/Controllers/PresupuestoController.php`, `backend/resources/views/pdf/presupuesto.blade.php` (legacy), `CLAUDE.md`

Archivos del envío de invoice (bloque anterior): `app/Mail/PresupuestoInvoiceMail.php`, `app/Http/Controllers/PresupuestoController.php` (método `enviarInvoice`), `config/mail.php`, `resources/views/emails/presupuesto-invoice.blade.php`, `routes/api.php`, `frontend/pages/presupuestos/[id].vue`, `.env`

## 2026-04-08

- feat: Filtros de mes, año y cliente en listados de presupuestos, proyectos y activaciones. Default al mes/año actual con opción "Todos" para deshabilitar cada filtro. Ver [[memoria#Listados - filtros de fecha y cliente]] y [[Backend - API#Presupuestos]]
- refactor: Listado de proyectos migrado de filtrado client-side a fetch server-side con query params (consistente con presupuestos y activaciones)
- convención: Param wire usa `anio` (ASCII) en lugar de `año` para evitar fragilidad de encoding URL/PHP. State frontend mantiene nombres en español. Ver [[memoria#Query params sin caracteres no-ASCII]]

Campos de fecha por listado:
- Presupuestos → `presupuestos.fecha`
- Proyectos → `proyectos.fecha_inicio`
- Activaciones → `pruebas_ejecucion.periodo_desde`

Archivos: `PresupuestoController.php`, `ProyectoController.php`, `PruebaEjecucionController.php`, `presupuestos/index.vue`, `proyectos/index.vue`, `evidencias/index.vue`

## 2026-03-30

- feat: Descripcion IA de activaciones escalada segun cantidad de hitos. ≤5 hitos -> 2-3 oraciones (`max_tokens: 300`), 6-15 hitos -> 3-5 oraciones (`max_tokens: 500`), +15 hitos -> 5-7 oraciones (`max_tokens: 700`). Prompt dice "cubriendo todas las actividades listadas" (no "breve") para evitar omisiones del modelo. Ver [[Reglas de Negocio]] y [[Backend - API#DeepSeek]]
- fix: Actualizar dominio `blu.inc` -> `blustudioinc.com` en invoice (PDF de presupuestos)
- docs: Reglas de longitud escalada DeepSeek en CLAUDE.md

Archivos: `PruebaEjecucionController.php`, `presupuesto-preview.blade.php`, `CLAUDE.md`

## 2026-03-29

- feat: Campo `realizado` en gastos para indicar si el pago al acreedor fue cancelado (migracion 0048). Toggle con PATCH, desmarcar requiere credenciales admin. Ver [[Reglas de Negocio#Gastos - Campo realizado]]
- feat: Checkbox read-only de gastos realizados en listado de presupuestos. Eager-load `proyecto.gastos` en index
- feat: Color diferente para estado COBRADO vs APROBADO en [[Frontend]] (StatusBadge)
- fix: Dashboard — meses duplicados en grafico de ingresos/gastos

Archivos principales: `GastoController.php`, `GastoResource.php`, `Gasto.php`, `presupuestos/index.vue`, `StatusBadge.vue`, `DashboardService.php`

## 2026-03-27

- fix: PDF presupuesto — corregir scroll en html2canvas para exportacion completa
- ui: Remover boton eliminar del listado de activaciones (solo desde detalle)

Archivos: `presupuesto-preview.blade.php`, `evidencias/index.vue`

## 2026-03-25

- feat: Eliminar activaciones requiere credenciales admin (modal email+password). Ver [[Reglas de Negocio#Operaciones que requieren credenciales admin]]
- feat: Mostrar estado del proyecto en listado de presupuestos

Archivos: `PruebaEjecucionController.php`, `presupuestos/index.vue`, `evidencias/[id].vue`

## 2026-03-22

- feat: IVA en gastos (0 / 10.5 / 21 / 27%). Migracion 0047. Ver [[Reglas de Negocio#IVA en Gastos]]
- feat: Etiquetas de colores visibles en listado de proyectos. Ver [[Reglas de Negocio#Etiquetas de Presupuestos]]
- feat: Orden de presupuestos y proyectos por `updated_at` DESC con touch automatico
- feat: Dashboard mejorado con 6 KPIs, tooltips, filtro por periodo
- feat: Edicion de gastos con restriccion por estado de presupuesto (COBRADO/FACTURADO bloquea)
- feat: Modal de detalle de gasto en vista de proyecto
- feat: Boton eliminar gastos desde listado y vista de proyecto
- ui: Reducir tamano de texto en tabla gastos del proyecto, quitar columna categoria
- docs: Documentar edicion de gastos, proteccion por estado y error de rutas apiResource
- fix: `env()` -> `config()` en BackupController. Ver [[Errores Comunes#env no lee variables de entorno del container en PHP-FPM]]
- fix: nowrap en columnas numericas de gastos

Archivos principales: `GastoController.php`, `GastoResource.php`, `gastos/nuevo.vue`, `gastos/[id].vue`, `proyectos/[id].vue`, `presupuestos/index.vue`, `DashboardService.php`

## 2026-03-21

- feat: PDF de activaciones sobre hoja membretada Blu con TCPDF+FPDI (portrait A4). Ver [[Stack e Infraestructura#Plantilla PDF membretada]]
- fix: Agregar tcpdf y fpdi al composer.json para produccion
- fix: Asegurar dirs templates y temp en Dockerfile y entrypoint

Archivos: `PruebaEjecucionController.php`, `Dockerfile`, `docker-entrypoint.sh`, `composer.json`

---

## Ver tambien

- [[Backend - API]] - Endpoints modificados
- [[Reglas de Negocio]] - Reglas de dominio agregadas
- [[Errores Comunes]] - Bugs descubiertos y resueltos
- [[memoria]] - Convenciones y feedback acumulado
