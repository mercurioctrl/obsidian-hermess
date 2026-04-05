---
jira_key: "PEGA-64"
aliases: ["PEGA-64"]
summary: "API - Feat - Listar destacados para la home"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2024-05-03 10:24"
updated: "2024-05-28 21:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-64"
---

# PEGA-64: API - Feat - Listar destacados para la home

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2024-05-03 10:24 |
| Actualizado | 2024-05-28 21:45 |
| Etiquetas | ninguna |
| Jira | [PEGA-64](https://bluinc.atlassian.net/browse/PEGA-64) |

## Relaciones

- **Padre:** [[PEGA-6]] Feat - Listar productos
- **blocks:** [[PEGA-65]] APP - Feat  Listar destacados para la home
- **is blocked by:** [[PEGA-83]] API - Listar destacados para la home - Validación del parámetro featured

## Descripcion

Puede ser un parametro para filtrar los destacados de los productos como se hizo en con el parametro 

```
rate: up/down
```

Estos productos son los que se marcan desde el cms

Agregar `featured` a Tabla PEGA.dbo.Items



Params query para obtener los descatados.

`GET /v1/items?featured=true`
