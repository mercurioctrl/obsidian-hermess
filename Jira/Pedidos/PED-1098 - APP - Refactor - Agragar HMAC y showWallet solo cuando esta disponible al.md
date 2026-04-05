---
jira_key: "PED-1098"
aliases: ["PED-1098"]
summary: "APP - Refactor - Agragar HMAC y showWallet solo cuando esta disponible al objeto de cuenta corriente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-10 12:37"
updated: "2025-09-18 01:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1098"
---

# PED-1098: APP - Refactor - Agragar HMAC y showWallet solo cuando esta disponible al objeto de cuenta corriente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-10 12:37 |
| Actualizado | 2025-09-18 01:35 |
| Etiquetas | ninguna |
| Jira | [PED-1098](https://bluinc.atlassian.net/browse/PED-1098) |

## Relaciones

- **Padre:** [[PED-54 - Cuenta corriente de clientes|PED-54]] Cuenta corriente de clientes
- **has action item:** [[PED-1097 - APP - Feat - Hacer reembolso a la wallet a parir de una devolución en cuenta|PED-1097]] APP - Feat - Hacer reembolso a la wallet a parir de una devolución en cuenta corriente

## Descripcion

```
GET {API_URL}/v1/currentAccount/{clientId}?itemsPerPage=15&currentPage=1
```

```
{
    "response": [
        {
            "date": "2025-09-03",
            "albNumber": "00630489",
            "total": -156.317195,
            "currencyQuote": 1375,
            "agent": "",
            "agentDescription": "",
            "branch": "0002",
            "comment": "Complejo de 3 pisos, tocar timbre 1B",
            "currentBalance": 7.017365999999882,
            "currencyQuoteDay": 1435,
            "currencyQuoteDayCheck": 1435,
            "subTotal": -156.31719500000008,
            "totalPesos": -214936.143125,
            "id": 924267,
            "notFiscalId": null,
            "voucherId": 586873,
            "token": "6bed21f8afbd453412d4847241513c",
            "availableBalance": 7.017365999999882,
            "dollarQuote": null,
            "availableBalancePesos": 10069.920209999831,
            "trCode": 24,
            "trName": "Remitos - Ventas",
            "order": "10427744"
            "hmac": null <-- SE AGREGA,
            "showWallet": true/false
        },
        {
            "date": "2025-09-03",
            "albNumber": "00630490",
            "total": -149.069815,
            "currencyQuote": 1375,
            "agent": "",
            "agentDescription": "",
            "branch": "0002",
            "comment": "Complejo de 3 pisos",
            "currentBalance": 7.017365999999882,
            "currencyQuoteDay": 1435,
            "currencyQuoteDayCheck": 1435,
            "subTotal": -305.3870100000001,
            "totalPesos": -204970.995625,
            "id": 924272,
            "notFiscalId": null,
            "voucherId": null,
            "token": null,
            "availableBalance": 7.017365999999882,
            "dollarQuote": null,
            "availableBalancePesos": 10069.920209999831,
            "trCode": 24,
            "trName": "Remitos - Ventas",
            "order": "10427742",
            "hmac": null <-- SE AGREGA,
            "showWallet": true/false
        },
    ...
    ],
    "pagination": {
        "total": 8,
        "current": 1,
        "pageSize": 15
    }
}
```
