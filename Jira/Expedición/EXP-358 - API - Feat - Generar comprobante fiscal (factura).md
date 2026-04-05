---
jira_key: "EXP-358"
aliases: ["EXP-358"]
summary: "API - Feat - Generar comprobante fiscal (factura)"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-07 08:23"
updated: "2024-04-25 15:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-358"
---

# EXP-358: API - Feat - Generar comprobante fiscal (factura)

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-07 08:23 |
| Actualizado | 2024-04-25 15:19 |
| Etiquetas | ninguna |
| Jira | [EXP-358](https://bluinc.atlassian.net/browse/EXP-358) |

## Relaciones

- **Padre:** [[EXP-355]] Emision de facturas
- **blocks:** [[EXP-357]] APP - Feat - Generar factura

## Descripcion

Para poder utilizar el recurso `/v2/CreateVoucher` se debe generar en base al pedido el siguiente objeto

```
POST /v1/makeVoucher
```

Y se debe generar un payload automáticamente del lado del back para poder enviarle al recurso del ms-comprobantes `{{API_URL}}/v2/CreateVoucher`

```
{
  "voucherTypeId": 1, <- o el que corresponda para facturar
  "clientId": 26806,
  "pedido":"X000200543640",
  iibbPerception: 4.4,
  "trade":[
          {
          "units":1,
          "price": 23.55,
          "ivaTax":21,
          "internalId": 1924,
          "description": "Esta es una descripcion opcional con id" 
          },
          {          
          "units":11,
          "price": 223.55,
          "ivaTax":10.5   
          internalId": 7216      
          },
          {
          "units":3,
          "price": 40,
          "ivaTax":21,
          "internalId": 7616
          }
  ]
}
```

El parámetro `iibbPerception` se obtiene de la siguiente columna y debe enviarse en el objeto `TRIBUTOS` al servicio de AFIP.

[adjunto]
[https://servicioscf.afip.gob.ar/facturadecreditoelectronica/documentos/wsfev1-Manual-desarrollador.pdf](https://servicioscf.afip.gob.ar/facturadecreditoelectronica/documentos/wsfev1-Manual-desarrollador.pdf)

Es decir que debemos modificar el servicio de comprobantes para aceptar percepciones enviando el objeto tributos (baseImp, Alic,Importe). [link](https://lioteam.atlassian.net/browse/EXP-356) 

`[NEW_BYTES].[dbo].[MS_REMITO_CABECERA].IMPPERCEP`

Este recurso, no toca stock no seriales, solo genera la factura fiscal

Se deben tener en cuenta la cantidad de unidades restando la columna ACREDITADO de albclit, para no facturar de mas en caso de haberse hecho devoluciones.
