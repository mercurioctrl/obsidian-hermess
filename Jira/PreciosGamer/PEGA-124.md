---
jira_key: "PEGA-124"
summary: "API - Refactor - Agregar repositorio de cotizaciones según fechas"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-09-25 09:03"
updated: "2024-10-05 08:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-124"
---

# PEGA-124: API - Refactor - Agregar repositorio de cotizaciones según fechas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-25 09:03 |
| Actualizado | 2024-10-05 08:20 |
| Etiquetas | ninguna |
| Jira | [PEGA-124](https://bluinc.atlassian.net/browse/PEGA-124) |

## Descripción

Agregaremos un recurso para mostrar todas las cotizaciones en el intervalo de tiempo deseado para poder proyectarlo debajo del gráfico y poder entender como se relacionan las mismas a cada precio. Esto no involucra aun prodcuto puntual, ya que son las referencias de cotizaciones para cada momento.

Para eso mostraremos a cada dia, la cotizacion de:

- Dolar


- Dolar oficial


- Salario Minimo Vital y móvil



Se recomienda usar una “signature” como se refactorizo el recurtso anterior, que tambien sera refactorizado para contemplar intervalos de fecha

```
GET {API_URL}/v1/quotes?between=01-08-2024_31-08-2024
```

```
{
    "histogram": {
        "date": [
            "28-05-24",
            "30-05-24",
            "31-05-24",
            "03-06-24"
        ],
        "priceUsdOfficial": [
            980.5,
            980.5,
            980.5,
            980.5,
        ],
        "maxValueDollarOfficial": 980.5,
        "maxValueDollarOfficial": 980.5,,
        "usd": [
            1200,
            1200,
            1200,
            1200
        ],
        "maxValueDollar": 1200,
        "minValueDollar": 1200,
        "smvm": [
            800000,
            800000,
            800000,
            800000
        ],
        "maxValueSmvm": 800000,
        "minValueSmvm": 800000
    }
}
```
