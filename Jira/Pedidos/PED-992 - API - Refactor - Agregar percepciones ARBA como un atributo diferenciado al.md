---
jira_key: "PED-992"
aliases: ["PED-992"]
summary: "API - Refactor - Agregar percepciones ARBA como un atributo diferenciado al momento de ver el detalle de una orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-25 07:50"
updated: "2025-05-07 10:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-992"
---

# PED-992: API - Refactor - Agregar percepciones ARBA como un atributo diferenciado al momento de ver el detalle de una orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-25 07:50 |
| Actualizado | 2025-05-07 10:32 |
| Etiquetas | ninguna |
| Jira | [PED-992](https://bluinc.atlassian.net/browse/PED-992) |

## Relaciones

- **Padre:** [[PED-497]] Ver orden de compra
- **action item from:** [[PED-991]] API - Refactor - Agregar percepciones ARBA en caso de que existan para el cliente en el repositorio para listar ordenes
- **has action item:** [[PED-993]] APP - Refactor - Agregar percepciones ARBA como un atributo diferenciado al momento de ver el detalle de la orden
- **has action item:** [[PED-994]] API - Refactor - Agregar percepciones ARBA al "pedido + INFO"

## Descripcion

A diferencia de como realizamos en [link](https://bluinc.atlassian.net/browse/PED-991) ** donde no importaba diferenciar las alicutoas, en el caso del detalle de la orden si es importante.**

Para esto agregaremos un nuevo atributo llamado `percepcionArba` que funciona como `percepcion` pero para el caso de ARBA. Si no tiene, es cero.

Para esto, haremos un refactor sobre el recurso

```
GET {API_URL}/v1/orders/{branch-order}
```

```
{
    "date": "2025-04-24 16:54:15",
    "makeSaleDate": "2025-04-24 17:15:56",
    "orderNumber": "10403640",
    "branchNumber": "0002",
    "albnumNumber": "00614855",
    "realAlbumNumber": null,
    "clientEmail": "cristian_certo@outlook.com.ar",
    "clientName": "CERTO CRISTIAN EMANUEL",
    "clientId": 41338,
    "userId": 56206,
    "observation": null,
    "status": "S",
    "invoice": "A000400154055",
    "token": "550a52ba454add23051049c184369e",
    "voucherId": 573481,
    "seller": "Albarracin",
    "sellerId": "30",
    "sellerCreator": "Albarracin Julian",
    "sellerIdCreator": "30",
    "items": [
        {
            "title": "MONITOR PHILIPS LED 19 193V5LHSB2",
            "sku": "193V5LHSB2\/77",
            "id": 117208,
            "price": {
                "value": 90.22536,
                "iva": 21,
                "finalPrice": 109.1726856,
                "percepcion": null,
                "letra": "PM",
                "priceList": {
                    "A": 93.20802,
                    "B": 91.43706762000001,
                    "C": 90.22536336,
                    "D": 90.85824,
                    "PM": 90.22536
                },
                "savedPriceList": "C",
                "currencyQuote": 1215,
                "effectiveness": 15.189999999999998,
                "profit": 23.8,
                "internalTax": 0,
                "averageCost": 78.33
            },
            "warranty": "36 meses",
            "amount": 2,
            "refundAmount": 0,
            "stock": 41,
            "stockLio": 0,
            "stockInOrders": 7,
            "availableStock": 34
        },
        {
            "title": "MEMORIA ADATA SODIMM DDR4 16GB 3200 G22 SGN",
            "sku": "AD4S320016G22-SGN",
            "id": 118295,
            "price": {
                "value": 25.0536,
                "iva": 10.5,
                "finalPrice": 27.684227999999997,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 26.9516,
                    "B": 26.4395196,
                    "C": 26.0891488,
                    "D": 25.0536
                },
                "savedPriceList": "D",
                "currencyQuote": 1215,
                "effectiveness": 32,
                "profit": 6.07,
                "internalTax": 0,
                "averageCost": 18.98
            },
            "warranty": "12 meses",
            "amount": 1,
            "refundAmount": 0,
            "stock": 38,
            "stockLio": 0,
            "stockInOrders": 14,
            "availableStock": 24
        },
        {
            "title": "SERVICIO DE TRANSPORTE",
            "sku": "",
            "id": 102048,
            "price": {
                "value": 7.41897,
                "iva": 21,
                "finalPrice": 8.9769537,
                "percepcion": null,
                "letra": "PM",
                "priceList": {
                    "A": 18.05809,
                    "B": 17.71498629,
                    "C": 17.48023112,
                    "D": 20.2496,
                    "PM": 7.41897
                },
                "savedPriceList": "E",
                "currencyQuote": 1215,
                "effectiveness": 0,
                "profit": 0,
                "internalTax": 0,
                "averageCost": 12.6
            },
            "warranty": "",
            "amount": 1,
            "refundAmount": 0,
            "stock": 848,
            "stockLio": 0,
            "stockInOrders": 54,
            "availableStock": 794
        }
    ],
    "currencyQuote": 1215,
    "shippingMethodId": 4069,
    "shippingMethodName": "ENTREGAR PickUp",
    "tracking": null,
    "packageGrouper": null,
    "localityId": 8884,
    "localityName": "ITUZAINGO",
    "provinceId": 2,
    "provinceName": "BUENOS AIRES ( BS. AS )",
    "alphaCode": "8881",
    "phoneNumber": "01168753887",
    "postalCode": "1714",
    "customerAddressId": 19400,
    "address": "Albert Schweitzer 1381",
    "niva": 1,
    "percepcion": 6.387698,
    "percepcionArba": 2.23, <-- Se agrega un nuevo parametro nominal, basado en el porcentual como se hace con "percepcion"
    "whoBuild": null,
    "whoAuthorized": null,
    "addressFinal": null,
    "postalCodeFinal": null,
    "provinceNameFinal": null,
    "localityNameFinal": null
}
```

### 🟦 **Criterios de Aceptación**

- Se debe agregar el nuevo campo `percepcionArba`en la respuesta del endpoint `GET {API_URL}/v1/orders/{branch-order}`.


- El cálculo de `percepcionArba`debe realizarse de la misma forma que `percepcion`, pero tomando el valor de `clientes.percepcion_arba`.


- Ambos campos (`percepcion` y `percepcionArba`) deben mostrarse de forma separada y explícita, sin sumarse entre sí.


- Si `percepcion_arba` es nulo, debe considerarse como 0.


- La performance del endpoint no debe verse afectada de manera significativa (mantener tiempos similares a los actuales).
