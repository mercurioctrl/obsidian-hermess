---
jira_key: "PEGA-147"
summary: "API - Refactor - Implementar Redis en los filtros de vendedores"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-20 06:52"
updated: "2024-11-25 00:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-147"
---

# PEGA-147: API - Refactor - Implementar Redis en los filtros de vendedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-20 06:52 |
| Actualizado | 2024-11-25 00:46 |
| Etiquetas | ninguna |
| Jira | [PEGA-147](https://bluinc.atlassian.net/browse/PEGA-147) |

## Descripción

Incorporaremos consultas a Redis para el recurso

```
GET {API_URL}/v1/resellers?order={order}&search={search}&rate={rate}
```
