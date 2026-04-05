---
jira_key: "NBWEB-956"
aliases: ["NBWEB-956"]
summary: "APP - Refactor - Agregar el parámetro quote en parámetros varios"
status: "Finalizada"
type: "Tarea"
priority: "Highest"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-03-10 07:13"
updated: "2025-03-10 19:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-956"
---

# NBWEB-956: APP - Refactor - Agregar el parámetro quote en parámetros varios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Highest |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-10 07:13 |
| Actualizado | 2025-03-10 19:23 |
| Etiquetas | ninguna |
| Jira | [NBWEB-956](https://bluinc.atlassian.net/browse/NBWEB-956) |

## Relaciones

- **Padre:** [[NBWEB-599]] CMS
- **action item from:** [[NBWEB-954]] API - Refactor - Agregar el parámetro quote a parametros varios

## Descripcion

Agregaremos un nuevo parámetro en la sección Parámetros Varios llamado “Descuento Cotización MP”

[adjunto]
```
PATCH {API_URL}/v1/cms/defaultParameters
```

```
{
 ...
    "quoteDiscountLo": 5.5 <<-- Este es el parametro nuevo 
 ...
}
```
