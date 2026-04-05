---
jira_key: "COB-388"
aliases: ["COB-388"]
summary: "API - Refactor - Al editar un cliente que no tiene saldo, no hace la inserción de manera correcta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-03-30 15:19"
updated: "2023-04-26 18:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-388"
---

# COB-388: API - Refactor - Al editar un cliente que no tiene saldo, no hace la inserción de manera correcta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-30 15:19 |
| Actualizado | 2023-04-26 18:12 |
| Etiquetas | ninguna |
| Jira | [COB-388](https://bluinc.atlassian.net/browse/COB-388) |

## Relaciones

- **Padre:** [[COB-374]] Feat - Editar estado crediticio de la cuenta del cliente
- **is blocked by:** [[COB-376]] API - Feat - Editar saldo de credito por cliente

## Descripcion

- Fijarse que no se creen dos registros en la tabla para un usuario que ya tiene algún movimiento


- Fijarse que no se creen dos registros en la tabla para un usuario que NO tienen ningún movimiento



deberia poder meterte saldo al cliente en la cuenta



pero se ve que ema no contemplo el caso donde aun el cliente nunca tuvo saldo



(solo hace un update)



habria que meter un refactor, para poder hacer un "IF EXISTS" o bien comprobar si existe y hacer un insert cuando corresponde o un update
