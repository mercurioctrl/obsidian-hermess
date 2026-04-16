# Backend - API Routes y Controllers

## Estructura de autenticacion

```
POST /api/auth/login                 <- publico
GET  /api/presupuestos/*/pdf         <- token via query string
GET  /api/archivos/publico/{token}   <- publico, 64 chars hex [desde 2026-04-15]
Todo lo demas -> middleware auth:sanctum (Bearer token)
Rutas de admin -> middleware adicional EnsureIsAdmin
```

**`GET /api/archivos/publico/{token}`** — sirve archivos de `proyecto_adjuntos` por `public_token` sin requerir auth. Si `tipo=ENLACE` hace `redirect()->away()`, si `tipo=ARCHIVO` devuelve el file con `Content-Disposition: inline`. La seguridad se basa en la imposibilidad de adivinar el token (hex 64 chars). Ver [[Modulo WhatsApp Inbox#Public token para acceso sin auth]].

## Auth
```
POST   /api/auth/login       -> AuthController@login
POST   /api/auth/logout      -> AuthController@logout
GET    /api/auth/me          -> AuthController@me
```

## Busqueda global
```
GET    /api/busqueda          -> BusquedaController (invokable)
         param: q (string, minimo 2 caracteres)
         Busca en: clientes, presupuestos, proyectos, gastos
```

Ver [[Frontend#Busqueda global]] para la UI.

## Clientes
```
GET    /api/clientes                  -> index (filtros: search, activo) [eager telefonos]
POST   /api/clientes                  -> store
GET    /api/clientes/{id}             -> show [con wrapper data:, eager telefonos + presupuestos]
PUT    /api/clientes/{id}             -> update [con wrapper data:]
DELETE /api/clientes/{id}             -> destroy (soft: activo=false)
GET    /api/clientes/{id}/cuenta      -> cuenta (movimientos)
GET    /api/clientes/{id}/presupuestos
GET    /api/clientes-export/csv

# Teléfonos del cliente (desde 2026-04-15)
POST   /api/clientes/{id}/telefonos            -> agregarTelefono
       body: { nombre?, codigo_area, numero, tipo? }
       tipo: WHATSAPP (default) | LLAMADA | FIJO
DELETE /api/clientes/{id}/telefonos/{telefono} -> eliminarTelefono
```

Las rutas de teléfonos se registran **antes** del `apiResource('clientes', …)` para no colisionar con `{cliente}`. Ver [[Errores Comunes#Rutas especificas despues de apiResource colisionan con id]]. `ClienteResource` siempre incluye el array `telefonos` (id, nombre, codigo_area, numero, tipo). Ver [[Modulo WhatsApp Inbox]] para el caso de uso principal.

## Presupuestos
```
GET    /api/presupuestos              -> index
         filtros: estado, cliente_id, search, etiqueta_id, mes, anio
         (mes y anio filtran sobre presupuestos.fecha)
POST   /api/presupuestos              -> store [con wrapper data:]
GET    /api/presupuestos/{id}         -> show [con wrapper data:]
PUT    /api/presupuestos/{id}         -> update [con wrapper data:]
DELETE /api/presupuestos/{id}         -> destroy (solo BORRADOR)
POST   /api/presupuestos/{id}/transicion -> cambio de estado
GET    /api/presupuestos/{id}/pdf
POST   /api/presupuestos/{id}/etiquetas      -> syncEtiquetas
POST   /api/presupuestos/{id}/crear-proyecto
POST   /api/presupuestos/{id}/enviar-invoice -> enviarInvoice
         body: email (required|email)
         efecto: guarda email en cliente si cambió, envía Mailable con PDF adjunto
         BCC automático a payments@blustudioinc.com (MAIL_PAYMENTS_BCC)
```

Ver [[Reglas de Negocio#Presupuestos - Flujo de estados]] para transiciones y efectos automaticos.

**Transicion a COBRADO** requiere `banco_caja_id` + `email` + `password` en el body. Ver [[Reglas de Negocio#Operaciones que requieren credenciales admin]].

**Envío de invoice:** El Mailable `PresupuestoInvoiceMail` genera el PDF in-memory con `Pdf::loadView(...)->output()` (no toca filesystem) y lo adjunta. El BCC se setea en el `Envelope()` del Mailable, no en el controller. Ver [[Stack e Infraestructura#Mail SMTP]] y [[memoria#Mail SMTP y envío de invoices]].

> Nota sobre el param `anio`: se usa ASCII (no `año`) en query params para evitar issues de encoding URL/PHP. Ver [[memoria#Query params sin caracteres no-ASCII]].

## Proyectos
```
GET    /api/proyectos                        -> index (sin wrapper)
         filtros: etiqueta_id, cliente_id, mes, anio
         (mes y anio filtran sobre proyectos.fecha_inicio)
GET    /api/proyectos/{id}                   -> show (sin wrapper, incluye empleados, jira_boards)
PUT    /api/proyectos/{id}                   -> update
POST   /api/proyectos/{id}/empleados         -> asignarEmpleado
DELETE /api/proyectos/{id}/empleados/{emp}   -> desasignarEmpleado
GET    /api/proyectos/{id}/adjuntos
POST   /api/proyectos/{id}/adjuntos/enlace
POST   /api/proyectos/{id}/adjuntos/archivo  -> multipart, max 10MB
DELETE /api/proyectos/{id}/adjuntos/{adj}
POST   /api/proyectos/{id}/adjuntos/{adj}/enviar-whatsapp
       body: { telefono_ids: number[] }
       genera/reutiliza public_token y postea al Inbox API por cada contacto.
       response: { url, enviados[], fallidos[] }
POST   /api/proyectos/{id}/jira-boards       -> vincularJiraBoard
DELETE /api/proyectos/{id}/jira-boards/{board}
```

Ver [[Frontend#Modulo Jira]] para la integracion de tableros.

## Cuenta Corriente
```
GET    /api/cuenta-corriente/{cliente_id}  -> movimientos (sin wrapper)
POST   /api/cuenta-corriente               -> crear movimiento manual
GET    /api/cuenta-corriente-deudores
GET    /api/cuenta-corriente-resumen
```

Ver [[Reglas de Negocio#Cuenta Corriente vs Gastos]] para la distincion.

## Bancos y Cajas
```
GET    /api/bancos-cajas           -> index (sin wrapper)
POST   /api/bancos-cajas           -> store
PUT    /api/bancos-cajas/{id}      -> update
DELETE /api/bancos-cajas/{id}      -> destroy (falla si tiene gastos)
POST   /api/bancos-cajas/{id}/ajuste -> ajuste manual de saldo
```

## Gastos
```
GET    /api/gastos                 -> index paginado [con wrapper data: + meta]
GET    /api/gastos/{id}            -> show [con wrapper data:, incluye campo editable]
POST   /api/gastos                 -> store (descuenta saldo BancoCaja)
PUT    /api/gastos/{id}            -> update (ajusta diferencia)
DELETE /api/gastos/{id}            -> destroy (devuelve saldo)
GET    /api/gastos/categorias      -> lista de categorias (ANTES del apiResource!)
POST   /api/gastos/categorias      -> crear categoria
GET    /api/gastos/cotizacion      -> cotizacion dolar oficial BCRA
GET    /api/gastos-resumen
```

> Las rutas `/gastos/categorias` y `/gastos/cotizacion` deben registrarse ANTES del `apiResource`. Ver [[Errores Comunes#Rutas especificas despues de apiResource colisionan con id]].

> `monto` es calculado por el controller, nunca se envia desde el [[Frontend]]. Ver [[Reglas de Negocio#IVA en Gastos]].

> Proteccion por estado: PUT y DELETE fallan con 422 si presupuesto COBRADO/FACTURADO. Ver [[Reglas de Negocio#Gastos - Proteccion por estado de presupuesto]].

## Dashboard
```
GET    /api/dashboard              -> KPIs
GET    /api/dashboard/ingresos-gastos -> datos mensuales para grafico
```

## Staff y Empleados
Ver [[Modulo Personal]] para documentacion completa.
```
GET    /api/staff                  -> usuarios del sistema (sin wrapper)
GET|POST|PUT|DELETE /api/empleados/{id}
POST   /api/empleados/{id}/proyectos
DELETE /api/empleados/{id}/proyectos/{proy}
GET|POST /api/empleados/{id}/pagos
DELETE /api/empleados/{id}/pagos/{pago}
```

## Jira (integracion externa)
```
POST   /api/jira/test
GET    /api/jira/projects
GET    /api/jira/projects/{key}/statuses
GET    /api/jira/projects/{key}/issues      -> cursor-based
GET    /api/jira/projects/{key}/search-issues
GET    /api/jira/hitos
POST   /api/jira/issues/{issueKey}/crear-hito
```

Auth Jira: Basic Auth con `email:api_token` de Atlassian. Configurado en tabla `configuracion`.

## Evidencias / Activaciones
```
GET    /api/evidencias                      -> index
         filtros: proyecto_id, etiqueta_id, cliente_id, mes, anio
         (mes y anio filtran sobre pruebas_ejecucion.periodo_desde)
         (cliente_id filtra via proyecto.presupuesto.cliente_id)
POST   /api/evidencias                      -> store
GET|PUT|DELETE /api/evidencias/{evidencia}  -> CRUD
POST   /api/evidencias/{evidencia}/generar-descripcion -> IA con DeepSeek
POST   /api/evidencias-copiar              -> copiar entre proyectos
GET    /api/evidencias/{evidencia}/pdf      -> PDF sobre membretada
```

> Parametro de ruta es `{evidencia}` (no `{prueba}`).

## MercadoPago, Stripe, Mercury
Ver [[Medios de Pago]] para documentacion completa de las tres integraciones.

### Mercury Invoicing — endpoints (desde 2026-04-14)

```
GET    /api/mercury/invoices/cotizacion       -> BCRA oficial venta para conversión ARS→USD
GET    /api/mercury/invoices                  -> listado cursor-based (limit, order, start_after, end_before)
                                                  acepta ?status=Unpaid|Paid|Overdue|Cancelled (filtro PHP)
                                                  resuelve customer name vía clientes.mercury_customer_id
                                                  y presupuesto vinculado vía presupuestos.mercury_invoice_id
POST   /api/mercury/invoices                  -> crear desde presupuesto
                                                  body: presupuesto_id, due_date, send_email_option, tasa_cambio?
GET    /api/mercury/invoices/{id}             -> detalle con lineItems
GET    /api/mercury/invoices/{id}/pdf         -> proxy del PDF de Mercury (soporta ?token=)
POST   /api/mercury/invoices/{id}/cancel      -> cancelar invoice y actualizar status local
POST   /api/mercury/invoices/{id}/refresh     -> re-sync status desde Mercury
POST   /api/mercury/invoices/{id}/link        -> vincular invoice existente a presupuesto
                                                  body: presupuesto_id. Persiste id/slug/status.
                                                  Falla con 422 si el presupuesto ya tiene invoice asociado.
```

> Las rutas de cotización y `/pdf` van fuera del middleware auth (la primera es pública, la segunda usa `?token=` query). El resto está dentro de `auth:sanctum`.

> ⚠️ **Orden de las rutas:** `/mercury/invoices/cotizacion` se registra ANTES de `/mercury/invoices/{id}` para que no colisione con el route model binding. Ver [[Errores Comunes#Rutas especificas despues de apiResource colisionan con id]].

## WhatsApp Inbox — envío de adjuntos

Integración con servicio externo tipo cola. Ver [[Modulo WhatsApp Inbox]] para doc completa del flow, el endpoint del worker, y las consideraciones de seguridad.

**Config** (singleton `configuracion`):
```
GET    /api/config                    -> show [hide inbox_api_token, expose inbox_tiene_token bool]
PUT    /api/config (admin)            -> update (valida inbox_api_url como url)
                                         inbox_api_token vacío → no se persiste (mantiene el anterior)
```

**Envío desde proyecto:**
```
POST   /api/proyectos/{proyecto}/adjuntos/{adjunto}/enviar-whatsapp
       body: { telefono_ids: number[] }
       1. Valida pertenencia del adjunto al proyecto y de los teléfonos al cliente del presupuesto
       2. asegurarPublicToken() → bin2hex(random_bytes(32)) si no existe
       3. Arma mensaje: "Hola {nombre}, te ha enviado el archivo {titulo} - {url}"
       4. Normaliza número: preg_replace('/\D+/', '', codigo_area.numero)
       5. Http::timeout(15)->asJson()->post(inbox_api_url, { token, telefono, mensaje }) por cada contacto
       6. Errores individuales NO rompen el loop — se acumulan en fallidos[]
       response: { url, enviados[], fallidos[] }
```

**Ruta pública** (fuera de `auth:sanctum`):
```
GET    /api/archivos/publico/{token}  -> ProyectoController::servirArchivoPublico
       ENLACE   → redirect()->away($adjunto->url)
       ARCHIVO  → response()->file() con Content-Disposition: inline
       404 si el token no existe o el archivo fue borrado del filesystem
```

**Controller methods nuevos en `ProyectoController` (2026-04-15):**
- `enviarAdjuntoWhatsApp(Request, Proyecto, ProyectoAdjunto)` — dentro de auth
- `servirArchivoPublico(string $token)` — público, sin auth

Imports agregados: `Illuminate\Support\Facades\Http`, `App\Models\ClienteTelefono`, `App\Models\Configuracion`.

**Eager-load en `show`:** `presupuesto.cliente.telefonos` (ya estaba `presupuesto.cliente`, se profundiza para que el frontend tenga los contactos WhatsApp disponibles sin request extra).

### Envío de invoice por email — payment links

```
POST   /api/presupuestos/{id}/enviar-invoice
   body: email (required)
         mercury_pay_url? (string url — botón "Depósito Bancario" en el email)
         stripe_payment_url? (string url — botón "Pagar con Tarjeta")
         mercadopago_payment_url? (string url — botón "Pagar con MercadoPago")
         attach_mercury_pdf? (boolean — adjunta el PDF del invoice Mercury como 2do attachment)
```

Los 3 URLs opcionales se renderizan como botones en el body del email solo si están presentes en el body del POST. El controller los pasa al `PresupuestoInvoiceMail` como 2do argumento (`$paymentLinks` array) y `attach_mercury_pdf` como 3er argumento (`bool $attachMercuryPdf`). Si `attachMercuryPdf=true` y el presupuesto tiene `mercury_invoice_id`, el Mailable baja el PDF de Mercury vía `MercuryInvoiceService::getInvoicePdf()` y lo adjunta como segundo PDF (además del PDF Blu del presupuesto). Si la descarga falla, se loguea warning y se sigue sin él. Ver [[Modulo Mercury Invoicing#Sub-flow — adjuntar PDF de Mercury al email]].

## Etiquetas
```
GET    /api/etiquetas              -> listado (sin wrapper)
POST   /api/etiquetas              -> crear (body: nombre, color)
PUT    /api/etiquetas/{id}
DELETE /api/etiquetas/{id}         -> cascade borra pivots
```

## Config y Usuarios
```
GET    /api/config      -> configuracion empresa
PUT    /api/config      -> solo admin
GET|POST|PUT|DELETE /api/usuarios  -> solo admin [con wrapper data:]
PUT    /api/usuarios/{id}/password -> solo admin
```

## wrapper `data:` en respuestas

| Con wrapper `data:` | Sin wrapper (JSON directo) |
|--------------------|--------------------------|
| /clientes/{id} | /proyectos |
| /presupuestos/{id} | /bancos-cajas |
| /gastos (paginado) | /dashboard |
| /usuarios | /gastos/categorias |
| | /cuenta-corriente-* |
| | /staff, /empleados |
| | /etiquetas |
| | /mercadopago/*, /stripe/*, /mercury/* |

**Patron frontend siempre seguro:** `const res = await api.get(...); modelo.value = res?.data ?? res`

Ver [[Errores Comunes#Olvidar el wrapper data en endpoints que usan API Resource]].

---

## Ver tambien

- [[Backend - Modelos]] - Modelos que usan estos endpoints
- [[Frontend]] - Paginas que consumen esta API
- [[Modulo Permisos]] - Enmascaramiento de campos sensibles
- [[Medios de Pago]] - Endpoints de MP, Stripe, Mercury
- [[Errores Comunes]] - Bugs frecuentes de API
- [[memoria]] - Convenciones de filtros y query params
