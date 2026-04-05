---
jira_key: "COB-374"
aliases: ["COB-374"]
summary: "Feat - Editar estado crediticio de la cuenta del cliente"
status: "Tareas por hacer"
type: "Historia"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2023-03-22 09:33"
updated: "2023-03-22 09:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-374"
---

# COB-374: Feat - Editar estado crediticio de la cuenta del cliente

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-22 09:33 |
| Actualizado | 2023-03-22 09:36 |
| Etiquetas | ninguna |
| Jira | [COB-374](https://bluinc.atlassian.net/browse/COB-374) |

## Relaciones

- **Padre:** [[COB-20 - Cuentas Corrientes|COB-20]] Cuentas Corrientes
- **Subtarea:** [[COB-375 - API - Feat - Listar saldos de credito por cliente|COB-375]] API - Feat - Listar saldos de credito por cliente
- **Subtarea:** [[COB-376 - API - Feat - Editar saldo de credito por cliente|COB-376]] API - Feat - Editar saldo de credito por cliente
- **Subtarea:** [[COB-377 - APP - Editar saldo de credito por cliente|COB-377]] APP - Editar saldo de credito por cliente
- **Subtarea:** [[COB-388 - API - Refactor - Al editar un cliente que no tiene saldo, no hace la inserción|COB-388]] API - Refactor - Al editar un cliente que no tiene saldo, no hace la inserción de manera correcta
- **Subtarea:** [[COB-430 - API - Feat - Fecha de vencimiento de la linea de credito|COB-430]] API - Feat - Fecha de vencimiento de la linea de credito
- **Subtarea:** [[COB-431 - APP - Feat - Fecha de vencimiento de la linea de credito|COB-431]] APP - Feat - Fecha de vencimiento de la linea de credito
- **Subtarea:** [[COB-432 - API - Feat - Días máximos de cheques aceptada para un cliente determinado|COB-432]] API - Feat - Días máximos de cheques aceptada para un cliente determinado
- **Subtarea:** [[COB-459 - API - Refactor - Agregar comentario al correo de edición de crédito|COB-459]] API - Refactor - Agregar comentario al correo de edición de crédito
- **Subtarea:** [[COB-461 - API - Feat - Incluir linea neutra en la CC del cliente, cada vez que este|COB-461]] API - Feat - Incluir linea "neutra" en la CC del cliente, cada vez que este reciba una edición en su linea de crédito
- **Subtarea:** [[COB-485 - APP - Refactor - No coincide el limite real de la observacion con el limite|COB-485]] APP - Refactor - No coincide el limite real de la observacion con el limite permitido
- **Subtarea:** [[COB-556 - API - Feat - Comentarios para las asignaciones de saldo en la linea de credito|COB-556]] API - Feat - Comentarios para las asignaciones de saldo en la linea de credito
- **Subtarea:** [[COB-557 - APP - Feat - Comentarios para las asignaciones de saldo en la linea de credito|COB-557]] APP - Feat - Comentarios para las asignaciones de saldo en la linea de credito
- **Subtarea:** [[COB-572 - APP - Refactor - Agregar accionable para acceder al historial crediticio de CC|COB-572]] APP - Refactor - Agregar accionable para acceder al historial crediticio de CC

## Descripcion

Utilizaremos esta feature para variar los saldos crediticios de un cliente especifico.

Solo quien tenga el permiso especifico para hacer esto, puede ejecutar un cambio.

Solo puede editarse el Credito en dolares y el Credito en cheques
