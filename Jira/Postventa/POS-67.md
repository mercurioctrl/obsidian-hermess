---
jira_key: "POS-67"
summary: "API - Feat - Filtros estadisticas marcas"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-10 12:19"
updated: "2022-09-12 08:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-67"
---

# POS-67: API - Feat - Filtros estadisticas marcas

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-10 12:19 |
| Actualizado | 2022-09-12 08:01 |
| Etiquetas | ninguna |
| Jira | [POS-67](https://bluinc.atlassian.net/browse/POS-67) |

## Descripción

```
GET {API_URL}/v1/metrics/brands/?categoryId=4&order=purchasesCost&limit=10
```

```


 [
 {
    "brandId": 32,
    "brandDescription": "Gigabyte",
    "afterSaleIncome": 509,
    "purchasesIncome": 9340000.0,
    "stock": 0.0,
    "reservation": 0,
    "incomeRate": 0.0,
    "failureRate": 0.0,
    "failureCost": 324434.0,
    "purchasesCost": 44324423.43,
  },
  {
    "brandId": 33,
    "brandDescription": "Gigabyte",
    "afterSaleIncome": 509,
    "purchasesIncome": 9340000.0,
    "stock": 0.0,
    "reservation": 0,
    "incomeRate": 0.0,
    "failureRate": 0.0,
    "failureCost": 324434.0,
    "purchasesCost": 44324423.43,
  }
  ]
```
