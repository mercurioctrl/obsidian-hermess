---
jira_key: "PED-1094"
aliases: ["PED-1094"]
summary: "API - Refactor - Agregar estados de la orden al detalle de la misma"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-31 22:42"
updated: "2025-09-03 10:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1094"
---

# PED-1094: API - Refactor - Agregar estados de la orden al detalle de la misma

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-31 22:42 |
| Actualizado | 2025-09-03 10:45 |
| Etiquetas | ninguna |
| Jira | [PED-1094](https://bluinc.atlassian.net/browse/PED-1094) |

## Relaciones

- **Padre:** [[PED-1093 - Ver detalle de orden|PED-1093]] Ver detalle de orden
- **has action item:** [[PED-1095 - APP - Refactor - Agergar estados de la orden al detalle de la misma|PED-1095]] APP - Refactor - Agergar estados de la orden al detalle de la misma

## Descripcion

Agregaremos al detalle de la orden `statusId` y `statusDescription` para que esten disponibles para ser mostrados en el modal, cuando no vengo desde el listado y no pude verlo (cuando abro el modal desde una cc u otro repo)

```
GET {API_URL}/v1/orders/{branch-order}
```

```
{
    "date": "2025-08-29 16:10:46",
    "makeSaleDate": "2025-08-29 16:25:56",
    "orderNumber": "10427127",
    "branchNumber": "0002",
    "albnumNumber": "00630116",
    "realAlbumNumber": null,
    "clientEmail": "compras@jadetech.com.ar",
    "clientName": "AQUINO FERNANDO EZEQUIEL",
    "clientId": 47491,
    "userId": 62517,
    "observation": null,
    "status": "S",
    "statusId": null, <-- Se agrega
    "statusDescription": "Pendiente",  <-- Se agrega   
    "invoice": "A000400162635",
    "token": "137b51df6939b7c84652eaf4cb6a44",
    "voucherId": 586057,
    "seller": "Albarracin",
    "sellerId": "30",
    "sellerCreator": "Albarracin Julian",
    "sellerIdCreator": "30",
    "items": [
        {
            "title": "DISCO SSD PATRIOT BURST ELITE SOLID 480 GB SATA3  PE000777",
            "sku": "PBE480GS25SSDR",
            "id": 109353,
            "price": {
                "value": 25.857,
                "iva": 10.5,
                "finalPrice": 28.571984999999998,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 28.067,
                    "B": 27.533727,
                    "C": 27.168856,
                    "D": 25.857,
                    "E": 25.415
                },
                "savedPriceList": "D",
                "currencyQuote": 1360,
                "effectiveness": 17,
                "profit": 3.76,
                "internalTax": 0,
                "averageCost": 22.1,
                "costForSale": null
            },
            "warranty": "12 meses",
            "amount": 1,
            "refundAmount": 0,
            "stock": 209,
            "stockLio": 0,
            "stockInOrders": 8,
            "availableStock": 201
        }
    ],
    "currencyQuote": 1360,
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
    "niva": 1,
    "percepcion": 0.77571,
    "percepcionArba": 0,
    "whoBuild": "garraza",
    "whoAuthorized": "spasserini",
    "addressFinal": null,
    "postalCodeFinal": null,
    "provinceNameFinal": null,
    "localityNameFinal": null
}
```
