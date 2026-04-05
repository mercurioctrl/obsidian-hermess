---
jira_key: "PEGA-122"
aliases: ["PEGA-122"]
summary: "API - Refactor - Agregar Signature permitiendo mostrar o ocultar indices"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-09-24 13:39"
updated: "2024-10-01 15:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-122"
---

# PEGA-122: API - Refactor - Agregar Signature permitiendo mostrar o ocultar indices

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-09-24 13:39 |
| Actualizado | 2024-10-01 15:50 |
| Etiquetas | ninguna |
| Jira | [PEGA-122](https://bluinc.atlassian.net/browse/PEGA-122) |

## Relaciones

- **Padre:** [[PEGA-1]] Bases y repositorios
- **has action item:** [[PEGA-123]] APP - Refactor - Sumar el gráfico "Indice de accesibilidad" al grafico

## Descripcion

Se ajusta 

```
GET 'http://localhost:8100/v1/itemDetail/{id_item}
```

se agrega: 

[?signature=usd,usdOfficial,ars,ripte](http://localhost:8100/v1/itemDetail/34481?signature=usd,usdOfficial,ars,ripte)

solo toma los valores: [usd, usdOfficial, ars, ripte](http://localhost:8100/v1/itemDetail/34481?signature=usd,usdOfficial,ars,ripte)

cualquier otro valor nosera tomado en cuenta.

de no enviarse el signature el recurso retorna todos los indices de precios.

de enviarse signature devolvera aquellos seleccionados. 



```
    "histogram": {
        "date": [
            "28-05-24",
            ...
        ],
        "price": [
            1157520,
            ....
        ],
        "maxValue": 1235430,
        "minValue": 303994.3,
        "priceUsd": [
            980.95,
          ...
        ],
        "maxValueDollar": 1030,
        "minValueDollar": 239.36,
        "priceUsdOfficial": [
            1319.86
            ...
        ],
        "maxValueDollarOfficial": 1397.55,
        "minValueDollarOfficial": 342.72,
        "priceRipte": [
            4.26,
            4.29,
            4.29,
            4.29,
            4.31,
            4.31,
            4.31,
            4.31,
            4.33,
            4.33,
            4.33,
            4.33,
            1.18
        ],
        "maxValueRipte": 4.55,
        "minValueRipte": 1.12
    }
```
