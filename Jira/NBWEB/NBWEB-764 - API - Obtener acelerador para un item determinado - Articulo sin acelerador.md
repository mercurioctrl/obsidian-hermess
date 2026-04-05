---
jira_key: "NBWEB-764"
aliases: ["NBWEB-764"]
summary: "API - Obtener acelerador para un item determinado - Articulo sin acelerador "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-07-03 13:23"
updated: "2024-07-05 11:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-764"
---

# NBWEB-764: API - Obtener acelerador para un item determinado - Articulo sin acelerador 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-07-03 13:23 |
| Actualizado | 2024-07-05 11:12 |
| Etiquetas | ninguna |
| Jira | [NBWEB-764](https://bluinc.atlassian.net/browse/NBWEB-764) |

## Relaciones

- **Padre:** [[NBWEB-602 - Sitio Web|NBWEB-602]] Sitio Web
- **relates to:** [[NBWEB-762 - API - Feat - Obtener acelerador para un item determinado|NBWEB-762]] API - Feat - Obtener acelerador para un item determinado

## Descripcion

Al buscar por el articulo `5199` no aparece su acelerador coincidente.

[https://gamma.nb.com.ar/outlet-amd-athlon-5150-1-6-ghbox_-_5199](https://gamma.nb.com.ar/outlet-amd-athlon-5150-1-6-ghbox_-_5199)


```
GET {API_URL}/v1/item/{itemId}/acelerator
```

[adjunto]
[adjunto]
