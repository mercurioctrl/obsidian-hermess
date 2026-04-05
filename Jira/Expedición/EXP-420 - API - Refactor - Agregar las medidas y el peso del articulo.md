---
jira_key: "EXP-420"
aliases: ["EXP-420"]
summary: "API - Refactor - Agregar las medidas y el peso del articulo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-24 10:02"
updated: "2024-07-25 17:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-420"
---

# EXP-420: API - Refactor - Agregar las medidas y el peso del articulo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-24 10:02 |
| Actualizado | 2024-07-25 17:38 |
| Etiquetas | ninguna |
| Jira | [EXP-420](https://bluinc.atlassian.net/browse/EXP-420) |

## Relaciones

- **Padre:** [[EXP-17]] Feat - Listar productos (Control de stock)
- **blocks:** [[EXP-422]] APP - Refactor - En el modulo de conteo se deben poder visualizar y editar tambien medidas y pesos

## Descripcion

Refactorizaremos el recurso para entregarnos las medidas del item si es que las tiene

En este caso, solo son las del items y no la de la categoría, ya que lo que intentamos es completar esta informacion a nivel del item

```
GET {API_URL}/v1/items
```

```
{
    "response": [
        {
            "title": "PLACA DE VIDEO SAPPHIRE PULSE RX 6600 XT OC 8 GB",
            "sku": "11309-03-20G",
            "id": "115279",
            "category": "PLACA DE VIDEO",
            "categoryId": "23",
            "brandId": "20",
            "brand": "SAPPHIRE                                          ",
            "imagenMarca": "https:\/\/static.nb.com.ar\/img\/c722679c6ad3d477686634a1a882b027.jpg",
            "imagenPrincipal": "f1d55640d8e0b039809f43902ea872a5.jpg",
            "counted": null,
            "countedDate": null,
            "createDate": "2024-06-19 13:24:46.417",
            "countable": "1",
            "weightAverage": null,
            "lengthAverage": null,
            "widthAverage": null,
            "highAverage": null            
        },
        {
            "title": "SAMSUNG TV 85 SMART 4K QLED UHD Q70",
            "sku": "QN85Q70AAGCZB",
            "id": "116489",
            "category": "TELEVISORES",
            "categoryId": "67",
            "brandId": "3",
            "brand": "SAMSUNG",
            "imagenMarca": "https:\/\/static.nb.com.ar\/img\/a092ae5731dc904e0b8c1328992e0a9c.jpg",
            "imagenPrincipal": "3cb5d66ce89ddcac4220e759fbfd343e.png",
            "counted": null,
            "countedDate": null,
            "createDate": "2024-06-19 13:02:26.183",
            "countable": "1",
            "weightAverage": null,
            "lengthAverage": null,
            "widthAverage": null,
            "highAverage": null            
        },
...
]
}
```

```
SELECT 
      [weightAverage]
      ,[lengthAverage]
      ,[widthAverage]
      ,[highAverage]
  FROM [NewBytes_DBF].[dbo].[articulo]
```
