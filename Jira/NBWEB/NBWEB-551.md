---
jira_key: "NBWEB-551"
summary: "API - Feat - Editar clientes"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-05-29 07:47"
updated: "2023-07-12 17:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-551"
---

# NBWEB-551: API - Feat - Editar clientes

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-29 07:47 |
| Actualizado | 2023-07-12 17:06 |
| Etiquetas | ninguna |
| Jira | [NBWEB-551](https://bluinc.atlassian.net/browse/NBWEB-551) |

## Descripción

Se debe construir el siguiente recurso para editar los objetos provistos en [https://lioteam.atlassian.net/browse/NBWEB-549](https://lioteam.atlassian.net/browse/NBWEB-549) 



```
PATCH {API_URL}/v1/cms/customers
```

```
[

  {

    "id": 77160 <-ESTE es el unico no editable

    "clientName": "ECHANIZ HERMANOS SOCIEDAD ANONIMA",

    "clientComercialName": "Echaniz hnos",

    "discount": 1.0,

    "priceList": 1.0,

    "defaultCurrency": 1,

    "ccoddiv": "DOL",

    "brokerage": 0,

    "userBlack": null,

    "userBlackpercentage": 5000000.0,

    "profile": 1,

    "company": 4,

    "sellerId": 41,

    "lastNameSeller": "Sheridaim",

    "sellerName": "Natalia"

  }
  ]
```
