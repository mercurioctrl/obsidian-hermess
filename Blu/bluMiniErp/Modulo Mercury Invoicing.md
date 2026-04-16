# Modulo Mercury Invoicing

Integración completa con la **API de Accounts Receivable de Mercury** para emitir, listar y cancelar invoices desde el ERP, embebiendo el link de pago en el email transaccional.

> **Disponibilidad:** solo cuentas Mercury con plan de suscripción que incluye Invoicing. La API es la misma `https://api.mercury.com/api/v1` que ya usábamos para [[Medios de Pago#Mercury]] balance/movimientos, pero bajo la sección `/ar/*`.

**Implementado:** 2026-04-14 — ver [[changelog#2026-04-14]].

---

## Por qué

El usuario factura en USD a clientes externos via Mercury y quería:
1. **Crear el invoice de Mercury desde el detalle del presupuesto del ERP** — sin tener que ir a la UI de Mercury y duplicar datos.
2. **Ver todos los invoices de Mercury en una tabla dentro del ERP** con acciones (cancelar, ver online, descargar PDF).
3. **Adjuntar el link de pago de Mercury en el email del invoice** junto con los de Stripe y MercadoPago, para que el cliente elija método.

---

## Arquitectura — capas

```
Frontend (Vue/Nuxt)
   ↓
ERP API (Laravel)              ← MercuryInvoiceController
   ↓
MercuryInvoiceService          ← wrapper único de la lógica HTTP
   ↓
api.mercury.com/api/v1/ar/*    ← API de Accounts Receivable
```

---

## Limitaciones críticas (leer antes de modificar)

- **Mercury solo opera en USD.** No acepta otras monedas. Para presupuestos ARS hay que convertir con tasa de cambio (precarga `pres.tasa_cambio` o BCRA via [[Reglas de Negocio#Monedas y Tipo de Cambio|dolarapi.com]]). La tasa usada se persiste en `presupuestos.mercury_invoice_tasa_cambio` para auditoría.
- **`amount` viene en dólares enteros, NO cents.** Lección: `1500` significa $1500 USD, no $15.00.
- **IP whitelist por token.** Los API tokens pueden tener IP whitelist activa (`errorCode: ipNotWhitelisted`). Las IPs egress de dev y prod son distintas — agregar las dos al whitelist del token en el dashboard de Mercury. Ver [[Errores Comunes#Mercury IP whitelist en API tokens]].
- **NO existen en la API:** "marcar como pagado" (Mercury detecta payments automáticamente cuando el customer paga vía hosted link), "resend email after creation" (sólo se controla con `sendEmailOption` al crear), recurring invoices, product catalog. Para esos features hay que usar la UI de Mercury.
- **El PDF descargable existe pero no está documentado:** `GET /ar/invoices/{id}/pdf` devuelve `application/pdf` (~26KB con la estética de Mercury). No aparece en el reference oficial pero funciona.

---

## Endpoints de Mercury (api.mercury.com/api/v1)

### Invoices

| Metodo | Ruta | Para que |
|--------|------|----------|
| GET    | `/ar/invoices` | Listado cursor-based: `limit`, `order`, `start_after`, `end_before` |
| GET    | `/ar/invoices/{id}` | Detalle (incluye `lineItems`) |
| POST   | `/ar/invoices` | Crear |
| PATCH  | `/ar/invoices/{id}` | Actualizar |
| POST   | `/ar/invoices/{id}/cancel` | Cancelar |
| GET    | `/ar/invoices/{id}/pdf` | **Descarga el PDF** (no documentado) |
| GET    | `/ar/invoices/{id}/attachments` | Archivos adjuntos al invoice (no es el invoice en sí) |

### Customers

| Metodo | Ruta | Para que |
|--------|------|----------|
| GET    | `/ar/customers` / `/ar/customers/{id}` | Listar / get |
| POST   | `/ar/customers` | Crear |
| PATCH  | `/ar/customers/{id}` | Actualizar |
| DELETE | `/ar/customers/{id}` | Borrar |

---

## Shape clave del Invoice object

```json
{
  "id": "uuid",
  "invoiceNumber": "INV-402",
  "customerId": "uuid",
  "destinationAccountId": "uuid",  // = mercury_account_id de la config
  "amount": 1500,                  // USD enteros, NO cents
  "status": "Paid|Unpaid|Overdue|Cancelled|Draft",
  "slug": "1nywsm6tkch14phq",      // ← clave para construir URLs
  "lineItems": [{"name", "unitPrice", "quantity", "salesTaxRate"}],
  "invoiceDate": "2026-04-13",
  "dueDate": "2026-04-29",
  "ccEmails": [...],
  "achDebitEnabled", "creditCardEnabled", "useRealAccountNumber": false
}
```

### URLs derivadas del `slug`

No vienen en el response, hay que construirlas:

| URL | Para que |
|-----|----------|
| `https://app.mercury.com/invoice/{slug}` | Vista del invoice hosteada (link compartible "ver online") |
| `https://app.mercury.com/pay/{slug}` | Landing de pago — el que se manda en el email como "Depósito Bancario" |

---

## Persistencia local en el ERP

Migraciones:

- **0049** — `clientes.mercury_customer_id` (varchar 64). UUID del customer en Mercury, persistido tras find-or-create. Permite resolver el nombre del cliente al listar invoices y reutilizar el customer entre presupuestos.
- **0050** — `presupuestos.mercury_invoice_id`, `mercury_invoice_slug`, `mercury_invoice_status`, `mercury_invoice_tasa_cambio` (decimal 12,4 — auditoría), `mercury_invoice_created_at`. Referencia + auditoría del invoice creado desde el presupuesto.
- **0051** — `presupuestos.mercadopago_payment_url` y `presupuestos.stripe_payment_url`. Antes los links de pago de MP/Stripe se generaban on-the-fly y eran ephemeral; ahora se persisten al crearlos para reusarlos en el modal de envío de invoice por email.

Ver [[Base de Datos#presupuestos]] y [[Base de Datos#clientes]].

---

## Servicio centralizado

`app/Services/MercuryInvoiceService.php` envuelve toda la lógica HTTP. Métodos clave:

- `listInvoices()`, `getInvoice()`, `getInvoicePdf()` (devuelve bytes), `cancelInvoice()`, `createInvoice()`
- `listCustomers()`, `getCustomer()`, `createCustomer()`
- `findOrCreateCustomer(Cliente)` — idempotente, persiste `mercury_customer_id` en clientes. Falla con 422 si el cliente local no tiene email (Mercury lo requiere).
- `createInvoiceFromPresupuesto(Presupuesto, opts)` — wrapper de alto nivel que:
  1. Mapea `presupuesto.items[]` → `lineItems[]` con conversión ARS→USD si aplica
  2. Asegura el customer con `findOrCreateCustomer`
  3. Llama `createInvoice` con el payload armado (`destinationAccountId` = `config.mercury_account_id`)
  4. Persiste el resultado en el presupuesto (`mercury_invoice_id`, `slug`, `status`, `tasa_cambio_usada`, `created_at`)
- `refreshPresupuestoInvoiceStatus(Presupuesto)` — re-fetch del status desde Mercury
- `static hostedUrl(?string $slug)` — helper para construir la URL `/invoice/{slug}`. Para el `/pay/{slug}` se construye inline en `PresupuestoResource`.

---

## Endpoints del ERP

`MercuryInvoiceController` — todos protegidos con `auth:sanctum` excepto `cotizacion` (público) y `pdf` (soporta `?token=` query):

```
GET    /api/mercury/invoices/cotizacion       BCRA oficial venta — para conversión ARS→USD
GET    /api/mercury/invoices                  Listado cursor-based, resuelve customer name local
                                              y vincula al presupuesto local
                                              ?status=Unpaid|Paid|Overdue|Cancelled (filtro PHP)
POST   /api/mercury/invoices                  Crear desde presupuesto
                                              body: presupuesto_id, due_date, send_email_option, tasa_cambio?
GET    /api/mercury/invoices/{id}             Detalle con lineItems
GET    /api/mercury/invoices/{id}/pdf         Proxy del PDF (soporta ?token= para abrir en navegador)
POST   /api/mercury/invoices/{id}/cancel      Cancela en Mercury y actualiza status local
POST   /api/mercury/invoices/{id}/refresh     Re-sync status local desde Mercury
POST   /api/mercury/invoices/{id}/link        Vincular invoice Mercury existente a un presupuesto
                                              body: presupuesto_id. Persiste id/slug/status.
                                              Falla con 422 si el presupuesto ya tiene invoice.
```

> ⚠️ **Orden de las rutas:** `/mercury/invoices/cotizacion` se registra ANTES de `/mercury/invoices/{id}` para que no colisione con el route binding. Ver [[Errores Comunes#Rutas especificas despues de apiResource colisionan con id]].

Ver [[Backend - API#Mercury Invoicing — endpoints (desde 2026-04-14)]].

---

## UI — listado en `/mercury`

`/mercury` ahora tiene tabs **Cuenta** (lo que ya estaba: balances + movimientos) e **Invoices** (nuevo). El tab Invoices carga lazy.

**Tabla:**
- Columnas: Número (+ link al presupuesto local si está vinculado), Cliente (resuelto vía `clientes.mercury_customer_id`), Importe USD, Estado, Fecha, Vencimiento
- Status badges: **Paid** verde, **Unpaid** amarillo, **Overdue** rojo, **Cancelled** gris, **Draft** neutral
- Paginación cursor-based (50 por página), botón "Cargar más"

**Acciones por fila:**
- 🔗 Ver online — abre `hostedUrl` en otra pestaña
- ⬇️ Descargar PDF — proxy backend, abre el PDF de Mercury en otra pestaña (con `?token=`)
- ✕ Cancelar — solo si Unpaid, pide confirm

Ver [[Frontend#Modulo Mercury]].

---

## UI — crear desde presupuesto

Botón **"Crear invoice Mercury"** en `/presupuestos/[id]`, visible solo si `!mercury_invoice_id`.

Modal de creación:
- **Si moneda es ARS:** card de aviso amarillo + input para tipo de cambio (precarga `pres.tasa_cambio` si existe, sino BCRA via botón). Muestra preview del USD convertido en vivo.
- **Si moneda es USD:** directo, sin conversión.
- Vencimiento (default +30 días)
- Selector `sendEmailOption` (default `DontSend` → el ERP maneja el email; alternativa `SendNow` → Mercury envía su propio email)

Tras crear, el botón se reemplaza por uno con badge del status del invoice + link al hosted URL.

---

## UI — modal "Enviar invoice por email"

Reescrito en Fase 4. Tiene una sección **"Métodos de pago a incluir"** con 3 filas:

| Método | Color de marca | Comportamiento |
|--------|---------------|----------------|
| Mercury — Depósito Bancario | `#0A85E0` | Si no hay invoice → **dos botones**: "Crear" (abre el modal de creación de Fase 3, apilable) y "Vincular existente" (abre picker con tabla de invoices Unpaid). Si existe → checkbox pre-marcado + sub-checkbox "Adjuntar PDF del invoice Mercury" (default ON). |
| Stripe — Pagar con Tarjeta | `#635BFF` | Si no hay link → botón "Generar" llama inline a `/stripe/preferencia` y persiste el link. Si existe → checkbox pre-marcado. |
| MercadoPago | `#009EE3` | Idem Stripe pero con `/mercadopago/preferencia`. |

Cada fila: checkbox + indicador "✓ Listo" + botón "Generar"/"Crear"/"Vincular" según corresponda.

Al enviar, el body del POST a `/presupuestos/{id}/enviar-invoice` incluye los URLs marcados (`mercury_pay_url`, `stripe_payment_url`, `mercadopago_payment_url`) y el flag `attach_mercury_pdf` (boolean). El controller los pasa al `PresupuestoInvoiceMail` como 2do y 3er argumento (`$paymentLinks`, `$attachMercuryPdf`).

### Sub-flow — vincular invoice Mercury existente

Si el usuario clickea "Vincular existente" en la fila Mercury, se abre un modal **picker**:

- Carga via `GET /api/mercury/invoices?status=Unpaid&limit=100`
- Tabla con columnas: Número, Cliente (nombre resuelto vía `clientes.mercury_customer_id`), Importe USD, Vencimiento, acción "Vincular"
- Si el `customerId` del invoice no coincide con `cliente.mercury_customer_id` del presupuesto, muestra **⚠ rojo** en la columna Cliente — alerta visual sin bloquear (el usuario puede vincular invoices de otros clientes intencionalmente, ej. para refacturas)
- Click "Vincular" → `POST /api/mercury/invoices/{id}/link` → persiste `mercury_invoice_id`/`slug`/`status` en el presupuesto, pre-marca los checkboxes del modal de envío (`includeMercury` + `attachMercuryPdf`), cierra picker
- `ClienteResource` ahora expone `mercury_customer_id` para que el frontend pueda detectar el mismatch

### Sub-flow — adjuntar PDF de Mercury al email

Si el presupuesto tiene `mercury_invoice_id`, en la fila Mercury aparece un sub-checkbox **"Adjuntar PDF del invoice Mercury"** (ícono `lucide:paperclip`). Cuando está marcado:

1. El frontend agrega `attach_mercury_pdf: true` al body del POST a `enviarInvoice`
2. El controller pasa `$attachMercuryPdf = true` al constructor del `PresupuestoInvoiceMail` (3er argumento)
3. En `attachments()`, el Mailable arma el array de adjuntos: primero el PDF Blu del presupuesto (siempre), después intenta bajar el PDF de Mercury con `app(MercuryInvoiceService::class)->getInvoicePdf($id)` y agregarlo como segundo adjunto
4. Si la descarga del PDF Mercury falla (conexión, IP whitelist, etc.), se loguea **warning** y se sigue sin él — **no rompe el envío** del email

El default del checkbox es ON cuando hay invoice asociado: la asunción es que si el usuario tomó el trabajo de generar/vincular un invoice Mercury, lo más probable es que quiera adjuntar el PDF.

### Email blade

`resources/views/emails/presupuesto-invoice.blade.php` renderiza una sección "Métodos de pago" con hasta 3 botones full-width. Cada botón se renderiza solo si el URL correspondiente viene en `$paymentLinks`. La key del array es el método (`mercury` / `stripe` / `mercadopago`).

---

## Errors / gotchas a recordar

- `findOrCreateCustomer` valida que el cliente tenga email (Mercury lo requiere). Si el cliente local no tiene email, falla con 422.
- `createInvoiceFromPresupuesto` falla si el presupuesto no tiene items o si la tasa de cambio es 0 cuando la moneda es ARS.
- El listado `GET /ar/invoices` devuelve `customerId` (uuid) y NO el nombre del customer — para mostrarlo hay que joinear con `clientes.mercury_customer_id`. El controller del ERP lo hace en el `index()`.
- El PDF del invoice viene de Mercury directamente (no es generado por el ERP), así que la estética es la de Mercury — esto es ÚTIL como prueba bancaria pero no reemplaza el PDF de Blu del presupuesto, son cosas distintas.
- Si Mercury cambia el endpoint del PDF (que no está documentado), nuestro `MercuryInvoiceController::pdf` va a romper — no hay alternativa documentada.

---

## Ver también

- [[Medios de Pago#Mercury Invoicing API (desde 2026-04-14)]] — sección extendida en la nota de Medios de Pago
- [[Backend - API#Mercury Invoicing — endpoints (desde 2026-04-14)]]
- [[Base de Datos#presupuestos]] — campos persistidos
- [[Errores Comunes#Mercury IP whitelist en API tokens]]
- [[Errores Comunes#Mercury accountNumber vs UUID]]
- [[Errores Comunes#Mercury endpoint singular vs plural]]
- [[changelog#2026-04-14]] — registro detallado del trabajo
- [[memoria#Integraciones]] — contexto de decisiones
