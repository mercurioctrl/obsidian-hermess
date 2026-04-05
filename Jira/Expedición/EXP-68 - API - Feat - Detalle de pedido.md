---
jira_key: "EXP-68"
aliases: ["EXP-68"]
summary: "API - Feat - Detalle de pedido"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-14 12:40"
updated: "2022-11-16 15:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-68"
---

# EXP-68: API - Feat - Detalle de pedido

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-14 12:40 |
| Actualizado | 2022-11-16 15:04 |
| Etiquetas | ninguna |
| Jira | [EXP-68](https://bluinc.atlassian.net/browse/EXP-68) |

## Relaciones

- **Padre:** [[EXP-14 - Feat - Listar pedidos para retiro|EXP-14]] Feat - Listar pedidos para retiro

## Descripcion

Esta historia describe el detalle de un pedido de de venta.

En el se pueden ver diferentes características del producto.

También se pueden ver parámetros relativos a su serializacion que los describo aca abajo:

- `fullSerialized` se trata sobre si el ítem del pedido entrante fue completamente serializado. (este no existe en la db, hay que crearlo)


- `incomingQuantity` es la cantidad saliente del producto en ese pedido


- `serializedQuantity` es la cantidad de seriales que tengo dentro de ese pedido, para ese producto


- `notSerializable` esto es un parámetro para poder distinguir aquellos productos que son “a granel” y no se serial izan, algunos cables y gabinetes tienen esta característica. (hay una columna serialAGranel en la tabla `articulo`)





```
GET {API_URL}/v1/orders/{pedido}
```

Retorna 

```
[
    {
    "Title": "FUENTE GAMER GIGABYTE 550W 80 PLUS",
    "Id": "104964",
    "Sku": "GP-P550B",
    "Category": "FUENTES ",
    "IdCategory": "38",
    "IdBrand": "4",
    "Brand": "GIGABYTE ",
    "imagen_principal": "https://static.nb.com.ar/i/nb_nombre-del-producto_ver_b65cd71de19e10c27d8c357cd99cded9.png",
    "fullSerialized": true, //este parametro aun no lo tenes, lo desarrollaremos mas adelante
    "incomingQuantity": 25,
    "serializedQuantity": 25,
    "notSerializable": false
   }
]
```

Las tablas que pueden intervenir son

`SELECT * FROM [NewBytes_DBF].[dbo].[clientes]`
`[NewBytes_DBF].[dbo].[albclit]`

`[NewBytes_DBF].[dbo].[albclil]`

`[NEW_BYTES].[dbo].[ST_REMITOS_VENTA_CABECERA_SALIDA] `

`[NEW_BYTES].[dbo].[ST_REMITOS_VENTA_DETALLE_SALIDA]`

`[NEW_BYTES].[dbo].[ST_DETALLE_STOCK]`

`[NewBytes_DBF].[dbo].[articulo]`

Es similar a[link](https://lioteam.atlassian.net/browse/EXP-38) pero para despacho de ventas de mercaderia en lugar de para la entrada
