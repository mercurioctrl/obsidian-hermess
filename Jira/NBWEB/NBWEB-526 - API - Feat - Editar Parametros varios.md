---
jira_key: "NBWEB-526"
aliases: ["NBWEB-526"]
summary: "API - Feat - Editar Parametros varios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-22 09:23"
updated: "2023-04-17 09:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-526"
---

# NBWEB-526: API - Feat - Editar Parametros varios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-22 09:23 |
| Actualizado | 2023-04-17 09:39 |
| Etiquetas | ninguna |
| Jira | [NBWEB-526](https://bluinc.atlassian.net/browse/NBWEB-526) |

## Relaciones

- **Padre:** [[NBWEB-524 - CMS - Parametros varios|NBWEB-524]] CMS - Parametros varios
- **blocks:** [[NBWEB-527 - APP - Feat - Seccion Parametros varios|NBWEB-527]] APP - Feat - Seccion Parametros varios

## Descripcion

```
PATCH {API_URL}/v1/cms/defaultParameters
```

Devuelve 

```
[
  {
    "rangeAuthOrders": 130.0,
    "truckLimit": 840000.0,
    "varCurrency": 1.0,
    "checksDays": 30,
    "maxCurrencyUser": 50.0,
    "annualRate": 100.0,
    "perceptionAndRetention": true
  }
]
```

Solo se modifican aquellos parametros que esten presentes

Tabla de referencia: `[NEW_BYTES].[dbo].[PV_PARAMETROS_VARIOS]`
