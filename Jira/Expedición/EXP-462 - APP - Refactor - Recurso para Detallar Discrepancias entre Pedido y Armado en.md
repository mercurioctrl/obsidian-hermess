---
jira_key: "EXP-462"
aliases: ["EXP-462"]
summary: "APP - Refactor - Recurso para Detallar Discrepancias entre Pedido y Armado en Depósito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-11-08 13:01"
updated: "2024-11-20 21:50"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/EXP-462"
---

# EXP-462: APP - Refactor - Recurso para Detallar Discrepancias entre Pedido y Armado en Depósito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-11-08 13:01 |
| Actualizado | 2024-11-20 21:50 |
| Etiquetas | esperandoDependencia |
| Jira | [EXP-462](https://bluinc.atlassian.net/browse/EXP-462) |

## Relaciones

- **Padre:** [[EXP-13 - Feat - Etiquetas y seguimiento|EXP-13]] Feat - Etiquetas y seguimiento
- **clones:** [[EXP-461 - API - Refactor - Recurso para Detallar Discrepancias entre Pedido y Armado en|EXP-461]] API - Refactor - Recurso para Detallar Discrepancias entre Pedido y Armado en Depósito

## Descripcion

Al ver los números de seguimiento del pedido, se debe cargar igual que cuando se genera el pedido, es decir las diferencias de lo cotizado para tener la informacion a la mano

[adjunto]


[adjunto]


Pedido ej: X000200597764

GET /v1/orders/{pedido}/trackingNumbers

details puede ser null.

```
{
    "details":{
        "quotedDetails": {
            "quoteAmount": 36976.389952,
            "package": {
                "amount": 2,
                "weight": 5.68,
                "dimensions": "18.65x18.65x18.65"
            }
        },
        "finalDispatchDetails": {
            "finalCost": 22446,
            "adjustedPackage": {
                "amount": 1,
                "weight": 11.35,
                "dimensions": "37.31x37.31x37.31"
            },
            "costVariance": {
                "differenceAmount": -14530.39,
                "percentageDifference": -39.3,
                "allowedPercentageDifference": 30,
                "isAllowed": true
            },
            "dispatchTimestamp": "2024-11-08 12:44:05"
        }
    },
    "trackings": [
        {
          "tracking": "E000479555",
          "packageGrouper": null
        }
    ]
}
```
