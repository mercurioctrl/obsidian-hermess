---
jira_key: "NBWEB-856"
summary: "API - Create bulk mis categorias"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Ezequiel manzano"
created: "2024-08-29 15:33"
updated: "2024-09-02 11:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-856"
---

# NBWEB-856: API - Create bulk mis categorias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Ezequiel manzano |
| Creado | 2024-08-29 15:33 |
| Actualizado | 2024-09-02 11:29 |
| Etiquetas | ninguna |
| Jira | [NBWEB-856](https://bluinc.atlassian.net/browse/NBWEB-856) |

## Descripción

{{API_URL}}/v1/miCuenta/misCategorias/bulk

Body

```
{
    "utility": 2.5,
    "hide": false
}
```

Se deben crear mis categorias para todas las categorias activas, y no se debe pisar una categoria propia ya creada
