---
jira_key: "COB-235"
aliases: ["COB-235"]
summary: "API - Refactor- Transferencia de banco a salida "
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-08 13:45"
updated: "2022-11-09 11:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-235"
---

# COB-235: API - Refactor- Transferencia de banco a salida 

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-08 13:45 |
| Actualizado | 2022-11-09 11:06 |
| Etiquetas | ninguna |
| Jira | [COB-235](https://bluinc.atlassian.net/browse/COB-235) |

## Relaciones

- **Padre:** [[COB-208]] Refactor - Transferencias bancarias

## Descripcion

Refactorizaremos el siguiente recurso para realizar transferncias a terceros o salidas bancarias.

```
POST {API_URL}/v1/bankTransfer
```

Recibe la siguiente carga útil:

```
[
  {
    "transferTypeId": 4, //Caja a salida. 
    "amount": 15,
    "paymentMethodId": 2,
    "reference": "Test Dev comment2",
    "currencyQuote": 140.5,
    "originBankId": 3,
    "outputConceptId": 2
  },
  {
  "transferTypeId": 4, //Caja a salida. 
    "amount": 15,
    "paymentMethodId": 2,
    "reference": "Test Dev comment2",
    "currencyQuote": 140.5,
    "originBankId": 3,
    "outputConceptId": 2
  }
  ]
```

Lo que hacemos es agregar una nueva `transferTypeId` para saber que tipode movimiento es y para asignar el concepto segun `outputConceptId` y no de manera hardcodeada.

Esto afecta obviamente el saldo del banco.
