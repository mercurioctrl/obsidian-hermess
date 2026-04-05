---
jira_key: "INV-63"
summary: "API - Feat - Agregar filtro con stock/sin stock/todos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-04-22 09:18"
updated: "2024-04-24 17:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-63"
---

# INV-63: API - Feat - Agregar filtro con stock/sin stock/todos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-22 09:18 |
| Actualizado | 2024-04-24 17:10 |
| Etiquetas | ninguna |
| Jira | [INV-63](https://bluinc.atlassian.net/browse/INV-63) |

## Descripción

Refactorizaremos el objeto

```
{API_URL}/items
```

Para enviar un parámetro que indique stock=1/0/null

Siendo que si esta en true, devuelve solo aquellos en stock

Si esta en false, devuelve solo sin stock

Si no esta el parametro o esta nulo, entonces devuelve todos

Se define stock como la suma de

nstock+nstock_lo+nstock_d1
