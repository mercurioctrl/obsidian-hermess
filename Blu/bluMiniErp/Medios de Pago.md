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

### Endpoints usados
| Metodo | Ruta | Para que |
|--------|------|----------|
| GET | `/accounts` | Test — lista cuentas |
| GET | `/account/{uuid}` | Balance real |
| GET | `/account/{uuid}/transactions` | Historial |

### Balance dual
Devuelve **dos fuentes separadas**: saldo real Mercury API (tiempo real) + saldo contabilidad interna (banco vinculado en DB).

### Diferencias con MP y Stripe
- **No tiene link de pago** — Mercury es banco, no procesador
- **Montos en USD directamente** (no centavos)
- **Sin DB local** para movimientos

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
