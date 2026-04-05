---
jira_key: "NBWEB-954"
summary: "API - Refactor - Agregar el parámetro quote a parametros varios"
status: "Finalizada"
type: "Tarea"
priority: "Highest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-03-07 11:38"
updated: "2025-03-10 10:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-954"
---

# NBWEB-954: API - Refactor - Agregar el parámetro quote a parametros varios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Highest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-07 11:38 |
| Actualizado | 2025-03-10 10:24 |
| Etiquetas | ninguna |
| Jira | [NBWEB-954](https://bluinc.atlassian.net/browse/NBWEB-954) |

## Descripción

```
GET {API_URL}/v1/cms/defaultParameters
```

```
{
    "rangeAuthOrders": 130,
    "truckLimit": 25000,
    "varCurrency": 1,
    "checksDays": 30,
    "maxCurrencyUser": 50,
    "annualRate": 40,
    "perceptionAndRetention": true,
    "minUtility": 0,
    "quoteDiscountLo": 5.5 <<-- Este es el parametro nuevo 
}
```

Se agregara en 

`[NEW_BYTES].[dbo].[PV_PARAMETROS_VARIOS].quoteDiscountLo`

## ¿Que hace al modificarse?

```
PATCH {API_URL}/v1/cms/defaultParameters
```

```
{
...
quoteDiscountLo: 5.5
...}
```

Se debe modificar 
`[NEW_BYTES].[dbo].[MS_COTIZACIONES]`para asimilar el cambio del porcentaje en la tabla de cotizaciones

Algo similar a esto

```
UPDATE  [NEW_BYTES].[dbo].[PV_PARAMETROS_VARIOS] SET 
quoteDiscountLo = 5.5;

Una vez actualizado, corremos:

UPDATE [NEW_BYTES].[dbo].[MS_COTIZACIONES]
SET COTIZACION = COTIZACION_SHOW_LO * (100 - (SELECT quoteDiscountLo FROM [NEW_BYTES].[dbo].[PV_PARAMETROS_VARIOS]))
WHERE id = 3;

```

Ojo esto solo aplica al id=3 que es libroOpcion, porque es para esto específicamente el parche
