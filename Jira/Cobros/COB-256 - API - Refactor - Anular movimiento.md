---
jira_key: "COB-256"
aliases: ["COB-256"]
summary: "API - Refactor - Anular movimiento"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-12-15 12:10"
updated: "2022-12-27 07:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-256"
---

# COB-256: API - Refactor - Anular movimiento

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-15 12:10 |
| Actualizado | 2022-12-27 07:47 |
| Etiquetas | ninguna |
| Jira | [COB-256](https://bluinc.atlassian.net/browse/COB-256) |

## Relaciones

- **Padre:** [[COB-5]] API - Feat - Obtener cuenta corriente de un cliente

## Descripcion

Esta historia trata sobre la refactorizacion que se necesita al momento de anular un movimiento SEMPRE QUE ESTE SEA UN COBRO, de modo tal que dentro de la cuenta corriente del cliente se haga la operación inversa (Debito a la cuenta) para anular el valor que se le acaba de cobrar.

Entiendo que debe utilizarse el `id = 32` de la tabla `GR_TRANSACCIONES` (débitos varios).

Si no se trata de una operacion que no altera la Cuenta corriente del cliente, no hacer nada.
