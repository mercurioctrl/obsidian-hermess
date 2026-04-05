---
jira_key: "COB-246"
aliases: ["COB-246"]
summary: "API - Refactor - Alterar saldo proveedor, en caso de que el concepto sea un \"pago de factura\" o \"pago proveedor\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-12-05 10:29"
updated: "2024-02-13 03:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-246"
---

# COB-246: API - Refactor - Alterar saldo proveedor, en caso de que el concepto sea un "pago de factura" o "pago proveedor"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-05 10:29 |
| Actualizado | 2024-02-13 03:46 |
| Etiquetas | ninguna |
| Jira | [COB-246](https://bluinc.atlassian.net/browse/COB-246) |

## Relaciones

- **Padre:** [[COB-101 - Feat - Realizar salida de caja|COB-101]] Feat - Realizar salida de caja
- **is blocked by:** [[COB-247 - APP - Refactor - Agregar al modal de salida un selector de proveedor si el id|COB-247]] APP - Refactor - Agregar al modal de salida un selector de proveedor si el id del concepto es 3 o 35
- **is blocked by:** [[COB-104 - API - Feat - Realizar salida|COB-104]] API - Feat - Realizar salida

## Descripcion

Basándonos en [link](https://lioteam.atlassian.net/browse/COB-104) se debe hacer un refactor del recurso 

```
POST {URL_API}/v1/cashOut
```

Para que en los casos que el concepto tenga `id` 3 o 35; osae ambos conceptos,* pago a proveedores* y *pago de facturas*

Se debe hacer la imputación de la cuenta corriente del proveedor. 

En este caso, a partir de ahora se recibirá el parámetro `providerId` dentro del objeto  (el parámetro se incluirá en [link](https://lioteam.atlassian.net/browse/COB-247))

```
[
{
  ammount: 250.33,
  paymentMethodId:2,
  outputConceptId: 3,
  reference: "Este es un texto de referencia.",
  currencyQuote: 140.5,
  providerId: 4
},
{
  ammount: 250.33,
  paymentMethodId:2,
  outputConceptId: 2,
  reference: "Este es un texto de referencia.",
  currencyQuote: 140.5
},
{
  ammount: 250.33,
  paymentMethodId:2,
  outputConceptId: 2,
  reference: "Este es un texto de referencia.",
  currencyQuote: 140.5
}
]
```
