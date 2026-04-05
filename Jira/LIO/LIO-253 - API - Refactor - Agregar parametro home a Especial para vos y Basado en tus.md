---
jira_key: "LIO-253"
aliases: ["LIO-253"]
summary: "API - Refactor - Agregar parametro \"home\" a \"Especial para vos\"  y \"Basado en tus busquedas\" para los datos de la home"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-06 15:52"
updated: "2025-03-10 23:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-253"
---

# LIO-253: API - Refactor - Agregar parametro "home" a "Especial para vos"  y "Basado en tus busquedas" para los datos de la home

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-06 15:52 |
| Actualizado | 2025-03-10 23:34 |
| Etiquetas | ninguna |
| Jira | [LIO-253](https://bluinc.atlassian.net/browse/LIO-253) |

## Relaciones

- **Padre:** [[LIO-166 - Catalogos y sincronizaciones|LIO-166]] Catalogos y sincronizaciones
- **action item from:** [[LIO-252 - APP - Refactor - Agregar al catalogo la sección Basado en tus busquedas y|LIO-252]] APP - Refactor - Agregar al catalogo la sección "Basado en tus busquedas" y enlazar en la home 
- **has action item:** [[LIO-251 - APP - Refactor - Agregar al catalogo la seccion Especial para vos y enlazarla|LIO-251]] APP - Refactor - Agregar al catalogo la seccion "Especial para vos" y enlazarla en la home

## Descripcion

Agregaremos el parámetro `home` para ambos recursos de modo tal que pueda traer los primeros resultados, segun la cantidad que indique el parámetro (generalmente uno) para poder componer los banners

Ejemplo

```
GET {API_V4}/v4/basedOnYourSearches?search=&offset=0&home=2
```

Devuelve

```
...
        {
            "id": 344979,
            "internalId": 103094,
            "description": "PROCESADOR AMD (AM4) RYZEN 3 3200G",
            "image": "c39621c8b7d6496567406e7e63e164c9.jpg",
            "brandImage": "266f407b98b3c0721710b6c651d4108f.jpg",
            "brandId": 3169,
            "brandName": "AMD",
            "categoryId": 44,
            "categoryName": "Procesadores",
            "freeShipping": false,
            "bestSeller": null,
            "instantFlash": false,
            "ratingStar": null,
            "price": {
                "listPrice": 80847.66,
                "discount": 0,
                "finalPrice": 80847.66
            },
            "sellerId": 447,
            "sellerName": "Gears Store",
            "gtin": null,
            "sku": "YD3200C5FHBOX"
        },
        {
            "id": 677568,
            "internalId": 116948,
            "description": "PROCESADOR AMD (AM4) RYZEN 5 4600G",
            "image": "2e33aaa87c3090cc8c12f6de800022ff.jpeg",
            "brandImage": "266f407b98b3c0721710b6c651d4108f.jpg",
            "brandId": 3169,
            "brandName": "AMD",
            "categoryId": 44,
            "categoryName": "Procesadores",
            "freeShipping": true,
            "bestSeller": null,
            "instantFlash": false,
            "ratingStar": null,
            "price": {
                "listPrice": 148559.04,
                "discount": 0,
                "finalPrice": 148559.04
            },
            "sellerId": 45,
            "sellerName": null,
            "gtin": null,
            "sku": "100-100000147BOX"
        }
...
```
