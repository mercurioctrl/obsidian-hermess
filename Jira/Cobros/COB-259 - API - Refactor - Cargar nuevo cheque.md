---
jira_key: "COB-259"
aliases: ["COB-259"]
summary: "API - Refactor - Cargar nuevo cheque"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-12-15 14:18"
updated: "2022-12-16 11:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-259"
---

# COB-259: API - Refactor - Cargar nuevo cheque

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-15 14:18 |
| Actualizado | 2022-12-16 11:32 |
| Etiquetas | ninguna |
| Jira | [COB-259](https://bluinc.atlassian.net/browse/COB-259) |

## Relaciones

- **Padre:** [[COB-188]] Feat - Cargar nuevo cheque
- **relates to:** [[COB-189]] API - Feat - Cargar nuevo cheque
- **blocks:** [[COB-257]] APP - Refactor - El ABM de cheques debe calcular la linea de cheques automáticamente al cargarse los mismo
- **blocks:** [[COB-260]] API - Refactor - Detalle cheque, agregar interes y cotizacion de cheque

## Descripcion

Haremos un refactor del recurso [link](https://lioteam.atlassian.net/browse/COB-189) para agregar 2 paremtros

`interest`

 `checkQuote`

Ambos vienen del front y deben guardarse en la cabecera del cheque
