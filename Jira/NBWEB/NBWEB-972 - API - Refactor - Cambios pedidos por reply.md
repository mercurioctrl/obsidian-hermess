---
jira_key: "NBWEB-972"
aliases: ["NBWEB-972"]
summary: "API - Refactor - Cambios pedidos por reply"
status: "Finalizada"
type: "Tarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-12 12:13"
updated: "2025-06-12 15:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-972"
---

# NBWEB-972: API - Refactor - Cambios pedidos por reply

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-12 12:13 |
| Actualizado | 2025-06-12 15:16 |
| Etiquetas | ninguna |
| Jira | [NBWEB-972](https://bluinc.atlassian.net/browse/NBWEB-972) |

## Relaciones

- **Padre:** [[NBWEB-602]] Sitio Web

## Descripcion

Modificaremos el recurso especifico que descarga la planilla de reply

```
https://api.nbe.com.ar/v1/priceListReplyLatam/4520348d5e5ab6d973b54aec33dcd3
```

Agregaremos:

- Una columna al final para mostrar el parámetro `[NewBytes_DBF].[dbo].[articulo]`.`officialSiteUrl` con el nombre “Informacion Adicional”
