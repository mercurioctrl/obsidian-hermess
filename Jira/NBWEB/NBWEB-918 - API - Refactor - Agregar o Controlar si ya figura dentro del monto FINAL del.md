---
jira_key: "NBWEB-918"
aliases: ["NBWEB-918"]
summary: "API - Refactor - Agregar / o Controlar si ya figura dentro del monto FINAL del listado de comprobante en mi cuenta INTERNAL TAX"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-04 18:11"
updated: "2024-11-06 03:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-918"
---

# NBWEB-918: API - Refactor - Agregar / o Controlar si ya figura dentro del monto FINAL del listado de comprobante en mi cuenta INTERNAL TAX

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-04 18:11 |
| Actualizado | 2024-11-06 03:24 |
| Etiquetas | ninguna |
| Jira | [NBWEB-918](https://bluinc.atlassian.net/browse/NBWEB-918) |

## Relaciones

- **Padre:** [[NBWEB-610]] API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro de Mi Cuenta

## Descripcion

```
GET {API_URL}/v1/miCuenta/comprobantes  
```

```
[
    {
        "cae": 74188506857016,
        "branch": "0003",
        "invoiceNumber": "00005823",
        "invoiceType": "B",
        "invoiceDate": "2024-04-30",
        "invoiceLabel": "NOTA DE CREDITO",
        "clientName": "Catriel (no usar)",
        "clientId": 19227,
        "subtotal": {
            "currencyQuote": 894,
            "subTotal": 1,
            "subTotalIva": 1.105,
            "perceptionsIIBB": 0,
            "subTotalFinal": 1.105, <- Se agrega al monto final
            "currency": "DOL"
        },
        "voucherId": 533621,
        "voucherUrl": "https:\/\/omega.comprobantes.lio.red\/voucher\/F\/533621\/5a99384b2634bc3b9597ad22777670?show=1"
    },
   ...
```
