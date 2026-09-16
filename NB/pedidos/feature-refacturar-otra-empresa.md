# Feature: Refacturar por otra empresa

Rama `feature/refacturar-otra-empresa` (2026-09-16, back + front). Botón derecho sobre un pedido **ya liquidado y facturado** → **"Refacturar por otra empresa"**: acredita, corrige la liquidación **sin borrarla** y vuelve a facturar por el emisor elegido.

## El problema

La empresa que factura a un cliente sale de `clientes.voucherCompanyCode`. Según cuál sea, la factura la emite **NB DISTRIBUIDORA MAYORISTA SRL** (que percibe IIBB) o **DIGITO BINARIO SRL** (que no), según `NewBytes_DBF.dbo.FP_Empresas.percepciones` (CODEMP 04 → 1, CODEMP 05 → 0).

Cuando un cliente que factura por DIGITO deposita en la cuenta de NB, hay que refacturarle por NB. Eso ya se podía hacer a mano (`POST /v1/creditToRebill` + cambiar el `voucherCompanyCode` + refacturar), **pero el pedido quedaba mal**: se había liquidado sin percepciones y la factura nueva las necesita.

## Endpoints

Todos bajo el permiso **`rebillCompany`** (`RebillCompanyMiddleware`).

| Método | Ruta | Qué hace |
|---|---|---|
| `GET` | `/v1/rebillCompany/{pedido}/companies` | Empresa actual + empresas destino elegibles |
| `GET` | `/v1/rebillCompany/{pedido}/preview?companyCode=4` | Comparativo, **sin efectos** |
| `POST` | `/v1/rebillCompany/{pedido}` | Ejecuta. **Emite comprobantes fiscales reales** |

`{pedido}` acepta tres formas (`RebillCompanyService::resolveOrderId()`): `X000200664885` (ID_NROREMCLI_ENC), `0002-00664885` (sucursal + **remito**) o `0002-10481864` (sucursal + **pedido**). El remito tiene prioridad; si un pedido generó más de un remito devuelve 409 en vez de elegir a ciegas.

El `POST` recibe `expectedTotal`, el total que el operador vio en el preview: si el pedido cambió desde entonces, corta con 409 **antes de emitir nada**.

## Los 7 pasos

```
1. valida y calcula            lo que puede fallar por datos, falla antes de AFIP
2. abre auditoría              guarda el voucherCompanyCode original
3. nota de crédito             IRREVERSIBLE (AFIP) + libera el pedido
4. reliquida                   totales del remito + ajuste de cuenta corriente
5. cambia voucherCompanyCode
6. factura                     IRREVERSIBLE (AFIP)
7. revierte voucherCompanyCode (finally)
```

Entre 3 y 6 hay una ventana donde el pedido queda acreditado y sin facturar. Si corta ahí no se revierte la NC (no se puede): queda el paso en la auditoría.

**El orden del paso 6 importa:** `getVoucherType()` pregunta a la API de comprobantes qué tipos tiene el cliente, y eso depende de su empresa. Va **después** del paso 5 o la factura sale por la empresa vieja.

## Cómo se calcula la percepción

Manda **`FP_Empresas.percepciones` de la empresa destino**, con las alícuotas del cliente (`clientes.percepcion` = CABA, `clientes.percepcion_arba` = ARBA) sobre `MS_REMITO_CABECERA.TOTALSINIVA`.

Se **ignora `clientes.excluirPercepcion`**, a diferencia de la liquidación original (`CreateOrderRepository::dataHeader`). Ese flag refleja la empresa con la que se facturaba antes: está en **1 en los 96.432 clientes de DIGITO**. La sucursal `0010` sigue anulando siempre porque no lleva factura fiscal.

El total intercambia **solo** el componente de percepción:

```
totalNuevo = totalActual - percepciónActual + percepciónNueva
```

No se recalculan neto, IVA ni impuestos internos: eso reproduciría el riesgo de no dar igual que lo liquidado (cotización manual, cabeceras unificadas por dos alícuotas de IVA, redondeos).

> **Dato:** el 85 % de los clientes de DIGITO tiene ambas alícuotas en 0, así que para ellos la refacturación solo cambia el emisor. No es un dato faltante: entre los que ya facturan por NB, 439 de 469 también las tienen en 0. Por eso el modal muestra el monto calculado antes de confirmar.

## Qué escribe

| Tabla | Acción |
|---|---|
| `MS_REMITO_CABECERA` | UPDATE `IMPPERCEP`, `TOTALREMITO` |
| `MS_REMITO_PERCEPCIONES` | upsert (la liquidación solo crea la fila si hay percepción) |
| `MC_ENLACE_REMITOS_FORMASPAGO` | UPDATE `EVFP_IMPORTE` |
| `MC_CCORRIENTES_MOVIMIENTOS` | **INSERT** de un movimiento de ajuste |
| `clientes.voucherCompanyCode` | UPDATE + revert |
| `NB_WEB.dbo.refacturacion_empresa` | INSERT + avance de estado |

### UPDATE relativo, no pisar el total

`TOTALREMITO` es de tipo **`real`** (4 bytes) y guarda valores como `49.87476348877`. Escribir un total recalculado y redondeado a 2 decimales le mete deriva **aunque la percepción no cambie**. Todo va como `col = col + :delta`; el redondeo es solo de presentación, en `RebillPreviewDto`.

### La cuenta corriente lleva un movimiento nuevo

No se edita el cargo de la liquidación (`TR_CODIGO = 24`). Se asienta uno nuevo por la diferencia: **TR 32 "Débitos Varios"** si la percepción sube, **TR 16** si baja.

La deuda original **puede estar ya cancelada** (sobre un remito conviven el cargo 24 y las imputaciones de pago 42). Pisar ese asiento escondería la deuda nueva dentro de uno saldado y reescribiría un extracto ya emitido. El saldo se calcula sumando todos los movimientos con signo por `TR_CODIGO`, así que el ajuste entra sin tocar el historial. Ver [[contexto#Cuenta corriente y comprobantes]].

Efecto colateral bueno: como el cargo original no se toca, no hay que regenerar su HMAC (`GenerateHmac` firma un JSON que incluye `CC_IMPORTEUSD`).

> **Gotcha:** buscar "el último movimiento del remito" con `ORDER BY ID_CCMOVIMIENTO DESC` **agarra un pago**, no el cargo. Hay que filtrar por `TR_CODIGO = 24`. Se detectó justo antes de escribir la fase de ejecución, cuando el preview devolvió un importe en 0.

## Auditoría

`NB_WEB.dbo.refacturacion_empresa` no es opcional: el proceso cambia el `voucherCompanyCode` del cliente y lo revierte al terminar. Si muere en el medio, **es el único registro del valor original**.

Estados: `iniciado` → `acreditado` → `reliquidado` → `completado`, o `error` con `error_mensaje`.

## Frontend

Ítem en el menú contextual de `pages/orders.vue`, habilitado solo si el pedido está facturado (`record.invoice`) y no es sucursal 10. Modal `components/Orders/RebillCompanyModal.vue`: empresa actual + factura vigente, explicación de qué hace la acción, selector (con tag naranja en las empresas que perciben) y comparativo de percepción / total / cuenta corriente con los avisos del backend.

> El permiso se lee del **token JWT**: después de otorgarlo hace falta **cerrar sesión y volver a entrar**, un refresh no alcanza. Ver [[decision-permiso-nuevo-agente]].

## Migraciones

```
database/sql/2026_09_16_001_add_rebill_company_permission.sql
database/sql/2026_09_16_002_create_refacturacion_empresa.sql
```

Con sus `_drop_`. Ambas aplicadas en **beta**.

## Pendientes

- **Guard faltante:** validar que el emisor de la factura vigente (`FP_FactWebCliEncabezado.CNUMSUC`) coincida con la empresa actual del cliente antes de emitir la NC. Sin eso se puede emitir una nota de crédito de una empresa contra una factura de otra — son CUIT distintos.
- **Incidente de la primera prueba:** se cambió a mano el `voucherCompanyCode` del cliente **26806 (MERCURIO CATRIEL EDUARDO)** de 4 a 5 cuando su factura vigente ya era de NB, así que la NC **`A000600001204` (DIGITO)** quedó anulando la factura **`A000400181390` (NB)**. ~USD 50 en beta, **sin resolver**. Además falta devolver ese cliente a `voucherCompanyCode = 4`.
- **Deuda técnica:** la emisión de la NC está duplicada respecto de `VoucherController::rebill`. No se refactorizó ese endpoint porque es un circuito fiscal en producción y no se puede probar un refactor sin emitir comprobantes reales. Corresponde colapsarlo en `RebillVoucherService`.
- Nada commiteado todavía.

## Ver también

- [[feature-comprobantes-emisor]] — el emisor se resuelve por `CNUMSUC`, no por el prefijo del CFACTURA
- [[feature-cuentas-bancarias-empresa]] — la otra feature que usa `voucherCompanyCode`
- [[decision-permiso-nuevo-agente|Checklist: agregar un permiso nuevo]]
- [[modulo-makesale|MakeSale]] — la liquidación que este proceso corrige
- [[contexto]] — reglas de cuenta corriente y el aviso de que el backend local escribe en beta
- [[changelog#2026-09-16 — Refacturar por otra empresa]]
