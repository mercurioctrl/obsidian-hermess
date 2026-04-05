---
jira_key: "EXP-138"
aliases: ["EXP-138"]
summary: "API - Feat - Generar objetos para volanta operativa"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-01-18 07:55"
updated: "2023-01-18 10:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-138"
---

# EXP-138: API - Feat - Generar objetos para volanta operativa

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-18 07:55 |
| Actualizado | 2023-01-18 10:02 |
| Etiquetas | ninguna |
| Jira | [EXP-138](https://bluinc.atlassian.net/browse/EXP-138) |

## Relaciones

- **Padre:** [[EXP-137 - Feat - Volanta operativa|EXP-137]] Feat - Volanta operativa

## Descripcion

Crearemos un recurso llamado

```
GET {API_URL}/v1/operationalOrder/{id_noremcli_enc}
```

Devuelve un objeto similar a:

```
[
  {
    "date": "2021-12-23 17:36:21",
    "invoiceId": "X000200521520",
    "clientName": "TOBARES LEANDRO AGUSTIN",
    "sellerSurname": "Albarracin",
    "sellerName": "Julian",
    "total": 1303360000.0,
    "perception": 0.0,
    "TOTALREMITO": 1577065600.0,
    "cotizacion": 107.25,
    "dailyQuote": 190.25,
    "paymentMethodDescription": "Efectivo Camioneta",
    "remitoStatusDescription": "Finalizado",
    "dispatch": "Envio Camioneta               ",
    "remitoStatusId": 4,
    "orderNumber": "10249231",
    "branch": "0002",
    "clientId": 27333,
    "invoice": "A000400100823",
    "remitoNumber": "00521520",
    "invoiceId": 464816,
    "perceptionsIIBB": 39.5631,
    "itemCref": "104965",
    "phoneA": "1553299083",
    "phoneB": null,
    "clientId": "027333",
    "sku": "GP-P750GM",
    "itemId": 104965,
    "description": "FUENTE GAMER GIGABYTE 750W MODULAR 80 PLUS GOLD",
    "quantity": 10000.0,
    "comment": "envio facturado en cuenta ADJUNTAR RMA 30895 fuente giga\nAv Dr Ricardo Balbin 3319 celu watsapp 11 5329-9083\nson dos reservas 200521520 1000019684 salen juntas"
  },
  {
    "date": "2021-12-23 17:36:21",
    "invoiceId": "X000200521520",
    "clientName": "TOBARES LEANDRO AGUSTIN",
    "sellerSurname": "Albarracin",
    "sellerName": "Julian",
    "total": 15410000.0,
    "perception": 0.0,
    "TOTALREMITO": 18646100.0,
    "cotizacion": 107.25,
    "dailyQuote": 190.25,
    "paymentMethodDescription": "Efectivo Camioneta",
    "remitoStatusDescription": "Finalizado",
    "dispatch": "Envio Camioneta               ",
    "remitoStatusId": 4,
    "orderNumber": "10249231",
    "branch": "0002",
    "clientId": 27333,
    "invoice": "A000400100823",
    "remitoNumber": "00521520",
    "invoiceId": 464816,
    "perceptionsIIBB": 39.5631,
    "itemCref": "FLETE",
    "phoneA": "1553299083",
    "phoneB": null,
    "clientId": "027333",
    "sku": null,
    "itemId": 172,
    "description": "FLETE CAMIONETA",
    "quantity": 1000.0,
    "comment": "envio facturado en cuenta ADJUNTAR RMA 30895 fuente giga\nAv Dr Ricardo Balbin 3319 celu watsapp 11 5329-9083\nson dos reservas 200521520 1000019684 salen juntas"
  }
]
```

Que se obtiene con una query similar a 

```
SELECT TOP(120)
CONVERT(VARCHAR,
dfecalb,
20)AS date, albclit.ID_NROREMCLI_ENC as invoiceId, cnomcli as clientName, capeage as sellerSurname, cnbrage as sellerName, 
SUM(ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)AS total, CASE WHEN albclit.cnumsuc='0010'OR clientes.excluirPercepcion=1 THEN 0 ELSE(SUM((ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)*clientes.percepcion)/100)END AS perception, CASE WHEN albclit.cnumsuc='0010'OR clientes.excluirPercepcion=1 THEN(SUM((ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)+(ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)*albclil.niva/100))ELSE(SUM((ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)+(ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)*albclil.niva/100)+ISNULL((SUM((ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)*clientes.percepcion)/100),
0))END AS TOTALREMITO, MS_REMITO_CABECERA.COTIZACION as cotizacion,
MS_COTIZACIONES
.COTIZACION as dailyQuote,
MS_FORMASPAGO_REMITOS_VENDEDORES.DESCRIPCION as paymentMethodDescription,
MS_STATUS_REMITO.DESCRIPCION as remitoStatusDescription,
transpor.DESCRIPCION as dispatch,
MS_VENTAS_REMITOS.ID_STATUS as remitoStatusId,
pedclit.cnumped as orderNumber,
albclit.cnumsuc as branch,
clientes.ID_CLIENTE as clientId,
FP_FactWebCliEncabezado.cfactura as invoice,
albclit.cnumalb as remitoNumber,
FP_FactWebCliEncabezado.ID_NROFACCLI_ENC as invoiceId,
MS_REMITO_CABECERA. IMPPERCEP as perceptionsIIBB,
albclil.cref as itemCref,
clientes.ctfo1cli as phoneA,
clientes.ctfo2cli as phoneB,
clientes.ccodcli as clientId,
articulo.id_producto as sku,
articulo.id_articulo as itemId,
articulo.cdetalle as description,
albclil.ncanent  as quantity,
OBSERVACIONES_FP as comment
FROM NewBytes_DBF.dbo.albclit
LEFT JOIN NewBytes_DBF.dbo.clientes on clientes.ID_CLIENTE=albclit.ID_CLIENTE
LEFT JOIN NewBytes_DBF.dbo.agentes on agentes.ID_VENDEDOR=albclit.ID_VENDEDOR
LEFT JOIN NewBytes_DBF.dbo.albclil ON albclil.ID_NROREMCLI_ENC=albclit.ID_NROREMCLI_ENC
LEFT JOIN NewBytes_DBF.dbo.pedclit ON albclit.cnumped=pedclit.cnumped
LEFT JOIN NEW_BYTES.dbo.MS_REMITO_CABECERA ON MS_REMITO_CABECERA.REMITO_FP=albclit.cnumalb and MS_REMITO_CABECERA.SUCURSAL_REMITO=albclit.cnumsuc LEFT JOIN NEW_BYTES.dbo.MS_COTIZACIONES ON MS_COTIZACIONES.NOMBRE='PESOS'
LEFT JOIN NB_WEB.dbo.liquidacion_guardada ON liquidacion_guardada.ID_NROREMCLI_ENC=albclit.ID_NROREMCLI_ENC
LEFT JOIN NEW_BYTES.dbo.MS_VENTAS_REMITOS ON MS_REMITO_CABECERA.REMITO_FP=MS_VENTAS_REMITOS.REMITO_FP AND MS_REMITO_CABECERA.SUCURSAL_REMITO=MS_VENTAS_REMITOS.SUCURSAL_REMITO
LEFT JOIN NEW_BYTES.dbo.MS_FORMASPAGO_REMITOS_VENDEDORES ON MS_FORMASPAGO_REMITOS_VENDEDORES.ID_FORMA=MS_VENTAS_REMITOS.ID_FORMA OR MS_FORMASPAGO_REMITOS_VENDEDORES.ID_FORMA=liquidacion_guardada.formaDePago LEFT JOIN NEW_BYTES.dbo.MS_STATUS_REMITO ON MS_STATUS_REMITO.ID_STATUS=MS_VENTAS_REMITOS.ID_STATUS LEFT JOIN NewBytes_DBF.dbo.transpor ON transpor.ID_TRANSPORTISTA=MS_VENTAS_REMITOS.TRANSPORTE_FP OR transpor.ID_TRANSPORTISTA=liquidacion_guardada.envioRetiro LEFT JOIN NewBytes_DBF.dbo.articulo ON articulo.cRef=albclil.cref
LEFT JOIN NewBytes_DBF.dbo.FP_FactWebCliEncabezado ON FP_FactWebCliEncabezado.ID_NROREMCLI_ENC=albclit.ID_NROREMCLI_ENC
WHERE ALBCLIT.ID_NROREMCLI_ENC ='X000200521520'
GROUP BY dfecalb,
albclit.ID_NROREMCLI_ENC,
cnomcli,
capeage,
cnbrage,
MS_REMITO_CABECERA.COTIZACION,MS_COTIZACIONES.COTIZACION,
albclit.ntipoalb,
albclit.cnumalb,
MS_FORMASPAGO_REMITOS_VENDEDORES.DESCRIPCION,
MS_STATUS_REMITO.DESCRIPCION,
transpor.DESCRIPCION,
MS_VENTAS_REMITOS.ID_STATUS,
pedclit.cnumped,
albclit.cnumsuc,
clientes.ID_CLIENTE,
FP_FactWebCliEncabezado.cfactura,
FP_FactWebCliEncabezado.ID_NROFACCLI_ENC,
MS_REMITO_CABECERA.IMPPERCEP,
clientes.percepcion,
excluirPercepcion,
albclil.cref,
clientes.ctfo1cli,
clientes.ctfo2cli,
articulo.id_producto,
articulo.id_articulo,
articulo.cdetalle,
albclil.ncanent,
clientes.ccodcli,
OBSERVACIONES_FP,
albclil.npreunit,
albclil.ndto,
albclil.niva
ORDER BY albclit.dfecalb DESC
```
