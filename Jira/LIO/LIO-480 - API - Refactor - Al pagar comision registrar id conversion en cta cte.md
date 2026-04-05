---
jira_key: "LIO-480"
aliases: ["LIO-480"]
summary: "API - Refactor - Al pagar comision registrar id conversion en cta cte"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-12-02 09:33"
updated: "2025-12-09 15:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-480"
---

# LIO-480: API - Refactor - Al pagar comision registrar id conversion en cta cte

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-12-02 09:33 |
| Actualizado | 2025-12-09 15:36 |
| Etiquetas | ninguna |
| Jira | [LIO-480](https://bluinc.atlassian.net/browse/LIO-480) |

## Relaciones

- **Padre:** [[LIO-408]] Referidos

## Descripcion

Con el objetivo de identificar el detalle de la orden en los movimientos de la wallet, se incorporó el campo `ReferralConversionId` en la tabla `NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS`. En este campo se persiste el `id` generado en la tabla `lo.dbo.referral_conversions`, lo que permite vincular cada movimiento con el detalle correspondiente de la orden.
