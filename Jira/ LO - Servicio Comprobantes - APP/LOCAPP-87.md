---
jira_key: "LOCAPP-87"
summary: "API - MVP - Servicio de facturación - Feat- implementar Documento de exportación SLI"
status: "Tareas por hacer"
type: "Subtarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Marbe Moreno"
created: "2025-10-15 17:16"
updated: "2025-11-13 18:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-87"
---

# LOCAPP-87: API - MVP - Servicio de facturación - Feat- implementar Documento de exportación SLI

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-15 17:16 |
| Actualizado | 2025-11-13 18:24 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-87](https://bluinc.atlassian.net/browse/LOCAPP-87) |

## Descripción

Respuesta: Automatico por default: por ejemplo si tenemos 3 items de 3 proveedores diferentes tendriamos 3 SLI pero que nos dé la opcion de cambiarlo manualmente.

Tarea 24 [link](https://docs.google.com/spreadsheets/d/18TUSaVG3bY_lMLunZ3kDCRlLnKpQV-_BPfrtbL4pHNA/edit?gid=723483997#gid=723483997) 

Objeto de referencia


```
 sliObj:{
  "shipper": {
    "name": "ASRock America, Inc.",
    "address": "13848 Magnolia Avenue Chino, CA",
    "zipCode": "91710-7027"
  },
  "exporterEinNo": "06-1674747",
  "ultimateConsignee": {
    "name": "EMAP S.A.",
    "rut": "80046975-9",
    "address": "Av Carlos A. Lopez c/Adrian Jara, Ciudad del Este, Paraguay"
  },
  "intermediateConsignee": {
    "name": "LASET S.A.",
    "address": "PRADINES CLEMENTE 1795 MONTEVIDEO URUGUAY (11500)"
        },
  
  
  "countryOfUltimateDestination": "Paraguay",
        "shipperRefNo": "A-3260",
  
  "commodities": [
    {
      "df": "F",
      "scheduleBNumber": "8471.30.0100",
      "quantity": "57 UNITS",
      "shippingWeightKgs": "100",
      "shippingWeightPounds": "220",
      "cubicMeters": "10",
      "sellingPriceOrCost": "30182",
    },
    {
      "df": "F",
      "scheduleBNumber": "847.330.0002",
      "quantity": "125 UNITS",
      "shippingWeightKgs": "100",
      "shippingWeightPounds": "220",
      "cubicMeters": "10",
      "sellingPriceOrCost": "30182",
    }
  ],
  "licensingNumberOrSymbol": "NLR",
  "eccn": "EAR99",
  "authorizedOfficer": {
    "name": "JC Chung",
    "title": "Logistics",
    "date": "10/15/2025"
  },
  "specialInstructions": "LASET S.A. must be put as Intermediate Consignee"
}
```
