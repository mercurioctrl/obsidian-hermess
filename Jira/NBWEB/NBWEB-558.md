---
jira_key: "NBWEB-558"
summary: "APP - Refactor - Al procesar el carrito devolver la palabra clave (cuando la tenga)"
status: "Code Review"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-07-14 16:55"
updated: "2023-07-17 10:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-558"
---

# NBWEB-558: APP - Refactor - Al procesar el carrito devolver la palabra clave (cuando la tenga)

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-14 16:55 |
| Actualizado | 2023-07-17 10:19 |
| Etiquetas | ninguna |
| Jira | [NBWEB-558](https://bluinc.atlassian.net/browse/NBWEB-558) |

## Descripción

Modificaremos el recurso

```
{API_URL}/v1/miCuenta/ordenesDeCompra
```

para devolver dentro de cada pedido la palabra clave (en caso de que la tenga), de esta forma es lo primero que ve en la pantalla da aterrizaje sea lo primero que el comprador vea, y sepa donde ir a buscarla. Por eso la agregaremos junto al usuario, pero de la forma mas resaltada posible, dentro de los estilos que venimos utilizando.

[attachment]
