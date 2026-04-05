---
jira_key: "INV-259"
aliases: ["INV-259"]
summary: "API - MVP - Refactor - Registro de stock -> Agregar control de stock al snapshot"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-11-30 23:46"
updated: "2025-12-05 05:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-259"
---

# INV-259: API - MVP - Refactor - Registro de stock -> Agregar control de stock al snapshot

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-11-30 23:46 |
| Actualizado | 2025-12-05 05:59 |
| Etiquetas | ninguna |
| Jira | [INV-259](https://bluinc.atlassian.net/browse/INV-259) |

## Relaciones

- **Padre:** [[INV-211 - API - MVP - Feat- Agregar repo con pestaña de producto por depósito|INV-211]] API - MVP - Feat- Agregar repo con pestaña de producto por depósito
- **relates to:** [[INV-213 - API - MVP - Feat- opción para cambiar el producto de depósito|INV-213]] API - MVP - Feat-  opción para cambiar el producto de depósito

## Descripcion

Agregaremos la columna `nstock_ctrl` a la tabla `[NB_WEB].[dbo].[registro_stock]`, con la finalidad de que, al cambiar el producto de un depósito y guardar el snapshot de `[NewBytes_DBF].[dbo].stocks`, también se incluya `nstock_ctrl`.
