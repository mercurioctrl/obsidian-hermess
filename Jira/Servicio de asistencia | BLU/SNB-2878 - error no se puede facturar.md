---
jira_key: "SNB-2878"
aliases: ["SNB-2878"]
summary: "error no se puede facturar"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Pedidos Jira"
created: "2025-03-17 09:42"
updated: "2025-03-29 16:18"
labels: ["Facturación"]
jira_url: "https://bluinc.atlassian.net/browse/SNB-2878"
---

# SNB-2878: error no se puede facturar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Pedidos Jira |
| Creado | 2025-03-17 09:42 |
| Actualizado | 2025-03-29 16:18 |
| Etiquetas | Facturación |
| Jira | [SNB-2878](https://bluinc.atlassian.net/browse/SNB-2878) |

## Relaciones

*Sin relaciones*

## Descripcion

Nos reclaman una factura pero el sistema tira error al tratar de facturar. Les paso error y pedido:

Server error: `POST http://ms-comprobantes.lio.red/v2/CreateVoucher` resulted in a `500 Internal Server Error` response: "Campo Cmp.Items.Pro_total_item invalido. El valor debe tener 13 enteros y 2 decimales como m\u00e1ximo."

Información del pedido: 0002 - 10396016
Cliente: 18823 - IT INSIDE S.R.L
Vendedor: Contardi Patricio
Cotización: $ 1.086,50

Detalle del pedido:

Cant. - Descripción | IVA | I. Int | Precio | Total sin impuestos

1 - SERVICIO DE TRANSPORTE | 0% | 0% | $ 0,00 | 0,00 
1 - MOUSE PAD TRUST XXL | 0% | 0% | $ 14,27 | 14,27 
3 - D-LINK [[DWA-582]] PCI-E WIFI 5 AC1200 DUAL BAND CON 2 ANTENAS | 0% | 0% | $ 19,53 | 58,59 
3 - MOTHER ASUS (AM4) PRIME A520M-K/CSM | 0% | 0% | $ 54,53 | 163,58 
3 - MONITOR NOBLEX 25 FHD VA ADAPTIVE SYNC SM2500 | 0% | 0% | $ 111,67 | 335,00 
4 - MOTHER GIGABYTE (AM5) A620M H 1.2 | 0% | 0% | $ 79,34 | 317,37 
5 - MONITOR NOBLEX 22 FHD VA ANTIRREFLEJO ADAPTATIVE SM2200 | 0% | 0% | $ 96,62 | 483,12 
10 - D-LINK [[DWA-185]] USB WIFI 5 AC1200 DUAL BAND CON ANTENA | 0% | 0% | $ 17,41 | 174,15 
10 - GRASA SILICONADA PASTERMAX PARA CPU A90 (GRIS) PASTA TERMICA | 0% | 0% | $ 3,75 | 37,49 
10 - D-LINK DWA-X1850 USB 3.2 WIFI 6 AX1800 DUAL BAND | 0% | 0% | $ 17,41 | 174,13 

Medio de envío: OCA
Dirección envío: RIO GRANDE - TIERRA DEL FUEGO - PERITO MORENO  1032 - CP:9420

Total sin impuestos.: u$s 1.757,70 | $ 1.909.739,62
Total Final:      u$s 1.757,70 | $ 1.909.739,62
Usuario: pat
