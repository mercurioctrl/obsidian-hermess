---
jira_key: "PED-192"
aliases: ["PED-192"]
summary: "API - Feat - Descargar listado de precios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-10-30 12:09"
updated: "2023-11-08 06:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-192"
---

# PED-192: API - Feat - Descargar listado de precios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-30 12:09 |
| Actualizado | 2023-11-08 06:57 |
| Etiquetas | ninguna |
| Jira | [PED-192](https://bluinc.atlassian.net/browse/PED-192) |

## Relaciones

- **Padre:** [[PED-191]] Descargar Listado de precios
- **blocks:** [[PED-193]] APP - Feat - Descargar listado de precios
- **is blocked by:** [[PED-240]] API - Descargar listado de precios - Incidencias varias

## Descripcion

Esta feature se encarga de descargar un fichero (txt o xlsx) segun corresponda al objeto recibido. 

Se trata de una lista de precios para el cliente seleccionado (Si no se selecciona ninguna, sera la lista del cliente del vendedor).

### Criterios de aceptación

- En caso de que `search` sea distinto de nulo, entonces aplicamos el filtro en el string del nombre del producto de modao tal que si search=memoria diremos que vamos a mostrar todos los productos que tengan la palabra "memoria"


- Si `type` es txt, mostrare un archivo con formato txt y si es xlsx, mostrare una hoja de calculo


- Si clientId es nulo, muestro los precios para el clientId del usuario del vendedor. Sino los de ese cliente puntual segun la *clases precios*


- El formato del archivo de salida sera el siguiente `lista_precios-{clientId}-{clietnDescription}-{date}.xls/txt`


- Solo mostrare los clientes que cumplan lo siguiente: ` ( nstock -  nstock_reserva_pedidos )> 0 `





```
GET {API_URL}/v1/download/priceList
```

```
[
  {
    search: 'String de busqueda para el titulo'
    clientId: 26806,
    type: txt/xlsx
  }
]
```



Esta consulta es solo un ejemplo, se puede optimizar sacando todo lo que no sirve. Para calcular los precios, si o si debemos pasar por la* clase precios*

```
SELECT articulo.ccodfam, NewBytes_DBF.dbo.stocks.nstock, codigo, NewBytes_DBF.dbo.articulo.cref, cDetalle, cpredef3, cpredef2, npvp1, ndto2, ndto3, cpredef4, NewBytes_DBF.dbo.articulo.Id_Marca, cpredef1, ID_FAMILIA, npvp5,nporciva
FROM NewBytes_DBF.dbo.articulo
LEFT JOIN NewBytes_DBF.dbo.STOCKS ON (NewBytes_DBF.dbo.ARTICULO.CREF = NewBytes_DBF.dbo.STOCKS.CREF) AND STOCKS.ID_ALMACEN = 2
LEFT JOIN NB_WEB.dbo.WebArtComplement ON (NewBytes_DBF.dbo.ARTICULO.CREF = NB_WEB.dbo.WebArtComplement.cRef)
LEFT JOIN NB_WEB.dbo.familias ON (articulo.ccodfam = NB_WEB.dbo.familias.ccodfam)
LEFT JOIN NewBytes_DBF.dbo.ivas ON (articulo.ctipoiva = NewBytes_DBF.dbo.ivas.ctipoiva)
WHERE NB_WEB.dbo.WebArtComplement.ocultar <> 1 AND EXCLUIR <> 1 AND npvp5 > 0  AND articulo.ocultarDeNb <> 1 
AND ( nstock -  nstock_reserva_pedidos )> 0 
...
GROUP BY articulo.ccodfam, NewBytes_DBF.dbo.stocks.nstock, codigo, NewBytes_DBF.dbo.articulo.cref, cDetalle, cpredef3, cpredef2, npvp1, ndto2, ndto3, cpredef4, NewBytes_DBF.dbo.articulo.Id_Marca, cpredef1, ID_FAMILIA, npvp5,nporciva
ORDER BY articulo.ccodfam ASC, cDetalle ASC
```
