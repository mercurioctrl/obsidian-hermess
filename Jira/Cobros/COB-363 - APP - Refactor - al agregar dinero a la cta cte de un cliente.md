---
jira_key: "COB-363"
aliases: ["COB-363"]
summary: "APP - Refactor - al agregar dinero a la cta cte de un cliente"
status: "CodeReview"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2023-03-15 11:09"
updated: "2023-03-15 11:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-363"
---

# COB-363: APP - Refactor - al agregar dinero a la cta cte de un cliente

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2023-03-15 11:09 |
| Actualizado | 2023-03-15 11:13 |
| Etiquetas | ninguna |
| Jira | [COB-363](https://bluinc.atlassian.net/browse/COB-363) |

## Relaciones

- **is blocked by:** [[COB-362]] API - Refactor - Cuando el pago se hace en pesos, debe mostrar el saldo en pesos en el comprobante y el tipo de cambio

## Descripcion

Se cambia en el response 

```
ctaCteId
```

 por 

```
id
```

 para mostrar el comprobante en pesos
