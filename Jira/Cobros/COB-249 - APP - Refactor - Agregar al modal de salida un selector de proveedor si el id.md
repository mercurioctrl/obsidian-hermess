---
jira_key: "COB-249"
aliases: ["COB-249"]
summary: "APP - Refactor - Agregar al modal de salida un selector de proveedor si el id del concepto es 3 o 35"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-12-05 15:35"
updated: "2022-12-06 16:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-249"
---

# COB-249: APP - Refactor - Agregar al modal de salida un selector de proveedor si el id del concepto es 3 o 35

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-05 15:35 |
| Actualizado | 2022-12-06 16:06 |
| Etiquetas | ninguna |
| Jira | [COB-249](https://bluinc.atlassian.net/browse/COB-249) |

## Relaciones

- **Padre:** [[COB-178 - API - Feat - Realizar transferencia entre bancos|COB-178]] API - Feat - Realizar transferencia entre bancos
- **is blocked by:** [[COB-248 - API - Refactor - Alterar saldo proveedor, en caso de que el concepto sea un|COB-248]] API - Refactor - Alterar saldo proveedor, en caso de que el concepto sea un "pago de factura" o "pago proveedor"

## Descripcion

Basándonos en el repositorio de [link](https://lioteam.atlassian.net/browse/COB-68) agregaremos un selector “con matcheo” por string y numero de proveedor en los casos que el id sea `3` o sea `35`

Adicionalmente debemos agregar el parámetros `providerId`
