---
jira_key: "NBWEB-708"
summary: "API - Agregar productos al carrito - Validar stock"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-04-15 04:18"
updated: "2024-04-15 11:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-708"
---

# NBWEB-708: API - Agregar productos al carrito - Validar stock

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-15 04:18 |
| Actualizado | 2024-04-15 11:24 |
| Etiquetas | ninguna |
| Jira | [NBWEB-708](https://bluinc.atlassian.net/browse/NBWEB-708) |

## Descripción

- Resultado obtenido: 



[attachment]


- Pasos para replicar error: 



Agregar cantidad de productos mayor al que tenemos en stock.



- Datos de la prueba: 



```
[
    {
    "productId":117160,
    "amount":9999,
    "type":0
    }
]
```

[attachment]


- Resultado esperado: 



Mensaje indicando que la cantidad solicitada del producto excede nuestra disponibilidad actual y el id del producto.



- Posible solución:



Validar que contamos con la cantidad solicitada del producto para añadir al carrito.
