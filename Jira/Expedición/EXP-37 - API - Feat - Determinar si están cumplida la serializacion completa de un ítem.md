---
jira_key: "EXP-37"
aliases: ["EXP-37"]
summary: "API - Feat - Determinar si están cumplida la serializacion completa de un ítem"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-04 09:04"
updated: "2023-01-11 16:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-37"
---

# EXP-37: API - Feat - Determinar si están cumplida la serializacion completa de un ítem

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-04 09:04 |
| Actualizado | 2023-01-11 16:02 |
| Etiquetas | ninguna |
| Jira | [EXP-37](https://bluinc.atlassian.net/browse/EXP-37) |

## Relaciones

- **Padre:** [[EXP-10 - Feat - Listar pedidos (despachos) proveedores|EXP-10]] Feat - Listar pedidos (despachos) proveedores

## Descripcion

```
PATCH {API_URL}/v1/providersOrders/{providerOrderId}/fullSerializerCheck
```

Se debe crear un booleano (`true`,`false`) en 2 niveles, el de detalle y el de cabecera para poder controlar y determinar el estado actual del serialziado de un pedido de compra. 

En este contexto solo tendremos que contabilizar la cantidad de seriales que un item contiene y marcarlo como `true` en su detalle, si es que contiene tantos seriales como la cantidad comprada.

Adicionalmente tendremos en cuenta el valor de la columna `[NewBytes_DBF].[dbo].[articulo].serialAGranel` como un “escape” que me permita excluir del control al producto y lo marque como `true`.

Una vez que todos los detalles son `true`, entonces el pedido se marca como `true` en la cabecera

Retorna algo similar a esto que de cuenta de los faltantes, de tal modo que podamos informarlo al operario para que preste atención

```
[
  {
  fullSerialized: false,
  pending:[
    3245345,
    5454545,
    4545,
  ]
  }
]
```
