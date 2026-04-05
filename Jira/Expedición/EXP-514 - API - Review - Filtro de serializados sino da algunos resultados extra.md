---
jira_key: "EXP-514"
aliases: ["EXP-514"]
summary: "API - Review - Filtro de serializados si/no da algunos resultados extra"
status: "Finalizada"
type: "Tarea"
priority: "Low"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-09 08:49"
updated: "2025-12-05 05:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-514"
---

# EXP-514: API - Review - Filtro de serializados si/no da algunos resultados extra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Low |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-09 08:49 |
| Actualizado | 2025-12-05 05:52 |
| Etiquetas | ninguna |
| Jira | [EXP-514](https://bluinc.atlassian.net/browse/EXP-514) |

## Relaciones

- **Padre:** [[EXP-7 - Despacho de retiros|EXP-7]] Despacho de retiros

## Descripcion

Mientras revisava algunas cosas para el MVP note algo extraño que podemos revisar y es que al agregar el filtro serializado (  [https://gamma.expedicion.saftel.com/pickUp?currentPage=1&itemsPerPage=300&between=01-01-2025_31-05-2025&status=2,11,10,13&fullSerialized=0](https://gamma.expedicion.saftel.com/pickUp?currentPage=1&itemsPerPage=300&between=01-01-2025_31-05-2025&status=2,11,10,13&fullSerialized=0) ) parece traer registros que al menos parecen estar como serialize:true

También me trajo algún mensaje tipo cuando se actualizo solo, aunque no se si esta realacionado, parece ser algo de otro recurso

```
{"code":500,"details":"SQLSTATE[42S22]: [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]El nombre de columna 'serialized' no es válido. SQL: SELECT CONVERT(VARCHAR, dfecalb, 20) as date, albclit.ID_NROREMCLI_ENC as pedido, null as clientId, null as clientName, null as sellerId, null AS sellerName, MS_FORMASPAGO_REMITOS_VENDEDORES.DESCRIPCION as paymentMethod, MS_FORMASPAGO_REMITOS_VENDEDORES.ID_FORMA as paymentMethodId, MS_STATUS_REMITO.DESCRIPCION as statusDescription, RTRIM(transpor.DESCRIPCION) as dispatch, MS_VENTAS_REMITOS.ID_STATUS as statusId, pedclit.cnumped as 'order', pedclit.cnumsuc as branch, null as cfactura, albclit.cnumalb as cnumalb, RTRIM(mediosEnvio.nombre) as currierName, IIF(mediosEnvio.id IS NULL, transpor.medioEnvioId, mediosEnvio.id) as currierId, null as provinceId, null as provinceName, null as placeId, null as placeName, d.cptlcli as zipCode, IIF((pedclit.tracking is null), 0, 1) as shippingLabel, IIF((pedclit.idDirCliNbWeb is null), null, pedclit.idDirCliNbWeb) as idDirCliNbWeb, null as fullSerialized, null as token, null as voucherIdFactura, MS_REMITO_CABECERA.alert, null as whoBuild, null as whoAuthorized, pedclit.secret_key, lfacturado as facturado, null as isJoinedShipping, pedclit.dropShipping, null as thirdVoucher, pedclit.idLo, MS_VENTAS_REMITOS.F_H_AUTORIZADO as authorizedDate, pedclit.companyCode as companyCode, ISNULL(assamblePc,0) as assemblePc, ISNULL(updateBios,0) as updateBios, ISNULL(installOs,0) as installOs, tiSuccess as tiSuccess FROM [NewBytes_DBF].[dbo].[albclit] LEFT JOIN NewBytes_DBF.dbo.pedclit ON albclit.cnumped = pedclit.cnumped AND albclit.cnumsuc = pedclit.cnumsuc LEFT JOIN NB_WEB.dbo.dircli d ON d.IdDirCli = pedclit.idDirCliNbWeb LEFT JOIN NewBytes_DBF.dbo.FP_Provincias as P ON P.Id_Provincia = d.provinceId LEFT JOIN [NewBytes_DBF].[dbo].[dircli] as dd ON CAST(dd.ccodcli AS INT) = CAST(d.ccodcli AS INT) LEFT JOIN NEW_BYTES.dbo.MS_REMITO_CABECERA ON MS_REMITO_CABECERA.REMITO_FP = albclit.cnumalb and MS_REMITO_CABECERA.SUCURSAL_REMITO = albclit.cnumsuc LEFT JOIN NEW_BYTES.dbo.MS_VENTAS_REMITOS ON MS_REMITO_CABECERA.REMITO_FP = MS_VENTAS_REMITOS.REMITO_FP AND MS_REMITO_CABECERA.SUCURSAL_REMITO = MS_VENTAS_REMITOS.SUCURSAL_REMITO LEFT JOIN NEW_BYTES.dbo.MS_FORMASPAGO_REMITOS_VENDEDORES ON MS_FORMASPAGO_REMITOS_VENDEDORES.ID_FORMA = MS_VENTAS_REMITOS.ID_FORMA LEFT JOIN NEW_BYTES.dbo.MS_STATUS_REMITO ON MS_STATUS_REMITO.ID_STATUS = MS_VENTAS_REMITOS.ID_STATUS LEFT JOIN NewBytes_DBF.dbo.transpor ON transpor.ID_TRANSPORTISTA = MS_VENTAS_REMITOS.TRANSPORTE_FP LEFT JOIN LO.dbo.mediosEnvio ON mediosEnvio.id = pedclit.medioEnvioId WHERE 1 = 1 AND MS_VENTAS_REMITOS.ANULADO = 'NO' AND MS_REMITO_CABECERA.ANULADO = 'NO' AND dfecalb BETWEEN '2025-01-01' AND '2027-07-05' AND MS_VENTAS_REMITOS.ID_STATUS IN (2,11,10,13) AND (pedclit.serialized = 0 OR pedclit.serialized IS NULL) AND albclit.ID_NROREMCLI_ENC IS NOT NULL AND MS_VENTAS_REMITOS.TRANSPORTE_FP IN (9,12,13,17,18,20,21,22) GROUP BY dfecalb, albclit.ID_NROREMCLI_ENC, albclit.ntipoalb, MS_FORMASPAGO_REMITOS_VENDEDORES.DESCRIPCION, MS_STATUS_REMITO.DESCRIPCION, transpor.DESCRIPCION, MS_VENTAS_REMITOS.ID_STATUS, pedclit.cnumped, pedclit.cnumsuc, albclit.cnumalb, mediosEnvio.nombre, mediosEnvio.id, P.Id_Provincia, P.Descripcion, d.cptlcli, pedclit.tracking, albclit.cnumsuc, MS_REMITO_CABECERA.alertDate, MS_REMITO_CABECERA.alert, pedclit.idDirCliNbWeb, transpor.medioEnvioId, MS_FORMASPAGO_REMITOS_VENDEDORES.ID_FORMA, pedclit.secret_key, lfacturado, pedclit.dropShipping, pedclit.idLo, MS_VENTAS_REMITOS.F_H_AUTORIZADO, pedclit.companyCode, assamblePc, updateBios, installOs, tiSuccess ORDER BY MS_REMITO_CABECERA.alertDate DESC, dfecalb DESC OFFSET 0 ROWS FETCH NEXT 300 ROWS ONLY","file":"/var/www/app/src/App/Database.php","line":122}
```

[adjunto]
