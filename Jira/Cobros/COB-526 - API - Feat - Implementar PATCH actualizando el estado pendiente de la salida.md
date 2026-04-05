---
jira_key: "COB-526"
aliases: ["COB-526"]
summary: "API - Feat - Implementar PATCH actualizando el estado pendiente de la salida "
status: "Finalizada"
type: "Tarea"
priority: "Highest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-07-10 12:15"
updated: "2024-07-21 23:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-526"
---

# COB-526: API - Feat - Implementar PATCH actualizando el estado pendiente de la salida 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Highest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-07-10 12:15 |
| Actualizado | 2024-07-21 23:05 |
| Etiquetas | ninguna |
| Jira | [COB-526](https://bluinc.atlassian.net/browse/COB-526) |

## Relaciones

- **Padre:** [[COB-19 - Cola de salidas|COB-19]] Cola de salidas

## Descripcion

Recursos afectados

 →  `POST /bankTransfers`

→  `POST /cashOut`



Se agrega la propiedad `id` a ambos recurso con el fin de poder identificar su precarga y actualizar su estado `pending` a `false`

Ademas se registra `movement_id` generado segun el tipo y se marca la fecha de operación . `updated_at`  

Tabla utlizada: `NEW_BYTES.dbo.PendingCashOut`
