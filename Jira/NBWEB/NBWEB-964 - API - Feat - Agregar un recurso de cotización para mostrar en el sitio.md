---
jira_key: "NBWEB-964"
aliases: ["NBWEB-964"]
summary: "API - Feat - Agregar un recurso de cotización para mostrar en el sitio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-16 11:54"
updated: "2025-04-21 10:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-964"
---

# NBWEB-964: API - Feat - Agregar un recurso de cotización para mostrar en el sitio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-16 11:54 |
| Actualizado | 2025-04-21 10:41 |
| Etiquetas | ninguna |
| Jira | [NBWEB-964](https://bluinc.atlassian.net/browse/NBWEB-964) |

## Relaciones

- **Padre:** [[NBWEB-524]] CMS - Parametros varios
- **has action item:** [[NBWEB-965]] APP - Feat - Mostrar / Ocultar en el sitio la cotizacion del momento segun corresponda

## Descripcion

Se agregará un nuevo endpoint en la API para exponer la cotización correspondiente a `IDFORMAPAGO = 1` desde la tabla `[NB_WEB].[dbo].[MS_COTIZACIONES]`, siempre y cuando el parámetro `quoteSiteShow` esté activado (`true`) en la tabla `[NEW_BYTES].[dbo].[PV_PARAMETROS_VARIOS]`

**Detalles técnicos:**

- **Recurso:** 


```
GET {API_URL}/v1/currencyQuote
```


- **Comportamiento:**

- Si `quoteSiteShow = true`, se devuelve la cotización como:

```
{   
"currencyQuote": 1235.56 
} 
```




- Si `quoteSiteShow = false`, se devuelve:

```
{   
"currencyQuote": null
} 
```






- **Query SQL para obtener la cotización:**

```
SELECT COTIZACION FROM [NB_WEB].[dbo].[MS_COTIZACIONES] WHERE IDFORMAPAGO = 1 
```



**Notas:**

- Este recurso será consumido por el frontend para mostrar u ocultar dinámicamente la cotización del dólar en el sitio.
