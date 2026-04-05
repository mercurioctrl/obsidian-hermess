---
jira_key: "NBWEB-912"
aliases: ["NBWEB-912"]
summary: "API - Refactor - Agregar internalTax al detalle de producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-04 17:29"
updated: "2024-11-06 02:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-912"
---

# NBWEB-912: API - Refactor - Agregar internalTax al detalle de producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-04 17:29 |
| Actualizado | 2024-11-06 02:14 |
| Etiquetas | ninguna |
| Jira | [NBWEB-912](https://bluinc.atlassian.net/browse/NBWEB-912) |

## Relaciones

- **Padre:** [[NBWEB-682]] Productos

## Descripcion

```
GET {API_URL}/v1/item/{itemId}
```

```
{
    "title": "PROCESADOR AMD (AM4) RYZEN 5 5600",
    "sku": "100-100000927BOX",
    "id": 116652,
    "category": "PROCESADORES",
    "categoryId": 3,
    "brand": "AMD",
    "brandId": 43,
    "mainImage": "https:\/\/static.nb.com.ar\/i\/nb_PROCESADOR-AMD-(AM4)-RYZEN-5-5600_ver_8db5dda8994a87d374132ca5dc19b1b5.jpeg",
    "brandImage": "https:\/\/static.nb.com.ar\/img\/266f407b98b3c0721710b6c651d4108f.jpg",
    "initialB": 5,
    "initialC": 10,
    "stock": "Alto",
    "amountInCart": 0,
    "description": {
        "type": "plain\/text",
        "value": ""
    },
    "amountStock": 10,
    "ean": "",
    "upc": "730143314190",
    "price": {
        "value": 150.52778,
        "iva": 10.5,
        "internalTax": 10.5, <- SE AGREGA
        "finalPrice": 166.33319690000002, <- SE INCLUYE DENTRO DEL FINAL
        "percepcion": null,
        "finalPriceWithUtility": 166.3332,
        "ncostoextra": 0
    },
    "warranty": "36 meses",
    "cotizacion": 1013,
    "images": [
        {
            "checksum": "8db5dda8994a87d374132ca5dc19b1b5.jpeg",
            "order": "646240"
        },
        {
            "checksum": "409d32ba126782dfd40c4f63a9a9d38b.jpeg",
            "order": "646241"
        }
    ],
    "attributes": [
        {
            "name": "Marca",
            "value": "AMD"
        },
        {
            "name": "Modelo de CPU",
            "value": "Ryzen 5"
        },
        {
            "name": "Velocidad de la CPU",
            "value": "4.4 GHz"
        },
        {
            "name": "Z\u00f3calo de CPU",
            "value": " \tSocket AM4"
        }
    ]
}
```
