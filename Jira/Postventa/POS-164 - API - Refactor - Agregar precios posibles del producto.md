---
jira_key: "POS-164"
aliases: ["POS-164"]
summary: "API - Refactor - Agregar precios posibles del producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-09-29 11:21"
updated: "2022-10-27 17:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-164"
---

# POS-164: API - Refactor - Agregar precios posibles del producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-29 11:21 |
| Actualizado | 2022-10-27 17:36 |
| Etiquetas | ninguna |
| Jira | [POS-164](https://bluinc.atlassian.net/browse/POS-164) |

## Relaciones

- **Padre:** [[POS-56 - API - Feat - Ver detalle ingreso|POS-56]] API - Feat - Ver detalle ingreso
- **blocks:** [[POS-166 - APP - Feat - Realizar credito de item de postventa|POS-166]] APP - Feat - Realizar credito de item de postventa

## Descripcion

```
GET {{API_URL}}/v1/makeAftersalesCredits/getPrices?itemId=7682&clientId=25789
```

Para obtener **el precio de compra del serial especifico** (si esta) se puede utilizar en principio algo como esto

```
SELECT
(D.npreunit - (D.npreunit*D.ndto/100)) as precioDeCompra, C.ccodcli, F.cDetalle, D.niva, E.COTIZACION,CONVERT(VARCHAR, C.dfecalb, 20) AS DFECFAC
FROM [NEW_BYTES].[dbo].[ST_RMADETALLE] A
LEFT JOIN NEW_BYTES.dbo.ST_REMITOS_VENTA_DETALLE_SALIDA B ON A.SERIAL = B.SERIAL
LEFT JOIN NewBytes_DBF.dbo.articulo F ON  A.PRODUCTO_CREF = F.cref
LEFT JOIN NewBytes_DBF.dbo.albclit C ON B.REMITO_FP = C.cnumalb AND B.SUCURSAL_REMITO = C.cnumsuc
LEFT JOIN NewBytes_DBF.dbo.albclil D ON D.cnumalb = C.cnumalb AND D.cnumsuc = C.cnumsuc AND D.cref = ?
LEFT JOIN [NEW_BYTES].[dbo].[MS_REMITO_CABECERA] E ON E.REMITO_FP = C.cnumalb AND E.SUCURSAL_REMITO = C.cnumsuc
WHERE ID_RMACLIENTE = ? AND A.PRODUCTO_CREF = ?
```

Que nos trae precio vinculando a través del serial y rma

Tambien suma si agregamos otras opciones de valor como un array con los **precios historicos para esa cuenta**

```
SELECT
(D.npreunit+ (D.npreunit*D.ndto/100)) as precioDeCompra
FROM
 NewBytes_DBF.dbo.albclit C
LEFT JOIN NewBytes_DBF.dbo.albclil D ON D.cnumalb = C.cnumalb AND D.cnumsuc = C.cnumsuc
WHERE  D.cref = ? AND C.ntipoalb>1 AND c.ccodcli = ?
GROUP BY (D.npreunit+ (D.npreunit*D.ndto/100))
```

La ultima opción que podemos agregar por ahora es el precio actual para ese cliente.

Esto ya lo hiciste en la api, porque es el precio del cliente actual, el de el momento. **Lo obtienes cruzando el id interno del producto con el id de cliente**
