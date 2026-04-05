---
jira_key: "PED-913"
aliases: ["PED-913"]
summary: "API - Refactor - Incluir costo promedio en el detalle de una orden para cada item"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-20 11:37"
updated: "2025-01-03 02:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-913"
---

# PED-913: API - Refactor - Incluir costo promedio en el detalle de una orden para cada item

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-20 11:37 |
| Actualizado | 2025-01-03 02:06 |
| Etiquetas | ninguna |
| Jira | [PED-913](https://bluinc.atlassian.net/browse/PED-913) |

## Relaciones

- **Padre:** [[PED-497]] Ver orden de compra
- **has action item:** [[PED-910]] APP - MVP - Refactor - Seleccionar costo para el item de una orden

## Descripcion

Refactorizaremos el recurso 

```
GET {API_URL}/v1/orders/{branch}-{order}
```

Para poder traer el dato `[NewBytes_DBF].[dbo].[articulo].ncosteprom` llamado `averageCost`

```
{
    "date": "2024-12-20 11:28:26",
    "makeSaleDate": "2024-12-20 11:30:09",
    "orderNumber": "10383700",
    "branchNumber": "0002",
    "albnumNumber": "00601982",
    "realAlbumNumber": null,
    "clientEmail": "digitalcentercj@gmail.com",
    "clientName": "MU\u00d1OZ ARGUELLO MARIA EUGENIA",
    "clientId": 75648,
    "userId": 66080,
    "observation": null,
    "status": "S",
    "invoice": null,
    "token": null,
    "voucherId": null,
    "seller": "Antonella",
    "sellerId": "47",
    "sellerCreator": "",
    "sellerIdCreator": null,
    "items": [
        {
            "title": "PROCESADOR AMD (AM4) RYZEN 7 5700X (SIN COOLER)",
            "sku": "100-100000926WOF",
            "id": 116714,
            "price": {
                "value": 195.29957,
                "iva": 10.5,
                "finalPrice": 215.80602484999997,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 212.78787,
                    "B": 208.74490047,
                    "C": 205.97865816,
                    "D": 195.29957
                },
                "savedPriceList": "D",
                "currencyQuote": 1044,
                "effectiveness": 9.11,
                "profit": 16.3,
                "internalTax": 0
            },
            "warranty": "36 meses",
            "amount": 1,
            "refundAmount": 0,
            "stock": 22,
            "stockLio": 0,
            "stockInOrders": 2,
            "availableStock": 20
        }
    ],
    "currencyQuote": 1044,
    "shippingMethodId": 3999,
    "shippingMethodName": "Retiro de cliente en Local    ",
    "tracking": null,
    "packageGrouper": null,
    "localityId": null,
    "localityName": null,
    "provinceId": null,
    "provinceName": null,
    "alphaCode": null,
    "phoneNumber": null,
    "postalCode": null,
    "customerAddressId": null,
    "address": null,
    "niva": 1,
    "percepcion": 0,
    "whoBuild": null,
    "whoAuthorized": null,
    "addressFinal": null,
    "postalCodeFinal": null,
    "provinceNameFinal": null,
    "localityNameFinal": null
}
```
