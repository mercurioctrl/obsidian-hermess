---
jira_key: "COB-597"
aliases: ["COB-597"]
summary: "APP - Refactor - Agregaremos el nuevo parametro de balance a la tabla para que se visualice primero"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-26 17:09"
updated: "2026-01-09 13:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-597"
---

# COB-597: APP - Refactor - Agregaremos el nuevo parametro de balance a la tabla para que se visualice primero

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-26 17:09 |
| Actualizado | 2026-01-09 13:50 |
| Etiquetas | ninguna |
| Jira | [COB-597](https://bluinc.atlassian.net/browse/COB-597) |

## Relaciones

- **Padre:** [[COB-573]] Clientes
- **action item from:** [[COB-594]] API - Refactor - En el filtro de balance de libre opcion se debe tomar el cero con decimales como un cero entero y agregaremos un nuevo parámetro llamado currentBalance que es el ultimo saldo

## Descripcion

Debemos agregar una nueva columna llamada "balance” para visualizar el nuevo parametro que viene con el refactor [link](https://bluinc.atlassian.net/browse/COB-594) 

## Nuevo parámetro

```
{
    "response": [
    ...
        {
            "clientId": 94806,
            "clientName": "SUCHUR JUAN AGUSTIN",
            "clientBusinessName": "SUCHUR JUAN AGUSTIN",
            "clientTaxNumber": "20409813136",
            "clientPerception": 0,
            "limitCheckBalanceAmount": 0,
            "usedCheckBalanceAmount": 2776000,
            "limitBalanceAmount": 2000,
            "usedBalanceAmount": 1933.33,
            "usedBalanceAmount": 1933.33,
            "currentBalance": -66.67019999999991, <--- SE AGREGA
            "desactive": false,
            "salespersonName": "Ariel Accme",
            "sellerId": 69,
            "companyCode": 9,
            "clientLo": null
        }
    ],
    "pagination": {
        "total": 3141,
        "current": 1,
        "pageSize": 15
    }
}
```



[adjunto]
