---
jira_key: "NBWEB-652"
aliases: ["NBWEB-652"]
summary: "API - Feat -Mis Categorías -> Eliminar \"Mi categoría\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-03-18 14:15"
updated: "2024-03-20 14:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-652"
---

# NBWEB-652: API - Feat -Mis Categorías -> Eliminar "Mi categoría"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-03-18 14:15 |
| Actualizado | 2024-03-20 14:43 |
| Etiquetas | ninguna |
| Jira | [NBWEB-652](https://bluinc.atlassian.net/browse/NBWEB-652) |

## Relaciones

- **Padre:** [[NBWEB-641]] Listas de precio
- **relates to:** [[NBWEB-656]] APP - Feat - Mis Categorías -> Eliminar "Mi categoría"

## Descripcion

Se creará un nuevo recurso encargado de eliminar permanentemente la categoría del cliente. Es fundamental llevar a cabo una verificación para asegurar que el ID de la categoría pertenezca al usuario que intenta eliminarla.

```
DELETE {{API_URL}}/v1/miCuenta/misCategorias/{categoryUserId}
```
