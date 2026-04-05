---
jira_key: "PEGA-101"
aliases: ["PEGA-101"]
summary: "API - Refactor - Syncup permitir sincronizacion de imagenes solo por parametro"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-08-08 09:59"
updated: "2024-08-25 21:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-101"
---

# PEGA-101: API - Refactor - Syncup permitir sincronizacion de imagenes solo por parametro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-08-08 09:59 |
| Actualizado | 2024-08-25 21:47 |
| Etiquetas | ninguna |
| Jira | [PEGA-101](https://bluinc.atlassian.net/browse/PEGA-101) |

## Relaciones

- **Padre:** [[PEGA-6]] Feat - Listar productos

## Descripcion

Se debe agregar un parametro que permitira agregar la actualización de imagenes por separado, con el fin de optimizar el syncup.

 

```
GET {API_URL/v1/sync/items/SYNC_TOKEN/img
```

**/img →** parametro agregado al final de la url, **no obligatorio **, en caso de no enviarse ejecuta el syncup sin actualizar las imaganes.

`SYNC_TOKEN` → se encuentra en el .env se utiliza como medida de validación.
