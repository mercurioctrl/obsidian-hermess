---
jira_key: "PED-509"
aliases: ["PED-509"]
summary: "API - Review - Falta cambiar un parametro al cambiar el vendedor de un cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-22 14:55"
updated: "2024-01-26 05:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-509"
---

# PED-509: API - Review - Falta cambiar un parametro al cambiar el vendedor de un cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-22 14:55 |
| Actualizado | 2024-01-26 05:36 |
| Etiquetas | ninguna |
| Jira | [PED-509](https://bluinc.atlassian.net/browse/PED-509) |

## Relaciones

- **Padre:** [[PED-16]] Listar clientes

## Descripcion

Al cambiar el vendedor que tiene un cliente determinado,  cambia `[NewBytes_DBF].[dbo].[clientes]`.`ID_VENDEDOR`, pero no cambia `[NewBytes_DBF].[dbo].[clientes]`.`CCCODAGE`

Algo importante, ccodage es un string de dos cifras. Es decir que si por ejemplo ID_VENDEDOR es 8, entonces ccodage es '08'
