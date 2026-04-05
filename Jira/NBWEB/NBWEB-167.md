---
jira_key: "NBWEB-167"
summary: "API CMS - Editar Cateogories"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-03 09:35"
updated: "2022-07-21 10:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-167"
---

# NBWEB-167: API CMS - Editar Cateogories

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-03 09:35 |
| Actualizado | 2022-07-21 10:43 |
| Etiquetas | ninguna |
| Jira | [NBWEB-167](https://bluinc.atlassian.net/browse/NBWEB-167) |

## Descripción

Edicion de cateogorias

Todos los recursos de CMA estan detras de un token del CMS, no mezclar con el de usuarios del sitio.

```
POST {{API_URL}}/v1/cms/Categories
```

Request

```json

    {
        "description": "Procesadores",
        "id": "42",
        "show": 1,
        "initialB": 3,
        "initialc": 4
    }
    
```
