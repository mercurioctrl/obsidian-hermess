---
jira_key: "EXP-187"
aliases: ["EXP-187"]
summary: "API - Review - Problemas para encontrar y abrir un pedido en devoluciones"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-01-27 12:25"
updated: "2023-02-23 16:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-187"
---

# EXP-187: API - Review - Problemas para encontrar y abrir un pedido en devoluciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-27 12:25 |
| Actualizado | 2023-02-23 16:20 |
| Etiquetas | ninguna |
| Jira | [EXP-187](https://bluinc.atlassian.net/browse/EXP-187) |

## Relaciones

- **Padre:** [[EXP-117]] Feat - Listar pedidos despachados para hacer devoluciones

## Descripcion

En ámbito de **producción** estaba buscando un pedido en devoluciones y tuve dos inconvenientes.

- Al poner en el buscador “`00020774`" que es el pedido que estoy buscando no lo pude encontrar. Opte por poner "`prestamos`" para encontrar todos los de el cliente` 30748 - PRESTAMOS MERCADERIAS` y ahí si lo pude ubicar.




- Al intentar abrirlo, veo: 

```sql
SQLSTATE[21000]: [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]La subconsulta ha devuelto más de un valor, lo que no es correcto cuando va a continuación de =, !=, <, <=, >, >= o cuando se utiliza como expresión. SQL: SELECT albclil.cdetalle as title, A.ID_ARTICULO as id, A.ID_PRODUCTO as sku, F.cnomfam as category, F.ID_FAMILIA as idCategory, M.referencia as brand, M.id as idBrand, P.checksum as mainImage, CAST(albclil.ncanent AS INT) as incomingQuantity, ( SELECT COUNT(*) FROM [NEW_BYTES].[dbo].[ST_REMITOS_VENTA_DETALLE_SALIDA] WHERE REMITO_FP = albclil.cnumalb and CREF = A.cRef ) AS serializedQuantity, A.serialAGranel as notSerializable, ( SELECT fullSerialized FROM [NEW_BYTES].[dbo].[ST_REMITOS_VENTA_CABECERA_SALIDA] WHERE REMITO_FP = albclil.cnumalb ) as fullSerialized, albclit.cnumalb as remitoFp, (albclil.npreunit+ (albclil.npreunit*albclil.niva/100)) as conIva, albclil.npreunit as sinIva, albclil.niva as ivaTax, E.COTIZACION as cotizacion, albclil.ACREDITADO as acreditado FROM [NewBytes_DBF].[dbo].[albclit] LEFT JOIN NewBytes_DBF.dbo.albclil ON albclil.ID_NROREMCLI_ENC = albclit.ID_NROREMCLI_ENC LEFT JOIN NewBytes_DBF.dbo.pedclit ON albclit.cnumped = pedclit.cnumped AND albclit.cnumsuc = pedclit.cnumsuc LEFT JOIN [NEW_BYTES].[dbo].[MS_REMITO_CABECERA] E ON E.REMITO_FP = albclil.cnumalb AND E.SUCURSAL_REMITO = albclil.cnumsuc LEFT JOIN [NewBytes_DBF].[dbo].[articulo] AS A ON albclil.cref = A.cRef LEFT JOIN NewBytes_DBF.dbo.familias AS F ON A.ccodfam = F.ccodfam LEFT JOIN NB_WEB.dbo.marcas as M ON A.ID_MARCA = M.id LEFT JOIN NB_WEB.dbo.fotos_productos AS FP ON FP.id_nb_producto = A.id_articulo AND FP.portada = 1 LEFT JOIN PRODUCTOS.dbo.fotos AS P ON FP.id_productos_fotos = P.id WHERE albclil.ID_NROREMCLI_ENC = 'X001000020774'
```



Es posible que este relacionado con las sucursal a la que pertenece el pedido.

Reporto el problema por aca, porque sospecho que es mas un arreglo para la lista que un bug.
