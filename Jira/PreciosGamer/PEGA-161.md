---
jira_key: "PEGA-161"
summary: "Almacenar informacion sobre las búsquedas"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-01-02 10:04"
updated: "2025-01-27 17:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-161"
---

# PEGA-161: Almacenar informacion sobre las búsquedas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-02 10:04 |
| Actualizado | 2025-01-27 17:34 |
| Etiquetas | ninguna |
| Jira | [PEGA-161](https://bluinc.atlassian.net/browse/PEGA-161) |

## Descripción

```
GET {API_URL}/v1/items?search=amd
```

Agregaremos una funcionalidad que al realizar una búsqueda, almacene la misma con fines estadísticos y operativos.

En principio agregaremos la tabla `PEGA.dbo.search_queries`

- id


- keywords (cadena buscada)


- date (fecha de la búsqueda)


- count (cantidad de resultados devueltos)
