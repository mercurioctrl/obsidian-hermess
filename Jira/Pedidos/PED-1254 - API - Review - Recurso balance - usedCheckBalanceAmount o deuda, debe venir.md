---
jira_key: "PED-1254"
aliases: ["PED-1254"]
summary: "API - Review - Recurso balance  -> usedCheckBalanceAmount o deuda, debe venir  negativo cuando es menor a cero"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-14 06:55"
updated: "2026-01-15 10:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1254"
---

# PED-1254: API - Review - Recurso balance  -> usedCheckBalanceAmount o deuda, debe venir  negativo cuando es menor a cero

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-14 06:55 |
| Actualizado | 2026-01-15 10:19 |
| Etiquetas | ninguna |
| Jira | [PED-1254](https://bluinc.atlassian.net/browse/PED-1254) |

## Relaciones

- **Padre:** [[PED-54]] Cuenta corriente de clientes
- **action item from:** [[PED-1206]] API - Refactor - Agreegar currentBalance al recurso balance

## Descripcion

Haciendo una revisión ya usando base de producción con  [https://pedidos2.saftel.com/](https://pedidos2.saftel.com/) y  [https://api2.orders.lio.red](https://api2.orders.lio.red) pude visualizar una pequeña diferencia minima sobre el parametro `usedCheckBalanceAmount` que actualmente se utiliza como un campo negativo.

Esto se puede ver con base de datos de producción para un caso especifico de ejemplo:

```
https://api.orders.lio.red/v1/balances/10073
```

```
{
    "limitBalanceAmount": 0,
    "limitCheckBalanceAmount": 10500000,
    "usedCheckBalanceAmount": -11057400.11,
    "usedBalanceAmount": 32.4935967200754
}
```

---

```
https://api2.orders.lio.red/v1/balances/10073
```

```
{
    "limitBalanceAmount": 0,
    "limitCheckBalanceAmount": 10500000,
    "usedCheckBalanceAmount": 11057400.11, <-- Este dato, cuando es deuda debe venir negativo como el ejemplo de arriba
    "usedBalanceAmount": 32.49,
    "currentBalance": 32.49
}
```
