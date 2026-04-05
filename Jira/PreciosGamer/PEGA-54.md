---
jira_key: "PEGA-54"
summary: "API - Feat - Listar marcas"
status: "Gamma"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-01-11 15:57"
updated: "2023-01-27 16:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-54"
---

# PEGA-54: API - Feat - Listar marcas

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-11 15:57 |
| Actualizado | 2023-01-27 16:41 |
| Etiquetas | ninguna |
| Jira | [PEGA-54](https://bluinc.atlassian.net/browse/PEGA-54) |

## Descripción

Basado en ` [PEGA].[dbo].[brands]` listar las marcas en

```
GET {API_URL}/v1/brands?search={}
```

Se debe poder paginar.

El orden es alfabético por defecto

También se agrega el parámetro search para filtrar con un like

Muestra los atributos id y descripcion
