---
jira_key: "COB-387"
aliases: ["COB-387"]
summary: "API - Refactor - Integrar nuevos estados \"finalizados\" al realizar un cobro pendiente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-29 09:55"
updated: "2023-03-30 10:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-387"
---

# COB-387: API - Refactor - Integrar nuevos estados "finalizados" al realizar un cobro pendiente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-29 09:55 |
| Actualizado | 2023-03-30 10:36 |
| Etiquetas | ninguna |
| Jira | [COB-387](https://bluinc.atlassian.net/browse/COB-387) |

## Relaciones

- **Padre:** [[COB-115 - Feat - Realizar un cobro|COB-115]] Feat - Realizar un cobro

## Descripcion

Al realizar un cobro, de un pedido que se encuentra en “Despachado, pendiente a cobrar (3)” o “Entregado, Pendiente a cobrar (14)”

Debe pasar a estado “Entregado Cobrado” (13).
