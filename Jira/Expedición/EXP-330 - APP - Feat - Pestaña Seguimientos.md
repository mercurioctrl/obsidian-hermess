---
jira_key: "EXP-330"
aliases: ["EXP-330"]
summary: "APP - Feat - Pestaña Seguimientos"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-07-04 10:11"
updated: "2023-07-05 15:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-330"
---

# EXP-330: APP - Feat - Pestaña Seguimientos

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-04 10:11 |
| Actualizado | 2023-07-05 15:20 |
| Etiquetas | ninguna |
| Jira | [EXP-330](https://bluinc.atlassian.net/browse/EXP-330) |

## Relaciones

- **Padre:** [[EXP-325]] Feat - Pestaña seguimiento

## Descripcion

Crearemos una nueva pestaña en donde mostraremos informacion de aquellos pedidos que ya fueron generadas las etiquetas

```
GET {API_URL}/v1/trackingOrders?tracking={tracking}&search={search}&shippingMethods={1,2,3,4}
```

- Orden


- Fecha de pedido


- Pedido


- Currier (oca,andreani,etc)


- bultos


- Recolección (Es una fecha, si no esta, quiere decir que el currier no se lo llevo)


- Armador


- Entregador


- Estado (Este por ahora va vcio, pero crearemos una tarea para actualizar el ultimo estado del currier)



### Filtros

- Por tracking (`tracking`)


- Por nombre y numero de cliente, pedido, orden (`search`)


- medio de envio (`shippingMethods`).


- dropped (Filtra solo por retirados)


- between (filtra por fecha)
