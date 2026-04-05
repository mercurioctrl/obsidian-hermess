---
jira_key: "EXP-443"
aliases: ["EXP-443"]
summary: "APP - Refactor PickUps y Shipments"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Ezequiel manzano"
created: "2024-09-06 14:59"
updated: "2024-09-10 10:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-443"
---

# EXP-443: APP - Refactor PickUps y Shipments

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Ezequiel manzano |
| Creado | 2024-09-06 14:59 |
| Actualizado | 2024-09-10 10:45 |
| Etiquetas | ninguna |
| Jira | [EXP-443](https://bluinc.atlassian.net/browse/EXP-443) |

## Relaciones

- **relates to:** [[SNB-2224]] mejora para el sistema

## Descripcion

Se debe refactorzar la grilla de retiros y envios.-



Se agregó un nuevo campo al objeto

“authorizedDate” : 



Se debe mostrar sobre el campo de “fecha” que esta actualmente, pero no siempre authorizedDate va a ser una fecha como tal, dado que puede apareer un pedido sin autorizar en esa tabla.

En ese caso debes mostrar la fecha de pedido que es “date” .

Si no está muy claro avisame q lo hablamos
