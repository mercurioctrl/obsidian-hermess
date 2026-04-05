---
jira_key: "COB-379"
aliases: ["COB-379"]
summary: "API - O. Mejora - Mejorar rendimiento de la consulta "
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-23 07:57"
updated: "2023-07-31 09:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-379"
---

# COB-379: API - O. Mejora - Mejorar rendimiento de la consulta 

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-23 07:57 |
| Actualizado | 2023-07-31 09:19 |
| Etiquetas | ninguna |
| Jira | [COB-379](https://bluinc.atlassian.net/browse/COB-379) |

## Relaciones

- **Padre:** [[COB-5]] API - Feat - Obtener cuenta corriente de un cliente

## Descripcion

Intentaremos mejorar esta consulta para que en producción, nos de un resultado en menos de 2,5 segundos

```
GET {API_URL}/v1/currentAccount/29531?itemsPerPage=15&currentPage=1
```
