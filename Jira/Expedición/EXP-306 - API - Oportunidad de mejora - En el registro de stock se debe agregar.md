---
jira_key: "EXP-306"
aliases: ["EXP-306"]
summary: "API - Oportunidad de mejora - En el registro de stock se debe agregar ID_VENDEDOR y Remito sobre el que se esta operando (si esta disponible)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-06-06 15:26"
updated: "2023-06-23 08:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-306"
---

# EXP-306: API - Oportunidad de mejora - En el registro de stock se debe agregar ID_VENDEDOR y Remito sobre el que se esta operando (si esta disponible)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-06 15:26 |
| Actualizado | 2023-06-23 08:36 |
| Etiquetas | ninguna |
| Jira | [EXP-306](https://bluinc.atlassian.net/browse/EXP-306) |

## Relaciones

- **Padre:** [[EXP-294]] Refactor - Devoluciones (pre-despacho)

## Descripcion

En `[NB_WEB].[dbo].[registro_stock]` si bien se guarda bien el registro, se pueden agregar algunos datos complementarios… especialmente 2 que son de mucha utilidad, el numero de pedido o remiuto (cuando esta disponible).

Y el mas importante de todos, que es quien realizo el “Credito” o “Devolucion” basandonos en la tarjeta ingresada al momento de hacerlo.

[adjunto]
