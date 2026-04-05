---
jira_key: "SNB-27"
aliases: ["SNB-27"]
summary: "Crear stored procedure para automatizar la exclusion de percepciones de monotributistas"
status: "Finalizada"
type: "Nueva función"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Catriel Mercurio"
created: "2021-09-29 18:10"
updated: "2021-09-30 10:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-27"
---

# SNB-27: Crear stored procedure para automatizar la exclusion de percepciones de monotributistas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Nueva función |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Catriel Mercurio |
| Creado | 2021-09-29 18:10 |
| Actualizado | 2021-09-30 10:17 |
| Etiquetas | ninguna |
| Jira | [SNB-27](https://bluinc.atlassian.net/browse/SNB-27) |

## Relaciones

*Sin relaciones*

## Descripcion

UPDATE [NewBytes_DBF].[dbo].[clientes]
SET excluirPercepcion = 1
WHERE niva = 6 and excluirPercepcion <> 1;

UPDATE [NewBytes_DBF].[dbo].[clientes]
SET excluirPercepcion = 0
WHERE niva <> 6 and excluirPercepcion <> 0;
