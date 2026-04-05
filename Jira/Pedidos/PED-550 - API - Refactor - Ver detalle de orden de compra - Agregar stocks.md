---
jira_key: "PED-550"
aliases: ["PED-550"]
summary: "API - Refactor - Ver detalle de orden de compra -> Agregar stocks"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-09 10:22"
updated: "2024-02-14 14:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-550"
---

# PED-550: API - Refactor - Ver detalle de orden de compra -> Agregar stocks

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-09 10:22 |
| Actualizado | 2024-02-14 14:17 |
| Etiquetas | ninguna |
| Jira | [PED-550](https://bluinc.atlassian.net/browse/PED-550) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **blocks:** [[PED-551]] APP - Refactor - Ver detalle de orden de compra -> Marcar faltantes en caso de existir (casillero rojo)
- **is blocked by:** [[PED-555]] API - Ver detalle de orden de compra -> Agregar stocks - Cantidades no coincidentes

## Descripcion

Agregaremos al recurso los parámetros para cada item 

`stock`, `stockLio`, `stockInOrders`, `availableStock`

Verificar si cambia mucho la performance y respetar la regla del 1,5 segundos

```
GET {API_URL}/v1/orders/{branch-order}
```

Devuelve

```json
{
    "orderNumber": "10338225",
    "branchNumber": "0002",
    "albnumNumber": null,
    "realAlbumNumber": null,
    "clientName": "Catriel (no usar)",
    "clientId": 19227,
    "observation": null,
    "status": "P",
    "invoice": null,
    "token": null,
    "voucherId": null,
    "seller": "Sin Vendedor",
    "sellerId": "36",
    "sellerCreator": "",
    "sellerIdCreator": null,
    "items": [
        {
            "title": "ANBYTE CABLE ALIMENTACION TREBOL\/MICKEY 1.50M",
            "sku": "959709",
            "id": 103506,
            "price": {
                "value": 4.66289,
                "iva": 21,
                "finalPrice": 5.642096899999999,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 5.02158,
                    "B": 4.92616998,
                    "C": 4.86088944,
                    "D": 4.66289
                },
                "savedPriceList": "D",
                "currencyQuote": 848,
                "effectiveness": 30,
                "profit": 1.08
            },
            "warranty": "12 meses",
            "amount": 1,
            "refundAmount": 0
        },
        {
            "title": "SERVICIO DE TRANSPORTE",
            "sku": "",
            "id": 102048,
            "price": {
                "value": 8.22158,
                "iva": 21,
                "finalPrice": 9.9481118,
                "percepcion": null,
                "letra": "PM",
                "priceList": {
                    "A": 22.83453,
                    "B": 22.40067393,
                    "C": 22.10382504,
                    "D": 21.57453,
                    "PM": 8.22158
                },
                "savedPriceList": "E",
                "currencyQuote": 848,
                "effectiveness": -34.75,
                "profit": -4.38
            },
            "warranty": "",
            "amount": 1,
            "refundAmount": 0,
            "stock": 4, <----- NUEVO
            "stockLio": 0, <----- NUEVO
            "stockInOrders": 0, <----- NUEVO
            "availableStock": 4, <----- NUEVO
        },
        {
            "title": "NOGA CARGADOR 3A 15W CON CABLE MICRO",
            "sku": "[[NGA-358]]",
            "id": 117841,
            "price": {
                "value": 5.59939,
                "iva": 21,
                "finalPrice": 6.775261899999999,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 6.03011,
                    "B": 5.915537909999999,
                    "C": 5.8371464799999995,
                    "D": 5.59939
                },
                "savedPriceList": "D",
                "currencyQuote": 848,
                "effectiveness": 30,
                "profit": 69.78
            },
            "warranty": "12 meses",
            "amount": 54,
            "refundAmount": 0,
            "stock": 4, <----- NUEVO
            "stockLio": 0, <----- NUEVO
            "stockInOrders": 0, <----- NUEVO
            "availableStock": 4, <----- NUEVO
            
        }
    ],
    "currencyQuote": 848,
    "shippingMethodId": 4065,
    "shippingMethodName": "ANDREANI PickUp",
    "tracking": null,
    "packageGrouper": null,
    "localityId": 20891,
    "localityName": "CIUDAD DE BUENOS AIRES",
    "provinceId": 1,
    "provinceName": "CAPITAL FEDERAL ( CAP. FED. )",
    "alphaCode": "BSAS",
    "phoneNumber": "13241412",
    "postalCode": "1225",
    "customerAddressId": 19338,
    "address": "Av. Independencia 3485",
    "niva": 3,
    "percepcion": 0,
    "whoBuild": null,
    "whoAuthorized": null
}
```
