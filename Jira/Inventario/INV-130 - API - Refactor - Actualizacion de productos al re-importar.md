---
jira_key: "INV-130"
aliases: ["INV-130"]
summary: "API - Refactor - Actualizacion de productos al \"re-importar\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-13 07:09"
updated: "2024-09-29 19:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-130"
---

# INV-130: API - Refactor - Actualizacion de productos al "re-importar"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-13 07:09 |
| Actualizado | 2024-09-29 19:43 |
| Etiquetas | ninguna |
| Jira | [INV-130](https://bluinc.atlassian.net/browse/INV-130) |

## Relaciones

- **Padre:** [[INV-125]] Importación de catálogos

## Descripcion

Al ejecutar al recurso [link](https://lioteam.atlassian.net/browse/INV-127)  se debe agregar un refactor para que al hacer un match que combine `sku` con `distributor` y `companyCode` entonces se haga un update de los campos, en lugar de insertarse.
