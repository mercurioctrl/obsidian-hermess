---
jira_key: "EXP-483"
aliases: ["EXP-483"]
summary: "APP - Refactor - Agregar internalTax en los casos que corresponda"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-04-03 12:30"
updated: "2025-04-08 13:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-483"
---

# EXP-483: APP - Refactor - Agregar internalTax en los casos que corresponda

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-03 12:30 |
| Actualizado | 2025-04-08 13:50 |
| Etiquetas | ninguna |
| Jira | [EXP-483](https://bluinc.atlassian.net/browse/EXP-483) |

## Relaciones

- **Padre:** [[EXP-116 - Devoluciones|EXP-116]] Devoluciones
- **is blocked by:** [[EXP-484 - API - Refactor - Agregar internalTax en el objeto de la orden para que el front|EXP-484]] API - Refactor - Agregar internalTax en el objeto de la orden para que el front sepa que debe enviarlo al acreditar
- **has action item:** [[SNB-2914 - ERROR EN NC CON ART. CON IMP. INTERNO|SNB-2914]] ERROR EN NC CON ART. CON IMP. INTERNO

## Descripcion

Refactorizaremos el objeto que enviamos para hacer una devolución o crédito

```
POST {API_URL}/v1/ordersRefund/{pedido}
```

```
{
"voucherTypeId":"2",
"clientId":26806,
"pedido":"X000200612288",
"autorizaUser":"FE5BA42E32632445",
"trade":[
  {
  "units":1,
  "price":213.9756,
  "ivaTax":21,
  "internalId":116291,
  "missing":false,
  "internalTax": 23.46 <<< -- Se debe agregar
  }
]
}
```
