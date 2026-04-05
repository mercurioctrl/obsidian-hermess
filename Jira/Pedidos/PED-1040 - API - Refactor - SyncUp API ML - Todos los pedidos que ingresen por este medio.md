---
jira_key: "PED-1040"
aliases: ["PED-1040"]
summary: "API - Refactor - SyncUp API ML - Todos los pedidos que ingresen por este medio por el momengo seran companyCode = 9 es decir, NBE"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-07 19:44"
updated: "2025-07-16 10:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1040"
---

# PED-1040: API - Refactor - SyncUp API ML - Todos los pedidos que ingresen por este medio por el momengo seran companyCode = 9 es decir, NBE

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-07 19:44 |
| Actualizado | 2025-07-16 10:44 |
| Etiquetas | ninguna |
| Jira | [PED-1040](https://bluinc.atlassian.net/browse/PED-1040) |

## Relaciones

- **Padre:** [[PED-915]] MercadoLibre

## Descripcion

Esto solo quiere decir que guardaremos `[NewBytes_DBF].[dbo].[pedclit].companyCode` harcodeado en 9, por el momento (si es un parametro en el .env mejor)
