---
jira_key: "LIO-450"
aliases: ["LIO-450"]
summary: "API - Refactor - Al confirmar un pedido que usa plata en wallet o billetera, agregar parametro idLo a la linea de cuenta corriente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-12 14:56"
updated: "2025-09-24 10:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-450"
---

# LIO-450: API - Refactor - Al confirmar un pedido que usa plata en wallet o billetera, agregar parametro idLo a la linea de cuenta corriente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-12 14:56 |
| Actualizado | 2025-09-24 10:52 |
| Etiquetas | ninguna |
| Jira | [LIO-450](https://bluinc.atlassian.net/browse/LIO-450) |

## Relaciones

- **Padre:** [[LIO-419]] Mejoras de pagos
- **action item from:** [[LIO-445]] API - Refactor - Al procesar la compra, comprobar y descontar monto de billetera en caso de ser utilizado

## Descripcion

Según lo realizado en [link](https://bluinc.atlassian.net/browse/LIO-445)  agergaremos como un extra, una nueva clave de vinculacion


`[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS].idLo`

Y lo completaremos con el id en `[LO].[dbo].[pedidosCabecera].id` para poder enlzarlo para distintos fines.



Como parte de la tarea realizada en [link](https://bluinc.atlassian.net/browse/LIO-445) , debemos incorporar una nueva clave de vinculación para mejorar la trazabilidad entre pedidos y movimientos de cuenta corriente.

Se agregará el campo `idLo` en la tabla `[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]`.
Este campo se completará con el valor correspondiente de `[LO].[dbo].[pedidosCabecera].id`, permitiendo enlazar ambas entidades para distintos fines operativos y de análisis.

**Criterios de aceptación:**

- Se agrega el campo `idLo` en la tabla `[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]`.


- El campo se completa automáticamente con el valor de `pedidosCabecera.id` al registrar el movimiento.


- La relación queda disponible para consultas, reportes y procesos futuros que requieran esta vinculación.
