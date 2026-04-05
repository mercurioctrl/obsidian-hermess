---
jira_key: "STASK-13"
aliases: ["STASK-13"]
summary: "TASK - Marcar envíos que llegaron a destino - Oportunidad de mejora en la fecha almacenada"
status: "Tareas por hacer"
type: "Tarea"
priority: "Lowest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-02-19 10:54"
updated: "2025-02-19 11:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-13"
---

# STASK-13: TASK - Marcar envíos que llegaron a destino - Oportunidad de mejora en la fecha almacenada

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Tarea |
| Prioridad | Lowest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-02-19 10:54 |
| Actualizado | 2025-02-19 11:05 |
| Etiquetas | ninguna |
| Jira | [STASK-13](https://bluinc.atlassian.net/browse/STASK-13) |

## Relaciones

- **Padre:** [[STASK-7]] Tares de evaluacion y estadisticas
- **action item from:** [[STASK-5]] TASK - Marcar envíos que llegaron a destino

## Descripcion

Según lo platicado en la daily, se identificó una oportunidad de mejora que consiste en modificar el almacenamiento de la fecha actual. En lugar de guardar la fecha en que se ejecuta la sincronización, se propone almacenar la fecha en que se realizó la entrega.

`[NewBytes_DBF].[dbo].[pedclit].delivered`

```
PATCH {{API_URL}}/v1/syncUp/markAsDelivered
```

[adjunto]
[adjunto]
