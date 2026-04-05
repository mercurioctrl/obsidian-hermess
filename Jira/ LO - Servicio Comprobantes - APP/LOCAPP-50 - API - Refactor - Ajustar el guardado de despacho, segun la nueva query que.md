---
jira_key: "LOCAPP-50"
aliases: ["LOCAPP-50"]
summary: "API - Refactor - Ajustar el guardado de despacho, segun la nueva query que vimos para que filtre los casos mejor por si hay un problema con el numero de remito proovedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-05 17:43"
updated: "2024-06-13 19:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-50"
---

# LOCAPP-50: API - Refactor - Ajustar el guardado de despacho, segun la nueva query que vimos para que filtre los casos mejor por si hay un problema con el numero de remito proovedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-05 17:43 |
| Actualizado | 2024-06-13 19:52 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-50](https://bluinc.atlassian.net/browse/LOCAPP-50) |

## Relaciones

- **Padre:** [[LOCAPP-23 - Generar un comprobante|LOCAPP-23]] Generar un comprobante

## Descripcion

Query orientativa que lo hace para todos los pendientes

```
UPDATE NewBytes_DBF.dbo.FP_FactWebCliDetalle SET nroDespacho = ( SELECT TOP 1
    DEC.DESCRIPCION
FROM NewBytes_DBF.dbo.FP_FactWebCliDetalle AS FD
    LEFT JOIN NewBytes_DBF.dbo.FP_FactWebCliEncabezado AS FE ON FD.ID_NROFACCLI_ENC = FE.ID_NROFACCLI_ENC
    LEFT JOIN NewBytes_DBF.dbo.albclit AS A ON FE.ID_NROREMCLI_ENC = A.ID_NROREMCLI_ENC
    LEFT JOIN [NEW_BYTES].[dbo].[ST_REMITOS_VENTA_DETALLE_SALIDA] AS RVDS ON RVDS.REMITO_FP = A.cnumalb
    LEFT JOIN [NEW_BYTES].[dbo].[ST_DETALLE_STOCK]  as D ON D.SERIAL = RVDS.SERIAL
    LEFT JOIN [NEW_BYTES].[dbo].[ST_ENL_DESPACHOS_ENTRADAS_REMITOS] AS E ON D.ID_COMPRA = E.ID_COMPRA
LEFT JOIN NewBytes_DBF.dbo.albprot ON albprot.nnumped =    E.REMITO_PRV_FP 
LEFT JOIN NewBytes_DBF.dbo.albprol ON albprol.nnumalb =    albprot.nnumalb AND albprol.CREF = FD.CREF    
    LEFT JOIN [NEW_BYTES].[dbo].[ST_DESPACHOS_ENTRADAS_CABECERA] AS DEC ON DEC.ID_DESPACHO_ENTRADA = E.ID_DESPACHO_ENTRADA
WHERE   (LEN( DEC.DESCRIPCION) = 20 OR LEN( DEC.DESCRIPCION) = 13) and albprol.cref IS NOT NULL AND D.SERIAL =  (SELECT TOP 1
        RVDS.SERIAL
    FROM NewBytes_DBF.dbo.FP_FactWebCliDetalle AS FD1
        LEFT JOIN NewBytes_DBF.dbo.FP_FactWebCliEncabezado AS FE1 ON FD1.ID_NROFACCLI_ENC = FE1.ID_NROFACCLI_ENC
        LEFT JOIN NewBytes_DBF.dbo.albclit AS A ON FE1.ID_NROREMCLI_ENC = A.ID_NROREMCLI_ENC
        LEFT JOIN [NEW_BYTES].[dbo].[ST_REMITOS_VENTA_DETALLE_SALIDA] AS RVDS ON RVDS.REMITO_FP = A.cnumalb AND FD1.CREF = RVDS.CREF
    where FE.ID_NROFACCLI_ENC = FE1.ID_NROFACCLI_ENC AND FD1.CREF = FD.CREF ) AND FE.ID_NROFACCLI_ENC = FP_FactWebCliDetalle.ID_NROFACCLI_ENC AND FD.CREF = FP_FactWebCliDetalle.CREF  )
 WHERE Fecha BETWEEN '01-05-2024' AND '01-12-2024' AND nroDespacho IS NULL;

```
