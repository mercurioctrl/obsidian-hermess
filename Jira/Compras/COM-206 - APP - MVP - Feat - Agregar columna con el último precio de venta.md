---
jira_key: "COM-206"
aliases: ["COM-206"]
summary: "APP - MVP - Feat - Agregar columna con el último precio de venta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2025-09-30 16:14"
updated: "2025-10-24 10:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-206"
---

# COM-206: APP - MVP - Feat - Agregar columna con el último precio de venta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2025-09-30 16:14 |
| Actualizado | 2025-10-24 10:16 |
| Etiquetas | ninguna |
| Jira | [COM-206](https://bluinc.atlassian.net/browse/COM-206) |

## Relaciones

- **Padre:** [[COM-77 - Editar orden de compra|COM-77]] Editar orden de compra
- **action item from:** [[COM-205 - API - MVP - Feat - Agregar columna con el último precio de venta|COM-205]] API - MVP - Feat - Agregar columna con el último precio de venta

## Descripcion

GET 

```
https://gamma.api.purchases.lio.red/v1/providerOrder/12259
```

Agregar nueva columna que solo es de lectura `lastCostForSale` para dar información sobre el útimo precio de venta de ese item

```
{
    "orderNumber": 12259,
    "trackingNumber": null,
    "arrivalDate": null,
    "providerId": "002320",
    "providerName": "MSI COMPUTER CORP.",
    "observation": "",
    "status": "P",
    "voucherPurchaseId": "",
    "countryId": 7,
    "countryName": "Argentina",
    "buyerName": "Obari Anabel",
    "buyerId": 72,
    "currencyQuote": 1310,
    "currencyFiscalQuote": 0,
    "distributeTaxes": [],
    "items": [
        {
            "id": 123834,
            "title": "ana usada",
            "sku": "ana usada",
            "price": {
                "value": 0,
                "iva": 0,
                "finalPrice": 0
            },
            lastCostForSale:0 // <---- NUEVO
            "warranty": "0 meses",
            "amount": 1,
            "position": null,
            "taxPosition": null,
            "amountEntered": ".000"
        }
    ]
}
```

[adjunto]


Corresponde a la tarea 12 de [link](https://docs.google.com/spreadsheets/d/18TUSaVG3bY_lMLunZ3kDCRlLnKpQV-_BPfrtbL4pHNA/edit?usp=sharing)
