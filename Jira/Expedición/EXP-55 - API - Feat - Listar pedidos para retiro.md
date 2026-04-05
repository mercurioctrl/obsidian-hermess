---
jira_key: "EXP-55"
aliases: ["EXP-55"]
summary: "API - Feat - Listar pedidos para retiro"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-09 09:46"
updated: "2025-02-18 22:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-55"
---

# EXP-55: API - Feat - Listar pedidos para retiro

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-09 09:46 |
| Actualizado | 2025-02-18 22:34 |
| Etiquetas | ninguna |
| Jira | [EXP-55](https://bluinc.atlassian.net/browse/EXP-55) |

## Relaciones

- **Padre:** [[EXP-14]] Feat - Listar pedidos para retiro
- **blocks:** [[EXP-84]] APP - Listar pedido para retiro
- **has action item:** [[EXP-479]] API - Listar pedidos para retiro - Error al buscar por cadena de texto

## Descripcion

Este recurso se encarga de listar aquellos pedidos (compras) que hay que preparar para retirar

Solo deben mostrarse los que están marcados como retiros

```
{API_URL}/v1/pickUp
```

Retorna 

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
