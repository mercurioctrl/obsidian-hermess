---
jira_key: "NBWEB-576"
aliases: ["NBWEB-576"]
summary: "API - Refactor - Editar/Leer parametros varios, agregar utilidad minima"
status: "Pruebas"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-08-29 09:57"
updated: "2023-09-06 09:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-576"
---

# NBWEB-576: API - Refactor - Editar/Leer parametros varios, agregar utilidad minima

| Campo | Valor |
|-------|-------|
| Estado | Pruebas (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-29 09:57 |
| Actualizado | 2023-09-06 09:40 |
| Etiquetas | ninguna |
| Jira | [NBWEB-576](https://bluinc.atlassian.net/browse/NBWEB-576) |

## Relaciones

- **Padre:** [[NBWEB-524 - CMS - Parametros varios|NBWEB-524]] CMS - Parametros varios

## Descripcion

Agregaremos `minUtility` para poder editarlo como un parámetro en el recurso [link](https://lioteam.atlassian.net/browse/NBWEB-526)  así como tambien lo agregaremos para su lectura en [link](https://lioteam.atlassian.net/browse/NBWEB-525) 

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
    "perceptionAndRetention": true,
    "minUtility": 100
  }
]
```

Solo se modifican aquellos parametros que esten presentes

Tabla de referencia: `[NEW_BYTES].[dbo].[PV_PARAMETROS_VARIOS]`
