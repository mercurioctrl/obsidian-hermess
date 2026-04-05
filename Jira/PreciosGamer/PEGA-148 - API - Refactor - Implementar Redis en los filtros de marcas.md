---
jira_key: "PEGA-148"
aliases: ["PEGA-148"]
summary: "API - Refactor - Implementar Redis en los filtros de marcas"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-20 06:57"
updated: "2024-11-25 00:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-148"
---

# PEGA-148: API - Refactor - Implementar Redis en los filtros de marcas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-20 06:57 |
| Actualizado | 2024-11-25 00:49 |
| Etiquetas | ninguna |
| Jira | [PEGA-148](https://bluinc.atlassian.net/browse/PEGA-148) |

## Relaciones

- **Padre:** [[PEGA-2]] Catalogos y Buscador

## Descripcion

Incorporaremos consultas a Redis para el recurso

```
GET {API_URL}/v1/brands?order={order}&search={search}&rate={rate}
```
