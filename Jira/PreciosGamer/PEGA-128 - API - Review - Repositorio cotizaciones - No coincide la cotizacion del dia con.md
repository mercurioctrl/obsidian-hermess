---
jira_key: "PEGA-128"
aliases: ["PEGA-128"]
summary: "API - Review - Repositorio cotizaciones - No coincide la cotizacion del dia con los dias propimente dichos"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-09-30 06:25"
updated: "2024-10-01 18:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-128"
---

# PEGA-128: API - Review - Repositorio cotizaciones - No coincide la cotizacion del dia con los dias propimente dichos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-30 06:25 |
| Actualizado | 2024-10-01 18:34 |
| Etiquetas | ninguna |
| Jira | [PEGA-128](https://bluinc.atlassian.net/browse/PEGA-128) |

## Relaciones

- **Padre:** [[PEGA-1]] Bases y repositorios

## Descripcion

```
GET {API_URL}/v1/itemDetail/27428/histogram/quotes
```

```
{
    "histogram": {
        "date": [
            "10-07-24",
            "15-07-24",
            "16-07-24",
            "19-07-24",
            "23-07-24",
            "29-07-24",
            "05-08-24",
            "06-08-24",
            "07-08-24",
            "16-08-24",
            "05-09-24",
            "06-09-24",
            "13-09-24",
            "14-09-24",
            "15-09-24",
            "16-09-24",
            "17-09-24",
            "19-09-24",
            "26-09-24",
            "27-09-24",
            "28-09-24",
            "29-09-24",
            "30-09-24"
        ],
        "priceUsd": [
            1430,
            1395,
            1380,
            1435,
            1425,
            1395,
            1350,
            1350,
            1350,
            1350,
            1350,
            1350,
            1350,
            1350,
            1350,
            1350,
            1350,
            1350,
            1350,
            1350,
            1350,
            1350,
            1350
        ],
        "maxValueDollar": 1506.75,
        "minValueDollar": 1282.5,
        "priceUsdOfficial": [
            901,
            903,
            903,
            905,
            908,
            912,
            913,
            913,
            913,
            913,
            913,
            913,
            913,
            913,
            913,
            913,
            913,
            913,
            913,
            913,
            913,
            913,
            913
        ],
        "maxValueDollarOfficial": 958.65,
        "minValueDollarOfficial": 855.95,
        "priceRipte": [
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22,
            271571.22
        ],
        "maxValueRipte": 285149.78,
        "minValueRipte": 257992.66
    }
}
```
