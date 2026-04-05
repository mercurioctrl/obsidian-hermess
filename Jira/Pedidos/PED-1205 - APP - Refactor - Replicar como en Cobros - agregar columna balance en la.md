---
jira_key: "PED-1205"
aliases: ["PED-1205"]
summary: "APP - Refactor - Replicar como en Cobros -  agregar columna balance en la pestaña de clientes y en la cta cte de clientes y en disponible usar usedBalanceAmount"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2025-12-29 12:52"
updated: "2026-01-09 14:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1205"
---

# PED-1205: APP - Refactor - Replicar como en Cobros -  agregar columna balance en la pestaña de clientes y en la cta cte de clientes y en disponible usar usedBalanceAmount

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2025-12-29 12:52 |
| Actualizado | 2026-01-09 14:00 |
| Etiquetas | ninguna |
| Jira | [PED-1205](https://bluinc.atlassian.net/browse/PED-1205) |

## Relaciones

- **Padre:** [[PED-54]] Cuenta corriente de clientes
- **has action item:** [[PED-1206]] API - Refactor - Agreegar currentBalance al recurso balance

## Descripcion

En el modal de la cuenta corriente de un cliente se debe agregar

```
GET {API_URL}/v1/balances/92236
```



```
{
    "limitBalanceAmount": 100000,
    "limitCheckBalanceAmount": 0,
    "usedCheckBalanceAmount": 0,
    "usedBalanceAmount": -473193.50,
    "currentBalance": -573.193.50 ---> nuevo parametro para el balance
}
```

asi como tambien en la pestaña de clientes ej:
[link](https://bluinc.atlassian.net/browse/COB-597)
