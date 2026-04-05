---
jira_key: "NBWEB-192"
aliases: ["NBWEB-192"]
summary: "API - Buscar por DESCRIPTION para formulario de postventa"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-19 13:37"
updated: "2022-06-26 21:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-192"
---

# NBWEB-192: API - Buscar por DESCRIPTION para formulario de postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-19 13:37 |
| Actualizado | 2022-06-26 21:23 |
| Etiquetas | ninguna |
| Jira | [NBWEB-192](https://bluinc.atlassian.net/browse/NBWEB-192) |

## Relaciones

- **Padre:** [[NBWEB-99]] API - Precarga postventa
- **relates to:** [[NBWEB-193]] APP - Agregar un suggest box  con description de producto al formulario de alta de post venta

## Descripcion

Este recurso es el que permite, en caso de no tener el serial, buscar el tipo de producto que quiere reclamar, y eligiéndolo de una lista, puedo obtener el id interno para saber que producto el cliente refiere que es

```
GET {{API_URL}}/v1/postventa/description/{description string}
```



```
{ 
  clientId: 2,
  warranty: 36, //son meses totales de la garantia 
  productoId: 2412, 
  productDescription: 'Descripcion del producto', 
  buyer:true //en caso de que la cuenta del cliente sea la misma que lo compro 
}
```



##### Sobre el parámetro ‘buyer’

Para obtenerlo se debe chequear, que en algún momento al menos el cliente compro el producto. Para esto vamos a buscar en las compras remitidas al cliente, si esta presente al menos una vez el ítem consignado mediante el id del producto.

Si miramos la función `getDetallePedido` ya hemos utilizado la conexion que se necesita

[adjunto]
```
        FROM NewBytes_DBF.dbo.albclit as E 
        RIGHT JOIN NewBytes_DBF.dbo.albclil as D ON E.cnumalb = D.cnumalb
```

Con eso podemos buscar en la tabla `albclil`, detalles de las compras consignadas por el cliente por id. En la cabecera se encuentran datos para vincularse con el cliente.
