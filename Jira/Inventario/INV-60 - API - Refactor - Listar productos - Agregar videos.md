---
jira_key: "INV-60"
aliases: ["INV-60"]
summary: "API - Refactor - Listar productos -> Agregar videos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-21 14:15"
updated: "2024-04-24 17:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-60"
---

# INV-60: API - Refactor - Listar productos -> Agregar videos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-21 14:15 |
| Actualizado | 2024-04-24 17:19 |
| Etiquetas | ninguna |
| Jira | [INV-60](https://bluinc.atlassian.net/browse/INV-60) |

## Relaciones

- **Padre:** [[INV-27 - Productos|INV-27]] Productos
- **blocks:** [[INV-59 - APP - Feat - Agregar y remover videos|INV-59]] APP - Feat - Agregar y remover videos 

## Descripcion

Agregaremos al objeto items del repositorio de productos el array que contiene los vídeos que ese producto tiene enlazado

```
GET {API_URL}/items
```

```
{
    "title": "PROCESADOR AMD (AM4) RYZEN 5 5600",
    "sku": "100-100000927BOX",
    "id": 116652,
    "category": "PROCESADORES",
    "categoryId": 3,
    "brand": "AMD                                               ",
    "brandId": 43,
    "brandImage": "https://static.nb.com.ar/img/266f407b98b3c0721710b6c651d4108f.jpg",
    "mainImage": "http://static.nb.com.ar/img/8db5dda8994a87d374132ca5dc19b1b5.jpeg",
    "stock": 11,
    "warranty": "36 meses                                                                                            ",
    "description": "",
    "attributes": 4,
    "images": [
        {
            "checksum": "http://static.nb.com.ar/img/409d32ba126782dfd40c4f63a9a9d38b.jpeg",
            "order": 1
        },
        {
            "checksum": "http://static.nb.com.ar/img/8db5dda8994a87d374132ca5dc19b1b5.jpeg",
            "order": 1
        }
    ],
    
    NUEVO
    ---> "videos": [
          {
              "videoId": "Blf0zZv6UsQ",
              "url": "https://www.youtube.com/watch?v=Blf0zZv6UsQ"
              "type":1
          } 
    ],    
    "ean": null,
    "upc": "730143314190"
}
```
