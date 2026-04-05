---
jira_key: "COB-594"
aliases: ["COB-594"]
summary: "API - Refactor - En el filtro de balance de libre opcion se debe tomar el cero con decimales como un cero entero y agregaremos un nuevo parámetro llamado currentBalance que es el ultimo saldo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-12-26 06:51"
updated: "2026-01-05 14:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-594"
---

# COB-594: API - Refactor - En el filtro de balance de libre opcion se debe tomar el cero con decimales como un cero entero y agregaremos un nuevo parámetro llamado currentBalance que es el ultimo saldo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-26 06:51 |
| Actualizado | 2026-01-05 14:31 |
| Etiquetas | ninguna |
| Jira | [COB-594](https://bluinc.atlassian.net/browse/COB-594) |

## Relaciones

- **Padre:** [[COB-573]] Clientes
- **has action item:** [[COB-597]] APP - Refactor - Agregaremos el nuevo parametro de balance a la tabla para que se visualice primero

## Descripcion

Cuando filtramos con el parámetro

```
GET {API_URL}/v1/clients?balanceState=debt
```

Aparecen varios casos que están en cero. Como hemos realizado alguna vez, sería una mejora que el balance se estime en base a su parte entera. 

Es decir que aquellos balances neutros sean los que su parte entera es cero ( independientemente de que sea cero coma algo).

Esta forma es mucho mas util para visualizar el dato que queremos ver.

Por otro lado al realizar estas pruebas se encontraron algunos casos donde al filtrar `balanceState=debt` eran positivos, cuando no deberia ser de esta forma (ver imagen) 

[adjunto]
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
