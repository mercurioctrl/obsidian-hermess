---
jira_key: "PED-633"
aliases: ["PED-633"]
summary: "API -  Validar para liquidar que si el pedido tiene marcado un envio en listado de ordenes, que este agregado el item de servicio de transporte"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2024-03-22 18:07"
updated: "2024-04-09 18:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-633"
---

# PED-633: API -  Validar para liquidar que si el pedido tiene marcado un envio en listado de ordenes, que este agregado el item de servicio de transporte

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2024-03-22 18:07 |
| Actualizado | 2024-04-09 18:11 |
| Etiquetas | ninguna |
| Jira | [PED-633](https://bluinc.atlassian.net/browse/PED-633) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra
- **relates to:** [[PED-632 - APP - Validar para liquidar que si el pedido tiene marcado un envio en listado|PED-632]] APP -  Validar para liquidar que si el pedido tiene marcado un envio en listado de ordenes, que este agregado el item de servicio de transporte

## Descripcion

Tiene un medio de envio marcado cuando se lista las ordenes pero luego en el detalle no lo tiene.

- Corregir esta incosistencia


- validar si tiene envio no permitir liquidar si no tiene el item de servicio de envio agregado




Caso de produccion **X000200575637**
EXP

[adjunto]
PED 


[adjunto]
Orden:


```json
{
    "date": "2024-03-22 15:39:39",
    "orderNumber": "10342960",
    "branchNumber": "0002",
    "albnumNumber": "X000200575637",
    "realAlbumNumber": "00575637",
    "clientDescription": "RETEC CONSORCIO DE COOPERACION EMPRESARIA",
    "clientId": 20967,
    "orderTypeId": 2,
    "observation": "INTERNO",
    "status": "S",
    "statusId": 2,
    "statusDescription": "Autorizados. Pendiente a despachar",
    "invoice": null,
    "token": null,
    "voucherId": null,
    "sellerId": 5,
    "seller": "Contardi Patricio",
    "totalInPesos": 1023408.2033304999,
    "total": 1060.28766,
    "finalTotal": 1171.617863,
    "shippingMethod": 3030, //<---- tiene marcado  moto
    "codePostal": 3302,
    "currency": 873.5,
    "perception": 0,
    "shippingLabel": false,
    "idLo": null,
    "mpExternalReference": null,
    "paymentMethodId": 3,
    "paymentMethodDescription": "Depósito en Banco",
    "joinShipping": false,
    "dropShipping": false
}
```

Detalle de la orden


```json
{
    "orderNumber": "10342960",
    "branchNumber": "0002",
    "albnumNumber": "00575637",
    "realAlbumNumber": null,
    "clientName": "RETEC CONSORCIO DE COOPERACION EMPRESARIA",
    "clientId": 20967,
    "observation": null,
    "status": "S",
    "invoice": null,
    "token": null,
    "voucherId": null,
    "seller": "Contardi",
    "sellerId": "05 ",
    "sellerCreator": "",
    "sellerIdCreator": null,
    "items": [ // <--------------------------- Ninguno de los items es servicio de transporte
        {
            "title": "PLACA DE VIDEO GIGABYTE RTX 4060 WF2 OC 8GB",
            "sku": "GV-N4060WF2OC-8GD",
            "id": 118507,
            "price": {
                "value": 442.95978,
                "iva": 10.5,
                "finalPrice": 489.4705569,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 474.38929,
                    "B": 465.37589349,
                    "C": 459.20883272000003,
                    "D": 442.95978
                },
                "savedPriceList": "D",
                "currencyQuote": 873.5,
                "effectiveness": 33.25999999999999,
                "profit": 110.56
            },
            "warranty": "12 meses",
            "amount": 1,
            "refundAmount": 0,
            "stock": 19,
            "stockLio": 4,
            "stockInOrders": 3,
            "availableStock": 16
        },
        {
            "title": "PROCESADOR AMD (AM4) RYZEN 7 5700G",
            "sku": "100-00000263BOX",
            "id": 111454,
            "price": {
                "value": 240.936,
                "iva": 10.5,
                "finalPrice": 266.23428,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 289.67124,
                    "B": 284.16748644,
                    "C": 280.40176032,
                    "D": 240.936
                },
                "savedPriceList": "D",
                "currencyQuote": 873.5,
                "effectiveness": 6.609999999999999,
                "profit": 14.94
            },
            "warranty": "36 meses",
            "amount": 1,
            "refundAmount": 0,
            "stock": 61,
            "stockLio": 42,
            "stockInOrders": 6,
            "availableStock": 55
        },
        {
            "title": "MOTHER ASUS (AM4) PRIME B550M-A AC",
            "sku": "PRIME B550M-A AC",
            "id": 106758,
            "price": {
                "value": 124.49751,
                "iva": 10.5,
                "finalPrice": 137.56974855,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 140.56251,
                    "B": 137.89182231,
                    "C": 136.06450968000001,
                    "D": 124.49751
                },
                "savedPriceList": "D",
                "currencyQuote": 873.5,
                "effectiveness": 8.489999999999995,
                "profit": 19.5
            },
            "warranty": "36 meses",
            "amount": 2,
            "refundAmount": 0,
            "stock": 8,
            "stockLio": 5,
            "stockInOrders": 1,
            "availableStock": 7
        },
        {
            "title": "DISCO SSD M.2 250GB WD BLACK SN750 NVME",
            "sku": "WDS250G3X0C",
            "id": 117803,
            "price": {
                "value": 63.69843,
                "iva": 10.5,
                "finalPrice": 70.38676515,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 87.06481,
                    "B": 85.41057860999999,
                    "C": 84.27873607999999,
                    "D": 63.69843
                },
                "savedPriceList": "D",
                "currencyQuote": 873.5,
                "effectiveness": 3.6500000000000057,
                "profit": 4.48
            },
            "warranty": "12 meses",
            "amount": 2,
            "refundAmount": 0,
            "stock": 10,
            "stockLio": 4,
            "stockInOrders": 0,
            "availableStock": 10
        }
    ],
    "currencyQuote": 873.5,
    "shippingMethodId": null,// <------------------------- no tiene medio de envio
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
    "percepcion": 0,
    "whoBuild": null,
    "whoAuthorized": null,
    "addressFinal": null,
    "postalCodeFinal": null,
    "provinceNameFinal": null,
    "localityNameFinal": null
}
```
