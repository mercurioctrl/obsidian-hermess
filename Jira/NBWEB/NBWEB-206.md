---
jira_key: "NBWEB-206"
summary: "API - Leer mensajes de un meesageChannel"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-26 11:25"
updated: "2022-06-26 21:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-206"
---

# NBWEB-206: API - Leer mensajes de un meesageChannel

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-26 11:25 |
| Actualizado | 2022-06-26 21:29 |
| Etiquetas | ninguna |
| Jira | [NBWEB-206](https://bluinc.atlassian.net/browse/NBWEB-206) |

## Descripción

```
GET {{API_URL}}/v1/postventa/{postsaleInboundId}/messageChannel/{token}
```

Devuelve un array con todos los objetos para cada issue, ordenados cronológicamente
