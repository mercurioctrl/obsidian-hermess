---
jira_key: "NBWEB-42"
aliases: ["NBWEB-42"]
summary: "Eliminar Carrito de compras"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-21 09:36"
updated: "2022-03-28 12:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-42"
---

# NBWEB-42: Eliminar Carrito de compras

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-21 09:36 |
| Actualizado | 2022-03-28 12:37 |
| Etiquetas | ninguna |
| Jira | [NBWEB-42](https://bluinc.atlassian.net/browse/NBWEB-42) |

## Relaciones

- **Padre:** [[NBWEB-1 - API - Carrito de compras|NBWEB-1]] API - Carrito de compras

## Descripcion

```
DELETE {{API_URL}}/v1/carrito/{id_carrito_por_el_que_eliminar}
```



Se marca como cerrado usando la columna `[NB_WEB].[dbo].[carritos].cerrado`

Si tengo algún otro carrito disponible para mi usuario, entonces selecciono el ultimo. Sino debo crear uno nuevo y seleccionarlo utilizando los métodos de cambiar carrito.
