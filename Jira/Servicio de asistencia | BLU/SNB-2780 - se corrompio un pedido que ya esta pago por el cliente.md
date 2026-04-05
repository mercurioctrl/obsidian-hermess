---
jira_key: "SNB-2780"
aliases: ["SNB-2780"]
summary: "se corrompio un pedido que ya esta pago por el cliente"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Pedidos Jira"
created: "2025-02-13 10:01"
updated: "2025-02-17 15:08"
labels: ["Sistemas"]
jira_url: "https://bluinc.atlassian.net/browse/SNB-2780"
---

# SNB-2780: se corrompio un pedido que ya esta pago por el cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Pedidos Jira |
| Creado | 2025-02-13 10:01 |
| Actualizado | 2025-02-17 15:08 |
| Etiquetas | Sistemas |
| Jira | [SNB-2780](https://bluinc.atlassian.net/browse/SNB-2780) |

## Relaciones

*Sin relaciones*

## Descripcion

El pedido ya esta pago por el cliente. tiene 2 problemas:
1- Cuando voy a liquidarlo veo que veo que tiene nro de remito pero figura pendiente en verde. Si lo paso a remito se duplica, aparecen 2 nros de remito asignados al mismo nro de pedido.
2- si ahora pongo el detalle del pedido, figura el costo de envio pero no figura la informacion de envio (no lo puedo recalcular pq me va a cobrar otro monto y ya esta pago, la idea es q los montos no cambien)

este es el detalle original q el cliente pago (necesitamos que quede asi):
Información del pedido: 0002 - 10390889
Cliente: 20967 - RETEC CONSORCIO DE COOPERACION EMPRESARIA
Vendedor: Contardi Patricio
Cotización: $ 1.076,00

Detalle del pedido:

Cant. - Descripción | IVA | I. Int | Precio | Total sin impuestos

1 - SERVICIO DE TRANSPORTE | 21% | 0% | $ 18,76 | 18,76
2 - PARLANTE GENIUS SP-HF1200B | 21% | 0% | $ 61,30 | 122,60
3 - PROCESADOR AMD (AM4) RYZEN 5 5600GT | 10.5% | 0% | $ 134,39 | 403,18

Medio de envío: Andreani
Dirección envío: ESPERANZA - SANTA FE - Cordoba 2011 - CP:3080

Total sin impuestos.: u$s 544,54 | $ 585.927,62
Total Final:      u$s 616,56 | $ 663.420,76


y este es el detalle que tira el sistema ahora sin la info de envio:
Información del pedido: 0002 - 10390889
Cliente: 20967 - RETEC CONSORCIO DE COOPERACION EMPRESARIA
Vendedor: Contardi Patricio
Cotización: $ 1.076,00

Detalle del pedido:

Cant. - Descripción | IVA | I. Int | Precio | Total sin impuestos

1 - SERVICIO DE TRANSPORTE | 21% | 0% | $ 18,76 | 18,76 
2 - PARLANTE GENIUS SP-HF1200B | 21% | 0% | $ 61,30 | 122,60 
3 - PROCESADOR AMD (AM4) RYZEN 5 5600GT | 10.5% | 0% | $ 134,39 | 403,18 

Total sin impuestos.: u$s 544,54 | $ 585.927,62
Total Final:      u$s 616,56 | $ 663.420,76

Usuario: pat
