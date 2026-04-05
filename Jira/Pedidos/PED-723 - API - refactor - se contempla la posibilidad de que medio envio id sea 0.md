---
jira_key: "PED-723"
aliases: ["PED-723"]
summary: "API - refactor - se contempla la posibilidad de que medio envio id sea  0"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-05-23 13:05"
updated: "2024-05-28 01:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-723"
---

# PED-723: API - refactor - se contempla la posibilidad de que medio envio id sea  0

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-05-23 13:05 |
| Actualizado | 2024-05-28 01:41 |
| Etiquetas | ninguna |
| Jira | [PED-723](https://bluinc.atlassian.net/browse/PED-723) |

## Relaciones

- **is blocked by:** [[SNB-1950 - LIQUIDACION DE RETIROS ERROR|SNB-1950]] LIQUIDACION DE RETIROS ERROR

## Descripcion

En los casos en que se retira por mostrador, medioEnvioId puede ser `3999` -> esta en la tabla `NewBytes_DBF.dbo.transpor`

para no ser disruptivo con los pedidos anteriores se adminte `NULL` y `0`



Entendiendo como `[3999, NULL , 0]` -> "`Retiro de cliente en Local`"
