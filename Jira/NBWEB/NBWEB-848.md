---
jira_key: "NBWEB-848"
summary: "API - Refactor - Agregar EAN y UPC al detalle del item"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-26 16:13"
updated: "2024-08-27 04:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-848"
---

# NBWEB-848: API - Refactor - Agregar EAN y UPC al detalle del item

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-26 16:13 |
| Actualizado | 2024-08-27 04:16 |
| Etiquetas | ninguna |
| Jira | [NBWEB-848](https://bluinc.atlassian.net/browse/NBWEB-848) |

## Descripción

```
GET {API_URL}/v1/item/{itemId}
```

```
{
...
"ean": "840272903049"
"upc": "879862008260"
...
}
```
