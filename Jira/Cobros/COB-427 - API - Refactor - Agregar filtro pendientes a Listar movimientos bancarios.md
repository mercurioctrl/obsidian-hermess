---
jira_key: "COB-427"
aliases: ["COB-427"]
summary: "API - Refactor - Agregar filtro pendientes a Listar movimientos bancarios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-04-28 09:03"
updated: "2023-05-23 15:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-427"
---

# COB-427: API - Refactor - Agregar filtro pendientes a Listar movimientos bancarios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-28 09:03 |
| Actualizado | 2023-05-23 15:49 |
| Etiquetas | ninguna |
| Jira | [COB-427](https://bluinc.atlassian.net/browse/COB-427) |

## Relaciones

- **Padre:** [[COB-218 - Feat - Movimientos bancarios|COB-218]] Feat - Movimientos bancarios

## Descripcion

Se debe agregar un filtro `pending` para que cuando reciba `true` muestre aquellos que tienen en `true` la columna `pending` dentro de la tabla `[NEW_BYTES].[dbo].[BA_BP_MOVIMIENTOS_ENTRADAS]`

Si no recibe nada, se muestran solo los que no la tienen en `true`
