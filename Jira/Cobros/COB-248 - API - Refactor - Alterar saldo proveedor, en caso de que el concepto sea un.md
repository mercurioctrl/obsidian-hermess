---
jira_key: "COB-248"
aliases: ["COB-248"]
summary: "API - Refactor - Alterar saldo proveedor, en caso de que el concepto sea un \"pago de factura\" o \"pago proveedor\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-12-05 14:47"
updated: "2024-02-13 03:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-248"
---

# COB-248: API - Refactor - Alterar saldo proveedor, en caso de que el concepto sea un "pago de factura" o "pago proveedor"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-05 14:47 |
| Actualizado | 2024-02-13 03:49 |
| Etiquetas | ninguna |
| Jira | [COB-248](https://bluinc.atlassian.net/browse/COB-248) |

## Relaciones

- **Padre:** [[COB-178]] API - Feat - Realizar transferencia entre bancos
- **blocks:** [[COB-249]] APP - Refactor - Agregar al modal de salida un selector de proveedor si el id del concepto es 3 o 35

## Descripcion

Basándonos en [link](https://lioteam.atlassian.net/browse/COB-177) se debe hacer un refactor del recurso

```
POST {URL_API}/v1/cashOutToBank
```

Para que en los casos que el concepto tenga `id` 3 o 35; osae ambos conceptos,* pago a proveedores* y *pago de facturas*

Se debe hacer la imputación de la cuenta corriente del proveedor.

En este caso, a partir de ahora se recibirá el parámetro `providerId` dentro del objeto (el parámetro se incluirá en 

```
[
{
  ammount: 250.33,
  paymentMethodId:2,
  outputConceptId: 3,
  reference: "Este es un texto de referencia.",
  currencyQuote: 140.5,
  BankId: 1
},
{
  ammount: 250.33,
  paymentMethodId:2,
  outputConceptId: 2,
  reference: "Este es un texto de referencia.",
  currencyQuote: 140.5,
  BankId: 1,
  providerId: 4
}
]
```
