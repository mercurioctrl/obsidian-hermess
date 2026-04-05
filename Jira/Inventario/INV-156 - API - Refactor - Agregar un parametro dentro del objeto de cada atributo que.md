---
jira_key: "INV-156"
aliases: ["INV-156"]
summary: "API - Refactor - Agregar un parametro dentro del objeto de cada atributo que indique si es obligatorio para el producto (para su categoría)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-10-14 08:27"
updated: "2024-10-15 19:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-156"
---

# INV-156: API - Refactor - Agregar un parametro dentro del objeto de cada atributo que indique si es obligatorio para el producto (para su categoría)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-14 08:27 |
| Actualizado | 2024-10-15 19:40 |
| Etiquetas | ninguna |
| Jira | [INV-156](https://bluinc.atlassian.net/browse/INV-156) |

## Relaciones

- **Padre:** [[INV-27]] Productos
- **has action item:** [[INV-157]] APP - Refactor - Modificar modal de atributos para tener en cuenta atributos obligatorios y herramienta de búsqueda automatica

## Descripcion

Agregaremos el parámetro `attributes`.`required` para marcar cuales son obligatorios para el producto (para su categoría en realidad). Algo importante a tener en cuenta, es que cuando el item tiene un atributo obligatorio, pero que no esta cargado, aparece igual pero sin valor.

De este modo cuando abra el cliente para editar cualquier atributo siempre estará obligado a completar los faltantes obligados para la categoría.

```
GET {API_URL}/item/{itemId}
```

```
[
    {
        "title": "TECLADO GAMER DUCKY SESALWWT1",
        "sku": "DKON1967ST-SESALWWT1",
        "id": 111699,
        "category": "TECLADOS                      ",
        "categoryId": 34,
        "brand": 132,
        "brandId": "DUCKY",
        "brandImage": "https://static.nb.com.ar/img/75d04b2fa7c96419c72f7d11993e6bf7.png",
        "mainImage": null,
        "stock": 8.0,
        "warranty": "12 meses",
        "description": "",
        "attributes": [
            {
                "name": "Marca",
                "value": "DUCKY",
                "id": 756146,
                "required": true <-- NUEVO
            },
            {
                "name": "Velocidad",
                "value": "",
                "id": 756147,
                "required": false <-- NUEVO
            }
        ],
        "images": [],
        "ean": null,
        "upc": null,
        "videoId": null,
        "companyCode": 4,
        "companyName": "NB DISTRIBUIDORA MAYORISTA SRL",
        "officialSiteUrl": null,
        "sindicateContentImg": null,
        "iva": 10.5,
        "notSerializable": 0
    }
]
```
