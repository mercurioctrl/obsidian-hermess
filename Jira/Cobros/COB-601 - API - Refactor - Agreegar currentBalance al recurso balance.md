---
jira_key: "COB-601"
aliases: ["COB-601"]
summary: "API - Refactor - Agreegar currentBalance al recurso balance"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-12-29 11:49"
updated: "2026-01-09 13:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-601"
---

# COB-601: API - Refactor - Agreegar currentBalance al recurso balance

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-29 11:49 |
| Actualizado | 2026-01-09 13:59 |
| Etiquetas | ninguna |
| Jira | [COB-601](https://bluinc.atlassian.net/browse/COB-601) |

## Relaciones

- **Padre:** [[COB-573]] Clientes

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
