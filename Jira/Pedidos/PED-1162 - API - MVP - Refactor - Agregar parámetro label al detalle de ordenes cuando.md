---
jira_key: "PED-1162"
aliases: ["PED-1162"]
summary: "API - MVP - Refactor - Agregar parámetro label al detalle de ordenes cuando este esta disponible"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-28 10:08"
updated: "2025-12-05 03:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1162"
---

# PED-1162: API - MVP - Refactor - Agregar parámetro label al detalle de ordenes cuando este esta disponible

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-28 10:08 |
| Actualizado | 2025-12-05 03:59 |
| Etiquetas | ninguna |
| Jira | [PED-1162](https://bluinc.atlassian.net/browse/PED-1162) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra

## Descripcion

Según lo realizado en [link](https://bluinc.atlassian.net/browse/PED-1118) 

Agregaremos para que sea mas simple de mostrar y operar el parámetro `label` al objeto que nos muestra el detalle de una orden de venta joineando `[NewBytes_DBF].[dbo].[articulo_label]` (asegurar los indices para que al hacer el join no perdamos rendimiento) 

```
GET /v1/orders/{branch}{order}
```

```
{
    "date": "2025-10-28 09:42:00",
    "makeSaleDate": null,
    "orderNumber": "10435216",
    "branchNumber": "0002",
    "albnumNumber": null,
    "realAlbumNumber": null,
    "clientEmail": "Portalgamesmdq@gmail.com",
    "clientName": "DATADS EVOMARKETING S.A.",
    "clientId": 92751,
    "userId": 81624,
    "observation": null,
    "status": "P",
    "invoice": null,
    "token": null,
    "voucherId": null,
    "seller": "Antonella",
    "sellerId": "47",
    "sellerCreator": "Hernandez Diego",
    "sellerIdCreator": "38",
    "items": [
        {
            "title": "FUENTE GAMER GIGABYTE 550W ICE 80 PLUS SILVER ATX 3.0 WHITE",
            "sku": "GP-P550SS ICE",
            "id": 119727,
            "label": "Origen China" <-- Se agrega
            "price": {
                "value": 41.99177,
                "iva": 21,
                "finalPrice": 50.8100417,
                "percepcion": null,
                "letra": "PM",
                "priceList": {
                    "A": 41.2496,
                    "B": 40.4658576,
                    "C": 39.9296128,
                    "D": 38.0016,
                    "E": 37.6768,
                    "PM": 41.99177
                },
                "savedPriceList": "A",
                "currencyQuote": 1460,
                "effectiveness": 29.289999999999992,
                "profit": 0,
                "internalTax": 0,
                "averageCost": 32.48,
                "costForSale": null,
                "niva": null
            },
            "warranty": "12 meses",
            "amount": 0,
            "refundAmount": 0,
            "stock": 119,
            "stockLio": 0,
            "stockInOrders": 5,
            "availableStock": 114
        },
        {
            "title": "PROCESADOR AMD (AM5) RYZEN 5 8500G",
            "sku": "100-100000931BOX",
            "id": 118980,
            "label": "Ultimas unidades" <-- Se agrega
            "price": {
                "value": 138.95694,
                "iva": 10.5,
                "finalPrice": 153.5474187,
                "percepcion": null,
                "letra": "PM",
                "priceList": {
                    "A": 140.2772,
                    "B": 137.61193319999998,
                    "C": 135.7883296,
                    "D": 132.0256,
                    "E": 130.8468,
                    "PM": 138.95694
                },
                "savedPriceList": "B",
                "currencyQuote": 1460,
                "effectiveness": 17.879999999999995,
                "profit": 0,
                "internalTax": 0,
                "averageCost": 117.88,
                "costForSale": null,
                "niva": null
            },
            "warranty": "36 meses",
            "amount": 0,
            "refundAmount": 0,
            "stock": 439,
            "stockLio": 0,
            "stockInOrders": 369,
            "availableStock": 70
        },
        {  
```
