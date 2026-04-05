---
jira_key: "PEGA-71"
aliases: ["PEGA-71"]
summary: "API - Detalle del producto - Mejora en los parámetros de precios"
status: "Finalizada"
type: "Tarea"
priority: "Lowest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-05-09 11:30"
updated: "2024-05-09 22:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-71"
---

# PEGA-71: API - Detalle del producto - Mejora en los parámetros de precios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Lowest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-05-09 11:30 |
| Actualizado | 2024-05-09 22:37 |
| Etiquetas | ninguna |
| Jira | [PEGA-71](https://bluinc.atlassian.net/browse/PEGA-71) |

## Relaciones

- **Padre:** [[PEGA-2 - Catalogos y Buscador|PEGA-2]] Catalogos y Buscador
- **relates to:** [[PEGA-19 - API - Feat - Detalle del producto|PEGA-19]] API - Feat - Detalle del producto
- **relates to:** [[PEGA-69 - APP - Detalle del producto - Mejora en los parámetros de precios|PEGA-69]] APP - Detalle del producto - Mejora en los parámetros de precios

## Descripcion

Vamos a optimizar los nombres de las claves de precios en el objeto de respuesta del detalle del artículo. El propósito es evitar confusiones entre el precio actual y el precio anterior. Dejo a tu la elección de los nombres que consideres más apropiados.

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
