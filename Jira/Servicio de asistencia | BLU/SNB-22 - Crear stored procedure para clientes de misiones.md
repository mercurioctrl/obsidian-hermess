---
jira_key: "SNB-22"
aliases: ["SNB-22"]
summary: "Crear stored procedure para clientes de misiones"
status: "Finalizada"
type: "Nueva función"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2021-09-29 10:37"
updated: "2021-09-29 18:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-22"
---

# SNB-22: Crear stored procedure para clientes de misiones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Nueva función |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2021-09-29 10:37 |
| Actualizado | 2021-09-29 18:10 |
| Etiquetas | ninguna |
| Jira | [SNB-22](https://bluinc.atlassian.net/browse/SNB-22) |

## Relaciones

*Sin relaciones*

## Descripcion

UPDATE 
[NewBytes_DBF].[dbo].[clientes]
SET CODEMP = 5
WHERE ID_PROVINCIA = 21 AND CODEMP <> 5
