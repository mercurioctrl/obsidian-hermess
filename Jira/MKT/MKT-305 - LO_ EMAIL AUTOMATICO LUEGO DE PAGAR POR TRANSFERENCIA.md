---
jira_key: "MKT-305"
aliases: ["MKT-305"]
summary: "LO_ EMAIL AUTOMATICO LUEGO DE PAGAR POR TRANSFERENCIA"
status: "Tareas por hacer"
type: "Tarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Eloy Passarella"
created: "2026-03-30 17:07"
updated: "2026-03-30 17:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/MKT-305"
---

# MKT-305: LO_ EMAIL AUTOMATICO LUEGO DE PAGAR POR TRANSFERENCIA

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Eloy Passarella |
| Creado | 2026-03-30 17:07 |
| Actualizado | 2026-03-30 17:39 |
| Etiquetas | ninguna |
| Jira | [MKT-305](https://bluinc.atlassian.net/browse/MKT-305) |

## Relaciones

*Sin relaciones*

## Descripcion

Según varios informes veo que tenemos muchas operaciones canceladas y me gustaria empezar a reducir esto. 

por ejemplo en la última semana tuvimos 


[adjunto]
## Operaciones que eligen pagar con TRANSFERENCIA:

Estrategia general

La automatización tiene 3 partes:

- **Detectar** cuándo una orden queda en estado "Esperando Pago" con transferencia


- **Esperar 24hs** sin que cambie el estado


- **Enviar un email** recordando al comprador
-Hola {$order['name']}, 
Tu compra #{$order['id']} por $ {$order['total']} todavía está esperando tu pago. Para completarla, podés: - Realizar la transferencia bancaria (datos bancarios) - Subir el comprobante de pago en: [https://libreopcion.com.ar/compra/mis-compras/{$order['id']}/comprobantes](https://libreopcion.com.ar/compra/mis-compras/{$order['id']}/comprobantes) Si ya realizaste el pago, recordá subir el comprobante para que podamos confirmarlo. 
¡Gracias! 
El equipo de Libre Opción ";





## Operaciones que eligen pagar con TARJETA DE CRÉDITO y RECHAZAN el pago:


He notado que varias operaciones que se pagan con tarjeta de crédito y se rechaza el pago, la plataforma no permite retomar el pago, directamente se cancela la operación. 
Los causantes de un rechazo de pago pueden ser varios (un mal digito a la hora de cargar la tarjeta, no tener saldo en una tarjeta pero si en otra, colocar mal la fecha o el codigo de seguridad). Lo que propongo, no se si es posible, que no pase de pantalla cuando se rechaza un pago, sino que quede en la misma pantalla para volver a intentar otro pago con otra tarjeta. 

Si es posible poner porque se rechaza el pago (error en los datos de la tarjeta, saldo insuficiente, el banco rechazó el pago).
