---
jira_key: "NBWEB-43"
aliases: ["NBWEB-43"]
summary: "Agregar producto al carrito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-21 09:37"
updated: "2022-03-28 12:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-43"
---

# NBWEB-43: Agregar producto al carrito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-21 09:37 |
| Actualizado | 2022-03-28 12:37 |
| Etiquetas | ninguna |
| Jira | [NBWEB-43](https://bluinc.atlassian.net/browse/NBWEB-43) |

## Relaciones

- **Padre:** [[NBWEB-1]] API - Carrito de compras

## Descripcion

Se trata del producto que sirve para agregar/editar/eliminar productos del carrito



```
POST {{API_URL}}/v1/carrito/item
```



En la request se envía el objeto



```json
{
  productId:34,
  amount:2,
  type:0
}
```

Y al procesar se debe determinar, usando la tabla `[NB_WEB].[dbo].[contenidoCarritos] (contenidoCarritos.id_carrito = carritos.id)`

a) Si el producto ya existe en el carrito (en combinación con el type) seleccionado, en ese caso debemos alterar la cantidad de unidades.

b) Si el producto no existe en el carrito (en combinación con el type), se debe crear.

Se deben tratar las columnas del siguiente modo

```
[id_carrito] -> Se trata del id de carrito seleccionado
[codProducto] -> Se trata de productId
[cantidad] -> Es la cantidad que se recibe en amount
[black] - > Si type =1, entonces black =1
[descuento] -> por ahora no lo vamos a utilizar
```
