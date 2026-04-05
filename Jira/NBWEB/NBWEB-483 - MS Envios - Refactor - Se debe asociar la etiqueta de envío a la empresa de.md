---
jira_key: "NBWEB-483"
aliases: ["NBWEB-483"]
summary: "MS Envios - Refactor - Se debe asociar la etiqueta de envío a la empresa de pertenencia que el cliente tiene asignado en el sistema"
status: "Code Review"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-09-08 10:29"
updated: "2022-09-09 08:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-483"
---

# NBWEB-483: MS Envios - Refactor - Se debe asociar la etiqueta de envío a la empresa de pertenencia que el cliente tiene asignado en el sistema

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-08 10:29 |
| Actualizado | 2022-09-09 08:52 |
| Etiquetas | ninguna |
| Jira | [NBWEB-483](https://bluinc.atlassian.net/browse/NBWEB-483) |

## Relaciones

- **Subtarea:** [[NBWEB-484]] API - Refactor - Etiqueta OCA
- **causes:** [[SNB-292]] MS - Refactor - Se debe asociar la etiqueta de envío a la empresa de pertenencia que el cliente tiene asignado en el sistema

## Descripcion

Segun 

```sql
/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 B.CNOMBRE
  FROM [NewBytes_DBF].[dbo].[clientes] A
  LEFT JOIN [NewBytes_DBF].[dbo].[FP_Empresas] B ON A.CODEMP = B.CODEMP
```

Mostrar siempre el nombre de la empresa correspondiente para cada cliente.
Si es null mostrar NB DISTRIBUIDORA MAYORISTA de la variable de entorno
