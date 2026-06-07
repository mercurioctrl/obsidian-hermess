---
jira_key: LOCAPP-87
status: Ready for QA
assignee: Ezequiel manzano
assignee_email: null
reporter: Marbe Moreno
priority: Medium
issuetype: Subtarea
project: LOCAPP
updated: "2026-05-22T13:12:27.152-0300"
created: "2025-10-15T17:16:56.899-0300"
url: "https://bluinc.atlassian.net/browse/LOCAPP-87"
tags: [jira, LOCAPP, ready-for-qa]
---

# LOCAPP-87 · API - MVP - Servicio de facturación - Feat- implementar Documento de exportación SLI

[LOCAPP-87 en Jira](https://bluinc.atlassian.net/browse/LOCAPP-87)

## Descripción

Respuesta: Automatico por default: por ejemplo si tenemos 3 items de 3 proveedores diferentes tendriamos 3 SLI pero que nos dé la opcion de cambiarlo manualmente.

Tarea 24 https://docs.google.com/spreadsheets/d/18TUSaVG3bY_lMLunZ3kDCRlLnKpQV-_BPfrtbL4pHNA/edit?gid=723483997#gid=723483997

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

## Comentarios (1)

### @Marbe Moreno — 2026-05-20 11:35:53

De esa tarea 24-mensionada  
*24 - Emisión de SLI (documento de exportación): Una misma factura debe poder tener posibilidad de generar varios SLIs, uno por proveedor. (Debe tener el formato estandar de SLI que manejamos, contemplando posición arancelaria, ECCN, datos del proveedor, nro factura de venta, datos del cliente, cantidad de items y total de venta)*

**Preguntamos desde sistemas: **¿que se debe elegir para generar el SLI, proveedor items? o si se genera automaticamente agrupando proveedores

**Respuesta de laset**: Automatico por default: por ejemplo si tenemos 3 items de 3 proveedores diferentes tendriamos 3 SLI pero que nos dé la opcion de cambiarlo manualmente.

---
_Sincronizado por jira-sidecar el 2026-06-07 22:29:15 UTC._
