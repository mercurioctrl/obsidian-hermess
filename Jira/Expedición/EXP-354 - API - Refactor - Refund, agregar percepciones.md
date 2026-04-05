---
jira_key: "EXP-354"
aliases: ["EXP-354"]
summary: "API - Refactor - Refund, agregar percepciones"
status: "Tareas por hacer"
type: "Subtarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2023-08-03 09:38"
updated: "2023-08-03 09:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-354"
---

# EXP-354: API - Refactor - Refund, agregar percepciones

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-03 09:38 |
| Actualizado | 2023-08-03 09:52 |
| Etiquetas | ninguna |
| Jira | [EXP-354](https://bluinc.atlassian.net/browse/EXP-354) |

## Relaciones

- **Padre:** [[EXP-117]] Feat - Listar pedidos despachados para hacer devoluciones

## Descripcion

Refactorizar el siguiente recurso para agregar el parámetro de percepciones

```
GET {API_URL}/v1/refund/{pedido}
```

El parametro que debemos agregar es

`[NEW_BYTES].[dbo].[MS_REMITO_CABECERA].IMPPERCEP`
