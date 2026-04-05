---
jira_key: "COB-324"
aliases: ["COB-324"]
summary: "API - Refactor - Agregar nombre real del agente en los movimientos de ccc"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-02-02 09:02"
updated: "2023-02-02 12:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-324"
---

# COB-324: API - Refactor - Agregar nombre real del agente en los movimientos de ccc

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-02-02 09:02 |
| Actualizado | 2023-02-02 12:41 |
| Etiquetas | ninguna |
| Jira | [COB-324](https://bluinc.atlassian.net/browse/COB-324) |

## Relaciones

- **Padre:** [[COB-322 - Refactor - Agregar nombre real a los movimientos de cc|COB-322]] Refactor - Agregar nombre real a los movimientos de cc

## Descripcion

Haremos un refactor para poder mostrar de manera correcta el nombre del operador del movimiento en el recurso [link](https://lioteam.atlassian.net/browse/COB-5) 

Es decir, si es CAJA1, deberíamos mostrar Carla Carpintieri.

No sacaremos el parametro del objeto, sino que agregaremos uno nuevo llamado `agentDescription`
