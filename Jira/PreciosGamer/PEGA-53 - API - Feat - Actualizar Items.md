---
jira_key: "PEGA-53"
aliases: ["PEGA-53"]
summary: "API - Feat - Actualizar Items"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-01-03 13:21"
updated: "2023-01-04 11:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-53"
---

# PEGA-53: API - Feat - Actualizar Items

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-03 13:21 |
| Actualizado | 2023-01-04 11:43 |
| Etiquetas | ninguna |
| Jira | [PEGA-53](https://bluinc.atlassian.net/browse/PEGA-53) |

## Relaciones

- **Padre:** [[PEGA-50]] Feat - Update catalogos

## Descripcion

Se creara la tabla `PEGA.dbo.items`

- id


- lastRepositoryid


- resellerid


- brandid


- description


- price


- lastPrice


- destinyUrl


- defaultimgUrl


- delete


- hide


- originid



```
GET {API_URL}/v1/sync/items/{token}
```

El recurso debe insertar o actualiizar un item segun corresponda, basandose en el dataset de `PEGA.dbo.repository`

En esta tabla se guardaran uno a uno los items que sean del mismo resellar para el mismo item y debera voncular brandId y resellerid.

Es el recurso desde el cual la api leera el catalogo.

Devuelve un parametro succes para saber que se ejecuto y otro con la cantidad de marcas agregadas.

El parametro token se compara con una variable en `.env` llamado `SYNCTOKEN` que es para que cualquiera no ejecute el recurso
