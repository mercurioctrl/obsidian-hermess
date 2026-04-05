---
jira_key: "COB-364"
aliases: ["COB-364"]
summary: "API - Refactor - Agregar columna \"datetime\" automtica en la tabla [NEW_BYTES].[dbo].[MC_SALDOS_CAJA]"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-16 11:05"
updated: "2023-04-11 09:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-364"
---

# COB-364: API - Refactor - Agregar columna "datetime" automtica en la tabla [NEW_BYTES].[dbo].[MC_SALDOS_CAJA]

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-16 11:05 |
| Actualizado | 2023-04-11 09:34 |
| Etiquetas | ninguna |
| Jira | [COB-364](https://bluinc.atlassian.net/browse/COB-364) |

## Relaciones

- **Padre:** [[COB-347]] Poder ver saldo inicial y final de caja en cada día

## Descripcion

Solo agregaremos la columnas `createdAt` y le pondremos de valor inicial `GETDATE()`
