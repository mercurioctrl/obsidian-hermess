---
jira_key: "COB-595"
aliases: ["COB-595"]
summary: "API - Refactor - Orden de el estado de balance"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-12-26 07:00"
updated: "2026-01-05 14:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-595"
---

# COB-595: API - Refactor - Orden de el estado de balance

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-26 07:00 |
| Actualizado | 2026-01-05 14:38 |
| Etiquetas | ninguna |
| Jira | [COB-595](https://bluinc.atlassian.net/browse/COB-595) |

## Relaciones

- **Padre:** [[COB-573]] Clientes
- **has action item:** [[COB-596]] APP - Refactor - Orden del estado de balance 

## Descripcion

Al utilizar el filtro `balanceState` se debe también poder ordenar este criterio en orden ascendente y descendente

```
GET {API_URL}/v1/clients?balanceState=debt
```

Para esto utilizaremos el parametro `balanceStateOrder={asc/desc}`

Cuando no esta definido tomaremos el siguiente criterio

Si `balanceState=debt` el balance es ascendente por defecto a menos que lo cambie

Si `balanceState=credit`entonces el balance es descendente por defecto a menos que lo cambie

Si `balanceState=none`entonces el orden ser ascendente por defecto a menos que lo cambie
