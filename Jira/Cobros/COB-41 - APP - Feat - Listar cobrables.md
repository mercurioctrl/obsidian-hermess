---
jira_key: "COB-41"
aliases: ["COB-41"]
summary: "APP - Feat -  Listar cobrables"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-01 08:31"
updated: "2022-10-25 09:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-41"
---

# COB-41: APP - Feat -  Listar cobrables

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-01 08:31 |
| Actualizado | 2022-10-25 09:02 |
| Etiquetas | ninguna |
| Jira | [COB-41](https://bluinc.atlassian.net/browse/COB-41) |

## Relaciones

- **Padre:** [[COB-33 - Cobrar|COB-33]] Cobrar
- **Subtarea:** [[COB-109 - API - Feat - Filtros y paginacion|COB-109]] API - Feat - Filtros y paginacion
- **Subtarea:** [[COB-111 - API - Feat - Listar Metodos de Pago Remitos Vendedores|COB-111]] API - Feat - Listar Metodos de Pago Remitos Vendedores
- **Subtarea:** [[COB-112 - API - Feat - Listar Transportes|COB-112]] API - Feat - Listar Transportes
- **Subtarea:** [[COB-120 - API - Feat - Listar Tipos de Comprobantes|COB-120]] API - Feat - Listar Tipos de Comprobantes
- **Subtarea:** [[COB-121 - API - Feat - Listar Tipos de Impuestos|COB-121]] API - Feat - Listar Tipos de Impuestos
- **Subtarea:** [[COB-238 - API - Refactor - Se agrega informacion sobre el banco donde el cliente hace el|COB-238]] API - Refactor - Se agrega informacion sobre el banco donde el cliente hace el deposito
- **Subtarea:** [[COB-273 - API - Performance - Mejorar velocidad en la carga del listado de cobrables 4s|COB-273]] API - Performance - Mejorar velocidad en la carga del listado de cobrables < 4s
- **Subtarea:** [[COB-346 - API - Refactor - Mostrar cotizacion especifica en el caso de los pedidos de|COB-346]] API - Refactor - Mostrar cotizacion especifica en el caso de los pedidos de libre opcion
- **blocks:** [[COB-42 - APP - Feat - Listar cobrables|COB-42]] APP - Feat -  Listar cobrables
- **is blocked by:** [[COB-55 - API - Feat - Listar estados cobrarbles|COB-55]] API - Feat - Listar estados cobrarbles
- **blocks:** [[COB-125 - APP - Feat - Modal de cobro|COB-125]] APP - Feat - Modal de cobro

## Descripcion

Se trata de un  recurso que sirve para listar los ‘transables’ o que se pueden cobrar para este caso especifico, es decir los pedidos (o remitos)

```
GET {{API_URL}}/v1/tradable
```

```
[
  {
    "fecha": "2022-07-31 19:05:15",
    "pedido": "X001000020625",
    "clientName": "MUGELLO SRL",
    "sellerName": "Altamiranda                    Dario",
    "total": 173314502210.0,
    "taxes": 0.0,
    "totalFinal": 173314502210.0,
    "currencyQuote": 138.0,
    "currencyQuoteDay": 138.0,
    "status": 3.0,
    "paymentMethod": "Efectivo Camioneta",
    "estado": "Finalizado",
    "dispatch": "Envio Camioneta               ",
    "settlement": 4,
    "order": "10287149",
    "orderBrunch": "0010",
    "brunch": "0010",
    "clientId": 33181,
    "invoice": null,
    "albId": "00020625",
    "invoiceId": null,
    "taxesAmount": 0.0
  },
  {
    "fecha": "2022-07-29 17:39:04",
    "pedido": "X001000020624",
    "clientName": "BLANCO INSUA GALO                  ",
    "sellerName": "Blanco Insua    Galo",
    "total": 51400000.0,
    "taxes": 0.0,
    "totalFinal": 51400000.0,
    "currencyQuote": 138.0,
    "currencyQuoteDay": 138.0,
    "status": 3.0,
    "paymentMethod": "Efectivo Caja",
    "estado": "Despachado, Pendiente a Cobrar",
    "dispatch": "Retiro de cliente en Local    ",
    "settlement": 3,
    "order": "10287114",
    "orderBrunch": "0010",
    "brunch": "0010",
    "clientId": 16718,
    "invoice": null,
    "albId": "00020624",
    "invoiceId": null,
    "taxesAmount": 0.0
  },
  {
    "fecha": "2022-07-29 16:38:29",
    "pedido": "X001000020623",
    "clientName": "VOMMARO VALERIA",
    "sellerName": "Altamiranda                    Dario",
    "total": 19317590.0,
    "taxes": 0.0,
    "totalFinal": 19317590.0,
    "currencyQuote": 138.0,
    "currencyQuoteDay": 138.0,
    "status": 3.0,
    "paymentMethod": "Cta. Cte Cliente",
    "estado": "Finalizado",
    "dispatch": "Retiro de cliente en Local    ",
    "settlement": 4,
    "order": "10287112",
    "orderBrunch": "0010",
    "brunch": "0010",
    "clientId": 28681,
    "invoice": null,
    "albId": "00020623",
    "invoiceId": null,
    "taxesAmount": 0.0
  }
]
```

```

SELECT
TOP(4)
CONVERT(VARCHAR, dfecalb, 20) AS fecha,
albclit.ID_NROREMCLI_ENC as pedido,
cnomcli as clientName,
capeage  + ' '+ cnbrage as sellerName,
SUM(ncanent*npreunit-ncanent*npreunit*albclil.ndto/100) AS total,
CASE
    WHEN albclit.cnumsuc = '0010' OR clientes.excluirPercepcion = 1
    THEN 0
    ELSE (SUM((ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)*clientes.percepcion)/100)
END AS taxes,

CASE
    WHEN albclit.cnumsuc = '0010' OR clientes.excluirPercepcion = 1
    THEN
    (SUM((ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)+(ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)*albclil.niva/100))
    ELSE
    (SUM((ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)+(ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)*albclil.niva/100)+ISNULL((SUM((ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)*clientes.percepcion)/100), 0 ))

END AS totalFinal,
MS_REMITO_CABECERA.COTIZACION as currencyQuote,
[MS_COTIZACIONES].COTIZACION as currencyQuoteDay,
albclit.ntipoalb as status,
MS_FORMASPAGO_REMITOS_VENDEDORES.DESCRIPCION as paymentMethod,
MS_STATUS_REMITO.DESCRIPCION as estado,
transpor.DESCRIPCION as dispatch,
MS_VENTAS_REMITOS.ID_STATUS as settlement,
pedclit.cnumped as 'order',
pedclit.cnumsuc as orderBrunch,
albclit.cnumsuc as brunch,
clientes.ID_CLIENTE as clientId,
FP_FactWebCliEncabezado.cfactura as invoice,
albclit.cnumalb as albId,
FP_FactWebCliEncabezado.ID_NROFACCLI_ENC as invoiceId,
MS_REMITO_CABECERA.[IMPPERCEP] as taxesAmount
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
WHERE ALBCLIT.ID_NROREMCLI_ENC IS NOT NULL        and cnomcli <>'Libre Opcion'
GROUP BY
dfecalb,
albclit.ID_NROREMCLI_ENC,
cnomcli,
capeage,
cnbrage,
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
ORDER BY albclit.dfecalb DESC
```
