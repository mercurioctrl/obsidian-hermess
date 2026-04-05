---
jira_key: "PEGA-126"
aliases: ["PEGA-126"]
summary: "APP - Refactor - Dividir en 3 recursos el detalle del producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2024-09-25 15:14"
updated: "2024-10-01 17:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-126"
---

# PEGA-126: APP - Refactor - Dividir en 3 recursos el detalle del producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2024-09-25 15:14 |
| Actualizado | 2024-10-01 17:11 |
| Etiquetas | ninguna |
| Jira | [PEGA-126](https://bluinc.atlassian.net/browse/PEGA-126) |

## Relaciones

- **Padre:** [[PEGA-7 - Feat - Detalle del producto (Ficha)|PEGA-7]] Feat - Detalle del producto (Ficha)
- **is blocked by:** [[PEGA-125 - API - Refactor - Dividir en 3 recursos el detalle del producto|PEGA-125]] API - Refactor - Dividir en 3 recursos el detalle del producto
- **relates to:** [[PEGA-127 - APP - Feat - Agregar parametro Between en los historamas|PEGA-127]] APP - Feat - Agregar parametro Between en los historamas

## Descripcion

Ficha:
`GET itemDetail/${id}`
HIstograma de precios:
`GET itemDetail/${id}/histogram/prices?signature=ars,usdOfficial,ripte,usd`

Histograma de cotizaciones:
`GET itemDetail/${id}/histogram/quotes`
