---
jira_key: "COM-272"
aliases: ["COM-272"]
summary: "API - MVP - Review - Cuando una orden genera un ingreso que no tiene marcado el costo promedio, el costo debe ser el mismo que lleva la orden directo"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-16 10:09"
updated: "2026-01-16 13:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-272"
---

# COM-272: API - MVP - Review - Cuando una orden genera un ingreso que no tiene marcado el costo promedio, el costo debe ser el mismo que lleva la orden directo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-16 10:09 |
| Actualizado | 2026-01-16 13:11 |
| Etiquetas | ninguna |
| Jira | [COM-272](https://bluinc.atlassian.net/browse/COM-272) |

## Relaciones

- **Padre:** [[COM-109]] Generar INGRESO o pedido (a partir de una orden de compra)
- **action item from:** [[COM-190]] API -MVP - Refactor - Elegir si altera o no el costo promedio del item para cada item

## Descripcion

El caso donde se usa `updateAverageCost = TRUE` se hace perfecto, promediando matemáticamente las cantidades.

Pero si `updateAverageCost =  FALSE` entonces no debe dejarlo en cero, sino que debe pisar el `ncosteprom` directamente con el costo que el producto tiene en `price.value`. Actualmente no lo impacta de ninguna manera.

```
https://gamma.api.purchases.lio.red/v1/makeProviderOrderInbound
```

```
{
  "orderNumber": 12733,
  "trackingNumber": null,
  "arrivalDate": null,
  "providerId": "002337",
  "providerName": "Allplus",
  "observation": "",
  "status": "P",
  "voucherPurchaseId": "",
  "countryName": "",
  "warehousesId": 19,
  "buyerName": "Mansilla Florencia",
  "buyerId": 73,
  "currencyQuote": 1310,
  "currencyFiscalQuote": 1,
  "dateVoucherNumber": null,
  "distributeTaxes": [],
  "items": [
    {
      "id": 125129,
      "title": "DISCO SSD ADATA SU650 2.5 1TB",
      "sku": "ASU650SS-1TT-R",
      "price": {
        "value": 23,
        "iva": 0,
        "subtotal": 0,
        "subtotalFinal": 0
      },
      "warranty": "Life Warranty",
      "amount": 100,
      "position": null,
      "taxPosition": [],
      "amountEntered": null,
      "updateAverageCost": FALSE, <--- CUANDO ESTO ES FALSO
      "suggestedCost": null,
      "totalItemTax": 0,
      "checkbox": false,
      "moveAmount": 0,
      "positions": [],
      "partial": 100,
      "amountClass": "green",
      "priceClass": "green"
    }
  ]
}
```
