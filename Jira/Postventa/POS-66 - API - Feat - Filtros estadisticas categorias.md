---
jira_key: "POS-66"
aliases: ["POS-66"]
summary: "API - Feat - Filtros estadisticas categorias"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-10 12:18"
updated: "2022-09-12 08:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-66"
---

# POS-66: API - Feat - Filtros estadisticas categorias

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-10 12:18 |
| Actualizado | 2022-09-12 08:01 |
| Etiquetas | ninguna |
| Jira | [POS-66](https://bluinc.atlassian.net/browse/POS-66) |

## Relaciones

- **Padre:** [[POS-58]] API - Feat - Estadisticas de categorias
- **blocks:** [[POS-99]] APP - Feat - Pestaña estadística por categorías 

## Descripcion

```
GET {API_URL}/v1/metrics/categories/?brandId=4&order=purchasesCost&limit=10
```

```
 [
 {
    "categoriesId": 32,
    "categoriesDescription": "Fuentes",
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
