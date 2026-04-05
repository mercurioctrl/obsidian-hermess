---
jira_key: "PED-1038"
aliases: ["PED-1038"]
summary: "APP - Feat- Crear un comprobante manual para un cliente determinado"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-07-03 17:29"
updated: "2025-07-11 02:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1038"
---

# PED-1038: APP - Feat- Crear un comprobante manual para un cliente determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-03 17:29 |
| Actualizado | 2025-07-11 02:44 |
| Etiquetas | ninguna |
| Jira | [PED-1038](https://bluinc.atlassian.net/browse/PED-1038) |

## Relaciones

- **Padre:** [[PED-1036 - Generar comprobantes manuales|PED-1036]] Generar comprobantes manuales
- **is blocked by:** [[PED-1037 - API - Feat- Crear un comprobante manual para un cliente determinado|PED-1037]] API - Feat- Crear un comprobante manual para un cliente determinado

## Descripcion

Haciendo uso de el recurso [link](https://bluinc.atlassian.net/browse/PED-1037)  crearemos un modal con un formulario para crear facturas o comprobantes de manera manual similar al siguiente

[adjunto]
Se deben incluir los parametros

- Tipo (`voucherTypeId`) para determinar si es nota de credito/ debito o factura (Aca eze comento que puede deducir esto con la palabra credito/debito/factura)


- Cliente (`clientId`)


- Cotización (`currencyQuote)` 


- Impactar en cuenta corriente `impactCurrentAccount`


- El body se forma con el item, donde se ingresa la cantidad una leyenda, un precio y el iva, para generar cada linea de `trade`



**¿Como se arma el body?**



- **Cantidad**: Es la cantidad numerica de ese item


- **Precio**, se pone el precio sin iva con hasta 2 decimales


- **Precio Final**, este dato se calcula agregandole el IVA a precio segun el campo IVA


- **Subtotal**: Es el calculo de **Precio Final** por la **cantidad**


- **IVA**: Agregaremos un selector de IVA con los valores 21,10.5 y 0 en ese orden, eso nos dará la pauta de que itemId enviar según el siguiente cuadro. Los mismos pueden repetirse a medida que agregamos lineas nuevas.



[adjunto]
Para los ID_ARTICULO crearemos las variables de entorno en el .env para cada caso de iva de item manual
