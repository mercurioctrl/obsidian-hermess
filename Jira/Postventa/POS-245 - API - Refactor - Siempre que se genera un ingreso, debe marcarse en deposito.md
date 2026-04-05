---
jira_key: "POS-245"
aliases: ["POS-245"]
summary: "API - Refactor - Siempre que se genera un ingreso, debe marcarse en deposito \"Servicio tecnico\""
status: "CodeReview"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-16 09:54"
updated: "2023-03-16 11:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-245"
---

# POS-245: API - Refactor - Siempre que se genera un ingreso, debe marcarse en deposito "Servicio tecnico"

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-16 09:54 |
| Actualizado | 2023-03-16 11:17 |
| Etiquetas | ninguna |
| Jira | [POS-245](https://bluinc.atlassian.net/browse/POS-245) |

## Relaciones

- **Padre:** [[POS-19 - Ingresos|POS-19]] Ingresos

## Descripcion

En la tabla `[NEW_BYTES].[dbo].[ST_RMADETALLE]` se debe marcar la columna `ID_DEPOSITO` en `2` según la tabla `[NEW_BYTES].[dbo].[ST_DEPOSITOS_SAF]`

para indicar que esta en soporte técnico cada vez que se hace un INGRESO.

En produccion, marcaremos aquellos que estan en null con “2” para que queden acomodados los casos viejos que no tienen el dato.
