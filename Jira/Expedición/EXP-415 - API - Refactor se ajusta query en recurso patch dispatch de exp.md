---
jira_key: "EXP-415"
aliases: ["EXP-415"]
summary: "API - Refactor se ajusta query en recurso patch dispatch de exp"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-06-10 17:46"
updated: "2024-06-13 19:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-415"
---

# EXP-415: API - Refactor se ajusta query en recurso patch dispatch de exp

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-06-10 17:46 |
| Actualizado | 2024-06-13 19:51 |
| Etiquetas | ninguna |
| Jira | [EXP-415](https://bluinc.atlassian.net/browse/EXP-415) |

## Relaciones

*Sin relaciones*

## Descripcion

Se remueve el join con la tabla  `liquidacion_guardada`  tomando como referencia de pago solo aquellas que participan en la liquidacion.
