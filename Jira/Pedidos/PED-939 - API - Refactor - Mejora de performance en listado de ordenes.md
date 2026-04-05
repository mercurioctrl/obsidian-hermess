---
jira_key: "PED-939"
aliases: ["PED-939"]
summary: "API - Refactor - Mejora de performance en listado de ordenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-01-29 13:37"
updated: "2025-01-31 10:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-939"
---

# PED-939: API - Refactor - Mejora de performance en listado de ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-01-29 13:37 |
| Actualizado | 2025-01-31 10:51 |
| Etiquetas | ninguna |
| Jira | [PED-939](https://bluinc.atlassian.net/browse/PED-939) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra

## Descripcion

Se debe mejorar la performance del recurso /orders

```
GET orders?currentPage=1&itemsPerPage=15&between=30-12-2024_29-01-2025&companyCode=4
```

Actualmente tarda mas de +7s.

Se debe lograr bajar este tiempo. a el estimado de ~2s.
