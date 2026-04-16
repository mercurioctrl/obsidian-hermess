# Changelog

Registro de lo trabajado en el proyecto, agrupado por fecha.

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
