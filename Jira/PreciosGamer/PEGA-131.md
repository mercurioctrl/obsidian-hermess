---
jira_key: "PEGA-131"
summary: "API - Refactor - Agregar el concepto \"interval\" al recurso de cotizaciones para poder mostrarlo por distintas cantidades de dias y suavizar las curvas"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-10-03 09:27"
updated: "2024-10-14 20:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-131"
---

# PEGA-131: API - Refactor - Agregar el concepto "interval" al recurso de cotizaciones para poder mostrarlo por distintas cantidades de dias y suavizar las curvas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-03 09:27 |
| Actualizado | 2024-10-14 20:56 |
| Etiquetas | ninguna |
| Jira | [PEGA-131](https://bluinc.atlassian.net/browse/PEGA-131) |

## Descripción

se puede hacer con el parametro “interval” por cantidad de dias

si queres mostrame como lo harias y lo dejamos aca

`interval=60` → cantidad de dias

`GET /itemDetail/25045/histogram/quotes?interval=60`

response:

```
{
    "histogram": {
        "date": [
            "28-05-24",
            "27-07-24",
            "25-09-24"
        ],
        "priceUsd": [
            1180,
            1415,
            1220
        ],
        "maxValueDollar": 1554,
        "minValueDollar": 1121,
        "priceUsdOfficial": [
            877,
            911,
            945
        ],
        "maxValueDollarOfficial": 1000.65,
        "minValueDollarOfficial": 833.15,
        "priceRipte": [
            9372.6,
            10169.28,
            10722.24
        ],
        "maxValueRipte": 11406.02,
        "minValueRipte": 8903.97,
        "smvm": {
            "month": 271571.22,
            "day": 10862.88,
            "hour": 1357.86
        }
    }
}
```
