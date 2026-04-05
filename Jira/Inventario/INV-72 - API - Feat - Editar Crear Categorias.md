---
jira_key: "INV-72"
aliases: ["INV-72"]
summary: "API - Feat - Editar / Crear Categorias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-07 09:54"
updated: "2024-06-12 13:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-72"
---

# INV-72: API - Feat - Editar / Crear Categorias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-07 09:54 |
| Actualizado | 2024-06-12 13:04 |
| Etiquetas | ninguna |
| Jira | [INV-72](https://bluinc.atlassian.net/browse/INV-72) |

## Relaciones

- **Padre:** [[INV-69 - Categorias|INV-69]] Categorias
- **blocks:** [[INV-71 - APP - Feat - Pestaña de categorias|INV-71]] APP - Feat - Pestaña de categorias
- **is blocked by:** [[INV-76 - API - Editar Crear Categorías - Stock guardado no coincidente|INV-76]] API - Editar / Crear Categorías - Stock guardado no coincidente 
- **relates to:** [[INV-78 - API - Refactor - Editar Crear Categorías - Ocultar categoría en el sitio web|INV-78]] API - Refactor - Editar / Crear Categorías - Ocultar categoría en el sitio web

## Descripcion

```
POST {{API_URL}}/v1/categories
```

```
[
  {
    "webShow": 1,
    "description": "MEMORIAS",
  }
]
```

```
PATCH {{API_URL}}/v1/categories
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
  }
]
```
