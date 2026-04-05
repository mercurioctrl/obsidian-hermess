---
jira_key: "PEGA-165"
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

## Descripción

Crearemos un parametro para poder filtrar “aquellos que tienen un máximo de `{dias}` desde el cambio

```
GET {API_URL}/v1/items?rate=up&search=&order=asc_price&offset=0&changedate={dias}
```
