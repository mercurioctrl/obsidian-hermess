---
jira_key: "EXP-49"
aliases: ["EXP-49"]
summary: "API - Feat - Listar pedidos para envío"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-09 09:00"
updated: "2024-03-27 13:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-49"
---

# EXP-49: API - Feat - Listar pedidos para envío

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-09 09:00 |
| Actualizado | 2024-03-27 13:08 |
| Etiquetas | ninguna |
| Jira | [EXP-49](https://bluinc.atlassian.net/browse/EXP-49) |

## Relaciones

- **Padre:** [[EXP-12]] Feat - Listar pedidos para envio
- **blocks:** [[EXP-50]] APP - Feat - Listar pedido para envio
- **relates to:** [[EXP-240]] API - Feat - Obtener comentarios del vendedor para un pedido determinado
- **blocks:** [[EXP-267]] API - Refactor - Listar envios: Las busquedas demoran bastante, se debe intentar bajar a <5 segundos
- **blocks:** [[EXP-405]] API - Feat - Agregar parametro dropShipping al listado de despacho de envios

## Descripcion

Este recurso se encarga de listar aquellos pedidos (compras) que hay que preparar para enviar

Solo deben mostrarse los que están marcados como ENVIOS

```
GET {API_URL}/v1/shipments
```

Retorna


```json
[
  {
    "date": "2022-11-09 08:15:46",
    "pedido": "X000200547628",
    "clientName": "URANO STREAM S.A.",
    "clientId": 75505,
    "sellerName": "Andrea Altamiranda",
    "sellerId": 8,
    "paymentMethod": "Depósito en Banco",
    "statusDescription": "Autorizados. Pendiente a despachar",
    "dispatch": "Retiro de cliente en Local    ",
    "statusId": 2,
    "order": "10297403",
    "branch": "0002",
    "cfactura": null,
    "cnumalb": "00547628",
    "fullSerialized": false,
    "currierName": "Andreani,
    "currierId": 23,
    "placeId": 1,
    "provinceId": 4,
     "placeDescription": "Rosario",
    "provinceDescription": "Santa Fe",
    "zipCode": "5000",
    "shippingLabel": true,
    "shippingStatus": ///este parametro lo veremos en una historai siguiente
  },
  {
    "date": "2022-11-09 08:15:46",
    "pedido": "X000200547628",
    "clientName": "URANO STREAM S.A.",
    "clientId": 75505,
    "sellerName": "Andrea Altamiranda",
    "sellerId": 8,
    "paymentMethod": "Depósito en Banco",
    "statusDescription": "Autorizados. Pendiente a despachar",
    "dispatch": "Retiro de cliente en Local    ",
    "statusId": 2,
    "order": "10297403",
    "branch": "0002",
    "cfactura": null,
    "cnumalb": "00547628",
    "fullSerialized": false,
    "currierName": "Andreani,
    "currierId": 23,
    "placeId": 1,
    "provinceId": 4,
     "placeDescription": "Rosario",
    "provinceDescription": "Santa Fe",
    "zipCode": "5000",
    "shippingLabel": true,
    "shippingStatus": ///este parametro lo veremos en una historai siguiente
  }
  ]
```

Usaremos una query del siguiente tipo

```sql
SELECT
TOP(120)
CONVERT(VARCHAR, dfecalb, 20) AS dfecalb,
albclit.ID_NROREMCLI_ENC,
cnomcli,
agentes.capeage,
agentes.cnbrage,
albclit.ntipoalb,
MS_FORMASPAGO_REMITOS_VENDEDORES.DESCRIPCION as cobro,
MS_STATUS_REMITO.DESCRIPCION as estado,
transpor.DESCRIPCION as despacho,
MS_VENTAS_REMITOS.ID_STATUS,
pedclit.cnumped,
pedclit.cnumsuc,
albclit.cnumsuc,
clientes.ID_CLIENTE,
FP_FactWebCliEncabezado.cfactura,
albclit.cnumalb,
FP_FactWebCliEncabezado.ID_NROFACCLI_ENC,
MS_REMITO_CABECERA.[IMPPERCEP],
AGE_SECRET_KEY.[cnbrage] as agenteSecretKey,
 CONVERT(VARCHAR, pedclit.secret_key_confirm_date, 3) AS secret_key_confirm_date
FROM [NewBytes_DBF].[dbo].[albclit]
LEFT JOIN NewBytes_DBF.dbo.clientes on clientes.ID_CLIENTE = albclit.ID_CLIENTE
LEFT JOIN NewBytes_DBF.dbo.agentes on agentes.ID_VENDEDOR = albclit.ID_VENDEDOR
LEFT JOIN NewBytes_DBF.dbo.albclil ON albclil.ID_NROREMCLI_ENC = albclit.ID_NROREMCLI_ENC
LEFT JOIN NewBytes_DBF.dbo.pedclit ON  albclit.cnumped = pedclit.cnumped AND  albclit.cnumsuc = pedclit.cnumsuc
LEFT JOIN NEW_BYTES.dbo.MS_REMITO_CABECERA ON MS_REMITO_CABECERA.REMITO_FP = albclit.cnumalb and MS_REMITO_CABECERA.SUCURSAL_REMITO = albclit.cnumsuc
LEFT JOIN NEW_BYTES.dbo.MS_COTIZACIONES ON MS_COTIZACIONES.NOMBRE = 'PESOS'
LEFT JOIN [NB_WEB].[dbo].[liquidacion_guardada] ON liquidacion_guardada.ID_NROREMCLI_ENC = albclit.ID_NROREMCLI_ENC
LEFT JOIN NEW_BYTES.dbo.MS_VENTAS_REMITOS ON MS_REMITO_CABECERA.REMITO_FP = MS_VENTAS_REMITOS.REMITO_FP AND MS_REMITO_CABECERA.SUCURSAL_REMITO = MS_VENTAS_REMITOS.SUCURSAL_REMITO
LEFT JOIN NEW_BYTES.dbo.MS_FORMASPAGO_REMITOS_VENDEDORES ON MS_FORMASPAGO_REMITOS_VENDEDORES.ID_FORMA = MS_VENTAS_REMITOS.ID_FORMA OR MS_FORMASPAGO_REMITOS_VENDEDORES.ID_FORMA = liquidacion_guardada.formaDePago
LEFT JOIN NEW_BYTES.dbo.MS_STATUS_REMITO ON MS_STATUS_REMITO.ID_STATUS = MS_VENTAS_REMITOS.ID_STATUS
LEFT JOIN NewBytes_DBF.dbo.transpor ON transpor.ID_TRANSPORTISTA = MS_VENTAS_REMITOS.TRANSPORTE_FP OR transpor.ID_TRANSPORTISTA = liquidacion_guardada.envioRetiro
LEFT JOIN NewBytes_DBF.dbo.articulo ON articulo.cRef = albclil.cref
LEFT JOIN [NewBytes_DBF].[dbo].[FP_FactWebCliEncabezado] ON FP_FactWebCliEncabezado.ID_NROREMCLI_ENC = albclit.ID_NROREMCLI_ENC
LEFT JOIN [NB_WEB].[dbo].[facturacionForzada] ON facturacionForzada.ID_NROREMCLI_ENC=albclit.ID_NROREMCLI_ENC
LEFT JOIN NewBytes_DBF.DBO.agentes AGE_SECRET_KEY ON AGE_SECRET_KEY.ID_VENDEDOR = pedclit.secret_key_confirm_user

WHERE ALBCLIT.ID_NROREMCLI_ENC IS NOT NULL         
AND MS_VENTAS_REMITOS.ID_STATUS IN (2,10,11)
GROUP BY
dfecalb,
albclit.ID_NROREMCLI_ENC,
cnomcli,
agentes.capeage,
agentes.cnbrage,
MS_REMITO_CABECERA.COTIZACION,
[MS_COTIZACIONES].COTIZACION,
albclit.ntipoalb,
albclit.cnumalb,
MS_FORMASPAGO_REMITOS_VENDEDORES.DESCRIPCION,
MS_STATUS_REMITO.DESCRIPCION,
transpor.DESCRIPCION,
MS_VENTAS_REMITOS.ID_STATUS,
pedclit.cnumped,
pedclit.cnumsuc,
albclit.cnumsuc,
clientes.ID_CLIENTE,
FP_FactWebCliEncabezado.cfactura,
FP_FactWebCliEncabezado.ID_NROFACCLI_ENC,
MS_REMITO_CABECERA.[IMPPERCEP],
clientes.percepcion,
excluirPercepcion
pedclit.secret_key_confirm_date,
AGE_SECRET_KEY.cnbrage
ORDER BY albclit.dfecalb DESC
```
