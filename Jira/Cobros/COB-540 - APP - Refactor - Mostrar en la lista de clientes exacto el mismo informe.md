---
jira_key: "COB-540"
aliases: ["COB-540"]
summary: "APP - Refactor - Mostrar en la lista de clientes exacto el mismo informe crediticio que se obtiene en la cuenta corriente con \"balances\""
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-08-13 09:32"
updated: "2024-08-15 02:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-540"
---

# COB-540: APP - Refactor - Mostrar en la lista de clientes exacto el mismo informe crediticio que se obtiene en la cuenta corriente con "balances"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-13 09:32 |
| Actualizado | 2024-08-15 02:43 |
| Etiquetas | ninguna |
| Jira | [COB-540](https://bluinc.atlassian.net/browse/COB-540) |

## Relaciones

- **Padre:** [[COB-538 - Oportunidad de Mejora Mostrar exacto la misma informacion dentro y fuera del|COB-538]] Oportunidad de Mejora: Mostrar exacto la misma informacion dentro y fuera del estado crediticio del cliente
- **is blocked by:** [[COB-539 - API - Refactor - Entregar los mismos parametros en el listado de clientes, que|COB-539]] API - Refactor - Entregar los mismos parametros en el listado de clientes, que en el recurso balances

## Descripcion

Basandonos en el refactor [link](https://lioteam.atlassian.net/browse/COB-539)  que agregara el parametro `limitCheckBalanceAmount` y arreglara los otros, debemos dejar el listado de clientes luego de la columna percepciones



[adjunto]
Lo que haremos sera agregar las mismas columnas que están dentro de la cuenta corriente, es decir:

- **Disponible**


- **Límite de crédito**


- **Deuda cheque**


- **Límite cheque**


- **Cheque disponible**



[adjunto]
