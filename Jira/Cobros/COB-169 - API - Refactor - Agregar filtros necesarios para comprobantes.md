---
jira_key: "COB-169"
aliases: ["COB-169"]
summary: "API - Refactor - Agregar filtros necesarios para comprobantes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-10-14 13:01"
updated: "2022-10-27 08:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-169"
---

# COB-169: API - Refactor - Agregar filtros necesarios para comprobantes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-14 13:01 |
| Actualizado | 2022-10-27 08:06 |
| Etiquetas | ninguna |
| Jira | [COB-169](https://bluinc.atlassian.net/browse/COB-169) |

## Relaciones

- **Padre:** [[COB-3]] API - Feat - Listar movimiento por caja
- **is blocked by:** [[COB-3]] API - Feat - Listar movimiento por caja
- **blocks:** [[COB-166]] MS - Feat - Ms comprobantes, recurso de recibo de dinero

## Descripcion

Se deben agregar los filtros por cnumalb e id para poder llamar al recurso de modo tal que pueda reutilizarse para enlazar comprobantes.

[link](https://lioteam.atlassian.net/browse/COB-3)

En el caso de que se llama cnumbal, se trae un array con todo el grupo (tal cual lo hace el matcheo), sino por id, se trae individualmente.
