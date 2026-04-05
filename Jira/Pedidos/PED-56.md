---
jira_key: "PED-56"
summary: "API - Feat - Mostrar totales de la cuenta del cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-07 08:57"
updated: "2023-09-12 10:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-56"
---

# PED-56: API - Feat - Mostrar totales de la cuenta del cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-07 08:57 |
| Actualizado | 2023-09-12 10:13 |
| Etiquetas | ninguna |
| Jira | [PED-56](https://bluinc.atlassian.net/browse/PED-56) |

## Descripción

Asi como lo hicimos en el sistema de caja ([link](https://lioteam.atlassian.net/browse/COB-6)  ), necesitaremos el recurso para leer cuenta corriente

```
GET /v1/balances/{clientId}
```

```json
{
    "limitCheckBalanceAmount": 0,
    "usedCheckBalanceAmount": -0,
    "limitBalanceAmount": 0,
    "usedBalanceAmount": -41.450874
}
```

Esto se pude hacer leyendo el recurso, o trayéndose el repositorio a a la nueva aplicaicon
