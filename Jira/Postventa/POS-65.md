---
jira_key: "POS-65"
summary: "API - Feat - Filtros estadisticas productos"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-10 12:09"
updated: "2022-09-26 08:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-65"
---

# POS-65: API - Feat - Filtros estadisticas productos

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-10 12:09 |
| Actualizado | 2022-09-26 08:29 |
| Etiquetas | ninguna |
| Jira | [POS-65](https://bluinc.atlassian.net/browse/POS-65) |

## Descripción

```
GET {API_URL}/v1/metrics/items/{stringNombreDeProducto}?categoryId=3&brandId=4&order=purchasesCost&limit=10
```

```
  [{
    "productId": 5685,
    "cref": "AUR_GX_LYCHAS",
    "Description": "AURICULAR GAMER GX GAMING ES LYCHAS",
    "afterSaleIncome": 509,
    "purchasesIncome": 9340000.0,
    "stock": 0.0,
    "reservation": null,
    "incomeRate": 0.0,
    "failureRate": 0.0,
    "failureCost": 324434.0,
    "purchasesCost": 44324423.43,
  },
  {
    "productId": 5685,
    "cref": "AUR_GX_LYCHAS",
    "Description": "AURICULAR GAMER GX GAMING ES LYCHAS",
    "afterSaleIncome": 509,
    "purchasesIncome": 9340000.0,
    "stock": 0.0,
    "reservation": null,
    "incomeRate": 0.0,
    "failureRate": 0.0,
    "failureCost": 324434.0,
    "purchasesCost": 44324423.43,
  },
  {
    "productId": 5685,
    "cref": "AUR_GX_LYCHAS",
    "Description": "AURICULAR GAMER GX GAMING ES LYCHAS",
    "afterSaleIncome": 509,
    "purchasesIncome": 9340000.0,
    "stock": 0.0,
    "reservation": null,
    "incomeRate": 0.0,
    "failureRate": 0.0,
    "failureCost": 324434.0,
    "purchasesCost": 44324423.43,
  }
  ]
```
