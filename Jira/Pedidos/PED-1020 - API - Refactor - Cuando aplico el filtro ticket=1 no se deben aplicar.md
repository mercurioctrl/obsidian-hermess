---
jira_key: "PED-1020"
aliases: ["PED-1020"]
summary: "API - Refactor - Cuando aplico el filtro ticket=1 no se deben aplicar intervalos de fecha"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-13 08:54"
updated: "2025-06-30 10:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1020"
---

# PED-1020: API - Refactor - Cuando aplico el filtro ticket=1 no se deben aplicar intervalos de fecha

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-13 08:54 |
| Actualizado | 2025-06-30 10:48 |
| Etiquetas | ninguna |
| Jira | [PED-1020](https://bluinc.atlassian.net/browse/PED-1020) |

## Relaciones

- **Padre:** [[PED-960]] Tickets de pedido
- **has action item:** [[SNB-3151]] FILTRO DE TICKET

## Descripcion

Al aplicar el filtro de ticket `ticket=1` no debo aplicar filtro de fecha, para poder verlos todos, si lo saco o recibo `ticket=0` las fechas se setean normalmente

```
GET {API_URL}/v1/orders?currentPage=1&itemsPerPage=15&between=29-05-2024_13-06-2025&ticket=1
```
