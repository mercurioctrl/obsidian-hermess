---
jira_key: "COB-375"
aliases: ["COB-375"]
summary: "API - Feat - Listar saldos de credito por cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-22 09:37"
updated: "2023-04-11 09:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-375"
---

# COB-375: API - Feat - Listar saldos de credito por cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-22 09:37 |
| Actualizado | 2023-04-11 09:38 |
| Etiquetas | ninguna |
| Jira | [COB-375](https://bluinc.atlassian.net/browse/COB-375) |

## Relaciones

- **Padre:** [[COB-374]] Feat - Editar estado crediticio de la cuenta del cliente

## Descripcion

```
GET {API_URL}/v1/assignedCredit/{clientId}
```

Usando `[NEW_BYTES].[dbo].[MS_CTACTE_CLIENTES]` mostraremos el siguiente objeto

```
[ {
    "clientId": 19164,
    "usdCredit": 0.0,
    "checkCredit": 0.0,
    "dateModify": "2011-11-24T11:10:44",
    "userModify": "EXP3",
    "usdCreditPeriod": 0,
    "checkCreditPeriod": 0,
    "comment": ""
  },
  {
    "clientId": 16998,
    "usdCredit": 500.0,
    "checkCredit": 115120.0,
    "dateModify": "2019-02-22T09:33:47",
    "userModify": "Dario",
    "usdCreditPeriod": 35,
    "checkCreditPeriod": 35,
    "comment": "ASEGURADO DISCRECIONAL U$s 500"
  },]
```

**Filtros**

Por el momento solo filtra por cliente
