---
jira_key: "POS-197"
aliases: ["POS-197"]
summary: "API - Feat - Obtener informacion completa de un serial"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-10-17 10:27"
updated: "2022-10-18 14:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-197"
---

# POS-197: API - Feat - Obtener informacion completa de un serial

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-17 10:27 |
| Actualizado | 2022-10-18 14:12 |
| Etiquetas | ninguna |
| Jira | [POS-197](https://bluinc.atlassian.net/browse/POS-197) |

## Relaciones

- **Padre:** [[POS-196]] Feat - Obtener informacion completa de un serial
- **blocks:** [[POS-198]] APP - Feat - Obtener informacion completa de un serial

## Descripcion

```
GET {API_URL}/V1/aboutSerial
```

```
SELECT AD.ccodcli as clientId, convert(varchar,AD.dfecalb, 5) as saleDate  , ART.cpredef2 as warranty, DATEDIFF(m,  ad.dfecalb, GETDATE()) as elapsedMonths,
CONCAT (AD.cnumsuc, '-',AD.cnumalb) AS referSale, ART.ID_ARTICULO as productId , ART.cDetalle as productDescription,
(
SELECT (albclil.npreunit - (albclil.npreunit * albclil.ndto / 100))  as purchasePrice
FROM NewBytes_DBF.dbo.albclil
WHERE albclil.ID_NROREMCLI_ENC = AB.ID_NROREMCLI_ENC AND ART.ID_ARTICULO = albclil.ID_Articulo ) as purchasePrice,
(
SELECT
TOP 1
Y.ccodcli
FROM
[NEW_BYTES].[dbo].[ST_REMITOS_VENTA_DETALLE_SALIDA] AS S1
LEFT JOIN [NewBytes_DBF].[dbo].[albclit] as Y
ON Y.cnumalb = S1.REMITO_FP
AND Y.cnumsuc = S1.SUCURSAL_REMITO
AND S1.CREF = ART.cRef
AND S1.SERIAL = STD.SERIAL
WHERE Y.cnumalb = AD.cnumalb AND Y.cnumsuc = AD.cnumsuc
ORDER BY S1.HORA_EXACTA DESC
) as ccodcliConfirm,
AD.userLo,
AD.secondaryClientNb,
CLILO.ccodcli,
CLILO.cnomcli,
CLILO.cnomcom,
CLINB.ccodcli,
CLINB.cnomcli,
CLINB.cnomcom,
STR3.REMITO_FP, 
albprot.nnumped,
albprol.cdetalle as purchaseName,
STD2.REMITO_PRV_FP AS purchaseId,
STD4.DESCRIPCION as dispatchId,
STD2.EDE_INVOICE as ticketPurchase,
albprot.dfecalb as dateInbound,
PROV.CCODPRO as supplierId,
PROV.cnompro as supplierDescription
FROM [NEW_BYTES].[dbo].[ST_DETALLE_STOCK] AS STD
LEFT JOIN [NewBytes_DBF].[dbo].articulo AS ART ON ART.cref = STD.cref
LEFT JOIN [NEW_BYTES].[dbo].[ST_REMITOS_VENTA_DETALLE_SALIDA] AS STR on STD.SERIAL = STR.serial
LEFT JOIN [NewBytes_DBF].[dbo].[albclit] as AD ON STR.REMITO_FP = AD.cnumalb and STR.SUCURSAL_REMITO = AD.cnumsuc
LEFT JOIN [NewBytes_DBF].[dbo].[albclil] as AB ON AD.ID_NROREMCLI_ENC = AB.ID_NROREMCLI_ENC
LEFT JOIN NewBytes_DBF.dbo.clientes CLINB ON CLINB.ccodcli = AD.ccodcli
LEFT JOIN NewBytes_DBF.dbo.clientes CLILO ON CLILO.ccodcli =  AD.secondaryClientNb
LEFT JOIN [NEW_BYTES].[dbo].[ST_REMITOS_VENTA_DETALLE_SALIDA] AS STR3 on STD.SERIAL = STR3.serial
LEFT JOIN [NEW_BYTES].[dbo].[ST_ENL_DESPACHOS_ENTRADAS_REMITOS] STD2 ON [STD].ID_COMPRA = [STD2].ID_COMPRA
LEFT JOIN [NEW_BYTES].[dbo].[ST_DESPACHOS_ENTRADAS_CABECERA] STD4 ON STD2.ID_DESPACHO_ENTRADA = STD4.ID_DESPACHO_ENTRADA
LEFT JOIN NewBytes_DBF.dbo.albprot ON STD2.REMITO_PRV_FP = albprot.nnumped
LEFT JOIN NewBytes_DBF.dbo.albprol ON albprol.cref = ART.cRef and albprot.nnumalb = albprol.nnumalb
LEFT JOIN NewBytes_DBF.dbo.FP_Proveedores PROV ON PROV.CCODPRO = albprot.ccodpro 
WHERE STD.SERIAL = 'A215000004911' // esta es una prueba de libre opcion
GROUP BY AD.ccodcli , AD.dfecalb , ART.cpredef2, ART.ID_ARTICULO , ART.cDetalle, AD.cnumsuc, AD.cnumalb, AB.ID_NROREMCLI_ENC, ART.cRef, STD.SERIAL,
AD.userLo,
AD.secondaryClientNb,
CLILO.ccodcli,
CLILO.cnomcli,
CLILO.cnomcom,
CLINB.ccodcli,
CLINB.cnomcli,
CLINB.cnomcom,
STR3.REMITO_FP,
albprot.nnumped,
albprol.cdetalle,
albprol.cref,
STD2.REMITO_PRV_FP,   STD4.DESCRIPCION, STD2.EDE_INVOICE
,albprot.dfecalb,
PROV.CCODPRO  ,
PROV.cnompro 


```
