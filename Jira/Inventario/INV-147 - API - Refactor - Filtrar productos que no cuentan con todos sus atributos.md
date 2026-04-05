---
jira_key: "INV-147"
aliases: ["INV-147"]
summary: "API - Refactor - Filtrar productos que no cuentan con todos sus atributos obligatorios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-10-04 07:28"
updated: "2025-01-20 13:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-147"
---

# INV-147: API - Refactor - Filtrar productos que no cuentan con todos sus atributos obligatorios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-04 07:28 |
| Actualizado | 2025-01-20 13:53 |
| Etiquetas | ninguna |
| Jira | [INV-147](https://bluinc.atlassian.net/browse/INV-147) |

## Relaciones

- **Padre:** [[INV-27]] Productos
- **action item from:** [[LIO-103]] API - DATA - Refactor -> Mover la tabla componentsAttributes a la bd PRODUCTOS
- **has action item:** [[INV-175]] APP - Feat - Agregar filtro para ver items que aun tienen atributos obligatorios sin satisfacer 

## Descripcion

Agregaremos el filtro `hasIncompleteAttr` para poder filtrar aquellos productos que tienen los atributos

```
GET {API_URL}/items?currentPage=1&itemsPerPage=300&hasAttributes=1
```

`hasAttributes`

Lo que haremos entonces es evaluar nuestra tabla `PRODUCTOS.dbo.componentsAttributes` respecto a los atributos del item en `[PRODUCTOS].[dbo].[etiquetas]` y si no estan completos, osea no tiene un valor para cada uno de los que son obligatorios para la categoria a la que pertenece el producto los mostraremos.

Si `hasIncompleteAttr=0` Mostraremos los completos

`hasIncompleteAttr=null` Mostraremos todos

Como puede ser un poco rebuscado y retrasar las búsquedas quizás tambien podemos parametrizar el estado  `hasIncompleteAttr` para definirlo en una accion concreta o en un syncUp. Eso decime vos que te parece.
