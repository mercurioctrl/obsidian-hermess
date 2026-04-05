---
jira_key: "NBWEB-45"
aliases: ["NBWEB-45"]
summary: "Chequear disponibilidad en carrito de compras"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-21 09:38"
updated: "2022-03-28 12:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-45"
---

# NBWEB-45: Chequear disponibilidad en carrito de compras

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-21 09:38 |
| Actualizado | 2022-03-28 12:37 |
| Etiquetas | ninguna |
| Jira | [NBWEB-45](https://bluinc.atlassian.net/browse/NBWEB-45) |

## Relaciones

- **Padre:** [[NBWEB-1 - API - Carrito de compras|NBWEB-1]] API - Carrito de compras

## Descripcion

```
GET {{API_URL}}/v1/carrito/availability
```



Este recurso de trata de obtener la disponibilidad de todos los productos contenidos en el carrito

retorna un array de objetos con la disponibilidad de cada uno de los items y el stock 



```json

[
  {
"Id":"104964",
"Stock":"Alto",
"AmountInCart":3,
"availability":1
},
  {
"Id":"101467",
"Stock":"Alto",
"AmountInCart":6,
"availability":0
},
]
```

Donde availability representa el estado de disponibilidad, segun la cantidad disponible en stock, es mas alta o igual a la cantidad de ese producto en el carrito
