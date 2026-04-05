---
jira_key: "LOCAPP-74"
aliases: ["LOCAPP-74"]
summary: "Fix: Arreglar cuando se hacen notas de creditos cruzadas de empresa emisora"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Ezequiel manzano"
created: "2025-06-23 10:51"
updated: "2025-07-09 18:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-74"
---

# LOCAPP-74: Fix: Arreglar cuando se hacen notas de creditos cruzadas de empresa emisora

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Ezequiel manzano |
| Creado | 2025-06-23 10:51 |
| Actualizado | 2025-07-09 18:54 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-74](https://bluinc.atlassian.net/browse/LOCAPP-74) |

## Relaciones

*Sin relaciones*

## Descripcion

Se debe agregar el parámetro `[NewBytes_DBF].[dbo].[FP_FactWebCliEncabezado].companyCode`Completaremos le campo según el `companyCode` del cliente el momento de realizarse cualquier factura Completaremos le campo según el `companyCode` del cliente el momento de realizarse cualquier NC (parcial, completa, de expedición o postventa)
