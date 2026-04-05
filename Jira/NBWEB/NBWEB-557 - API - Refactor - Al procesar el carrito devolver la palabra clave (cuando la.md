---
jira_key: "NBWEB-557"
aliases: ["NBWEB-557"]
summary: "API - Refactor - Al procesar el carrito devolver la palabra clave (cuando la tenga)"
status: "Code Review"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-07-14 16:49"
updated: "2023-07-17 09:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-557"
---

# NBWEB-557: API - Refactor - Al procesar el carrito devolver la palabra clave (cuando la tenga)

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-14 16:49 |
| Actualizado | 2023-07-17 09:17 |
| Etiquetas | ninguna |
| Jira | [NBWEB-557](https://bluinc.atlassian.net/browse/NBWEB-557) |

## Relaciones

- **Padre:** [[NBWEB-50]] Sitio Web
- **blocks:** [[SNB-984]] PALABRA CLAVE

## Descripcion

Modificaremos el recurso

```
{API_URL}/v1/miCuenta/ordenesDeCompra
```

para devolver dentro de cada pedido la palabra clave (en caso de que la tenga), de esta forma es lo primero que ve en la pantalla da aterrizaje sea lo primero que el comprador vea, y sepa donde ir a buscarla
