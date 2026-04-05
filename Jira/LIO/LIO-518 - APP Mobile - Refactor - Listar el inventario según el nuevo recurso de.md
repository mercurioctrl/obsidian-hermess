---
jira_key: "LIO-518"
aliases: ["LIO-518"]
summary: "APP Mobile - Refactor -  Listar el inventario según el nuevo recurso de inventario desde API 4, en lugar de legacy"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-20 08:15"
updated: "2026-02-03 17:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-518"
---

# LIO-518: APP Mobile - Refactor -  Listar el inventario según el nuevo recurso de inventario desde API 4, en lugar de legacy

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-20 08:15 |
| Actualizado | 2026-02-03 17:52 |
| Etiquetas | ninguna |
| Jira | [LIO-518](https://bluinc.atlassian.net/browse/LIO-518) |

## Relaciones

- **Padre:** [[LIO-501]] Catálogo / Inventario de productos

## Descripcion

Utilizaremos el nuevo recurso provisto en V4 para la misma finalidad de navegar por el inventario del vendedor

```
GET {{API_URL}}/v4/inventories/products?search=&offset=2&brandId=3337&categoryId=226&order=description&orderDirection=desc
```

```
{
    "metadata": {
        "total": 1323,
        "offset": 2,
        "limit": 30,
        "order": "asc"
    },
    "items": [
        {
            "id": 742715,
            "internalId": 120162,
            "description": "DASHCAM TRANSCEND DRIVEPRO 250 GPS QHD 2K 60FPS +SD64GB",
            "image": "e5b0bee9cc696a64a2a5b7503ca3c313.png",
            "brandId": 3337,
            "brandName": "TRANSCEND",
            "categoryId": 226,
            "categoryName": "Iluminaci\u00f3n",
            "freeShipping": true,
            "instantFlash": false,
            "ratingStar": null,
            "resellerCost": 94.41,
            "utility": 2.00000000,
            "iva": 21.00,
            "internalTax": 0,
            "discount": 0.00,
            "priceUsd": 116.520822,
            "price": 171868,
            "gtin": null,
            "sku": "TS-DP250B-64G",
            "hide":0,
            "stock_cliente":0
        },
        {
            "id": 518547,
            "internalId": 108947,
            "description": "TECLADO GAMER DUCKY MECHA MINI V2 RGB KAILH BOX RED SWITCH ISO ES",
            "image": "a1b4b622fc087e260d6afa9147796c72.jpeg",
            "brandImage": "75d04b2fa7c96419c72f7d11993e6bf7.png",
            "brandId": 5687,
            "brandName": "DUCKY",
            "categoryId": 3,
            "categoryName": "Teclados",
            "freeShipping": true,
            "bestSeller": null,
            "instantFlash": false,
            "ratingStar": null,
            "resellerCost": 138.89,
            "utility": 2.00000000,
            "iva": 10.50,
            "internalTax": 0,
            "discount": 0.00,
            "priceUsd": 156.54,
            "price": 230900,
            "sellerId": 447,
            "sellerName": "Gears Store",
            "gtin": null,
            "sku": "DKME2061ST-KESALAATR",
            "hide":0,
            "stock_cliente":0
        },
       ..
    ]
}
```
