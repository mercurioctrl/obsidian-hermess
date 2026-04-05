---
jira_key: "COM-118"
aliases: ["COM-118"]
summary: "API - Feat - Listar categorias"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-06-26 09:12"
updated: "2024-06-28 15:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-118"
---

# COM-118: API - Feat - Listar categorias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-26 09:12 |
| Actualizado | 2024-06-28 15:13 |
| Etiquetas | ninguna |
| Jira | [COM-118](https://bluinc.atlassian.net/browse/COM-118) |

## Relaciones

- **Padre:** [[COM-117 - Listar Editar Categorias|COM-117]] Listar / Editar Categorias
- **blocks:** [[COM-120 - APP - Feat - Pestaña categorias|COM-120]] APP - Feat - Pestaña categorias
- **relates to:** [[COM-122 - API - Refactor - Listar categorías - Mostrar no visibles en la web|COM-122]] API - Refactor - Listar categorías - Mostrar no visibles en la web

## Descripcion

Agregaremos un recurso para listar las categorías, adicionalmente agregaremos una columna en la tabla `[NewBytes_DBF].[dbo].[familias]` para almacenar un a posición arancelaria que tienen los productos de esa categoría por default llamado `defaultTariffPosition`

```
GET {{API_URL}}/v1/categories
```

```
[
  {
    "id": 1,
    "webShow": 1,
    "description": "MEMORIAS",
    "alphaCode": "0001",
    "highAverage": 1000.0,
    "widthAverage": 5000.0,
    "lengthAverage": 1000.0,
    "weightAverage": 30000.0,
    "initStockMedium": 5,
    "initStockLarge": 10,
    "defaultTariffPosition": '8471.60.53.000Q'
  },
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
...
]
```

```
SELECT  f1.cnomfam as description, f1.ID_FAMILIA as id, CASE WHEN f2.inicioBdesc is not null THEN f2.inicioBdesc ELSE 5 END as initialB,
            CASE WHEN f2.inicioCdesc is not null THEN f2.inicioCdesc ELSE 10 END  as initialC
            FROM NewBytes_DBF.dbo.familias as f1 LEFT JOIN NB_WEB.dbo.familias as f2 ON f2.ccodfam = f1.ccodfam WHERE f2.mostrar = 1  AND f1.sitio IS NOT NULL ORDER BY f1.cnomfam ASC
```
