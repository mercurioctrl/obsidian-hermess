---
jira_key: "EXP-67"
summary: "API - Feat - Determinar si están cumplida la serializacion completa de un ítem para un pedido especifico"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-14 12:34"
updated: "2023-01-27 12:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-67"
---

# EXP-67: API - Feat - Determinar si están cumplida la serializacion completa de un ítem para un pedido especifico

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-14 12:34 |
| Actualizado | 2023-01-27 12:01 |
| Etiquetas | ninguna |
| Jira | [EXP-67](https://bluinc.atlassian.net/browse/EXP-67) |

## Descripción

```
PATCH {API_URL}/v1/orders/{pedido}/fullSerializerCheck
```

Se debe crear un booleano (`true`,`false`) en 2 niveles en [NEW_BYTES].[dbo].[MS_VENTAS_REMITOS] y [NEW_BYTES].[dbo].[MS_REMITO_DETALLE] esto ya se hacia en otras tablas, el de detalle y el de cabecera para poder controlar y determinar el estado actual del serialziado de un pedido de compra.

En este contexto solo tendremos que contabilizar la cantidad de seriales que un item contiene y marcarlo como `true` en su detalle, si es que contiene tantos seriales como la cantidad comprada.

Adicional mente tendremos en cuenta el valor de la columna `[NewBytes_DBF].[dbo].[articulo].serialAGranel` como un “escape” que me permita excluir del control al producto y lo marque como `true`.

Tener en cuenta ademas, que tambien puede haberse ya verificado en true cuando se hizo el ingreso en [link](https://lioteam.atlassian.net/browse/EXP-66)

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

Este recurso es muy parecido a uno que ya existe para la entrada de mercaderia

[link](https://lioteam.atlassian.net/browse/EXP-37)
