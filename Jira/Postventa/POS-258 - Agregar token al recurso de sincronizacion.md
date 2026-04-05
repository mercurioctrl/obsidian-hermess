---
jira_key: "POS-258"
aliases: ["POS-258"]
summary: "Agregar token al recurso de sincronizacion"
status: "CodeReview"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-06-07 17:28"
updated: "2023-06-08 09:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-258"
---

# POS-258: Agregar token al recurso de sincronizacion

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-07 17:28 |
| Actualizado | 2023-06-08 09:58 |
| Etiquetas | ninguna |
| Jira | [POS-258](https://bluinc.atlassian.net/browse/POS-258) |

## Relaciones

- **Padre:** [[POS-22 - Dashboard y estadisticas|POS-22]] Dashboard y estadisticas

## Descripcion

Agregaremos un token para ejecutar la tarea y el valor del mismo se encuentra en las variables de entorno

```
GET {{API_URL}}/v1/metrics/cronProducts?between={fecha}&token={tokenEnEl.Env}
```
