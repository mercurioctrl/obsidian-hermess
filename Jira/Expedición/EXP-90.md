---
jira_key: "EXP-90"
summary: "API - Feat - Contar producto"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-22 10:10"
updated: "2022-12-14 10:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-90"
---

# EXP-90: API - Feat - Contar producto

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-22 10:10 |
| Actualizado | 2022-12-14 10:27 |
| Etiquetas | ninguna |
| Jira | [EXP-90](https://bluinc.atlassian.net/browse/EXP-90) |

## Descripción

Se debe contabilizar el producto y registrar fechas y estados de los distintos stocks al momento del conteo

```
PATCH {API_URL}/v1/items
```

```
[
{
"Id":"104964",
"counted":25
},
{
"Id":"104965",
"counted":26
}
]
```
