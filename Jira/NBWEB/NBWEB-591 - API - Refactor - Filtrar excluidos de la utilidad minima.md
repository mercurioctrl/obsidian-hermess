---
jira_key: "NBWEB-591"
aliases: ["NBWEB-591"]
summary: "API - Refactor - Filtrar excluidos de la utilidad minima"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-10-17 08:42"
updated: "2024-04-16 12:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-591"
---

# NBWEB-591: API - Refactor - Filtrar excluidos de la utilidad minima

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-17 08:42 |
| Actualizado | 2024-04-16 12:16 |
| Etiquetas | ninguna |
| Jira | [NBWEB-591](https://bluinc.atlassian.net/browse/NBWEB-591) |

## Relaciones

- **Padre:** [[NBWEB-524 - CMS - Parametros varios|NBWEB-524]] CMS - Parametros varios

## Descripcion

Agregaremos a los tres casos de uso, un filtro para evitar modificar aquellos que estan excluidos del controld e utilidad minima. 

Para esto usaremos la columna `NewBytes_DBF.dbo.articulo.minUtilityExclude` de la siguiente manera **para cada uno de los tres casos de uso**

```sql
WITH CTE2
AS (
    SELECT GAN.ID_ARTICULO AS idItem
        , PORC_GANAN_ESTIP AS profitPercentageConstant
        , PORC_GANAN_ESTIP2 AS profitPercentageVariable
    FROM NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS GAN
    LEFT JOIN NewBytes_DBF.dbo.articulo ART
        ON ART.cref = GAN.ID_ARTICULO
    WHERE GAN.ID_ARTICULO NOT IN (
            SELECT albprol.cref
            FROM NewBytes_DBF.DBO.albprot
            INNER JOIN NewBytes_DBF.dbo.albprol
                ON albprot.nnumalb = albprol.nnumalb
            INNER JOIN NewBytes_DBF.dbo.FP_Proveedores
                ON albprot.ccodpro = FP_Proveedores.CCODPRO
            WHERE CNACPRO = 'ARGE'
                AND albprot.dfecalb BETWEEN '01-01-2020 00:00' AND '01-01-2024 00:00'
            GROUP BY albprol.cref
            )
        AND ART.ccodfam <> '0065'
        AND (PORC_GANAN_ESTIP + PORC_GANAN_ESTIP2) < {montoMinimo}
        AND ART.minUtilityExclude <> 1 <--- se agrega este parametro
    )
UPDATE [NEW_BYTES].[dbo].[ST_GANANCIA_ESTIPULADA_ARTICULOS]
SET PORC_GANAN_ESTIP2_BACK = CTE2.profitPercentageVariable
    , PORC_GANAN_ESTIP2 = ({montoMinimo} - CTE2.profitPercentageConstant)
    , DATE_MODIFIED = FORMAT(GETDATE(), 'yyyy-MM-dd hh:mm:ss')
FROM CTE2
WHERE [NEW_BYTES].[dbo].[ST_GANANCIA_ESTIPULADA_ARTICULOS].ID_ARTICULO = CTE2.idItem;
```
