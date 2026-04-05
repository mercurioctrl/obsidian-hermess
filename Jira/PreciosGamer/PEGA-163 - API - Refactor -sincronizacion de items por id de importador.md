---
jira_key: "PEGA-163"
aliases: ["PEGA-163"]
summary: "API - Refactor -sincronizacion de items por id de importador"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-01-03 13:07"
updated: "2025-01-27 17:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-163"
---

# PEGA-163: API - Refactor -sincronizacion de items por id de importador

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-01-03 13:07 |
| Actualizado | 2025-01-27 17:31 |
| Etiquetas | ninguna |
| Jira | [PEGA-163](https://bluinc.atlassian.net/browse/PEGA-163) |

## Relaciones

- **Padre:** [[PEGA-6]] Feat - Listar productos

## Descripcion

Se debe agregar un parametro `importerId` 

`GET /v1/sync/items/{token}?importerId=3041 -> libre opcion.`

Permitiendo actualizar unicamente items del correspondiente importador.
