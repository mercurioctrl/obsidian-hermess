---
jira_key: "INV-58"
aliases: ["INV-58"]
summary: "API - Feat - Remover video"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-21 14:04"
updated: "2025-09-02 08:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-58"
---

# INV-58: API - Feat - Remover video

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
| Jira | [INV-58](https://bluinc.atlassian.net/browse/INV-58) |

## Relaciones

- **Padre:** [[INV-27 - Productos|INV-27]] Productos
- **is blocked by:** [[INV-57 - API - Feat - Agregar videos|INV-57]] API - Feat - Agregar videos
- **blocks:** [[INV-59 - APP - Feat - Agregar y remover videos|INV-59]] APP - Feat - Agregar y remover videos 

## Descripcion

```
DELETE {API_URL}/item/{itemId}
```

Carga útil

```
{
"videoId":"yH2J29Bj5aY"
}
```

Cuando recibimos el parámetro `videoId` con el verbo delete para in item determinado, lo buscaremos en la tabla`[PRODUCTOS].[dbo].[videos]` y lo removeremos
