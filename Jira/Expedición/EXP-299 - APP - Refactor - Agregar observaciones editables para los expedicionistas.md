---
jira_key: "EXP-299"
aliases: ["EXP-299"]
summary: "APP - Refactor - Agregar observaciones editables para los expedicionistas"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-05-29 06:35"
updated: "2023-05-31 17:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-299"
---

# EXP-299: APP - Refactor - Agregar observaciones editables para los expedicionistas

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-29 06:35 |
| Actualizado | 2023-05-31 17:35 |
| Etiquetas | ninguna |
| Jira | [EXP-299](https://bluinc.atlassian.net/browse/EXP-299) |

## Relaciones

- **Padre:** [[EXP-13 - Feat - Etiquetas y seguimiento|EXP-13]] Feat - Etiquetas y seguimiento
- **is blocked by:** [[EXP-300 - MS - Refactor - Agregar parametro de comentarios|EXP-300]] MS - Refactor - Agregar parametro de comentarios
- **is blocked by:** [[EXP-298 - API - Refactor - Agregar observaciones editables para los expedicionistas|EXP-298]] API - Refactor - Agregar observaciones editables para los expedicionistas

## Descripcion

Considerando que existe en cada una de las APIs de los transportes (OCA,Andreani,Entregar,etc, transporte propio) un campo para poner observaciones, que a su vez, sale en la etiqueta, atenderemos el reclamo de [https://lioteam.atlassian.net/browse/SNB-759](https://lioteam.atlassian.net/browse/SNB-759) donde se pide que agreguemos un campo para poner observaciones mas detalladas o de manera libre.

Este parámetro observaciones debe estar limitado en caracteres al máximo de caracteres permitidos por el transportista que menos caracteres permita.  

Se debe agregar un campo “obseravaciones” con limita de caracteres en el siguiente modal

[adjunto]
de forma tal que pueda enviar el parámetro en [link](https://lioteam.atlassian.net/browse/EXP-298)
