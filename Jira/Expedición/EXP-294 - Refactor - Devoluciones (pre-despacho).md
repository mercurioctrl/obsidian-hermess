---
jira_key: "EXP-294"
aliases: ["EXP-294"]
summary: "Refactor - Devoluciones (pre-despacho)"
status: "Tareas por hacer"
type: "Historia"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2023-05-28 19:58"
updated: "2023-05-28 20:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-294"
---

# EXP-294: Refactor - Devoluciones (pre-despacho)

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-28 19:58 |
| Actualizado | 2023-05-28 20:06 |
| Etiquetas | ninguna |
| Jira | [EXP-294](https://bluinc.atlassian.net/browse/EXP-294) |

## Relaciones

- **Padre:** [[EXP-116 - Devoluciones|EXP-116]] Devoluciones
- **Subtarea:** [[EXP-295 - API - Refactor - ordersRefund debe admitir pedidos que aun no fueron despachados|EXP-295]] API - Refactor - ordersRefund debe admitir pedidos que aun no fueron despachados
- **Subtarea:** [[EXP-296 - APP - Refactor - Agregar feature para hacer devoluciones en el despacho|EXP-296]] APP - Refactor - Agregar feature para hacer devoluciones en el despacho
- **Subtarea:** [[EXP-306 - API - Oportunidad de mejora - En el registro de stock se debe agregar|EXP-306]] API - Oportunidad de mejora - En el registro de stock se debe agregar ID_VENDEDOR y Remito sobre el que se esta operando (si esta disponible)
- **Subtarea:** [[EXP-322 - API - Refactor - Devolución, excepciones de cambio de estado|EXP-322]] API - Refactor - Devolución, excepciones de cambio de estado
- **Subtarea:** [[EXP-338 - APP - Refactor - Cuando un pedido esta armado finalizado, pero no entregado|EXP-338]] APP - Refactor - Cuando un pedido esta "armado finalizado", pero no "entregado: verificar validación que aparezca el tachito para eliminar un serial
- **Subtarea:** [[EXP-368 - API - Review - Cuando se realiza una devolucion, y posterior refacturacion, no|EXP-368]] API - Review - Cuando se realiza una devolucion, y posterior refacturacion, no se tiene en cuenta los items devueltos para descontarlos en la factura

## Descripcion

Modificaremos algunos recursos existentes para permitir que se puedan hacer devoluciones de pedidos que aun no fueron despachados.

¿Para que sirve esto? Sirve para cuando están preparando un pedido y se dan cuenta que uno de los items que el pedido contiene no esta disponible en el deposito. O no se alcanza la cantidad pedida por este mismo motivo. O bien el cliente se arrepiente de comprarlo.

Para permitir que el pedido continúe y se pueda despachar, pero sin la mercadería devuelta.
