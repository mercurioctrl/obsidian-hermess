---
jira_key: "NBWEB-601"
aliases: ["NBWEB-601"]
summary: "APP - Refactor - Precalcular campos segun la logica establecida"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-11-28 09:28"
updated: "2023-11-29 10:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-601"
---

# NBWEB-601: APP - Refactor - Precalcular campos segun la logica establecida

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-28 09:28 |
| Actualizado | 2023-11-29 10:55 |
| Etiquetas | ninguna |
| Jira | [NBWEB-601](https://bluinc.atlassian.net/browse/NBWEB-601) |

## Relaciones

- **Padre:** [[NBWEB-600]] Cotizaciones

## Descripcion

[adjunto]
Solo cuando cambio **A**

- Seteo **B** y **D** con el Mismo valor que puse en **A**


- Seteo **E** y** F** con el valor de **A** + 10% (el 10 estará en el .env)


- Seteo **G** con el valor de **A** - 10% (el 10 estará en el .env)



Esto sucede solo cuando toco **A. **Todo lo demas cuando lo tocas, solo se cambia a si mismo. De esta forma podremos retocar algo si asi lo deseamos una vez que cambiamos A.
