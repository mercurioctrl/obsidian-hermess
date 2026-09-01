# Pagos freelance — Guillermo Avila (QA) · Respaldo Mercury

Documentación de respaldo para **Mercury** de los pagos salientes a un colaborador
**freelance de QA** en el exterior. Complementa a [[caso-mercury-acer]] (que cubre
fondos **entrantes**); este caso cubre pagos **salientes** a colaboradores, que ya se
le explicaron a Mercury como parte de la operatoria de BLU con freelancers en distintos
países.

Se generaron 3 comprobantes PDF profesionales (uno por pago mensual) que documentan
servicios efectivamente prestados y pagos ya realizados vía **USDT / Binance**.

## Prestador del servicio (colaborador)

- **Nombre:** Guillermo Avila
- **Rol:** Freelance QA Analyst / Software Developer
- **Dirección:** Serravalle #315, Residencial San Marino, Irapuato, Guanajuato, C.P. 36625
- **País:** México
- **Teléfono:** +52 1 442 602 2591
- **Email:** g.avila0880@gmail.com

## Cliente

**BLU STUDIO GROUP LLC**

## Servicio

Freelance Quality Assurance (QA) and Software Testing Services — testing manual y
funcional, regression testing, identificación y reporte de bugs, y soporte general de QA.

## Pagos documentados

| Documento (Record No.) | Período | Monto (USDT) | Fecha de pago | Binance Order ID |
|---|---|---|---|---|
| BLU-QA-2026-06 | Junio 2026 | 960.53 | 2026-06-08 | 436124527922372608 |
| BLU-QA-2026-07 | Julio 2026 | 1.386,87 | 2026-07-08 | 441691926367928322 |
| BLU-QA-2026-08 | Agosto 2026 | 921.14 | 2026-08-08 | 447445936996720640 |

- **Método de pago:** USDT vía Binance
- **Beneficiario final:** Guillermo Avila
- **Binance ID:** 433743631 · **Usuario Binance:** Guillermoh

## Documentos generados

3 PDF independientes, US Letter, una página cada uno, en inglés:

- `Guillermo_Avila_QA_June_2026.pdf`
- `Guillermo_Avila_QA_July_2026.pdf`
- `Guillermo_Avila_QA_August_2026.pdf`

**Ubicación local:** `/var/www/blu/bancos/Mercury/Requerimientos/Paymonede/`
Generados con `generate_invoices.py` (HTML + Chrome headless → PDF); los `.html`
fuente quedan junto a los PDF para regenerar si hace falta.

## Decisiones de diseño (importantes para el criterio bancario)

- **Emitido ahora, no retrodatado:** Issue Date = fecha actual de emisión, separada del
  período de servicio y de la fecha efectiva del pago. No se simula que el documento se
  creó en la fecha histórica del pago.
- **Reencuadre como registro retrospectivo:** título **"SERVICE & PAYMENT RECORD"** (no
  "invoice") + aviso explícito: *"...issued on [fecha] to record ... services already
  rendered ... and a payment already completed. It is a record of past services and
  settled payment, not a request for payment."*
- **Sin estado "PAID":** a pedido, se removió el badge/estado "PAID" (y las etiquetas
  "Total Paid"/"Amount Paid" → "Total"/"Amount"). Los datos del pago quedan como registro.
- **Sin datos inventados:** no se agregaron Tax IDs, números de registro, logos ni firmas.
  Dirección/país/teléfono/email fueron provistos explícitamente por el usuario.
- Declaración factual al pie: *"This document records freelance QA and software testing
  services provided to BLU STUDIO GROUP LLC and the corresponding payment made to the
  service provider through Binance."*

## Estado

- [x] 3 PDF generados y verificados (2026-08-26)
- [x] Estado "PAID" removido y datos de contacto/país agregados (2026-09-01)
- [ ] Adjuntar como respaldo ante Mercury si lo solicitan

## Ver también

- [[finanzas]]
- [[caso-mercury-acer]]
- [[bluMiniErp/Modulo Mercury Invoicing|Mercury Invoicing (bluMiniErp)]]
