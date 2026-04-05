---
jira_key: "INV-19"
summary: "API - Feat - Ver detalle de producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-16 15:26"
updated: "2022-06-16 16:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-19"
---

# INV-19: API - Feat - Ver detalle de producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-16 15:26 |
| Actualizado | 2022-06-16 16:17 |
| Etiquetas | ninguna |
| Jira | [INV-19](https://bluinc.atlassian.net/browse/INV-19) |

## Descripción

Se trata del recurso necesario par visualizar un detalle del producto que luego puede ser visualizado

```
GET {{API_URL}}/v1/item/{productId}
```

```

[{
    "Title": "FUENTE GAMER GIGABYTE 550W 80 PLUS",
    "Id": "104964",
    "Sku": "GP-P550B",
    "Category": "FUENTES ",
    "IdCategory": "38",
    "IdBrand": "4",
    "upc": "447646834",
    "ean": "447-646-834",
    "Brand": "GIGABYTE ",
    "brandImage": "https://static.nb.com.ar/img/f2aae2c829b051430eb6a039ad6bc7ae.jpg",
    "initialB": null,
    "initialC": null,
    "Stock": "Alto",
    "imagen_principal": "https://static.nb.com.ar/i/nb_nombre-del-producto_ver_b65cd71de19e10c27d8c357cd99cded9.png",
    "images": [{
            "order": "0",
            "url": "https://static.nb.com.ar/i/nb_nombre-del-producto_ver_b65cd71de19e10c27d8c357cd99cded9.png",
            "secure_url": "https://http2.mlstatic.com/D_NQ_NP_123-MLA456_112021-F.jpg"
        },
        {
            "order": "0",
            "url": "https://static.nb.com.ar/i/nb_nombre-del-producto_ver_b65cd71de19e10c27d8c357cd99cded9.png",
            "secure_url": "https://http2.mlstatic.com/D_NQ_NP_123-MLA456_112021-F.jpg"
        },
        {
            "order": "0",
            "url": "https://static.nb.com.ar/i/nb_nombre-del-producto_ver_b65cd71de19e10c27d8c357cd99cded9.png",
            "secure_url": "https://http2.mlstatic.com/D_NQ_NP_123-MLA456_112021-F.jpg"
        }
    ],
    "Attributes": [{
            "name": "Marca del repuesto",
            "value": "Razer"
        },
        {
            "name": "Código universal de producto",
            "value": "810056142155"
        },
        {
            "name": "Condición del ítem",
            "value": "Nuevo"
        },
        {
            "name": "Modelo del repuesto",
            "value": "RC21-01720100-R3M1"
        }
    ],
    "description": [{
        "type": "plain/text ",
        "content": "lorem ipsum lo que sea..."

    }]

}]
```
