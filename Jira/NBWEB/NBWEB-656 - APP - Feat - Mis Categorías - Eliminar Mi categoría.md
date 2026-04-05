---
jira_key: "NBWEB-656"
aliases: ["NBWEB-656"]
summary: "APP - Feat - Mis Categorías -> Eliminar \"Mi categoría\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-03-18 16:31"
updated: "2024-03-20 14:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-656"
---

# NBWEB-656: APP - Feat - Mis Categorías -> Eliminar "Mi categoría"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-03-18 16:31 |
| Actualizado | 2024-03-20 14:43 |
| Etiquetas | ninguna |
| Jira | [NBWEB-656](https://bluinc.atlassian.net/browse/NBWEB-656) |

## Relaciones

- **Padre:** [[NBWEB-641]] Listas de precio
- **relates to:** [[NBWEB-652]] API - Feat -Mis Categorías -> Eliminar "Mi categoría"

## Descripcion

Agregaremos una nueva característica para poder eliminar la categoría creada por el usuario.

```
DELETE {{API_URL}}/v1/miCuenta/misCategorias/{categoryUserId}
```

[adjunto]
