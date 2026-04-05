---
jira_key: "PED-247"
aliases: ["PED-247"]
summary: "API - Refactor - Al liquidar un pedido, marcar [ULTIMA_COMPRA]"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-11-08 09:59"
updated: "2024-01-08 12:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-247"
---

# PED-247: API - Refactor - Al liquidar un pedido, marcar [ULTIMA_COMPRA]

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-08 09:59 |
| Actualizado | 2024-01-08 12:39 |
| Etiquetas | ninguna |
| Jira | [PED-247](https://bluinc.atlassian.net/browse/PED-247) |

## Relaciones

- **Padre:** [[PED-123 - Feat - Liquidar pedido|PED-123]] Feat - Liquidar pedido
- **is blocked by:** [[PED-265 - API - Al liquidar un pedido, marcar ultima compra - Incidencias varias|PED-265]] API - Al liquidar un pedido, marcar ultima compra - Incidencias varias

## Descripcion

Al liquidar un pedido, debe marcarse con la fecha del día el campo `[NewBytes_DBF].[dbo].[clientes].[ULTIMA_COMPRA]`
