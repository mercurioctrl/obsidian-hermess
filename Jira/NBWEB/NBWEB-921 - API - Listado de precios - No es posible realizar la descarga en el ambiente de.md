---
jira_key: "NBWEB-921"
aliases: ["NBWEB-921"]
summary: "API - Listado de precios - No es posible realizar la descarga en el ambiente de desarrollo"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-11-07 13:52"
updated: "2024-11-13 10:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-921"
---

# NBWEB-921: API - Listado de precios - No es posible realizar la descarga en el ambiente de desarrollo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-11-07 13:52 |
| Actualizado | 2024-11-13 10:48 |
| Etiquetas | ninguna |
| Jira | [NBWEB-921](https://bluinc.atlassian.net/browse/NBWEB-921) |

## Relaciones

- **Padre:** [[NBWEB-602]] Sitio Web
- **blocks:** [[NBWEB-913]] API - Refactor - Agregaremos internalTax a todos nuestros listados de precio de descarga

## Descripcion

Por algún motivo, no es posible descargar los listados de precios en Gamma; sin embargo, en el entorno de producción se descargan correctamente.

Adjunto un ejemplo de uno de los intentos que realicé.

```
https://gamma.api.nb.com.ar/v1//priceListExcel/fbce8d0420649ee43383ce1e3a9a7c
```

[adjunto]
