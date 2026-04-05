---
jira_key: "INV-319"
aliases: ["INV-319"]
summary: "APP - Refactor - Mover stock por ítem"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-08 08:28"
updated: "2026-01-21 19:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-319"
---

# INV-319: APP - Refactor - Mover stock por ítem

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-08 08:28 |
| Actualizado | 2026-01-21 19:26 |
| Etiquetas | ninguna |
| Jira | [INV-319](https://bluinc.atlassian.net/browse/INV-319) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios

## Descripcion

Esto resuelve lo mismo que lo que se resuelve en [link](https://bluinc.atlassian.net/browse/INV-318) 

Por lo tanto para evitar errores agregaremos un selector de deposito para el `companyCode` determinado en el modal de “mover stock”

[adjunto]
Si no esta preseleccionado, para realizar el movimiento es obligatorio seleccionarlo.

Adicionalmente, para tener un panorama visual de donde estan las distintas unidades, incluiremos una vista debajo de la grilla resultante de  [link](https://bluinc.atlassian.net/browse/INV-313)
