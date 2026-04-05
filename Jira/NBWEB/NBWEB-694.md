---
jira_key: "NBWEB-694"
summary: "API - Feat - Recurso de validación cruzada (cross-validation)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-04-10 07:44"
updated: "2024-04-15 03:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-694"
---

# NBWEB-694: API - Feat - Recurso de validación cruzada (cross-validation)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-10 07:44 |
| Actualizado | 2024-04-15 03:45 |
| Etiquetas | ninguna |
| Jira | [NBWEB-694](https://bluinc.atlassian.net/browse/NBWEB-694) |

## Descripción

Crearemos un recurso que nos permite entender si distintas respuestas auto generadas, son validas para re evaluarlas mediante asistencia humana

El mismo se ejecuta en el front asignando una respuestra `true/false `



[attachment]
**¿que hace el recurso?**

Básicamente en 2 columnas nuevas que agregaremos y cuentan la cantidad de true / false recibidos y se lo suma en una columna especifica al dato que estamos validando 

**¿donde encontramos los datos?**

` [PRODUCTOS].[dbo].[iaDescriptions]`
