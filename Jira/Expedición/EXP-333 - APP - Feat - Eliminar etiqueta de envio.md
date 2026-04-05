---
jira_key: "EXP-333"
aliases: ["EXP-333"]
summary: "APP - Feat - Eliminar etiqueta de envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-07-05 09:19"
updated: "2023-07-24 08:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-333"
---

# EXP-333: APP - Feat - Eliminar etiqueta de envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-05 09:19 |
| Actualizado | 2023-07-24 08:54 |
| Etiquetas | ninguna |
| Jira | [EXP-333](https://bluinc.atlassian.net/browse/EXP-333) |

## Relaciones

- **Padre:** [[EXP-13 - Feat - Etiquetas y seguimiento|EXP-13]] Feat - Etiquetas y seguimiento
- **is blocked by:** [[EXP-331 - API - Feat - Eliminar etiqueta de envio|EXP-331]] API - Feat - Eliminar etiqueta de envio

## Descripcion

Agregaremos un nuevo “boton” operador, a los pedidos que tienen etiqueta

[adjunto]
Lo que se necesita en esos casos, es agregar uno mas, que sirve para borrar la etiqueta (para cuando se equivocan, actualmente se lo piden a sistemas).

Para poder hacerlo usaremos el recurso [link](https://lioteam.atlassian.net/browse/EXP-331) 

Es importante que antes de ejecutar el recurso mostremos un mensaje de “¿Esta seguro que desea eliminar la etiqueta para el pedido xxxx? Esta acción es irreversible.”

Ademas cabe tener en cuenta que si el pedido ya fue Entregado (en cualquiera de sus estados entregados) el botoncito aparece “disabled”

Si tenes consultas, no dudes en preguntarme.
