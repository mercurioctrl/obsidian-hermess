---
jira_key: "EXP-190"
aliases: ["EXP-190"]
summary: "API - Refactor - Ocultar los anulados en listado de envios y listado de retiros"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-01-27 14:46"
updated: "2023-01-27 16:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-190"
---

# EXP-190: API - Refactor - Ocultar los anulados en listado de envios y listado de retiros

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-27 14:46 |
| Actualizado | 2023-01-27 16:15 |
| Etiquetas | ninguna |
| Jira | [EXP-190](https://bluinc.atlassian.net/browse/EXP-190) |

## Relaciones

- **Padre:** [[EXP-15]] Feat - Serializar salida

## Descripcion

Existen dos columnas en dos tablas diferentes

`NEW_BYTES.dbo.MS_REMITOS_CABECERA.ANULADO`

`NEW_BYES.dbo.MS_VENTAS_REMITO.ANULADO`

Que cuando toman valor `SI` no deberían mostrarse

aplica tanto a la lista de envíos, como de retiros
