---
jira_key: "PEGA-69"
aliases: ["PEGA-69"]
summary: "APP - Detalle del producto - Mejora en los parámetros de precios"
status: "Finalizada"
type: "Tarea"
priority: "Lowest"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-05-08 15:26"
updated: "2024-05-09 22:37"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/PEGA-69"
---

# PEGA-69: APP - Detalle del producto - Mejora en los parámetros de precios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Lowest |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-05-08 15:26 |
| Actualizado | 2024-05-09 22:37 |
| Etiquetas | esperandoDependencia |
| Jira | [PEGA-69](https://bluinc.atlassian.net/browse/PEGA-69) |

## Relaciones

- **Padre:** [[NBWEB-498]] Oportunidades de mejora
- **relates to:** [[PEGA-20]] APP - Feat - Detalle del producto
- **relates to:** [[PEGA-71]] API - Detalle del producto - Mejora en los parámetros de precios

## Descripcion

Vamos a optimizar los nombres de las claves de precios en el objeto de respuesta del detalle del artículo. El propósito es evitar confusiones entre el precio actual y el precio anterior. 

```
GET {API_URL}/v1/itemDetail/{id}
```

```
[
  {
  ...
  price: 3243,
  lastPrice: 3231,
  ...
  }
] 
```
