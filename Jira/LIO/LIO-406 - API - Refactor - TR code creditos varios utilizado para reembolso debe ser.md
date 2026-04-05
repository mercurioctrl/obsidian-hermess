---
jira_key: "LIO-406"
aliases: ["LIO-406"]
summary: "API - Refactor - TR code creditos varios utilizado para reembolso debe ser income"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-08-05 17:06"
updated: "2025-08-18 10:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-406"
---

# LIO-406: API - Refactor - TR code creditos varios utilizado para reembolso debe ser income

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-08-05 17:06 |
| Actualizado | 2025-08-18 10:48 |
| Etiquetas | ninguna |
| Jira | [LIO-406](https://bluinc.atlassian.net/browse/LIO-406) |

## Relaciones

- **Padre:** [[LIO-231]] Billetera

## Descripcion

En caso de un reembolos, el cual tiene un tr_codigo  = 30 (creditos varios). Debe mostrarse en la wallet como un ingreso.



Mal:

[adjunto]


Bien:

[adjunto]




Como probar:

Crea una linea en `NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS ` con tr_code =30.

generar el reembolso con el recurso [link](https://bluinc.atlassian.net/browse/PED-1075)  → api de pedidos.
