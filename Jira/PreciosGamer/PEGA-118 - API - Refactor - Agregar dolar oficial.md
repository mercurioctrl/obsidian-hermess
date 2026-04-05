---
jira_key: "PEGA-118"
aliases: ["PEGA-118"]
summary: "API - Refactor - Agregar dolar oficial"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-09-19 16:03"
updated: "2024-09-25 00:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-118"
---

# PEGA-118: API - Refactor - Agregar dolar oficial

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-19 16:03 |
| Actualizado | 2024-09-25 00:46 |
| Etiquetas | ninguna |
| Jira | [PEGA-118](https://bluinc.atlassian.net/browse/PEGA-118) |

## Relaciones

- **Padre:** [[PEGA-7 - Feat - Detalle del producto (Ficha)|PEGA-7]] Feat - Detalle del producto (Ficha)
- **blocks:** [[PEGA-117 - APP - Refactor - Hisotograma de dolar oficial paralelo|PEGA-117]] APP - Refactor - Hisotograma de dolar oficial / paralelo 

## Descripcion

De la misma forma que lo hicimos con los doalres paralelos, y teniendo en cuenta que tenemos el dato, tambien entregaremos el oficial



```
{
    "id": 34481,
    ...
    "histogram": {
        "date": [
            "28-05-24",
            ...
        ],
        "price": [
            1157520,
            ...
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
            1319.86,
            ...
        ],
        "maxValueDollarOfficial": 1397.55,
        "minValueDollarOfficial": 342.72
    }
}
```



Campos agregados.

`priceUsdOfficial`

`maxValueDollarOfficial`

`minValueDollarOfficial`
