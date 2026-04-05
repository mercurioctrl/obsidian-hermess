---
jira_key: "NBWEB-768"
aliases: ["NBWEB-768"]
summary: "API - Refactor - Agregar medidas al catalogo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-16 07:21"
updated: "2024-07-23 15:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-768"
---

# NBWEB-768: API - Refactor - Agregar medidas al catalogo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-16 07:21 |
| Actualizado | 2024-07-23 15:46 |
| Etiquetas | ninguna |
| Jira | [NBWEB-768](https://bluinc.atlassian.net/browse/NBWEB-768) |

## Relaciones

- **Padre:** [[NBWEB-682]] Productos
- **blocks:** [[NBWEB-769]] EXTESION - Refactor - Agregar medidas a la importación que se hace con woocomerce 

## Descripcion

1- Mediremos cuanto demora el recurso en traer todo el catalogo

2 - Agregaremos a la tabla `[NewBytes_DBF].[dbo].[articulo]` los parámetros `highAverage`,`widthAverage`,`lengthAverage`,`weightAverage`

3 - Modificaremos el recurso de catalogo para agregar estos parámetros `highAverage`,`widthAverage`,`lengthAverage`,`weightAverage` teniendo en cuenta que de no encontrarse en `[NewBytes_DBF].[dbo].[articulo]`  lo traeremos de `[NewBytes_DBF].[dbo].[familias]`

4- Mediremos cuanto demora el recurso en traer todo el catalogo y lo ajustaremos para obtener una performance similar o mejor a la inicial 

```
GET {{API_URL}}/v1/
```

```
[
    {
        "title": "OUTLET AMD ATHLON 5150 1.6 GHBOX",
        "sku": "O5150AMD",
        "id": 5199,
        "category": "OUTLET",
        "categoryId": 8,
        "brand": "AMD",
        "brandId": 43,
        "mainImage": "https://static.nb.com.ar/i/nb_OUTLET-AMD-ATHLON-5150-1.6-GHBOX_ver_e51b37755db5fc014e72b5648cf38535.jpeg",
        "brandImage": "https://static.nb.com.ar/img/266f407b98b3c0721710b6c651d4108f.jpg",
        "initialB": 5,
        "initialC": 10,
        "stock": "Bajo",
        "amountInCart": 0,
        "amountStock": 1,
        "categoryIdUser": null,
        "categoryDescriptionUser": null,
        "utility": null,
        "price": {
            "value": 44.79253,
            "iva": 10.5,
            "finalPrice": 49.495745649999996,
            "percepcion": null,
            "finalPriceWithUtility": 49.49575,
            "ncostoextra": 0
        },
        "warranty": "3 meses",
        "cotizacion": 940.5,
        "highAverage": 1000.0,
        "widthAverage": 5000.0,
        "lengthAverage": 1000.0,
        "weightAverage": 30000.0,
    },
    
  ...
```
