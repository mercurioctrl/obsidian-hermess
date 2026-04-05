---
jira_key: "COB-329"
aliases: ["COB-329"]
summary: "Refactor - Auto liquidar si el medio de pago es efectivo y retiro"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-02-07 14:01"
updated: "2023-12-12 21:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-329"
---

# COB-329: Refactor - Auto liquidar si el medio de pago es efectivo y retiro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-02-07 14:01 |
| Actualizado | 2023-12-12 21:12 |
| Etiquetas | ninguna |
| Jira | [COB-329](https://bluinc.atlassian.net/browse/COB-329) |

## Relaciones

- **Padre:** [[COB-33]] Cobrar
- **Subtarea:** [[COB-330]] API - Refactor - Autoliquidar si el medio de pago es efectivo y retiro
- **Subtarea:** [[COB-331]] API - Refactor - Modificar listado para que aparezcan aquellos pedidos no liquidados, para poder cobrarlos en efectivo
- **Subtarea:** [[COB-332]] APP - Refactor - Modificar modal de cobro para poder cobrar los "sin liquidar" pero solo en efectivo y retiro.
- **Subtarea:** [[COB-337]] API - Refactor - Tipo de cambio especifico para pedidos de libre opcion
- **Subtarea:** [[COB-338]] API - Refactor - Olvide un cambio que hay que hacer en albclit al liquidar con exito
- **Subtarea:** [[COB-345]] API - Refactor - Cotizacion para pedidos de libre opcion
- **blocks:** [[SNB-554]] monto diferente de LO en NB

## Descripcion

En los casos donde el cliente paga y retira en el momento, no se necesita nada especial al momento del cobro. Por esto podemos generar toda la informacion de liquidación de manera automatica para poder realizar la operación sin mas intervención del vendedor.



Criterios de aceptacion en desarrollo
