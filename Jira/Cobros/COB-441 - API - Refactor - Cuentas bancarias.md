---
jira_key: "COB-441"
aliases: ["COB-441"]
summary: "API - Refactor - Cuentas bancarias"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-06-08 13:20"
updated: "2023-06-16 17:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-441"
---

# COB-441: API - Refactor - Cuentas bancarias

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-08 13:20 |
| Actualizado | 2023-06-16 17:29 |
| Etiquetas | ninguna |
| Jira | [COB-441](https://bluinc.atlassian.net/browse/COB-441) |

## Relaciones

- **Padre:** [[COB-440]] Refactor - Cuentas bancarias

## Descripcion

Se debe refactorizar [link](https://lioteam.atlassian.net/browse/COB-219) para que no sea obligatorio `{BankId}` y si el mismo no se envío, mezclar los bancos.

En su lugar usaremos el recurso de la siguiente forma 

```
{{API_URL}}/v1/currentBankAccount?&currency=1&agentId=12&bankId=1,2,3
```

A su vez, agregaremos al objeto el nombre e id del banco

```
{
    "response": [
        {
            "dateOperation": "2023-06-06 14:06:19",
            "amount": -200,
            "subTotal": 1613486051.6984906,
            "symbolCurrency": "$",
            "nameCurrency": "Pesos",
            "agent": "Seba",
            "observation": "test dev banco a caja sec-2",
            "voucherId": null,
            "balanceTotal": 1613486051.6984906,
            "clientId": null,
            "clientDescription": null,
            "providerId": null,
            "providerDescription": null,
            bakId : <--
            bankDescription: <--
        },
```
