---
jira_key: "NBWEB-753"
summary: "API - Catálogos de productos - Sugerencia de mejora al filtrar por categoría errónea"
status: "Finalizada"
type: "Subtarea"
priority: "Lowest"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-06-19 15:46"
updated: "2024-06-26 01:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-753"
---

# NBWEB-753: API - Catálogos de productos - Sugerencia de mejora al filtrar por categoría errónea

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Lowest |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-19 15:46 |
| Actualizado | 2024-06-26 01:55 |
| Etiquetas | ninguna |
| Jira | [NBWEB-753](https://bluinc.atlassian.net/browse/NBWEB-753) |

## Descripción

Al filtrar desde el sitio web por la categoría `camaras-fotos-digitales` devuelve una cantidad grande de datos, lo que provoca que se trabe el sitio web y se termine la memoria del explorador. 

Para evitar esto se propone que realicemos las validaciones necesarias para evitar la advertencia por variables indefinidas.

```
GET {{API_URL}}/v1/category/camaras-fotos-digitales
```

[attachment]
[attachment]
