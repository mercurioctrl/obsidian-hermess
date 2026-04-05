---
jira_key: "SNB-3570"
aliases: ["SNB-3570"]
summary: "error no se puede facturar"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Pedidos Jira"
created: "2025-12-19 16:08"
updated: "2025-12-22 14:22"
labels: ["Facturación"]
jira_url: "https://bluinc.atlassian.net/browse/SNB-3570"
---

# SNB-3570: error no se puede facturar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Pedidos Jira |
| Creado | 2025-12-19 16:08 |
| Actualizado | 2025-12-22 14:22 |
| Etiquetas | Facturación |
| Jira | [SNB-3570](https://bluinc.atlassian.net/browse/SNB-3570) |

## Relaciones

*Sin relaciones*

## Descripcion

este pedido esta reclamando la factura el cliente, veo que de deposito cuando lo sacaron no lo facturaron y cuando intentamos tira el siguiente error

Server error: `POST http://ms-comprobantes.lio.red/v2/CreateVoucher` resulted in a `500 Internal Server Error` response: "(10020) El campo BaseImp en AlicIVA es obligatorio y debe ser mayor a 0 cero."

Información del pedido: 0002 - 10441726
Cliente: 20967 - RETEC CONSORCIO DE COOPERACION EMPRESARIA
Vendedor: Contardi Patricio
Cotización: $ 1.475,00

Detalle del pedido:

Cant. - Descripción | IVA | I. Int | Precio | Total sin impuestos

1 - SERVICIO DE TRANSPORTE | 21% | 0% | $ 0,00 | 0,00 
3 - PROCESADOR AMD (AM4) RYZEN 7 5700G | 10.5% | 0% | $ 156,46 | 469,37 
5 - PROCESADOR AMD (AM4) RYZEN 7 5700 | 10.5% | 0% | $ 136,22 | 681,12 

Medio de envío: Entregar
Dirección envío: LA PLATA - BUENOS AIRES ( BS. AS ) - CALLE 12 N 1392 (ENTRE 60 Y 61) - CP:1900

Total sin impuestos: u$s 1.150,49 | $ 1.696.966,58
Total Final:      u$s 1.271,29 | $ 1.875.148,64
Usuario: pat
