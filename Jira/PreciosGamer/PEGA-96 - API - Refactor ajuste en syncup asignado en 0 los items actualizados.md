---
jira_key: "PEGA-96"
aliases: ["PEGA-96"]
summary: "API - Refactor ajuste en syncup asignado en 0 los items actualizados "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-07-01 15:00"
updated: "2024-07-09 03:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-96"
---

# PEGA-96: API - Refactor ajuste en syncup asignado en 0 los items actualizados 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-07-01 15:00 |
| Actualizado | 2024-07-09 03:51 |
| Etiquetas | ninguna |
| Jira | [PEGA-96](https://bluinc.atlassian.net/browse/PEGA-96) |

## Relaciones

- **Padre:** [[PEGA-6]] Feat - Listar productos

## Descripcion

Se agrego `initializeHide()`  en `SyncUpRepository::class` 

con el fin de poder pasar el campo `hide = 0` . al estar en este valor, se entiende que el item estaria actualizado y que cumple

 con los parametros globales, (actualmente son de `48hs`)
