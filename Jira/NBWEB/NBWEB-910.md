---
jira_key: "NBWEB-910"
summary: "API - Feat - Crear Recurso para Detallar Discrepancias entre Pedido y Armado en Depósito"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-11-01 14:57"
updated: "2024-11-21 20:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-910"
---

# NBWEB-910: API - Feat - Crear Recurso para Detallar Discrepancias entre Pedido y Armado en Depósito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-11-01 14:57 |
| Actualizado | 2024-11-21 20:53 |
| Etiquetas | ninguna |
| Jira | [NBWEB-910](https://bluinc.atlassian.net/browse/NBWEB-910) |

## Descripción

Se debe ajustar el recurso en ms-envios. 

`GET /v1/trackingNumbe `

agregando **details** para  los casos donde tenemos las medidas originales y alteradas de los bultos cotizados y armados.

por lo que **“details“ **en algunos casos podria ser **null**.



```
{
   "Package": {
      "branch": "2",
      "numOrder": "10377507",
      "medioEnvioId": "4041",
      "packageGrouper": null,
      "trackingPackage": [
         "6017800000000049667"
      ]
   },
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
    }
}
```
