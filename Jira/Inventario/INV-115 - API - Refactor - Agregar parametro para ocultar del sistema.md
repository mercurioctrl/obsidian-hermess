---
jira_key: "INV-115"
aliases: ["INV-115"]
summary: "API - Refactor - Agregar parametro para ocultar del sistema"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-09 18:05"
updated: "2024-09-13 03:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-115"
---

# INV-115: API - Refactor - Agregar parametro para ocultar del sistema

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-09 18:05 |
| Actualizado | 2024-09-13 03:38 |
| Etiquetas | ninguna |
| Jira | [INV-115](https://bluinc.atlassian.net/browse/INV-115) |

## Relaciones

- **Padre:** [[INV-69]] Categorias
- **blocks:** [[INV-116]] APP - Refactor - Cambiar columnas de ocultar para el sistema y mostrar en la web
- **relates to:** [[INV-121]] API - Refactor - Parámetro para ocultar del sistema - Agregar al consultar
- **is blocked by:** [[INV-124]] API - Agregar parámetro para ocultar del sistema - Discrepancias al ocultar/mostrar la categoría

## Descripcion

```
POST {{API_URL}}/v1/categories
```

```
[
  {
    "hide": 1,
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
    ...
    "hide": 1,
    ...
  }
]
```

Esto altera el parámetro `[NB_WEB].[dbo].[familias].mostrar`
