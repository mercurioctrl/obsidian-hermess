---
jira_key: "PEGA-73"
summary: "API - Refactor - Solo mostraremos aquellos productos que se actualizaron en las ultimas horas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-05-15 08:42"
updated: "2024-05-31 20:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-73"
---

# PEGA-73: API - Refactor - Solo mostraremos aquellos productos que se actualizaron en las ultimas horas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-05-15 08:42 |
| Actualizado | 2024-05-31 20:27 |
| Etiquetas | ninguna |
| Jira | [PEGA-73](https://bluinc.atlassian.net/browse/PEGA-73) |

## Descripción

```
GET {API_URL}/v1/items
```

Dado que aun no tenemos disponible un parámetro certero de stock, utilizaremos este criterio para poder leer aquellos que si aparecen en hardgamers basándonos en la fecha de ultimo scrappeo según `[PEGA].[dbo].[Repository]`

Para esto crearemos una tabla de parámetros globales donde iremos introduciendo algunos criterios, el primero: `HoursSinceLastUpdate` es decir una cantidad de horas, por ejemplo 48hs.

Joineando anmbas tablas puedo solo listar aquellos que encontre en las ultimas 24hs y dejar de lado todos aquellos que no pude verificar el stock de una forma mas precisa.
