---
jira_key: "INV-70"
aliases: ["INV-70"]
summary: "API - Feat - Repositorio de categorias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-07 09:53"
updated: "2024-06-11 13:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-70"
---

# INV-70: API - Feat - Repositorio de categorias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-07 09:53 |
| Actualizado | 2024-06-11 13:42 |
| Etiquetas | ninguna |
| Jira | [INV-70](https://bluinc.atlassian.net/browse/INV-70) |

## Relaciones

- **Padre:** [[INV-69]] Categorias
- **blocks:** [[INV-71]] APP - Feat - Pestaña de categorias

## Descripcion

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
    "initStockLarge": 10
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
    "initStockLarge":10
  }
...
]
```
