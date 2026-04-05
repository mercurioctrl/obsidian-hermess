---
jira_key: "NBWEB-902"
aliases: ["NBWEB-902"]
summary: "API - Refactor - Agregar vídeo cuando esta disponible"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-10-20 18:37"
updated: "2024-10-22 03:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-902"
---

# NBWEB-902: API - Refactor - Agregar vídeo cuando esta disponible

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-20 18:37 |
| Actualizado | 2024-10-22 03:11 |
| Etiquetas | ninguna |
| Jira | [NBWEB-902](https://bluinc.atlassian.net/browse/NBWEB-902) |

## Relaciones

- **Padre:** [[NBWEB-682 - Productos|NBWEB-682]] Productos
- **has action item:** [[NBWEB-901 - APP - Refactor - Agregar video cuando este esta disponible|NBWEB-901]] APP - Refactor - Agregar video cuando este esta disponible

## Descripcion

```
GET {API_URL}/v1/ytVideo/{itemId}
```

```
{
"videoId":"yH2J29Bj5aY"
}
```

Utilizaremos la tabla `[PRODUCTOS].[dbo].[videos]` para leer los registros para cada item
