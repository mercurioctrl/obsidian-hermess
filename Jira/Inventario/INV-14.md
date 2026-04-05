---
jira_key: "INV-14"
summary: "API - Listar productos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-07 15:34"
updated: "2024-09-11 21:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-14"
---

# INV-14: API - Listar productos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-07 15:34 |
| Actualizado | 2024-09-11 21:46 |
| Etiquetas | ninguna |
| Jira | [INV-14](https://bluinc.atlassian.net/browse/INV-14) |

## Descripción

Se trata del recurso necesario para poder traer el listado de productos para poder editar su informacion

```
GET {{API_URL}}/v1/?categoryId={categoryId}&brandId={brandId}
```

```
GET {{API_URL}}/v1/?categoryId={categoryId}
```

```
GET {{API_URL}}/v1/?brandId={brandId}
```

```
GET {{API_URL}}/v1/?search={termino de busqueda}
```

Retorna:



```json
[
  {
        "title": "AURICULAR ADATA ERATO BLUETOOTH WHITE",
        "sku": "AEMU05WH00",
        "id": 104183,
        "category": "AURICULARES",
        "categoryId": 28,
        "brand": "ADATA",
        "brandId": 91,
        "mainImage": "https://static.nb.com.ar/i/nb_AURICULAR-ADATA-ERATO-BLUETOOTH-WHITE_ver_07b50426385670365fcda5daac069c37.jpeg",
        "brandImage": "http://static.nb.com.ar/img/d411bd521b946ee7702e2b87578957e2.jpg",
        "stock": true,
        "warranty": "12 meses",
        "description":1,
        "atributes":32, //indica la cantidad de atributos que tiene el producto
        "images": 5,
        "ean": , //el ean si lo tiene
        "upc": , //el upc si lo tiene
    },
    {
        "title": "AURICULAR ADATA ERATO BLUETOOTH WHITE",
        "sku": "AEMU05WH00",
        "id": 104183,
        "category": "AURICULARES",
        "categoryId": 28,
        "brand": "ADATA",
        "brandId": 91,
        "mainImage": "https://static.nb.com.ar/i/nb_AURICULAR-ADATA-ERATO-BLUETOOTH-WHITE_ver_07b50426385670365fcda5daac069c37.jpeg",
        "brandImage": "http://static.nb.com.ar/img/d411bd521b946ee7702e2b87578957e2.jpg",
        "stock": false,
        "warranty": "12 meses",
        "description":1,
        "atributes":32, //indica la cantidad de atributos que tiene el producto
        "images": 5,
        "ean": , //el ean si lo tiene
        "upc": , //el upc si lo tiene
    },
    
    {
        "title": "AURICULAR ADATA ERATO BLUETOOTH WHITE",
        "sku": "AEMU05WH00",
        "id": 104183,
        "category": "AURICULARES",
        "categoryId": 28,
        "brand": "ADATA",
        "brandId": 91,
        "mainImage": "https://static.nb.com.ar/i/nb_AURICULAR-ADATA-ERATO-BLUETOOTH-WHITE_ver_07b50426385670365fcda5daac069c37.jpeg",
        "brandImage": "http://static.nb.com.ar/img/d411bd521b946ee7702e2b87578957e2.jpg",
        "stock": true,
        "warranty": "12 meses",
        "description":1,
        "atributes":32, //indica la cantidad de atributos que tiene el producto
        "images": 5,
        "ean": , //el ean si lo tiene
        "upc": , //el upc si lo tiene
    }
    ]
```
