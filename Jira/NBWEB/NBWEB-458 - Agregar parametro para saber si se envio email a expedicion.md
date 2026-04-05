---
jira_key: "NBWEB-458"
aliases: ["NBWEB-458"]
summary: "Agregar parametro para saber si se envio email a expedicion"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Ezequiel manzano"
created: "2022-08-12 09:51"
updated: "2022-11-25 10:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-458"
---

# NBWEB-458: Agregar parametro para saber si se envio email a expedicion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Ezequiel manzano |
| Creado | 2022-08-12 09:51 |
| Actualizado | 2022-11-25 10:22 |
| Etiquetas | ninguna |
| Jira | [NBWEB-458](https://bluinc.atlassian.net/browse/NBWEB-458) |

## Relaciones

*Sin relaciones*

## Descripcion

Agregar parametro a la tabla de pedidos para ver si se envío el email



```
alter table NewBytes_DBF.dbo.pedclit
add emailed tinyint null
```
