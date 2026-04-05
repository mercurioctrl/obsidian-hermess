---
jira_key: "POS-319"
aliases: ["POS-319"]
summary: "APP - Rollback order"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Ezequiel manzano"
created: "2024-09-11 16:35"
updated: "2024-09-20 05:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-319"
---

# POS-319: APP - Rollback order

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Ezequiel manzano |
| Creado | 2024-09-11 16:35 |
| Actualizado | 2024-09-20 05:35 |
| Etiquetas | ninguna |
| Jira | [POS-319](https://bluinc.atlassian.net/browse/POS-319) |

## Relaciones

- **relates to:** [[POS-318 - API - Funcionalidad rollback|POS-318]] API - Funcionalidad "rollback"
- **relates to:** [[POS-320 - APP - Refactor - Rollback order - No regresar a ingresos ordenes entregadas|POS-320]] APP - Refactor - Rollback order - No regresar a ingresos ordenes entregadas

## Descripcion

Se creo el recurso 

{{API_URL}}/v1/afterSales/{rmaId}/finalized/rollback



Para poder volver una orden finalizada a ingresos, siempre y cuando la orden no tenga en el detalle un cambio o un credito. 

Habría q agregar una opcion en el desplegable para realizar esto. Avisame si necewsitas una mano
