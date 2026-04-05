---
jira_key: "INV-78"
summary: "API - Refactor - Editar / Crear Categorías - Ocultar categoría en el sitio web"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-06-12 13:03"
updated: "2024-09-13 03:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-78"
---

# INV-78: API - Refactor - Editar / Crear Categorías - Ocultar categoría en el sitio web

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-12 13:03 |
| Actualizado | 2024-09-13 03:28 |
| Etiquetas | ninguna |
| Jira | [INV-78](https://bluinc.atlassian.net/browse/INV-78) |

## Descripción

Actualmente, al ocultar una categoría desde el sistema de Inventario, no se oculta la categoría en el sitio web. Por lo que realizaremos un refactor para que al ocultar una categoría:

En lugar de apuntar a `NewBytes_DBF.dbo.familias.sitio`

Apunte a `NB_WEB.dbo.familias.mostrar`



```
PATCH {{API_URL}}/categories
```

[attachment]
[attachment]
