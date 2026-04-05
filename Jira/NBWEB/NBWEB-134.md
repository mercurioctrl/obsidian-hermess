---
jira_key: "NBWEB-134"
summary: "Sys - Crear tabla para confirmacion de cuenta"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Ezequiel manzano"
created: "2022-04-25 12:11"
updated: "2022-04-26 15:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-134"
---

# NBWEB-134: Sys - Crear tabla para confirmacion de cuenta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Ezequiel manzano |
| Creado | 2022-04-25 12:11 |
| Actualizado | 2022-04-26 15:25 |
| Etiquetas | ninguna |
| Jira | [NBWEB-134](https://bluinc.atlassian.net/browse/NBWEB-134) |

## Descripción

CREATE TABLE [dbo].[account_confirmation](
 [id] [int] IDENTITY(1,1) NOT NULL,
 [token] [varchar](50) NOT NULL,
 [sender] [varchar](50) NOT NULL,
 [exp_date] [datetime] NOT NULL)
