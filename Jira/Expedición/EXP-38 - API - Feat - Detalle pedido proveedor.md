---
jira_key: "EXP-38"
aliases: ["EXP-38"]
summary: "API - Feat - Detalle pedido proveedor"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-04 09:11"
updated: "2023-01-11 16:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-38"
---

# EXP-38: API - Feat - Detalle pedido proveedor

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-04 09:11 |
| Actualizado | 2023-01-11 16:02 |
| Etiquetas | ninguna |
| Jira | [EXP-38](https://bluinc.atlassian.net/browse/EXP-38) |

## Relaciones

- **Padre:** [[EXP-10]] Feat - Listar pedidos (despachos) proveedores
- **blocks:** [[EXP-40]] APP - Feat - Detalle pedido proveedor

## Descripcion

Esta historia describe el detalle de un pedido de proveedor.

En el se pueden ver diferentes características del producto.

También se pueden ver parámetros relativos a su serializacion que los describo aca abajo:

- `fullSerialized` se trata sobre si el ítem del pedido entrante fue completamente serializado. (este no existe en la db, hay que crearlo)


- `incomingQuantity` es la cantidad entrante del producto en ese pedido


- `serializedQuantity` es la cantidad de seriales que tengo dentro de ese pedido, para ese producto


- `notSerializable` esto es un parámetro para poder distinguir aquellos productos que son “a granel” y no se serial izan, algunos cables y gabinetes tienen esta característica. (hay una columna serialAGranel en la tabla `articulo`)





```
GET {API_URL}/v1/providersOrders/{providerOrderId}
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

`SELECT * FROM [NewBytes_DBF].[dbo].[FP_Proveedores]`
`[NewBytes_DBF].[dbo].[PedProT]`

`[NewBytes_DBF].[dbo].[PedProl]`

`[NEW_BYTES].[dbo].[ST_DETALLE_STOCK]`

`[NewBytes_DBF].[dbo].[articulo]`

`[NEW_BYTES].[dbo].[ST_DESPACHOS_ENTRADAS_CABECERA]`
`[NEW_BYTES].[dbo].[ST_ENL_DESPACHOS_ENTRADAS_REMITOS]`
`[NEW_BYTES].[dbo].[ST_DESPACHOS_ENTRADAS_CABECERA]`
