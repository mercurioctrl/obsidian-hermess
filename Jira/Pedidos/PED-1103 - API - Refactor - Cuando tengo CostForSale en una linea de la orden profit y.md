---
jira_key: "PED-1103"
aliases: ["PED-1103"]
summary: "API - Refactor - Cuando tengo CostForSale en una linea de la orden profit y effectiveness deben usar ese monto para calcular utilidad y no el costopromedio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-09-17 09:10"
updated: "2025-11-10 09:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1103"
---

# PED-1103: API - Refactor - Cuando tengo CostForSale en una linea de la orden profit y effectiveness deben usar ese monto para calcular utilidad y no el costopromedio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-17 09:10 |
| Actualizado | 2025-11-10 09:40 |
| Etiquetas | ninguna |
| Jira | [PED-1103](https://bluinc.atlassian.net/browse/PED-1103) |

## Relaciones

- **Padre:** [[PED-1093 - Ver detalle de orden|PED-1093]] Ver detalle de orden

## Descripcion

En la linea de lo que vimos ayer, modificaremos ambos parametros para asimilar los casos donde tenemos el costo diferenciado del que usamos siempre (ncosteprom)

```
GET {API_URL}/v1/orders/{branch-order}
```

```
{
    "date": "2025-09-16 14:58:35",
    "makeSaleDate": "2025-09-16 15:00:39",
    "orderNumber": "10425759",
    "branchNumber": "0002",
    "albnumNumber": "00628442",
    "realAlbumNumber": null,
    "clientEmail": "sfdsdf@sdf.com",
    "clientName": "Emanuel Ferreyra",
    "clientId": 76712,
    "userId": 66962,
    "observation": null,
    "status": "S",
    "invoice": null,
    "token": null,
    "voucherId": null,
    "seller": "Sistema",
    "sellerId": "12 ",
    "sellerCreator": "Sistema Web",
    "sellerIdCreator": "12 ",
    "items": [
        {
            "title": "LAMPARA PHILIPS HUE PORTATIL",
            "sku": "915005822401",
            "id": 111510,
            "price": {
                "value": 98.51806,
                "iva": 21,
                "finalPrice": 119.2068526,
                "percepcion": null,
                "letra": "A",
                "priceList": {
                    "A": 98.51806,
                    "B": 96.64621686000001,
                    "C": 95.36548208,
                    "D": 96.01336,
                    "E": 96.01336
                },
                "savedPriceList": "A",
                "currencyQuote": 1310,
                "effectiveness": 18, <-- REFACTOR
                "profit": 15.03, <-- REFACTOR
                "internalTax": 0,
                "averageCost": 83.49,
                "costForSale": null,
                "niva": null
            },
            "warranty": "6 meses",
            "amount": 1,
            "refundAmount": 0,
            "stock": 3,
            "stockLio": 0,
            "stockInOrders": 0,
            "availableStock": 3
        }
    ],
    "currencyQuote": 1310,
    "shippingMethodId": null,
    "shippingMethodName": null,
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
    "niva": 3,
    "percepcion": 0,
    "percepcionArba": 0,
    "whoBuild": null,
    "whoAuthorized": null,
    "addressFinal": null,
    "postalCodeFinal": null,
    "provinceNameFinal": null,
    "localityNameFinal": null,
    "statusId": 2,
    "statusDescription": "Autorizados. Pendiente a despachar",
    "cancelled": 0,
    "delivered": null
}
```
