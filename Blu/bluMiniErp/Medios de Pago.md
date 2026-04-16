# Medios de Pago

Tres integraciones financieras: **MercadoPago** (procesador, ARS), **Stripe** (procesador, USD/ARS) y **Mercury** (banco, USD).

Cada una tiene su propio controller, banco vinculado en `configuracion`, y pagina en el [[Frontend]].

## Configuracion comun

Credenciales en la tabla `configuracion` (singleton). Ver [[Base de Datos#configuracion]].

Las secret keys **nunca se devuelven en `GET /config`** — se reemplazan por flags booleanos.

---

## MercadoPago

### Autenticacion
Bearer token (`mp_access_token`). OAuth adicional (`mp_oauth_token`) para settlement reports.

### Endpoints usados
| Metodo | Ruta MP | Para que |
|--------|---------|----------|
| GET | `/users/me` | Test de conexion |
| GET | `/v1/payments/search` | Pagos intra-MP |
| GET | `/v1/account/settlement_report/search` | Listar reportes |
| POST | `/v1/account/settlement_report` | Crear reporte |
| POST | `/checkout/preferences` | Crear link de pago |

### Tabla local: mercadopago_movimientos

MP no tiene endpoint de historial completo. Se persisten movimientos localmente con upsert por `mp_id`. Ver [[Base de Datos#mercadopago_movimientos]].

### Clasificacion de direccion

```
operation_type = 'account_fund' -> SIEMPRE ingreso
collector_id = propio userId    -> ingreso
collector_id = otro o null      -> egreso
```

> `account_fund` con `collector_id = null` debe ser ingreso. Ver [[Errores Comunes#MercadoPago account_fund clasificado como egreso]].

### Balance
El saldo mostrado es el del banco vinculado, actualizable manualmente. El calculado desde DB local es referencial (~0.5% error).

### Link de pago
- Con `presupuesto_id`: total del presupuesto (solo APROBADO/FACTURADO)
- Con `cliente_id` + `monto`: cobro libre
- Convierte USD->ARS automaticamente. Ver [[Reglas de Negocio#Monedas y Tipo de Cambio]]

### OAuth para settlement reports
Se necesita un token obtenido via OAuth Authorization Code con scope Facturacion.

---

## Stripe

### Autenticacion
HTTP Basic Auth: `secret_key` como username, password vacio.

### Endpoints usados
| Metodo | Ruta | Para que |
|--------|------|----------|
| GET | `/v1/balance` | Test + saldo real |
| GET | `/v1/balance_transactions` | Historial |
| POST | `/v1/checkout/sessions` | Crear link de pago |

### Particularidades
- **Montos en centavos**: dividir por 100 al mostrar, multiplicar por 100 al enviar
- **Timestamps Unix**: convertir con `Carbon::createFromTimestamp()`
- **Balance real disponible** via API (a diferencia de MP)
- **Direccion**: positivo = ingreso, negativo = egreso

### Link de pago (Checkout Session)
- Param `moneda_cobro` opcional para forzar conversion
- Respuesta incluye `url` (no `init_point` como MP)

### Diferencias con MP

| Aspecto | MercadoPago | Stripe |
|---------|-------------|--------|
| Auth | Bearer token | HTTP Basic |
| Montos | En la moneda | En centavos |
| Balance real | No (403) | Si |
| Link de pago | `init_point` | `url` |
| Movimientos | DB local | API directa |

---

## Mercury

### Autenticacion
Bearer token (`mercury_api_key`).

### Particularidades criticas

**account_id es el UUID — nunca el accountNumber:**
```
id: "a28d3184-..."          <- ESTE se usa en las rutas
accountNumber: "261238..."  <- NO usar en API
```

Ver [[Errores Comunes#Mercury accountNumber vs UUID]].

**Rutas singulares vs plurales:**
```
GET /accounts              -> lista de cuentas OK
GET /account/{uuid}        -> detalle OK (SINGULAR)
GET /accounts/{uuid}       -> 404!
```

Ver [[Errores Comunes#Mercury endpoint singular vs plural]].

### Endpoints usados (cuenta corriente)
| Metodo | Ruta | Para que |
|--------|------|----------|
| GET | `/accounts` | Test — lista cuentas |
| GET | `/account/{uuid}` | Balance real |
| GET | `/account/{uuid}/transactions` | Historial |

### Balance dual
Devuelve **dos fuentes separadas**: saldo real Mercury API (tiempo real) + saldo contabilidad interna (banco vinculado en DB).

### Mercury Invoicing API (desde 2026-04-14)

Mercury **sí tiene** función de cobro vía la **API de Accounts Receivable** (solo cuentas con plan de suscripción que incluye Invoicing). Reemplaza la afirmación previa de "Mercury es solo banco, no procesador".

**Servicio centralizado:** `app/Services/MercuryInvoiceService.php` — wrapper de toda la lógica HTTP. Métodos: `listInvoices`, `getInvoice`, `getInvoicePdf` (devuelve bytes), `cancelInvoice`, `createInvoice`, `findOrCreateCustomer`, `createInvoiceFromPresupuesto`, `refreshPresupuestoInvoiceStatus`, `static hostedUrl(slug)`.

**Endpoints API consumidos:**

| Metodo | Ruta | Para que |
|--------|------|----------|
| GET    | `/ar/invoices` | Listado cursor-based (limit, order, start_after, end_before) |
| GET    | `/ar/invoices/{id}` | Detalle (incluye `lineItems`) |
| POST   | `/ar/invoices` | Crear |
| PATCH  | `/ar/invoices/{id}` | Actualizar |
| POST   | `/ar/invoices/{id}/cancel` | Cancelar |
| GET    | `/ar/invoices/{id}/pdf` | **Descarga el PDF** (no documentado en reference oficial pero existe) |
| GET    | `/ar/customers` / `/ar/customers/{id}` | Listar / get |
| POST   | `/ar/customers` | Crear |
| PATCH/DELETE | `/ar/customers/{id}` | Actualizar / borrar |

**Shape clave del Invoice:**
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
  "invoiceDate", "dueDate", "ccEmails": [...]
}
```

**URLs derivadas del `slug`** (no vienen en el response, hay que construirlas):
- `https://app.mercury.com/invoice/{slug}` — vista hosteada del invoice (link compartible "ver online")
- `https://app.mercury.com/pay/{slug}` — landing de pago (lo que se manda en el email como "Depósito Bancario")

**Limitaciones críticas:**
- **Mercury solo opera en USD.** Para presupuestos ARS hay que convertir con tasa de cambio (precarga de `pres.tasa_cambio` o BCRA via dolarapi.com). La tasa usada se persiste en `presupuestos.mercury_invoice_tasa_cambio` para auditoría.
- **IP whitelist:** los API tokens pueden tener IP whitelist activa. Si está activa, solo funciona desde IPs autorizadas (`errorCode: ipNotWhitelisted`). Las IPs egress de dev y prod son distintas — agregar las dos. Ver [[Errores Comunes#Mercury IP whitelist en API tokens]].
- **NO existen en la API:** "marcar como pagado" (Mercury detecta payments automáticamente cuando el customer paga vía hosted link), "resend email" (sólo se controla con `sendEmailOption` al crear), recurring invoices, product catalog.
- **`amount` en dólares enteros**, no cents (lección: 1500 = $1500 USD, no $15.00).

**Persistencia local en el ERP** (migraciones 0049-0051):
- `clientes.mercury_customer_id` — uuid del customer en Mercury, persistido tras find-or-create. Permite resolver el nombre del cliente al listar invoices y reutilizar el customer entre presupuestos.
- `presupuestos.mercury_invoice_id`, `mercury_invoice_slug`, `mercury_invoice_status`, `mercury_invoice_tasa_cambio`, `mercury_invoice_created_at` — referencia + auditoría del invoice creado desde el presupuesto.
- `presupuestos.mercadopago_payment_url` y `presupuestos.stripe_payment_url` — antes los links se generaban on-the-fly y eran ephemeral; ahora se persisten al crearlos para reusarlos en el modal de envío de invoice por email.

### Diferencias con MP y Stripe
- **Montos en USD directamente** (no centavos)
- **Sin DB local** para movimientos de cuenta (los invoices sí persisten referencia)
- **Hosted invoice + payment landing** propios — el cliente paga directamente en Mercury (ACH debit, credit card opcional), no se necesita webhook para detectar pago
- Tres niveles de URL del invoice: el `id` interno, el `/invoice/{slug}` (vista compartible), el `/pay/{slug}` (landing de pago)

---

## Frontend - Paginas dedicadas

- `/mercadopago` - Saldo contabilidad + calculado, importar movimientos, desglose. Ver [[Frontend#Modulo MercadoPago]]
- `/mercury` - Saldo real + contabilidad, ajuste manual, movimientos. Ver [[Frontend#Modulo Mercury]]
- `/bancos-cajas` - Badges MP/Stripe/Mercury, botones sync y movimientos

## Flujo de reconciliacion

```
Banco vinculado en DB (saldo_actual)
    | se actualiza manualmente con /sync

MercadoPago:  pagos + retiros -> DB local -> balance calculado
Stripe:       balance_transactions -> API directa
Mercury:      transactions -> API directa
```

---

## Ver tambien

- [[Backend - API]] - Endpoints de MP, Stripe, Mercury
- [[Base de Datos#configuracion]] - Credenciales y bancos vinculados
- [[Reglas de Negocio#Monedas y Tipo de Cambio]] - Conversion automatica al cobrar
- [[Frontend]] - Paginas de cada integracion
- [[Errores Comunes]] - Bugs de integraciones externas
