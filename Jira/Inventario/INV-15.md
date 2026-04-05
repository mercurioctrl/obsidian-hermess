---
jira_key: "INV-15"
summary: "API - Listar Marcas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-07 16:01"
updated: "2022-06-09 14:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-15"
---

# INV-15: API - Listar Marcas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-07 16:01 |
| Actualizado | 2022-06-09 14:48 |
| Etiquetas | ninguna |
| Jira | [INV-15](https://bluinc.atlassian.net/browse/INV-15) |

## Descripción

Se trata del recurso necesario para listar las marcas en el backoffice

```
{{API_URL}}/v1/brands
```

Retorna:



```json
[
    {
        "description": "ACER",
        "id": "42",
        "imagen": "https://static.nb.com.ar/img/70b0907f583faae03680196d9bf42d42.jpg"
    },
    {
        "description": "ADATA",
        "id": "91",
        "imagen": "http://static.nb.com.ar/img/d411bd521b946ee7702e2b87578957e2.jpg"
    },
    {
        "description": "AIWA                                              ",
        "id": "45",
        "imagen": "https://static.nb.com.ar/img/751db53936d6c61e646c4acf214d2cc7.jpg"
    },
    ]
```
