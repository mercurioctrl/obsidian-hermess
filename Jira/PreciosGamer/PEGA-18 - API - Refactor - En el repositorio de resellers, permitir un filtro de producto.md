---
jira_key: "PEGA-18"
aliases: ["PEGA-18"]
summary: "API - Refactor - En el repositorio de resellers, permitir un filtro de producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-15 17:20"
updated: "2024-05-06 16:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-18"
---

# PEGA-18: API - Refactor - En el repositorio de resellers, permitir un filtro de producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-15 17:20 |
| Actualizado | 2024-05-06 16:25 |
| Etiquetas | ninguna |
| Jira | [PEGA-18](https://bluinc.atlassian.net/browse/PEGA-18) |

## Relaciones

- **Padre:** [[PEGA-6]] Feat - Listar productos
- **blocks:** [[PEGA-60]] APP - Refactor - En el menú vertical de la izquierda permitir un filtro por producto para poder mostrar contenido reactivo a la busqueda

## Descripcion

Esta feature en el repositorio te permite hacer la búsqueda del producto, pero dentro de una clausula in, para filtrar solo aquellas resellers que están contenidas en esta búsqueda.

Agregaremos el parámetro itemSearch de la siguiente manera

```
GET {API_URL}/v1/resellers?search={termino de busqueda para la resellers}&itemSearch={termino de busqueda para el producto}
```

Los id de resellers que debo obtener, son los que entregarian los productos listados en [link](https://lioteam.atlassian.net/browse/PEGA-14) (es el mismo recurso, pero sin la paginacion y solo seleccionando el id de resellers).

Lo que se intenta hacer es algo como lo del siguiente jemplo

```
Select nombresresellers FROM marcas WHERE idresellers IN (SELECT idresellers FROM items WHERE description LIKE {terminos de busqueda} )
```
