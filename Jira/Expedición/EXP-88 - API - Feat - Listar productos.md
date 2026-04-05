---
jira_key: "EXP-88"
aliases: ["EXP-88"]
summary: "API - Feat - Listar productos"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-22 10:08"
updated: "2022-12-12 13:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-88"
---

# EXP-88: API - Feat - Listar productos

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-22 10:08 |
| Actualizado | 2022-12-12 13:16 |
| Etiquetas | ninguna |
| Jira | [EXP-88](https://bluinc.atlassian.net/browse/EXP-88) |

## Relaciones

- **Padre:** [[EXP-17 - Feat - Listar productos (Control de stock)|EXP-17]] Feat - Listar productos (Control de stock)
- **is blocked by:** [[EXP-89 - API - Feat - Pedir control sobre un producto|EXP-89]] API - Feat - Pedir control sobre un producto
- **blocks:** [[EXP-89 - API - Feat - Pedir control sobre un producto|EXP-89]] API - Feat - Pedir control sobre un producto

## Descripcion

Esta historia es en algún sentido similar a [link](https://lioteam.atlassian.net/browse/NBWEB-4?jql=text%20~%20%22catalogo%22) porque se trata de listar los productos para su posterior contabilización.

La diferencia es que no incluye ningun excluido ni oculto a menos que se lo especifique un filtro concreto.

La lista la utilizaremos para mostrar aquellos productos que vamos a contabilizar o bien los que tiene algún problema lógico en la configurar de su stock o cualquier filtro similar

```
GET {API_URL}/v1/items?q={string}&=counted=true
```

Debe devolver algo similar a esto

```
[{
"Title":"FUENTE GAMER GIGABYTE 550W 80 PLUS",
"Id":"104964",
"Sku":"GP-P550B",
"Category":"FUENTES ",
"IdCategory":"38",
"IdBrand":"4",
"Brand":"GIGABYTE ",
"fullSerialized":true,
"lastStockControlDate": "10/12/2021 12:44",//Este parametro es nuevo, ver descripcion mas adelante
"stockHealthId": 1,//Este parametro es nuevo, ver descripcion mas adelante
"stockHealthDescription": 'Ok',//Este parametro es nuevo, ver descripcion mas adelante
"imagen_principal":"https://static.nb.com.ar/i/nb_nombre-del-producto_ver_b65cd71de19e10c27d8c357cd99cded9.png"
},
{
"Title":"FUENTE GAMER GIGABYTE 550W 80 PLUS",
"Id":"104964",
"Sku":"GP-P550B",
"Category":"FUENTES ",
"IdCategory":"38",
"IdBrand":"4",
"Brand":"GIGABYTE ",
"fullSerialized":true,
"lastStockControlDate": "10/12/2021 12:44",
"stockHealthId": 1,
"stockHealthDescription": 'Ok',
"imagen_principal":"https://static.nb.com.ar/i/nb_nombre-del-producto_ver_b65cd71de19e10c27d8c357cd99cded9.png"
}
]
```

Para esto crearemos la tabla `[NewBytes_DBF].[dbo].[stocksControl]` y mostraremos en el listado inicialmente (cuando esta sin filtrar) aquellos que están en ambas tablas.

Sobre `[NewBytes_DBF].[dbo].[stocksControl]`

Estructura:

- `id`


- `itemId` // el id para relacionarlo con los items


- `counted` // Es la cantidad contada (esto se hace en un paso posterior), inicio nuall


- `nstock` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `nstock_lo` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `nstock_en_cola` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `regularizacion_global` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `nstock_virtual` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `nstock_reserva_pedidos` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `nstock_postventa` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `nstock_lo_reserva_pedidos` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `countedDate` // La fecha de cuando se contabilizo  (esto se hace en un paso posterior) , inicio nuall


- `createDate` // corresponde a la fecha de inserción de la fila 


- `requestingUser` // el usuario que solicito el control



---

¿Como Funciona?

Al tratarse de un sistema de “control de stock” mediante el conteo físico de la mercaderia, lo que haremos sera “pedir” que cuenten un producto determinado.

Para pedir que cuenten un producto, lo introduciremos en la tabla `[NewBytes_DBF].[dbo].[stocksControl]` [link](https://lioteam.atlassian.net/browse/EXP-89)

Y diremos que si esta en la tabla `[NewBytes_DBF].[dbo].[stocksControl]` con la columna `counted` en `null` entonces no fue contado aun (`counted=false`). Este es el estado por defecto del listado, porque me muestra aquellos que debo controlar. Si quiero ver uno en especifico pasare un string y un `counted=true`
