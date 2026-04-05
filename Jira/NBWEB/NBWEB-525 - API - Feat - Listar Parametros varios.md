---
jira_key: "NBWEB-525"
aliases: ["NBWEB-525"]
summary: "API - Feat - Listar Parametros varios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-22 09:17"
updated: "2023-04-17 09:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-525"
---

# NBWEB-525: API - Feat - Listar Parametros varios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-22 09:17 |
| Actualizado | 2023-04-17 09:39 |
| Etiquetas | ninguna |
| Jira | [NBWEB-525](https://bluinc.atlassian.net/browse/NBWEB-525) |

## Relaciones

- **Padre:** [[NBWEB-524 - CMS - Parametros varios|NBWEB-524]] CMS - Parametros varios
- **blocks:** [[NBWEB-527 - APP - Feat - Seccion Parametros varios|NBWEB-527]] APP - Feat - Seccion Parametros varios

## Descripcion

```
GET {API_URL}/v1/cms/defaultParameters
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

Tabla de referencia: `[NEW_BYTES].[dbo].[PV_PARAMETROS_VARIOS]`
