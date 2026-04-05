---
jira_key: "PED-1245"
aliases: ["PED-1245"]
summary: "API - OM - Ordenar los items del detalle de una orden por id de creacion"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2026-01-06 18:12"
updated: "2026-01-21 18:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1245"
---

# PED-1245: API - OM - Ordenar los items del detalle de una orden por id de creacion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2026-01-06 18:12 |
| Actualizado | 2026-01-21 18:42 |
| Etiquetas | ninguna |
| Jira | [PED-1245](https://bluinc.atlassian.net/browse/PED-1245) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra

## Descripcion

La idea es que los ítems de una orden se muestren **siempre en el mismo orden**, de forma consistente cada vez que se consulta la orden.

Para eso, se debe ordenar el array `items` según el **orden natural en el que los ítems fueron agregados a la orden**.

El criterio de orden será **ascendente por**:

```
[NewBytes_DBF].[dbo].[pedclil].id ASC
```

De esta forma, el endpoint:

```
GET /v1/orders/{branch}-{order}
```

devolverá el array `items` siempre en un orden determinístico, estable y repetible, sin depender del front ni de otros criterios implícitos.

El cambio solo afecta el orden del array `items`; no se modifica la estructura ni los datos de los ítems.

```
{
...
    "sellerCreator": "",
    "sellerIdCreator": null,

    ---- El array items es lo que queremos ordenar --- 
    "items": [
        {
            "title": "PROCESADOR AMD (AM5) RYZEN 5 8600G",
            "sku": "100-100001237BOX",
            "id": 118837,
            "price": {
                "value": 166.4208,
                "iva": 10.5,
                "finalPrice": 183.89498400000002,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 178.308,
                    "B": 174.92014799999998,
                    "C": 172.60214399999998,
                    "D": 166.4208,
                    "E": 163.449
                },
                "savedPriceList": "D",
                "currencyQuote": 1490,
                "effectiveness": 12,
                "profit": 17.83,
                "internalTax": 0,
                "averageCost": 148.59,
                "costForSale": null,
                "niva": null
            },
            "warranty": "36 meses",
            "amount": 1,
            "refundAmount": 0,
            "stock": 66,
            "stockLio": 0,
            "stockInOrders": 2,
            "availableStock": 64
        },
        {
            "title": "MOTHER GIGABYTE (AM5) A620M H",
            "sku": "A620M H 1.0",
            "id": 119720,
            "price": {
                "value": 69.2037,
                "iva": 10.5,
                "finalPrice": 76.4700885,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 80.5752,
                    "B": 79.0442712,
                    "C": 77.99679359999999,
                    "D": 69.2037,
                    "E": 67.9041
                },
                "savedPriceList": "D",
                "currencyQuote": 1490,
                "effectiveness": 6.5,
                "profit": 4.22,
                "internalTax": 0,
                "averageCost": 64.98,
                "costForSale": null,
                "niva": null
            },
            "warranty": "12 meses",
            "amount": 1,
            "refundAmount": 0,
            "stock": 262,
            "stockLio": 0,
            "stockInOrders": 4,
            "availableStock": 258
        },
        {
            "title": "FUENTE GAMER RAIDMAX VORTEX 600W WHITE",
            "sku": "RX-600ACV",
            "id": 121486,
            "price": {
                "value": 31.01,
                "iva": 21,
                "finalPrice": 37.5221,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 33.225,
                    "B": 32.593725,
                    "C": 32.1618,
                    "D": 31.01,
                    "E": 31.01
                },
                "savedPriceList": "D",
                "currencyQuote": 1490,
                "effectiveness": 40,
                "profit": 8.86,
                "internalTax": 0,
                "averageCost": 22.15,
                "costForSale": null,
                "niva": null
            },
            "warranty": "12 meses",
            "amount": 1,
            "refundAmount": 0,
            "stock": 124,
            "stockLio": 9,
            "stockInOrders": 1,
            "availableStock": 123
        }
    ],
    "currencyQuote": 1490,
    "shippingMethodId": 3999,
    ...
}
```
