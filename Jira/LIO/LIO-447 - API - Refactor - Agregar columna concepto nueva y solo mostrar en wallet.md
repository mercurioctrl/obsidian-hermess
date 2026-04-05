---
jira_key: "LIO-447"
aliases: ["LIO-447"]
summary: "API - Refactor - Agregar columna concepto nueva y solo mostrar en wallet aquellos movimientos específicos de la misma"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-09 12:15"
updated: "2025-09-18 21:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-447"
---

# LIO-447: API - Refactor - Agregar columna concepto nueva y solo mostrar en wallet aquellos movimientos específicos de la misma

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-09 12:15 |
| Actualizado | 2025-09-18 21:36 |
| Etiquetas | ninguna |
| Jira | [LIO-447](https://bluinc.atlassian.net/browse/LIO-447) |

## Relaciones

- **Padre:** [[LIO-419 - Mejoras de pagos|LIO-419]] Mejoras de pagos

## Descripcion

Agregaremos una nueva columna a la tabla `[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]` llamada `conceptLoWallet` con un string para darle un “concepto alternativo” mas manejable.

En la wallet, solo mostraremos los que tengan este concepto y HMAC
