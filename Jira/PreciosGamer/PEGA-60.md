---
jira_key: "PEGA-60"
summary: "APP - Refactor - En el menú vertical de la izquierda permitir un filtro por producto para poder mostrar contenido reactivo a la busqueda"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-02-06 09:44"
updated: "2024-05-07 16:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-60"
---

# PEGA-60: APP - Refactor - En el menú vertical de la izquierda permitir un filtro por producto para poder mostrar contenido reactivo a la busqueda

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-02-06 09:44 |
| Actualizado | 2024-05-07 16:03 |
| Etiquetas | ninguna |
| Jira | [PEGA-60](https://bluinc.atlassian.net/browse/PEGA-60) |

## Descripción

El objetivo es poder mostrar solo aquellas marcas que están incluidas en la búsqueda por producto que estoy haciendo.

Esta feature en el repositorio te permite hacer la búsqueda del producto, pero dentro de una clausula in, para filtrar solo aquellas marcas que están contenidas en esta búsqueda.

Agregaremos el parámetro itemSearch de la siguiente manera

```
GET {API_URL}/v1/brands?search={termino de busqueda para la marca}&itemSearch={termino de busqueda para el producto}
```

```
GET {API_URL}/v1/resellers?search={termino de busqueda para la marca}&itemSearch={termino de busqueda para el producto}
```

Los id de marca que debo obtener, son los que entregarían los productos listados en [link](https://lioteam.atlassian.net/browse/PEGA-14) (es el mismo recurso, pero sin la paginacion y solo seleccionando el id de marca).

Se utiliza el recurso de [link](https://lioteam.atlassian.net/browse/PEGA-59)
