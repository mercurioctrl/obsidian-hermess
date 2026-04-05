---
jira_key: "PEGA-59"
aliases: ["PEGA-59"]
summary: "API - Refactor - En el repositorio de marcas, permitir un filtro por producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-02-06 09:33"
updated: "2024-05-06 20:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-59"
---

# PEGA-59: API - Refactor - En el repositorio de marcas, permitir un filtro por producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-02-06 09:33 |
| Actualizado | 2024-05-06 20:23 |
| Etiquetas | ninguna |
| Jira | [PEGA-59](https://bluinc.atlassian.net/browse/PEGA-59) |

## Relaciones

- **Padre:** [[PEGA-6]] Feat - Listar productos
- **blocks:** [[PEGA-60]] APP - Refactor - En el menú vertical de la izquierda permitir un filtro por producto para poder mostrar contenido reactivo a la busqueda

## Descripcion

Esta feature en el repositorio te permite hacer la búsqueda del producto, pero dentro de una clausula in, para filtrar solo aquellas marcas que están contenidas en esta búsqueda.

Agregaremos el parámetro itemSearch de la siguiente manera

```
GET {API_URL}/v1/brands?search={termino de busqueda para la marca}&itemSearch={termino de busqueda para el producto}
```

Los id de marca que debo obtener, son los que entregarian los productos listados en [link](https://lioteam.atlassian.net/browse/PEGA-14) (es el mismo recurso, pero sin la paginacion y solo seleccionando el id de marca).

Lo que se intenta hacer es algo como lo del siguiente jemplo

```
Select nombresMarcas FROM marcas WHERE idMarca IN (SELECT idMarca FROM items WHERE description LIKE {terminos de busqueda} )
```
