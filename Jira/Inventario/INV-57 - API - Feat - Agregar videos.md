---
jira_key: "INV-57"
aliases: ["INV-57"]
summary: "API - Feat - Agregar videos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-21 14:04"
updated: "2025-09-02 08:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-57"
---

# INV-57: API - Feat - Agregar videos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-21 14:04 |
| Actualizado | 2025-09-02 08:24 |
| Etiquetas | ninguna |
| Jira | [INV-57](https://bluinc.atlassian.net/browse/INV-57) |

## Relaciones

- **Padre:** [[INV-27]] Productos
- **blocks:** [[INV-58]] API - Feat - Remover video
- **blocks:** [[INV-59]] APP - Feat - Agregar y remover videos 

## Descripcion

```
PATCH {API_URL}/item/{itemId}
```

Carga útil

```
{
"videoId":"yH2J29Bj5aY"
}
```

Utilizaremos la tabla `[PRODUCTOS].[dbo].[videos]` para agregar los registros para cada item
