# Memoria del Proyecto

Consolidacion de la memoria persistente de Claude para este proyecto. Organizada por tipo.

Ultima sincronizacion: 2026-04-13 (iteración: migración PDF presupuestos a Browsershot)

---

## Feedback (patrones tecnicos)

Lecciones aprendidas y correcciones del usuario. Estas guian el comportamiento de desarrollo.

### Docker
- **Local vs servidor:** En local, docker corre desde `mini-saas/`. En servidor Ubuntu necesita `sudo`. `git pull` puede fallar por backups con permisos root
- **Frontend rebuild:** Siempre usar `--no-cache` y reiniciar nginx despues para resolver nueva IP del container. Ver [[Stack e Infraestructura#Comandos de deploy]]

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

### Integraciones
- **MercadoPago:** Access token + banco vinculado. Movimientos via `/v1/payments/search`. Sync saldo manual. Conversion USD->ARS. Limitaciones API (balance 403, movements requiere permisos especiales). Ver [[Medios de Pago#MercadoPago]]
- **Stripe:** Secret key + banco vinculado. Montos en centavos. Checkout Sessions. Conversion moneda. Ver [[Medios de Pago#Stripe]]
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

**Fix del `\Log::error` (2026-04-13):** El catch del `enviarInvoice` usaba `\Log::error(...)` sin FQN, que en Laravel 11 no resuelve (no hay alias `\Log` global). Cuando `Mail::to(...)` lanzaba un error real, el propio catch crasheaba con "Class Log not found", enmascarando la causa. Siempre usar `\Illuminate\Support\Facades\Log::error(...)` o agregar `use Illuminate\Support\Facades\Log;` al tope. Ver [[Errores Comunes#Log facade sin FQN completo falla en Laravel 11]].

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
