---
jira_key: "EXP-461"
aliases: ["EXP-461"]
summary: "API - Refactor - Recurso para Detallar Discrepancias entre Pedido y Armado en Depósito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-11-08 13:00"
updated: "2024-11-21 21:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-461"
---

# EXP-461: API - Refactor - Recurso para Detallar Discrepancias entre Pedido y Armado en Depósito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-11-08 13:00 |
| Actualizado | 2024-11-21 21:16 |
| Etiquetas | ninguna |
| Jira | [EXP-461](https://bluinc.atlassian.net/browse/EXP-461) |

## Relaciones

- **Padre:** [[EXP-13]] Feat - Etiquetas y seguimiento
- **is cloned by:** [[EXP-462]] APP - Refactor - Recurso para Detallar Discrepancias entre Pedido y Armado en Depósito
- **has action item:** [[SNB-2463]] MS -Envios - Refactor - Implementar cambiar el parametro 'items' por 'package_dimensions' par Entregar

## Descripcion

Exp.

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
