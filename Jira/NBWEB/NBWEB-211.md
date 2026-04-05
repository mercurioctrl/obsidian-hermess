---
jira_key: "NBWEB-211"
summary: "API - Detalle de producto"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-30 09:15"
updated: "2022-06-21 21:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-211"
---

# NBWEB-211: API - Detalle de producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-30 09:15 |
| Actualizado | 2022-06-21 21:57 |
| Etiquetas | ninguna |
| Jira | [NBWEB-211](https://bluinc.atlassian.net/browse/NBWEB-211) |

## Descripción

Se trata del recurso que devuelve los detallas del producto

```
{{API_URL}}/v1/item/{productId}
```

```json
[{
    "Title": "FUENTE GAMER GIGABYTE 550W 80 PLUS",
    "Id": "104964",
    "Sku": "GP-P550B",
    "Category": "FUENTES ",
    "IdCategory": "38",
    "IdBrand": "4",
    "Brand": "GIGABYTE ",
    "brandImage": "https://static.nb.com.ar/img/f2aae2c829b051430eb6a039ad6bc7ae.jpg",
    "initialB": null,
    "initialC": null,
    "Stock": "Alto",
    "imagen_principal": "https://static.nb.com.ar/i/nb_nombre-del-producto_ver_b65cd71de19e10c27d8c357cd99cded9.png",
    "Price": {
        "value": "53.56365",
        "iva": 10.5,
        "finalPrice": 59.187833250000004
    },
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
