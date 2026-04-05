---
jira_key: "COB-463"
aliases: ["COB-463"]
summary: "API - Feat - Listar retenciones de ganancias"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-07-17 07:01"
updated: "2023-07-17 11:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-463"
---

# COB-463: API - Feat - Listar retenciones de ganancias

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-17 07:01 |
| Actualizado | 2023-07-17 11:11 |
| Etiquetas | ninguna |
| Jira | [COB-463](https://bluinc.atlassian.net/browse/COB-463) |

## Relaciones

- **Padre:** [[COB-462]] Feat - Retencion de ganancias

## Descripcion

Crearemos un recurso similar a [link](https://lioteam.atlassian.net/browse/COB-296) Para mostrar las retenciones de ganancias

```
{API_URL}/v1/profitRetention
```

Con los parámetros que vimos en el archivo que nos paso Dario.

Este recurso se llamara desde la misma pestaña de ganancias, pero usando un filtro para el tipo de ganancia que quiero ver.

En este caso el filtro funcionara escogiendo el recurso que debo utilizar y no filtrando el mismo recurso.
