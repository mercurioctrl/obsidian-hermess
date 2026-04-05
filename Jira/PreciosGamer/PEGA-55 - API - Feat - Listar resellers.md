---
jira_key: "PEGA-55"
aliases: ["PEGA-55"]
summary: "API - Feat - Listar resellers"
status: "Gamma"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-01-11 15:57"
updated: "2023-01-27 16:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-55"
---

# PEGA-55: API - Feat - Listar resellers

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-11 15:57 |
| Actualizado | 2023-01-27 16:43 |
| Etiquetas | ninguna |
| Jira | [PEGA-55](https://bluinc.atlassian.net/browse/PEGA-55) |

## Relaciones

- **Padre:** [[PEGA-1 - Bases y repositorios|PEGA-1]] Bases y repositorios

## Descripcion

Basado en ` [PEGA].[dbo].[resellers]` listar las marcas en

```
GET {API_URL}/v1/resellers?search={}
```

Se debe poder paginar.

El orden es alfabético por defecto

También se agrega el parámetro search para filtrar con un like.

Muestra los atributos id y descripcion
