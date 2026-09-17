# Conciliación Impuestos 2026-08 (BLU INC S.R.L.)

Cotejo de las DDJJ que presentó el estudio para **agosto 2026** contra lo que tiene cargado el ERP.
Cotejado el **2026-09-16**. Contribuyente **BLU INC S.R.L.**, CUIT **30-71909207-8** (coincide con `empresas.id = 1`).

Fuente: carpeta `impuestos/` en la raíz del repo — `IVA 08-2026.pdf` (F.2051), `IIBB 08-2026.pdf` (SICOL/AGIP),
y dos certificados de retención de Microglobal Argentina S.A.

Ver [[Modulo Contabilidad]] para cómo el ERP arma la liquidación.

> [!summary] Resultado
> **Coincide.** Ventas, débito fiscal y base de IIBB dan **exacto al peso**.
> La única diferencia es de **$737,10** en el crédito fiscal de IVA, y está **sin explicar**.

---

## Panorama de agosto 2026

### Ventas — una sola factura

| Comprobante | Fecha | Moneda | Cotiz. | Neto ARS | IVA ARS | Total ARS |
|---|---|---|---:|---:|---:|---:|
| **A 0003-00000007** | 20/08/2026 | USD 2.066,12 | 1515 | 3.130.171,80 | 657.343,35 | 3.787.515,15 |

Es el único comprobante AFIP de agosto (`comprobantes_afip.id = 9`, estado `EMITIDA`).
De acá salen **todos** los números de venta de las dos DDJJ.

### Compras con crédito fiscal — dos gastos

| Fecha comp. | Proveedor (CUIT) | Nro | Neto | IVA 21% | Total | Gasto |
|---|---|---:|---:|---:|---:|---|
| 18/08/2026 | 30-71930468-7 | 73 | 650.000,00 | 136.500,00 | 786.500,00 | `id 201` Servicio Técnico evento 25/08 |
| 18/08/2026 | 30-70974890-0 | 964 | 1.614.240,00 ⚠️ | 302.400,00 | 1.916.640,00 | `id 202` Evento 25-08 Mirador Central |
| | | | | **438.900,00** | | |

⚠️ El neto de la segunda fila es el *implícito* (`monto − iva_monto`), no el cargado. Ver [[#Gasto 202 con el monto inconsistente]].

### IVA — F.2051, presentado 15/09/2026, transacción 1194370996

| Concepto | Estudio | ERP | Dif |
|---|---:|---:|---:|
| Débito fiscal | 657.343,35 | 657.343,35 | **0,00** ✅ |
| Crédito fiscal | 439.637,10 | 438.900,00 | **−737,10** ❓ |
| Saldo técnico a favor de ARCA | 217.706,25 | 218.443,35 | +737,10 |
| **Saldo de impuesto a favor de ARCA** | **217.706,25** | — | |

### IIBB — SICOL CABA, F.5220, vto. y pago 17/09/2026

| Concepto | Estudio | ERP | Dif |
|---|---:|---:|---:|
| Base imponible (act. 620900) | 3.130.171,80 | 3.130.171,80 | **0,00** ✅ |
| Alícuota | 3,000 % | 3,00 % | ✅ |
| Impuesto determinado | 93.905,15 | 93.905,15 | **0,00** ✅ |
| Retenciones | 93.899,70 | *no modelado* | — |
| **Total a ingresar** | **5,45** | *diría 93.905,15* | |

### Ganancias

**Sin comparar** — no hay DDJJ en la carpeta (es anual). De referencia, el ERP calcula para agosto:
ganancia base 865.931,80 × 35 % = **303.076,13** (bajaría a **242.092,13** si se corrige el gasto 202).

---

## Retenciones sufridas — son de SEPTIEMBRE, no de agosto

Los dos certificados de **Microglobal Argentina S.A.** (CUIT 30-66153522-5) son del **09/09/2026**, sobre
la orden de pago O0000-00080645, y aplican a facturas de **septiembre**. **No entran en la DDJJ de agosto.**

| Factura | ERP (USD @ 1535) | Base en el certificado |
|---|---:|---:|
| A 0003-00000008 (01/09/2026) | 991,60 → 1.522.106,00 | 1.522.106,00 ✅ |
| A 0003-00000009 (01/09/2026) | 2.000,00 → 3.070.000,00 | 3.070.000,00 ✅ |
| | **4.592.106,00** | 4.592.106,00 ✅ |

- **Ganancias RG 830** (cert. 17366, concepto RGL094): base 4.592.106,00 − 67.170,00 no sujeto
  = 4.524.936,00 → retenido **90.503,60**
- **IIBB CABA 3 %** (cert. 21380, R-122 V2): 3.070.000 × 3 % = 92.100,00 + 1.522.106 × 3 % = 45.663,18
  → total **137.763,18** (recalculado: da exacto)

Las **retenciones de 93.899,70** que descuenta la DDJJ de agosto son de **otros** certificados
(sobre facturas anteriores) que no están en la carpeta.

---

## Qué hay que averiguar

### 1. El hueco de $737,10 en el crédito fiscal — LO PRINCIPAL

El F.2051 declara **439.637,10** de crédito fiscal; el ERP tiene **438.900,00**. Faltan **737,10**.

**Hipótesis del momento: son percepciones de IVA.** Hay que confirmarlo, y tiene un problema previo:

> [!warning] Las percepciones normalmente NO van en crédito fiscal
> El crédito fiscal es el IVA de las compras (saldo **técnico**). Las percepciones y retenciones de IVA
> sufridas son **ingresos directos** y van en la *posición mensual*, como saldo de **libre disponibilidad**.
>
> Y en este F.2051 la posición mensual **no tiene ningún ingreso directo**: el saldo técnico a favor de ARCA
> (217.706,25) es **idéntico** al saldo de impuesto final (217.706,25). Si se hubieran computado percepciones
> del período, el saldo final tendría que haber quedado **por debajo** del técnico. No pasó.
>
> O sea: o no hubo percepciones computadas en el mes, o el estudio las metió dentro del crédito fiscal
> (no es lo estándar). **Es exactamente lo que hay que preguntar.**

**Ojo con la pista falsa:** 737,10 ÷ 0,21 = 3.510,00 da redondo, pero también ÷ 0,105 = 7.020,00
y ÷ 0,27 = 2.730,00. El redondo es el 737,10 — **no indica ni la alícuota ni el proveedor**. No alcanza
para identificar nada.

**Otras causas posibles del mismo residuo** (todas dan 737,10, no se distinguen con los PDFs que hay):
- una compra de agosto **no cargada** en el ERP
- una compra **sí cargada** pero con importe distinto (tipeo, redondeo, otra cotización si era USD)
- una **nota de crédito de compra** que el estudio computó y el ERP no
- una compra a **10,5 % o 27 %** en vez de 21 %
- una de las dos compras del ERP cargada **de menos**

**Cómo se resuelve:** pedir el detalle contra el que diferenciar. El F.2051 trae el **total** del crédito
fiscal, no su composición.
- [ ] Pedirle al estudio el **Libro IVA Compras 08/2026** (el detalle línea por línea)
- [ ] O bajar **"Mis Comprobantes" → Recibidos** de ARCA para 08/2026 (fuente autoritativa)
- [ ] Diferenciar contra el Libro IVA del ERP (`/contabilidad` → descarga Excel de agosto): el ERP tiene
      **dos** líneas de compra; ver cuál es la tercera que tiene el estudio
- [ ] Si resultan ser percepciones: preguntar **en qué línea del F.2051 las imputaron** y por qué la
      posición mensual no bajó

> [!note] Si son percepciones, el ERP nunca va a coincidir — y está bien
> [[Modulo Contabilidad]] **excluye percepciones de compras a propósito** (no son crédito fiscal).
> No es un bug: es una decisión de diseño. Si el estudio las computa ahí, la diferencia es estructural
> y hay que dejarla documentada como tal, no "arreglarla" cargando un gasto.

### 2. Gasto 202 con el monto inconsistente

`gastos.id = 202` ("Evento 25-08 Mirador Central") rompe la regla `monto = subtotal + iva_monto`:

```
precio_unitario 1.440.000 × cantidad 1 + IVA 21 % (302.400) = 1.742.400   ← esperado
monto cargado                                               = 1.916.640   ← +174.240 (exactamente +10 %)
```

- **No afecta el IVA** (el crédito sale de `iva_monto`, que está bien en 302.400)
- **Sí afecta Ganancias**: la liquidación toma el neto como `monto − iva_monto` = 1.614.240 en vez de
  1.440.000 → **infla las compras en 174.240** y baja la base de Ganancias en el mismo monto

- [ ] Averiguar cuál es el importe real: si se desembolsaron **1.916.640**, el que está mal es el
      precio unitario; si se desembolsaron **1.742.400**, el banco/caja quedó descontado de más
- [ ] Ver de dónde salió el +10 % exacto (¿recargo? ¿percepción? ¿edición manual del monto?)

### 3. El ERP no modela retenciones ni percepciones sufridas

No hay tabla ni columna de retenciones/percepciones en **todo** el esquema (verificado por búsqueda en
migraciones, modelos y servicios). Consecuencia concreta:

- El ERP muestra el **impuesto determinado** (IIBB 93.905,15) y nunca el **saldo real a ingresar** (5,45)
- Los certificados de retención que llegan en papel no tienen dónde cargarse ni contra qué imputarse
- Es la brecha conceptual más grande entre el ERP y las DDJJ reales

- [ ] Decidir si se modela (tabla de retenciones/percepciones sufridas imputables al período) o si se
      asume que ese cálculo queda del lado del estudio

---

## Lo que sí quedó validado

- **El etiquetado multi-empresa funciona.** Los tres gastos de agosto de **DIGITO BINARIO** (Bolsas,
  TERMOS, Cafe to Go — **581.338,59** de IVA) quedaron correctamente **fuera** de BLU. Es *por eso* que
  el crédito fiscal calza: si se hubieran mezclado, la diferencia sería de medio millón, no de 737 pesos.
  Ver [[Modulo Contabilidad]] y la nota de multi-empresa.
- **La conversión USD → ARS del ERP es correcta**: las bases de las tres facturas (7, 8 y 9) reproducen
  al peso lo que declararon el estudio y el agente de retención, con cotizaciones distintas (1515 y 1535).
- **La alícuota de IIBB (3 %) y la actividad (620900, servicios de informática n.c.p.)** coinciden con
  lo configurado en el ERP.
