---
jira_key: "PED-393"
aliases: ["PED-393"]
summary: "API - Feat - Ver detalle de orden de compra -> Agregar direccion al objeto de la orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-26 08:56"
updated: "2024-03-05 14:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-393"
---

# PED-393: API - Feat - Ver detalle de orden de compra -> Agregar direccion al objeto de la orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-26 08:56 |
| Actualizado | 2024-03-05 14:29 |
| Etiquetas | ninguna |
| Jira | [PED-393](https://bluinc.atlassian.net/browse/PED-393) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **blocks:** [[PED-394]] APP - Refactor - Agregaremos la direccion completa a el modal de pedido
- **blocks:** [[PED-431]] API - Review - Revisar calculo de utilidad en "ver detalle de pedido"

## Descripcion

```
GET {API_URL}/v1/orders/{orden}
```

```
{
    "orderNumber": "10332380",
    "branchNumber": "0002",
    "albnumNumber": "00568898",
    "realAlbumNumber": null,
    "clientName": "MERCURIO CATRIEL EDUARDO",
    "clientId": 26806,
    "observation": null,
    "status": "S",
    "invoice": null,
    "token": null,
    "voucherId": null,
    "seller": "Sin Vendedor",
    "sellerId": "36",
    "sellerCreator": "Sistema",
    "sellerIdCreator": "12 ",
    "items": [
        {
            "title": "ACCESORIOS SAMSUNG CABLE C A C 1.8M 3A 60W",
            "sku": "EP-DX310JBEGWW",
            "id": 118309,
            "price": {
                "value": 24.18754,
                "iva": 21,
                "finalPrice": 29.266923399999996,
                "percepcion": null,
                "letra": "A",
                "priceList": {
                    "A": 24.18754,
                    "B": 23.72797674,
                    "C": 23.41353872,
                    "D": 22.71044
                },
                "savedPriceList": "A",
                "currencyQuote": 1019,
                "effectiveness": 131,
                "profit": 5.72
            },
            "warranty": "12 meses",
            "amount": 1
        },
        {
            "title": "SERVICIO DE TRANSPORTE",
            "sku": "",
            "id": 102048,
            "price": {
                "value": 1.0138,
                "iva": 21,
                "finalPrice": 1.226698,
                "percepcion": null,
                "letra": "PM",
                "priceList": {
                    "A": 27.72,
                    "B": 27.19332,
                    "C": 26.83296,
                    "D": 27.72,
                    "PM": 1.0138
                },
                "savedPriceList": "E",
                "currencyQuote": 1019,
                "effectiveness": 8.05,
                "profit": -11.59
            },
            "warranty": "",
            "amount": 1
        }
    ],
    "currencyQuote": 1019,
    "shippingMethodId": 3030,
    "shippingMethodName": "Envio Moto                    ",
    "localityId": 3684,  <----
    "locality": "CASHICO", <----
    "address": "ANDRES FERREYRA 2685", <----
    "alphaCode": "3681", <----
    "phoneNumber": "2235181916", <----
    "provinceId": 18, <----
    "province": "SANTIAGO DEL ESTERO", <----
    "postalCode": "1678", <----
    "customerAddressId": 26889, <----    
    "tracking": null,
    "packageGrouper": null
}
```

Agregaremos la direccion completa a donde se hace el envio, en caso de que este esta disponible en `pedclit.medioEnvioId` o `pedclit.idDirCliNbWeb`
