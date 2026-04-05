---
jira_key: "SNB-3082"
aliases: ["SNB-3082"]
summary: "IIBB en la factura figura distinto al detalle que se pago"
status: "Abandonado por usuario"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Pedidos Jira"
created: "2025-05-15 16:22"
updated: "2025-05-16 16:08"
labels: ["Facturación"]
jira_url: "https://bluinc.atlassian.net/browse/SNB-3082"
---

# SNB-3082: IIBB en la factura figura distinto al detalle que se pago

| Campo | Valor |
|-------|-------|
| Estado | Abandonado por usuario (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Pedidos Jira |
| Creado | 2025-05-15 16:22 |
| Actualizado | 2025-05-16 16:08 |
| Etiquetas | Facturación |
| Jira | [SNB-3082](https://bluinc.atlassian.net/browse/SNB-3082) |

## Relaciones

*Sin relaciones*

## Descripcion

Buenas, tenemos un reclamo del cliente porque en este pedido el cliente pago segun el detalle y despues en la factura el impuesto IIBB figura en cero:

Información del pedido: 0002 - 10406461
Cliente: 19665 - ANYX SRL
Vendedor: Contardi Patricio
Cotización: $ 1.150,00

Detalle del pedido:

Cant. - Descripción | IVA | I. Int | Precio | Total sin impuestos

3 - SAMSUNG CELULAR GALAXY S24FE 256GB NEGRO | 21% | 0% | $ 850,26 | 2.550,79 

Total sin impuestos: u$s 2.550,79 | $ 2.933.409,04
Percepción AGIP: 5 (u$s 127.54 | $ 146670.45)
Total Final:      u$s 3.214,00 | $ 3.696.095,39


en la factura:
Importe Neto Gravado: DOL 2550,79
IVA 21%: DOL 535,66
IVA 10.5%: DOL 0,00
IVA 0%: DOL 0,00
Importe Otros Tributos: DOL 0,00 <- figura en cero IIBB
Importe Total: DOL 3086,46

Usuario: pat
