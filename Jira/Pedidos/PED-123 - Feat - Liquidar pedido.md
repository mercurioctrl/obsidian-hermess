---
jira_key: "PED-123"
aliases: ["PED-123"]
summary: "Feat - Liquidar pedido"
status: "Tareas por hacer"
type: "Historia"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2023-10-06 08:10"
updated: "2023-10-06 08:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-123"
---

# PED-123: Feat - Liquidar pedido

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-06 08:10 |
| Actualizado | 2023-10-06 08:10 |
| Etiquetas | ninguna |
| Jira | [PED-123](https://bluinc.atlassian.net/browse/PED-123) |

## Relaciones

- **Padre:** [[PED-4]] Pedidos
- **Subtarea:** [[PED-124]] API - Feat - Liquidar pedido
- **Subtarea:** [[PED-125]] APP - Feat - Modal de liquidacion
- **Subtarea:** [[PED-126]] API - Feat - Liquidar pedido 2 parte -> Autorizacion
- **Subtarea:** [[PED-138]] API - Feat - Implementar y agregar middleware para todas las rutas
- **Subtarea:** [[PED-145]] APP - Review - Al liquidar pedido se envian mal los nombres de los parametros
- **Subtarea:** [[PED-152]] API - Feat - Desliquidar pedido
- **Subtarea:** [[PED-156]] APP - Feat - Desliquidar pedido
- **Subtarea:** [[PED-247]] API - Refactor - Al liquidar un pedido, marcar [ULTIMA_COMPRA]
- **Subtarea:** [[PED-332]] API - Review - Cuando se hace una liquidacion exitosa, siempre se debe marcar albclit.ntipoalb = 2
- **Subtarea:** [[PED-336]] API - Review - En la liquidacion se itera la insercion de ganancias, que deberia ser una sola en esta tabla
- **Subtarea:** [[PED-360]] API - Review - Error al realizar una liquidacion en produccion
- **Subtarea:** [[PED-371]] API - Feat - Guardar condiciones de liquidación (Sin liquidar)
- **Subtarea:** [[PED-372]] APP - Feat - Guardar condiciones de liquidación (Sin liquidar)
- **Subtarea:** [[PED-374]] API - Feat - Leer condiciones de liquidación 
- **Subtarea:** [[PED-398]] APP - Refactor - En el cuadro de comentarios del modal de liquidacion, se debe sostener los comentarios del pedido
- **Subtarea:** [[PED-439]] API - Refactor -  Al Desliquidar se debe ajustar ultima fecha de compra en clientes
- **Subtarea:** [[PED-444]] API - Feat - Unir pedido a otro envio 
- **Subtarea:** [[PED-447]] APP - Feat - Unir pedido a otro envío (pedido)
- **Subtarea:** [[PED-448]] APP - Feat - DESunir pedido a otro envio (pedido)
- **Subtarea:** [[PED-454]] API - Refactor - Agregar el pedido al cual esta vinculado un pedido, en caso de que exista a las condiciones
- **Subtarea:** [[PED-455]] APP - Feat - Desunir pedido de otro envio ()
- **Subtarea:** [[PED-456]] API - Refactor - Al desliquidar un pedido que tiene otro pedidos vnculados, se deben soltar, tanto siendo host, como guest.
- **Subtarea:** [[PED-467]] APP - Feat - En el modal de "liquidar pedido" si el pedido esta unido, restringir el medio de envio segun "Unido a otro pedido"
- **Subtarea:** [[PED-468]] API - Feat - Al liquidar, validar que si es "Unido a otro pedido" debe estar efectivamente vinculado a un host. Sino, no liquidar.
- **Subtarea:** [[PED-507]] API - Refactor - Al liquidar, guardaremos la cotizacion blue, ademas de la oficial (como ya venimos haciendo)
- **Subtarea:** [[PED-539]] APP - Refactor - Al liquidar con cheque, debo enviar la cotizacion del calculo de cheque como si lo hubiera cambiado a mano. A menos que la vuelva a cambiar a mano.
- **Subtarea:** [[PED-540]] API - Review - Luego de intentar liquidar, sin saldo de cheque, no puedo volver a liquidar
- **Subtarea:** [[PED-565]] APP - Refactor - Liquidacion -> Carga de cheques, facilitar calculadora eliminando campos necesarios
- **Subtarea:** [[PED-590]] API - Refactor - se agrega validacion de credito para casos de pago diferidos al Liquidar
- **Subtarea:** [[PED-617]] API - Refactor - Control de "pedidos pendientes" al liquidar
- **Subtarea:** [[PED-634]] API - Refactor - Ajuste en query ordenes pendiente con limite de dias
- **Subtarea:** [[PED-643]] APP - Refactor - Si esta combinado con un host, no mostrar selector de envio
- **Subtarea:** [[PED-673]] API - Feat - Agregar correo electronico del cliente a los detalles del pedido
- **Subtarea:** [[PED-674]] APP - Feat - Agregar correo electronico del cliente a los detalles de la liquidacion
- **Subtarea:** [[PED-675]] APP - Refactor - Un pedido "dropshipping" solo puede liquidarse si es un currier de envio (oca,andreani,entregar)
- **Subtarea:** [[PED-676]] API - Refactor - Un pedido "dropshipping" solo puede liquidarse si es un currier de envio (oca,andreani,entregar)
- **Subtarea:** [[PED-685]] API - Refactor - Marcar en la tabla pedclit el id heredado al asociar un pedido
- **Subtarea:** [[PED-798]] API - Refactor - En la liquiadacion, solo cuando el pedido queda autorizaco (ID_sTATUS > 1), marcaremos la fecha de aturizacion
- **Subtarea:** [[PED-923]] API - MVP - Refactor - Calcular ganancias con el costForSale solo cuando corresponda
- **Subtarea:** [[PED-951]] API - Refactor - Validaciones necesarias para desliquidar
- **Subtarea:** [[PED-954]] API - Refactor - Validacion de permisos para desliquidar pedido
- **Subtarea:** [[PED-968]] API - Refactor - Validacion de estados posible para poder desliquidar una orden en variables de entorno
- **Subtarea:** [[PED-978]] API - Refactor - Al liquidar un pedido de libreOpcion, marcaremos el debito/credito como un movimiento de billetera
- **Subtarea:** [[PED-979]] API - Refactor - Al autorizar un pedido de banco (casos especificos de LO) marcaremos el movimiento de billetera
- **Subtarea:** [[PED-996]] API - Refactor - Agregar percepción ARBA en la liquidación 
- **Subtarea:** [[PED-1025]] API - Refactor - Al liquidar un pedido de para un cliente "liberado" se debe asignar al vendedor que lo esta liquidando
- **Subtarea:** [[PED-1051]] API - Agregar "Envio a cargo de NBE" como medio de envio y que al liquidar se pueda combinar con "Efectivo Moto"
- **Subtarea:** [[PED-1066]] API - Refactor - Nuevo medio de pago "Pago diferido NBE" 
- **Subtarea:** [[PED-1096]] API - Refactor - Autorizacion  para los pedidos NBE pagos en mercadopago
- **Subtarea:** [[PED-1100]] APP - Refactor - Autorizacion  para los pedidos NBE pagos en mercadopago
- **Subtarea:** [[PED-1327]] APP - Feat - Cambio como se muestran los datos de cuenta del cliente, en el modal liquidacion
- **Subtarea:** [[PED-1341]] API - Refactor - Validación de unicidad de pago para evitar autorización de pedidos duplicados

## Descripcion

*Sin descripcion*
