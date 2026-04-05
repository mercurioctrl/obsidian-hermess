---
jira_key: "PEGA-165"
aliases: ["PEGA-165"]
summary: "API - Refactor - Nuevo parámetro para filtrar limite de días desde la ultima modificación de precio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-01-07 10:12"
updated: "2025-01-27 17:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-165"
---

# PEGA-165: API - Refactor - Nuevo parámetro para filtrar limite de días desde la ultima modificación de precio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-07 10:12 |
| Actualizado | 2025-01-27 17:32 |
| Etiquetas | ninguna |
| Jira | [PEGA-165](https://bluinc.atlassian.net/browse/PEGA-165) |

## Relaciones

- **Padre:** [[PEGA-6 - Feat - Listar productos|PEGA-6]] Feat - Listar productos
- **action item from:** [[PEGA-164 - API - Refactor - Modificar SyncUp para guardar la fecha del ultimo cambio de|PEGA-164]] API - Refactor - Modificar SyncUp para guardar la fecha del ultimo cambio de precios
- **has action item:** [[PEGA-167 - APP - Refactor - Agregar fecha de cambio en los repositorios de baja de precio|PEGA-167]] APP - Refactor - Agregar "fecha de cambio" en los repositorios de baja de precio de la home

## Descripcion

Crearemos un parametro para poder filtrar “aquellos que tienen un máximo de `{dias}` desde el cambio

```
GET {API_URL}/v1/items?rate=up&search=&order=asc_price&offset=0&changedate={dias}
```
