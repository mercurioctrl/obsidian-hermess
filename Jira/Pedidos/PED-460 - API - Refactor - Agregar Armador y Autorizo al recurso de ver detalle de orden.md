---
jira_key: "PED-460"
aliases: ["PED-460"]
summary: "API - Refactor - Agregar \"Armador\" y \"Autorizo\" al recurso de ver detalle de orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-01-08 15:49"
updated: "2024-01-11 18:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-460"
---

# PED-460: API - Refactor - Agregar "Armador" y "Autorizo" al recurso de ver detalle de orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-08 15:49 |
| Actualizado | 2024-01-11 18:43 |
| Etiquetas | ninguna |
| Jira | [PED-460](https://bluinc.atlassian.net/browse/PED-460) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra

## Descripcion

Agregaremos los parámetros `whoBuild` y `whoAuthorized` tal cual lo hacemos en expedición 

```
GET {API_URL}/v1/orders/{suc-order}
```

```
{
    "orderNumber": "10334968",
    "branchNumber": "0002",
    "albnumNumber": "00570616",
    "realAlbumNumber": null,
    "clientName": "COLQUHOUN BRIAN",
    "clientId": 55647,
    "observation": null,
    "status": "S",
    "invoice": "A000400124794",
    "token": "5234898376d4ec8035265e034afb14",
    "voucherId": 522015,
    "seller": "Lautaro",
    "sellerId": "51",
    "sellerCreator": "",
    "sellerIdCreator": null,
    "items": [
        {
            "title": "MOTHER GIGABYTE (AM4) B550M K",
            "sku": "B550M K",
            "id": 118120,
            "price": {
                "value": 120.055,
                "iva": 10.5,
                "finalPrice": 132.660775,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 129.29,
                    "B": 126.83349,
                    "C": 125.15271999999999,
                    "D": 120.055
                },
                "savedPriceList": "D",
                "currencyQuote": 1030,
                "effectiveness": 30,
                "profit": 27.71
            },
            "warranty": "36 meses",
            "amount": 1
        },
        {
            "title": "PROCESADOR AMD (AM4) RYZEN 7 5700X (SIN COOLER)",
            "sku": "100-100000926WOF",
            "id": 116714,
            "price": {
                "value": 300.495,
                "iva": 10.5,
                "finalPrice": 332.046975,
                "percepcion": null,
                "letra": "PM",
                "priceList": {
                    "A": 449.61,
                    "B": 441.06741,
                    "C": 435.22248,
                    "D": 417.495,
                    "PM": 300.495
                },
                "savedPriceList": "E",
                "currencyQuote": 1030,
                "effectiveness": 30,
                "profit": 69.35
            },
            "warranty": "36 meses",
            "amount": 1
        }
    ],
    "currencyQuote": 1030,
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
    "percepcion": 0,
    "whoBuild": "antonellalo", <--- NUEVO PARAMETRO
    "whoAuthorized": "zoccoliNB", <--- NUEVO PARAMETRO
}
```
