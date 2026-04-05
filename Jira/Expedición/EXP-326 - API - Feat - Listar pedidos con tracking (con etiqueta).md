---
jira_key: "EXP-326"
aliases: ["EXP-326"]
summary: "API - Feat - Listar pedidos con tracking (con etiqueta)"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-06-30 09:25"
updated: "2023-06-30 14:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-326"
---

# EXP-326: API - Feat - Listar pedidos con tracking (con etiqueta)

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-30 09:25 |
| Actualizado | 2023-06-30 14:27 |
| Etiquetas | ninguna |
| Jira | [EXP-326](https://bluinc.atlassian.net/browse/EXP-326) |

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



Los nombres de los parametros deben ser en ingles, respetando los lineamientos que venimos teniendo

### Filtros

- Por tracking (`tracking`)


- Por nombre y numero de cliente, pedido, orden (`search`)


- medio de envio (`shippingMethods`).


- dropped (Filtra solo por retirados)


- between (filtra por fecha)
