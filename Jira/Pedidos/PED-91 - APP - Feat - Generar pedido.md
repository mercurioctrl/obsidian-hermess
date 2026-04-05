---
jira_key: "PED-91"
aliases: ["PED-91"]
summary: "APP - Feat - Generar pedido"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-09-26 17:24"
updated: "2025-09-19 11:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-91"
---

# PED-91: APP - Feat - Generar pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-26 17:24 |
| Actualizado | 2025-09-19 11:09 |
| Etiquetas | ninguna |
| Jira | [PED-91](https://bluinc.atlassian.net/browse/PED-91) |

## Relaciones

- **Padre:** [[PED-4]] Pedidos
- **Subtarea:** [[PED-128]] API - Refactor - Agregar un item a un pedido de POSTVENTA
- **Subtarea:** [[PED-211]] API - Review - Generar pedido de una orden de libre opcion
- **Subtarea:** [[PED-269]] API - Review - Detalles del log al ELIMINAR PEDIDO
- **Subtarea:** [[PED-501]] APP - Review - Al generar un pedido, el mismo se agrega en el registro de stock como si fuera al vendedor, en lugar de la persona que realmente hizo el movimiento
- **Subtarea:** [[PED-824]] API - Refactor - Generar orden de POSTVENTA
- **Subtarea:** [[PED-922]] API - Refactor - Agregar en el caso que corresponda el costForSale al generar un pedido
- **Subtarea:** [[PED-1109]] API - Refactor - Al generar remito ajustar id de pago de ser necesario en los casos LO
- **is blocked by:** [[PED-90]] API - Feat- Generar pedido (albclit) desde una orden de compra (pedclit)
- **relates to:** [[PED-1105]] API - Review - Generar pedido -> Ordenes de NBE parecieran duplicarse

## Descripcion

Crearemos un accionable en el menu “boton derecho” con la leyenda “Generar Remito” que ejecute el siguiente recurso [link](https://lioteam.atlassian.net/browse/PED-90) 

Una vez que se obtiene el numero de pedido y branch (`cnumsuc` - `cnumalb`) entonces lo cargamos en la columna PEDIDO
