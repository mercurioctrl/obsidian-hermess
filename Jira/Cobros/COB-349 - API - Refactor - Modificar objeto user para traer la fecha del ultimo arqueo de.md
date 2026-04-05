---
jira_key: "COB-349"
aliases: ["COB-349"]
summary: "API - Refactor - Modificar objeto user para traer la fecha del ultimo arqueo de caja"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-10 08:30"
updated: "2023-03-13 15:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-349"
---

# COB-349: API - Refactor - Modificar objeto user para traer la fecha del ultimo arqueo de caja

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-10 08:30 |
| Actualizado | 2023-03-13 15:26 |
| Etiquetas | ninguna |
| Jira | [COB-349](https://bluinc.atlassian.net/browse/COB-349) |

## Relaciones

- **Padre:** [[COB-347 - Poder ver saldo inicial y final de caja en cada día|COB-347]] Poder ver saldo inicial y final de caja en cada día

## Descripcion

Agregaremos al objeto del recurso user el parámetro `cashRegisterOk`con el propósito de saber si para el día de la fecha actual, ya se hizo el arqueo de caja. Y en caso contrario obligar al cajero a realizarlo.

Si el parámetro es `true`, quiere decir que para el día de la fecha, ya existe el registro. De lo contrario informara `false`.
