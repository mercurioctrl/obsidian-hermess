---
jira_key: "COB-222"
aliases: ["COB-222"]
summary: "Refactor - Redondeo al cobrar"
status: "Gamma"
type: "Historia"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2022-11-02 17:01"
updated: "2022-11-29 11:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-222"
---

# COB-222: Refactor - Redondeo al cobrar

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-02 17:01 |
| Actualizado | 2022-11-29 11:33 |
| Etiquetas | ninguna |
| Jira | [COB-222](https://bluinc.atlassian.net/browse/COB-222) |

## Relaciones

- **Padre:** [[COB-33]] Cobrar
- **Subtarea:** [[COB-223]] APP - Refactor - Redondeo al cobrar
- **Subtarea:** [[COB-224]] API - Refactor - Redondeo al cobrar
- **Subtarea:** [[COB-225]] API - Refactor - Agregar toleranca a los medios de pago

## Descripcion

Introduciremos el concepto “tolerancia” para designar aquella diferencia en favor del cliente, que puede faltarle a un total abonando para el pago de un pedido.

En este caso, solo podremos cobrar un pedido cuya tolerancia sea menor o igual al parámetro `paymentTolerance`

El parámetro tiene dos decimales y esta en dolares.
