---
jira_key: "SNB-572"
aliases: ["SNB-572"]
summary: "Aparece la leyenda 'Facturacion sin item 21' en las NC desde comprobantes"
status: "Finalizada"
type: "Nueva función"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-02-13 09:51"
updated: "2023-02-27 10:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-572"
---

# SNB-572: Aparece la leyenda 'Facturacion sin item 21' en las NC desde comprobantes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Nueva función |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-02-13 09:51 |
| Actualizado | 2023-02-27 10:36 |
| Etiquetas | ninguna |
| Jira | [SNB-572](https://bluinc.atlassian.net/browse/SNB-572) |

## Relaciones

*Sin relaciones*

## Descripcion

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
  where ID_NROFACCLI_ENC = 495054
  ORDER BY ID_NROFACCLI_ENC DESC
```

[adjunto]
