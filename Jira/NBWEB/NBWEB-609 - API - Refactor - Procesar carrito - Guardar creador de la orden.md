---
jira_key: "NBWEB-609"
aliases: ["NBWEB-609"]
summary: "API - Refactor - Procesar carrito - Guardar creador de la orden"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-01-15 02:57"
updated: "2024-01-26 02:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-609"
---

# NBWEB-609: API - Refactor - Procesar carrito - Guardar creador de la orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-01-15 02:57 |
| Actualizado | 2024-01-26 02:56 |
| Etiquetas | ninguna |
| Jira | [NBWEB-609](https://bluinc.atlassian.net/browse/NBWEB-609) |

## Relaciones

- **Padre:** [[NBWEB-50 - Sitio Web|NBWEB-50]] Sitio Web

## Descripcion

Al momento de generar la orden se debe guardar el creador que en este caso es el cliente en `ccodageCreator` y `agentDescriptionCreator` en la tabla `NewBytes_DBF.dbo.pedclit`
