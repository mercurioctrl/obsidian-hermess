---
jira_key: "COM-119"
aliases: ["COM-119"]
summary: "API - Feat - Editar Categorias"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-06-26 09:12"
updated: "2024-06-27 16:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-119"
---

# COM-119: API - Feat - Editar Categorias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-26 09:12 |
| Actualizado | 2024-06-27 16:26 |
| Etiquetas | ninguna |
| Jira | [COM-119](https://bluinc.atlassian.net/browse/COM-119) |

## Relaciones

- **Padre:** [[COM-117 - Listar Editar Categorias|COM-117]] Listar / Editar Categorias
- **blocks:** [[COM-120 - APP - Feat - Pestaña categorias|COM-120]] APP - Feat - Pestaña categorias

## Descripcion

Agregaremos un recurso para listar las categorías, adicionalmente agregaremos una columna en la tabla `[NewBytes_DBF].[dbo].[familias]` para almacenar un a posición arancelaria que tienen los productos de esa categoría por default llamado `defaultTariffPosition`

```
PATCH {{API_URL}}/v1/categories
```

```
[
  {
    "id": 2,
    "webShow": 1,
    "description": "DISCOS HDD",
    "alphaCode": "0002",
    "highAverage": 10000.0,
    "widthAverage": 10200.0,
    "lengthAverage": 10000.0,
    "weightAverage": 97000.0,
    "initStockMedium": 5,
    "initStockLarge":10,
    "defaultTariffPosition": '8471.60.53.000Q'
  }
]
```
