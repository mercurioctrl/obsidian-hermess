---
jira_key: "COB-115"
aliases: ["COB-115"]
summary: "Feat - Realizar un cobro"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2022-09-27 09:56"
updated: "2023-03-10 17:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-115"
---

# COB-115: Feat - Realizar un cobro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-27 09:56 |
| Actualizado | 2023-03-10 17:05 |
| Etiquetas | ninguna |
| Jira | [COB-115](https://bluinc.atlassian.net/browse/COB-115) |

## Relaciones

- **Padre:** [[COB-33]] Cobrar
- **Subtarea:** [[COB-125]] APP - Feat - Modal de cobro
- **Subtarea:** [[COB-126]] API - Feat - Realizar cobro
- **Subtarea:** [[COB-127]] API - Feat - Crear recibo
- **Subtarea:** [[COB-128]] API - Feat - Mostrar recibo
- **Subtarea:** [[COB-129]] APP - Feat - Mostrar recibo
- **Subtarea:** [[COB-130]] APP - Feat - Modal cheque
- **Subtarea:** [[COB-131]] API - Refactor - Realizar cobros con tolerancia en la variación de cotizaciones
- **Subtarea:** [[COB-166]] MS - Feat - Ms comprobantes, recurso de recibo de dinero
- **Subtarea:** [[COB-182]] APP - Refactor - Sacar los filtros en busqueda de pedidos en los cobros
- **Subtarea:** [[COB-239]] APP - Refactor - Agregar informacion sobre el banco donde se hace el cobro
- **Subtarea:** [[COB-240]] APP - Refactor - Se debe poder cambiar el banco en el contexto de cobro
- **Subtarea:** [[COB-241]] API - Refactor - Se debe poder cambiar el banco que recibe el pago (leer del payload))
- **Subtarea:** [[COB-245]] API - Oportunidad de mejora - Agregar la leyenda a el movimiento en la CC del banco cuando es un cobro
- **Subtarea:** [[COB-250]] API - Review - Al realizar un cobro, parece no estar afectando los saldos de caja.
- **Subtarea:** [[COB-257]] APP - Refactor - El ABM de cheques debe calcular la linea de cheques automáticamente al cargarse los mismo
- **Subtarea:** [[COB-261]] API - Refactor - Realizar cobro, agregar nuevos parámetros de cotización
- **Subtarea:** [[COB-290]] API - Refactor - Cobrar con retencion
- **Subtarea:** [[COB-291]] API - Feat - Listar provincias (para retención)
- **Subtarea:** [[COB-292]] APP - Refactor - Cobrar Retencion
- **Subtarea:** [[COB-304]] API - Refactor - Agregar el monto del pedido actual al pendiente de la cuenta corriente para poder permitir que en en caso de tener dinero disponible, se lo pueda tomar
- **Subtarea:** [[COB-305]] APP - Refactor - Agregar el monto del pedido actual al pendiente de la cuenta corriente para poder permitir que en en caso de tener dinero disponible, se lo pueda tomar
- **Subtarea:** [[COB-310]] APP - Refactor - Agregar cotización de la operación y la cotización que surge de la operación.
- **Subtarea:** [[COB-311]] APP - Refactor - Agregar abajo del saldo disponible, el crédito asignado
- **Subtarea:** [[COB-313]] APP - Feat - En el modal de cobrables, agregar al nombre del cliente el enlace para que cuando haces clic sobre el, ves la cuenta corriente
- **Subtarea:** [[COB-320]] APP - Feat - Agregar al modal de cobro una confirmacion por excedente cuando se abona un pedido
- **Subtarea:** [[COB-334]] API - Refactor - Si se recibe el parametro de excedente, se debe enviar un correo a los administradores
- **Subtarea:** [[COB-387]] API - Refactor - Integrar nuevos estados "finalizados" al realizar un cobro pendiente
- **Subtarea:** [[COB-555]] API - Refactor - Al cobrar se debe registrar cotización en operaciones con cuenta corriente (billetera LO)

## Descripcion

- Los cobros realizados deben impactar en la caja, o bien en una cuenta bancaria de la manera correcta y debe poder visualizarse el movimiento, incluyendo en la observación el cliente y pedido vinculantes.


- Los cobros realizados deben impactar EN EL SALDO de caja, o bien en una cuenta bancaria de la manera correcta.


- El cobro realizado debe impactar en la cuenta corriente del cliente, de la forma correcta.


- El cobro debe impactar EN EL SALDO del cliente de manera correcta.


- Una vez cobrado un pedido, no debe poder volverse a cobrar.


- Los pedidos deben visualizarse como cobrados, una vez cobrado, en la lista de cobrables.


- Si al buscar un pedido, no lo encuentro que se vea el mensaje que me indique lo que sucede.


- Si al buscar un cliente, no lo encuentro que se vea el mensaje que me indique lo que sucede.


- Se deben anexar las observaciones (en caso de haber sido cargadas) a la informacion del pedido cuando lo vez en la caja o cuenta bancaria (Información + Observación)


- Verificar saldo del caja según movimientos (Si tenes dudas con esto, lo vemos)


- Verificar saldo del cuenta bancaria según movimientos (Si tenes dudas con esto, lo vemos)


- Verificar saldo del cuenta corriente del cliente según movimientos (Si tenes dudas con esto, lo vemos)


- El importe de cheques, debe ser igual al monto total de cheques que quiero pagar.


- Los cheques deben verse reflejados, con toda la informacion de ingreso correcta en el listado de cheques y debe estar en la caja correcta.


- Se debe poder descargar (y ver) un recibo de la operación, por cada medio de pago.


- Los pagos de autorizan el pedido para su despacho. (Ver estado remito en `[NEW_BYTES].[dbo].[MS_VENTAS_REMITOS].ID_STATUS`). osea, si esta en `1` poner en `2` segun `[NEW_BYTES].[dbo].[MS_STATUS_REMITO]`



---



- 23-01-23 - Cuando cobro por cuenta corriente, se debe sumar el pedido actual que se esta cobrando, de modo tal que si el pedido se quisiera cobrar con plata en cuenta corriente, se pueda hacer (ver: [link](https://lioteam.atlassian.net/browse/COB-304)  y [link](https://lioteam.atlassian.net/browse/COB-305) )
