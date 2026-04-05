---
jira_key: "COB-459"
aliases: ["COB-459"]
summary: "API - Refactor - Agregar comentario al correo de edición de crédito"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-07-13 15:25"
updated: "2023-07-13 18:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-459"
---

# COB-459: API - Refactor - Agregar comentario al correo de edición de crédito

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-13 15:25 |
| Actualizado | 2023-07-13 18:33 |
| Etiquetas | ninguna |
| Jira | [COB-459](https://bluinc.atlassian.net/browse/COB-459) |

## Relaciones

- **Padre:** [[COB-374 - Feat - Editar estado crediticio de la cuenta del cliente|COB-374]] Feat - Editar estado crediticio de la cuenta del cliente

## Descripcion

En el recurso [link](https://lioteam.atlassian.net/browse/COB-377)  pide enviar un correo con el detalle de la asginacion de credito, pero el comentario que alli se introduce no lo vemos nunca mas, ya que no se visualiza en la cuenta corriente (no es una fila, ni un movimiento) y tampoco en el correo.

Lo que haremos entonces, es enviarlo con el correo para que las personas que lo reciben puedan leer la razón.

Por otro lado, haría obligatorio el comentario, en el caso de que no lo sea.
