---
jira_key: "PED-1073"
aliases: ["PED-1073"]
summary: "API - Refactor - Que aparezcan en el ranking interno (como en el de la landing) los que aun no tienen compras pero estan en los grupos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-01 09:23"
updated: "2025-08-08 10:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1073"
---

# PED-1073: API - Refactor - Que aparezcan en el ranking interno (como en el de la landing) los que aun no tienen compras pero estan en los grupos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-01 09:23 |
| Actualizado | 2025-08-08 10:49 |
| Etiquetas | ninguna |
| Jira | [PED-1073](https://bluinc.atlassian.net/browse/PED-1073) |

## Relaciones

- **Padre:** [[PED-753 - Incentivos Clientes|PED-753]] Incentivos Clientes

## Descripcion

La idea es hacer lo mismo que en de la landing, donde los que aun no sumaron puntas

```
GET {API_URL}/v1/clientsObjectives/acelerateRanking
```

[adjunto]
