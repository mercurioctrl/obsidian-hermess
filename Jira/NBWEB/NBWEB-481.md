---
jira_key: "NBWEB-481"
summary: "Correccion en el form de postventa al buscar por numero de serie"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2022-08-29 16:29"
updated: "2022-11-25 10:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-481"
---

# NBWEB-481: Correccion en el form de postventa al buscar por numero de serie

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2022-08-29 16:29 |
| Actualizado | 2022-11-25 10:22 |
| Etiquetas | ninguna |
| Jira | [NBWEB-481](https://bluinc.atlassian.net/browse/NBWEB-481) |

## Descripción

[attachment]
Se hizo un cambio en el front para poder recibir el caracter “/”, parseando por un “*”
ejemplo: `https://gamma.api.nb.com.ar/v1/postventa/serial/S*N:WE4791013661`
 
De tu lado solo debes reemplazar de nuevo por “/” para hacer el match
