---
jira_key: "POS-318"
aliases: ["POS-318"]
summary: "API - Funcionalidad \"rollback\""
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Ezequiel manzano"
created: "2024-09-10 16:30"
updated: "2024-09-20 05:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-318"
---

# POS-318: API - Funcionalidad "rollback"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Ezequiel manzano |
| Creado | 2024-09-10 16:30 |
| Actualizado | 2024-09-20 05:38 |
| Etiquetas | ninguna |
| Jira | [POS-318](https://bluinc.atlassian.net/browse/POS-318) |

## Relaciones

- **relates to:** [[SNB-2297]] RMA 35378 retroceder orden
- **relates to:** [[POS-319]] APP - Rollback order
- **relates to:** [[POS-321]] API - Refactor - Rollback order - No regresar a ingresos ordenes entregadas

## Descripcion

Se debe agregar un recurso para poder hacer un rollback de las postvetnas q estan finalizadas, pero el estao de testeo es incorrecto. Simpre y cuando el resultado de testeo no sea ni Cambio ni Credito
