---
jira_key: "PED-47"
summary: "API - Feat - Descargar ordenes de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-28 09:53"
updated: "2024-04-30 13:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-47"
---

# PED-47: API - Feat - Descargar ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-28 09:53 |
| Actualizado | 2024-04-30 13:40 |
| Etiquetas | ninguna |
| Jira | [PED-47](https://bluinc.atlassian.net/browse/PED-47) |

## Descripción

Cuando se recibe un pedido, que un cliente realizo por cualquier medio, ya sea por la web de NB, por la web de Libre Opción,, por una integración de la API (privada o de terceros como producteca, etc) este se genera, pero no se descuentan los items que contienen del stock, hasta que alguien “Descarga la orden”.

Al ver un pedido en la grilla, tendremos la opción “Descargar orden”

```
PATCH {API_URL}/v1/downloadOrder
```

- **Obtener los datos para trabajar**

```
SELECT
A.ID_ARTICULO, A.cref, A.CDETALLE, A.ID_PRODUCTO, A.ivaVenta, A.cpredef2, S.nstock, pedclit.ccodcli, pedclil.ncanped, 
(SELECT SUM(ncanped) FROM [NewBytes_DBF].[dbo].pedclil pl_sub
 LEFT JOIN NewBytes_DBF.dbo.pedclit pt_sub ON pl_sub.cnumsuc = pt_sub.cnumsuc AND pl_sub.cnumped = pt_sub.cnumped
 WHERE (pt_sub.cobserv = 'INTERNO' OR pt_sub.cobserv = 'DESCARGADO') AND pt_sub.cestado = 'P' AND 
 (pl_sub.cref = A.cRef or pl_sub.ID_Articulo = A.ID_ARTICULO) AND pl_sub.cnumped <> ?) AS ncanped_internos
FROM [NewBytes_DBF].[dbo].[articulo] A
LEFT JOIN [NB_WEB].[dbo].[WebArtComplement] W ON A.codigo = W.codigoArt
LEFT JOIN [NewBytes_DBF].[dbo].stocks S ON S.ID_ARTICULO = A.ID_ARTICULO
INNER JOIN [NewBytes_DBF].[dbo].pedclil ON pedclil.cref = A.cref or pedclil.id_articulo = A.id_articulo
LEFT JOIN NewBytes_DBF.dbo.pedclit ON pedclit.cnumped = pedclil.cnumped AND pedclit.cnumsuc = pedclil.cnumsuc
WHERE EXCLUIR <> 1 AND pedclil.cnumped = ? AND pedclil.cnumsuc = ? AND pedclil.ncanped > 0
GROUP BY A.ID_ARTICULO, A.CDETALLE, pedclil.ncanped, A.ID_PRODUCTO, A.ivaVenta, A.cpredef2, S.nstock, a.cref, pedclit.ccodcli;

```



**Verificar Condiciones Específicas**:

- **Iterar a través de los Productos y Preparar Actualizaciones**:

- Según el producto, preparar las consultas de actualización, obteniendo el precio con la misma funcion de precios que se utiliza en la API [link](https://lioteam.atlassian.net/browse/NBWEB-36?jql=text%20~%20%22precio%22%20AND%20project%20IN%20(10038)) 
Ejemplos de estas consultas incluyen 

Si es sucursal 10

```
UPDATE NewBytes_DBF.dbo.pedclil SET npreunit = ?, ndto = 0, niva = ?, listaPrecio = ? WHERE cref = ? AND cnumped = ? AND cnumsuc = ?;

```


Si NO es sucursal 10:

```
UPDATE NewBytes_DBF.dbo.pedclil SET ndto = 0, niva = ?, listaPrecio = ? WHERE cref = ? AND cnumped = ? AND cnumsuc = ?;

```


- **Decidir Acción Basada en la Satisfacción del Stock**:

Se verifican dos escenarios:

a. Si el resultado de la diferencia (el stock disponible después de considerar los pedidos internos) es menor que la cantidad solicitada en el pedido.

b. O si ambos, el resultado de la diferencia y la cantidad solicitada en el pedido, son cero.
¿como seria esto en terminos formales? Algo si:
`if ((((int) ( round($item->nstock) - round($item->ncanped_internos))) < round((int) $item->ncanped)) || ((int) ( round($item->nstock) - round($item->ncanped_internos)) == 0 && round((int) $item->ncanped) == 0)) {`


Si se cumple alguna de las condiciones anteriores, significa que no hay suficiente stock para satisfacer el pedido. Por lo tanto, se añade el producto actual a un array para después mostrar la lista de productos con stock insatisfactorio.
Si no se cumple la condición (lo que significa que hay suficiente stock para el producto actual), simplemente se tiene una línea comentada que mostraría la letra



- Si todos los productos cumplen con la disponibilidad de stock, proceder con las actualizaciones:

```
UPDATE [NewBytes_DBF].[dbo].pedclit SET cobserv = 'DESCARGADO', cnumsuc = ? WHERE pedclit.cnumped = ? AND pedclit.cnumsuc = ? AND (cobserv = 'PEDIDO DE INTERNET' OR cobserv = 'PRESUPUESTO');
```




- **Manejo de Errores**:

- En caso de que la ejecución de alguna consulta SQL falle, manejar el error y devolver un valor negativo (`false`) junto un detalle de que productos y en donde no se satisface el stock.
