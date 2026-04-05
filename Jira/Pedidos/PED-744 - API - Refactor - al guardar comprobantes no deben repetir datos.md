---
jira_key: "PED-744"
aliases: ["PED-744"]
summary: "API - Refactor - al guardar comprobantes no deben repetir datos"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-06-13 15:50"
updated: "2024-06-14 18:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-744"
---

# PED-744: API - Refactor - al guardar comprobantes no deben repetir datos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-06-13 15:50 |
| Actualizado | 2024-06-14 18:37 |
| Etiquetas | ninguna |
| Jira | [PED-744](https://bluinc.atlassian.net/browse/PED-744) |

## Relaciones

- **is blocked by:** [[SNB-1999]] Liquidaciones que estan duplicadas

## Descripcion

Dentro del mismo payload no se debe permitir el mismo nro de operacion.



si bien esto no es lo que ocurrio en el reporte, es una mejora para evitar cargas duplicadas de comprobantes.



En la misma rama de esta tarea se realizo el ajuste para evitar duplicar los importes al listar ordenes con varios voucher cargados.
