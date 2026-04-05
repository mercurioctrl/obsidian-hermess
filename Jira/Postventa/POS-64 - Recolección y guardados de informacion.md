---
jira_key: "POS-64"
aliases: ["POS-64"]
summary: "Recolección y guardados de informacion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-09 13:28"
updated: "2022-10-11 10:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-64"
---

# POS-64: Recolección y guardados de informacion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-09 13:28 |
| Actualizado | 2022-10-11 10:21 |
| Etiquetas | ninguna |
| Jira | [POS-64](https://bluinc.atlassian.net/browse/POS-64) |

## Relaciones

- **Padre:** [[POS-57]] API - Feat - Estadisticas de productos

## Descripcion

Basándonos en una consulta del siguiente estilo

```
SELECT 
  codigo, 
  cref, 
  cdetalle, 
  (
    SELECT 
      Count(ingreso_rma) 
    FROM 
      [NEW_BYTES].[dbo].[st_rmadetalle] 
    WHERE 
      producto_cref = A.cref
  ) AS INGRESOS_RMA, 
  (
    SELECT 
      Sum(ncanent) 
    FROM 
      newbytes_dbf.dbo.albprol 
    WHERE 
      cref = A.cref
  ) AS INGRESOS_COMPRAS, 
  (
    SELECT 
      sum(
        nstock + nstock_lo + nstock_en_cola + nstock_d1
      ) 
    FROM 
      NewBytes_DBF.dbo.stocks 
    WHERE 
      cref = A.cref
  ) as STOCK, 
  (
    SELECT 
      SUM(albclil.ncanent) 
    FROM 
      NewBytes_DBF.dbo.albclit 
      LEFT JOIN NewBytes_DBF.dbo.albclil ON albclit.ID_NROREMCLI_ENC = albclil.ID_NROREMCLI_ENC 
    WHERE 
      albclil.cref = A.cRef 
      AND albclit.ntipoalb = 1 
      and lfacturado = 0
  ) AS RESERVAS,

  ROUND(ISNULL(  (
    SELECT 
      Count(ingreso_rma) 
    FROM 
      [NEW_BYTES].[dbo].[st_rmadetalle] 
    WHERE 
      producto_cref = A.cref
  ) / NULLIF(
      
   (
    SELECT 
      Sum(ncanent) 
    FROM 
      newbytes_dbf.dbo.albprol 
    WHERE 
      cref = A.cref
  )-
        (
    SELECT 
      sum(
        nstock + nstock_lo + nstock_en_cola + nstock_d1
      ) 
    FROM 
      NewBytes_DBF.dbo.stocks 
    WHERE 
      cref = A.cref
  )
  -
  (
    SELECT 
      SUM(albclil.ncanent) 
    FROM 
      NewBytes_DBF.dbo.albclit 
      LEFT JOIN NewBytes_DBF.dbo.albclil ON albclit.ID_NROREMCLI_ENC = albclil.ID_NROREMCLI_ENC 
    WHERE 
      albclil.cref = A.cRef 
      AND albclit.ntipoalb = 1 
      and lfacturado = 0
  )
  
      ,0)*100,0),2) as porcentajeDeIngresoARma



FROM 
  [NewBytes_DBF].[dbo].[articulo] A 
ORDER BY 
  (
    SELECT 
      Count(ingreso_rma) 
    FROM 
      [NEW_BYTES].[dbo].[st_rmadetalle] 
    WHERE 
      producto_cref = A.cref
  ) DESC
```

Se debe almacenar la informacion en una tabla llamada

`afterSaleMetrics` o similar

Lo que se intenta lograr es crear una tabla simple, donde estén los cálculos que luego se utilizaran para poder mostrar estadística filtrada y agrupada



La estrctura de la nueva tabla sera

- id


- productId


- cref


- Descroption 


- afterSaleIncome


- purchasesIncome


- reservation


- incomeRate


- failureRate



Si tenes alguna duda consultame!
