---
jira_key: "COB-539"
aliases: ["COB-539"]
summary: "API - Refactor - Entregar los mismos parametros en el listado de clientes, que en el recurso balances"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-08-13 09:14"
updated: "2024-08-15 02:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-539"
---

# COB-539: API - Refactor - Entregar los mismos parametros en el listado de clientes, que en el recurso balances

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-13 09:14 |
| Actualizado | 2024-08-15 02:36 |
| Etiquetas | ninguna |
| Jira | [COB-539](https://bluinc.atlassian.net/browse/COB-539) |

## Relaciones

- **Padre:** [[COB-538]] Oportunidad de Mejora: Mostrar exacto la misma informacion dentro y fuera del estado crediticio del cliente
- **blocks:** [[COB-540]] APP - Refactor - Mostrar en la lista de clientes exacto el mismo informe crediticio que se obtiene en la cuenta corriente con "balances"

## Descripcion

Refactorizaremos el recurso 

```
GET {API_URL}/v1/clients/
```

Para que tenga los siguientes parámetros exactamente con la misma lógica que el recurso


    `limitCheckBalanceAmount`
    `usedCheckBalanceAmount`
    `limitBalanceAmount`
    `usedBalanceAmount`



```
GET {API_URL}/v1/balances/{clientId}
```



En la historia original puede verse que aunque hay parámetros que coinciden el nombre, los valores son diferentes

[link](https://lioteam.atlassian.net/browse/COB-538) 

Lo que esta mas claro y realmente queremos mostrar es lo de dentro de la cuenta corriente (blanaces)

```
{
    "limitCheckBalanceAmount": 1500000,
    "usedCheckBalanceAmount": 1090005.08,
    "limitBalanceAmount": 0,
    "usedBalanceAmount": -0.7199800000001619
}
```

Ver diferencias con clients

```
{
    "response": [
        {
            "clientId": 83869,
            "clientName": "GRUPO MAX  S. A. S.",
            "clientBusinessName": "GRUPO MAX  S. A. S.",
            "clientTaxNumber": "30717775550",
            "clientPerception": 0,
            "limitCheckBalanceAmount": 1500000, <<<<-- este no esta
            "usedCheckBalanceAmount": 1090005.08, 1500000, <<<<-- este esta correcto
            "limitBalanceAmount": 0,
            "usedBalanceAmount": -0, , <<<<-- este esta redondeado distinto, o es incorrecto
        },
```
