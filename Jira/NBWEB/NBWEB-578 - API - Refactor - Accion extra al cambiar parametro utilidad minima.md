---
jira_key: "NBWEB-578"
aliases: ["NBWEB-578"]
summary: "API - Refactor - Accion extra al cambiar parametro utilidad minima"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-09-07 16:57"
updated: "2024-04-16 12:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-578"
---

# NBWEB-578: API - Refactor - Accion extra al cambiar parametro utilidad minima

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-07 16:57 |
| Actualizado | 2024-04-16 12:20 |
| Etiquetas | ninguna |
| Jira | [NBWEB-578](https://bluinc.atlassian.net/browse/NBWEB-578) |

## Relaciones

- **Padre:** [[NBWEB-524 - CMS - Parametros varios|NBWEB-524]] CMS - Parametros varios

## Descripcion

Para poder cambiar la utilidad minima, debemos tomar todos los proecios cuyas utilidades no cunmplen con la minima y ponerles esa utilidad como piso.

Las utilidades siempre se calculan con dos columnas en conjunto para cada producto por ejemplo:

`(PORC_GANAN_ESTIP3 + PORC_GANAN_ESTIP4)`

o

`(PORC_GANAN_ESTIPLO + PORC_GANAN_ESTIPLO1)`

y lo que nosotros queremos, es tomar la utilidad actual, ver que diferencia tiene con la minima y agregarle en la segunda columna (`PORC_GANAN_ESTIP4` y `PORC_GANAN_ESTIPLO1`) el faltante necesario para llegar a ese piso

Una query orientadores seria esta.

Es importante que solo se aplique a aquellos productos que cumplen las condiciones del where y ademas, que realemente esten por debajo de la minima.

MUY IMPORTANTE verificar bien que todo se corra en DESARROLLO

```

--Mostrar Cambios a realizar
SELECT
B.ID_ARTICULO,
articulo.cdetalle,
PORC_GANAN_ESTIP4,
PORC_GANAN_ESTIP3,
( (A.minUtility - (PORC_GANAN_ESTIP3 + PORC_GANAN_ESTIP4))) as AGREGAR_PORC_GANAN_ESTIP4,
PORC_GANAN_ESTIPLO,
PORC_GANAN_ESTIPLO1,
(  (A.minUtility - (PORC_GANAN_ESTIPLO + PORC_GANAN_ESTIPLO1))) as AGREGAR_PORC_GANAN_ESTIPLO1,
A.minUtility
FROM [NEW_BYTES].[dbo].[ST_GANANCIA_ESTIPULADA_ARTICULOS] B
LEFT JOIN NEW_BYTES.dbo.PV_PARAMETROS_VARIOS A ON 1=1
LEFT JOIN newbytes_dbf.dbo.articulo ON articulo.cref = B.ID_ARTICULO
WHERE  b.ID_ARTICULO NOT IN (
SELECT albprol.cref FROM NewBytes_DBF.DBO.albprot
INNER JOIN NewBytes_DBF.dbo.albprol ON albprot.nnumalb = albprol.nnumalb
INNER JOIN [NewBytes_DBF].[dbo].[FP_Proveedores] ON albprot.ccodpro = FP_Proveedores.CCODPRO
WHERE CNACPRO = 'ARGE' AND albprot.dfecalb BETWEEN '01-01-2020 00:00' AND  '01-01-2024 00:00'
GROUP BY albprol.cref
)
AND articulo.ccodfam <> '0065'
ORDER BY  b.ID_ARTICULO DESC;
```
