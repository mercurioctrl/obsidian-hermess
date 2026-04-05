---
jira_key: "PED-1057"
aliases: ["PED-1057"]
summary: "API - Refactor - Agregar I. Internos a las ordenes que son Import/Export (tierra del fuego), pero no el IVA, solo impuesto interno."
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-21 13:07"
updated: "2025-08-04 10:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1057"
---

# PED-1057: API - Refactor - Agregar I. Internos a las ordenes que son Import/Export (tierra del fuego), pero no el IVA, solo impuesto interno.

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-21 13:07 |
| Actualizado | 2025-08-04 10:29 |
| Etiquetas | ninguna |
| Jira | [PED-1057](https://bluinc.atlassian.net/browse/PED-1057) |

## Relaciones

- **Padre:** [[PED-34 - Generar Editar ordenes|PED-34]] Generar / Editar ordenes
- **has action item:** [[SNB-3260 - ERROR pedido a tierra del fuego impuestos|SNB-3260]] ERROR pedido a tierra del fuego impuestos

## Descripcion

Por lo visto en el caso [link](https://bluinc.atlassian.net/jira/servicedesk/projects/SNB/queues/custom/63/[[SNB-3260]])  deberemos agregar para los casos donde la categoria es Import / Export el impuesto interno.

Quizas si lo toma directo desde precios es un cambio siemple, pero en definitiva hay qu revisar si impacta sobre ordenes, pedidos, pedido + info y liquidación.

Es probable que haciendo el cambio al principio impacte en todo, pero avisame cualquier cosa y revisamos sino!
