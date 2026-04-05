---
jira_key: "PED-1206"
aliases: ["PED-1206"]
summary: "API - Refactor - Agreegar currentBalance al recurso balance"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-12-29 15:18"
updated: "2026-01-14 06:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1206"
---

# PED-1206: API - Refactor - Agreegar currentBalance al recurso balance

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-12-29 15:18 |
| Actualizado | 2026-01-14 06:55 |
| Etiquetas | ninguna |
| Jira | [PED-1206](https://bluinc.atlassian.net/browse/PED-1206) |

## Relaciones

- **Padre:** [[PED-54]] Cuenta corriente de clientes
- **action item from:** [[PED-1205]] APP - Refactor - Replicar como en Cobros -  agregar columna balance en la pestaña de clientes y en la cta cte de clientes y en disponible usar usedBalanceAmount
- **has action item:** [[PED-1254]] API - Review - Recurso balance  -> usedCheckBalanceAmount o deuda, debe venir  negativo cuando es menor a cero

## Descripcion

```
GET {API_URL}/v1/balances/92236
```

Vamos a agregar `currentBalance` al recurso

De la siguiente forma

```
{
    "limitBalanceAmount": 100000,
    "limitCheckBalanceAmount": 0,
    "usedCheckBalanceAmount": 0,
    "usedBalanceAmount": -473193.50,
    "currentBalance": -573.193.50
}
```
