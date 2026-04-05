---
jira_key: "POS-99"
summary: "APP - Feat - Pestaña estadística por categorías "
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-09-08 09:04"
updated: "2023-03-07 09:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-99"
---

# POS-99: APP - Feat - Pestaña estadística por categorías 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-08 09:04 |
| Actualizado | 2023-03-07 09:08 |
| Etiquetas | ninguna |
| Jira | [POS-99](https://bluinc.atlassian.net/browse/POS-99) |

## Descripción

Tener en cuenta: Se debe mostrar por cada gráfico la mayor informacion posible, dentro de lo que el gráfico permite. Elegir el gráfico mas adecuado para cada caso (Cualquier duda la vemos).

Los distintos gráficos que se deben lograr están descritos en la tareas dentro de esta historia.

La informacion se puede obtener del recurso

```
GET {API_URL}/v1/metrics/categories/
```



**Filtros: **

Deben aplicarse filtros que te permitan aplicar cruces por marca. 

Y de ser posible matchear por string en el nombre de producto.
