---
jira_key: "COM-196"
aliases: ["COM-196"]
summary: "API - Refactor - MVP - Hacer que el repositorio de categorías sea reactivo al filtro de empresa"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-25 10:05"
updated: "2025-10-02 15:06"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/COM-196"
---

# COM-196: API - Refactor - MVP - Hacer que el repositorio de categorías sea reactivo al filtro de empresa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-25 10:05 |
| Actualizado | 2025-10-02 15:06 |
| Etiquetas | MVPLaset |
| Jira | [COM-196](https://bluinc.atlassian.net/browse/COM-196) |

## Relaciones

- **Padre:** [[COM-116]] Categorias

## Descripcion

La idea es hacer el filtro reactivo a `companyCode`(`[NewBytes_DBF].[dbo].[familias].companyCode`)

```
GET /v1/categories?companyCode={companyCode}
```

```
[
    {
        "id": 1,
        "webShow": true,
        "description": "MEMORIAS",
        "alphaCode": "0001",
        "highAverage": 4000,
        "widthAverage": 100,
        "lengthAverage": 5,
        "weightAverage": 500,
        "initStockMedium": 5,
        "initStockLarge": 10,
        "defaultTariffPosition": null
    },
    {
        "id": 2,
        "webShow": true,
        "description": "DISCOS HDD",
        "alphaCode": "0002",
        "highAverage": 100,
        "widthAverage": 102,
        "lengthAverage": 100,
        "weightAverage": 970,
        "initStockMedium": 5,
        "initStockLarge": 35,
        "defaultTariffPosition": null
    }
]
```
