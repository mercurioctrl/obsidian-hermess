---
jira_key: "PEGA-52"
aliases: ["PEGA-52"]
summary: "API - Feat - Actualizar resellers"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-01-03 13:20"
updated: "2023-01-03 15:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-52"
---

# PEGA-52: API - Feat - Actualizar resellers

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-03 13:20 |
| Actualizado | 2023-01-03 15:50 |
| Etiquetas | ninguna |
| Jira | [PEGA-52](https://bluinc.atlassian.net/browse/PEGA-52) |

## Relaciones

- **Padre:** [[PEGA-50]] Feat - Update catalogos

## Descripcion

Esta historia trata sobre como guardar marcas nuevas en el repositorio de resellers.

Lo que vamos a hacer es buscar en la tabla de repositorios ` [PEGA].[dbo].[Repository]` buscando marcas que aun no fueron creadas en la tabla `PEGA.dbo.resellers`

La tabla brands tiene al menos las siguientes columnas

- id


- description


- createdDate



El recurso se ejecuta en 

```
GET {API_URL}/v1/sync/resellers/{token}
```

Devuelve un parametro succes para saber que se ejecuto y otro con la cantidad de marcas agregadas.

El parametro token se compara con una variable en `.env` llamado `SYNCTOKEN` que es para que cualquiera no ejecute el recurso
