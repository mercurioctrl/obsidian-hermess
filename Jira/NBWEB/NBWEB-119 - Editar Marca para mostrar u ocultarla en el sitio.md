---
jira_key: "NBWEB-119"
aliases: ["NBWEB-119"]
summary: "Editar Marca para mostrar u ocultarla en el sitio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-19 12:43"
updated: "2022-07-21 10:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-119"
---

# NBWEB-119: Editar Marca para mostrar u ocultarla en el sitio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-19 12:43 |
| Actualizado | 2022-07-21 10:42 |
| Etiquetas | ninguna |
| Jira | [NBWEB-119](https://bluinc.atlassian.net/browse/NBWEB-119) |

## Relaciones

- **Padre:** [[NBWEB-73 - API - CMS - ABMS|NBWEB-73]] API - CMS - ABMS

## Descripcion

Se trata de un recurso para mostrar / ocultar marcas

```
PATCH {{API_URL}}/v1/cms/brand/{brandId}/show/true
```



```
PATCH {{API_URL}}/v1/cms/brand/{brandId}/show/false
```



Se hace uso de la columna `siteShow` (bit) en `[NB_WEB].[dbo].[marcas]`
