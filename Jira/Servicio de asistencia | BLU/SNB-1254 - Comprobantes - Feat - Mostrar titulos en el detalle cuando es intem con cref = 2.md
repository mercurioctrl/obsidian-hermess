---
jira_key: "SNB-1254"
aliases: ["SNB-1254"]
summary: "Comprobantes - Feat - Mostrar titulos en el detalle cuando es intem con cref = 2"
status: "Finalizada"
type: "Nueva función"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-10-25 17:53"
updated: "2023-10-26 14:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-1254"
---

# SNB-1254: Comprobantes - Feat - Mostrar titulos en el detalle cuando es intem con cref = 2

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Nueva función |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-25 17:53 |
| Actualizado | 2023-10-26 14:19 |
| Etiquetas | ninguna |
| Jira | [SNB-1254](https://bluinc.atlassian.net/browse/SNB-1254) |

## Relaciones

*Sin relaciones*

## Descripcion

Ejemplo:



```
SELECT TOP (1000) [CSERIE]
      ,[CNUMFAC]
      ,[CREF]
      ,[CDETALLE]
      ,[NPREUNIT]
      ,[NDTO]
      ,[NIVA]
      ,[NCANENT]
      ,[LCONTROL]
      ,[NUNIDADES]
      ,[NCOMISION]
      ,[NSERVICIO]
      ,[LSUPLIDOS]
      ,[NTIPODOCU]
      ,[CNUMSUC]
      ,[NIMP]
      ,[LMODIF]
      ,[NEXENTO]
      ,[CCODBAR]
      ,[CCOMENTA]
      ,[LSINIMPINT]
      ,[LBIENUSO]
      ,[NMONTOIMP]
      ,[NTIPOIMP]
      ,[ID_Articulo]
      ,[IdDetalleFactura]
      ,[Id_Sucursal]
      ,[ID_NROFACCLI_ENC]
      ,[Fecha]
      ,[NRORMA]
      ,[NROREM]
      ,[Id_marca]
      ,[id_articulo_fac_manual]
  FROM [NewBytes_DBF].[dbo].[FP_FactWebCliDetalle]
  WHERE ID_NROFACCLI_ENC = 517249
```
