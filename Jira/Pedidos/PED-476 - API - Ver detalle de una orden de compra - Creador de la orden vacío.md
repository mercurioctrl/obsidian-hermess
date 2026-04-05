---
jira_key: "PED-476"
aliases: ["PED-476"]
summary: "API - Ver detalle de una orden de compra - Creador de la orden vacío"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-01-15 02:34"
updated: "2024-01-26 05:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-476"
---

# PED-476: API - Ver detalle de una orden de compra - Creador de la orden vacío

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-01-15 02:34 |
| Actualizado | 2024-01-26 05:38 |
| Etiquetas | ninguna |
| Jira | [PED-476](https://bluinc.atlassian.net/browse/PED-476) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra
- **relates to:** [[PED-82 - API - Feat - Ver detalle de una orden de compra|PED-82]] API - Feat - Ver detalle de una orden de compra

## Descripcion

Al momento de obtener el detalle de una orden de compra el creador me aparece el creador vacío.
Pude observar que esto sucedía con ordenes que fueron creadas por el cliente.

[adjunto]
- Existen dos maneras de resolver esto, una cuando el campo `ccodageCreator` y `agentDescriptionCreator` de la tabla `NewBytes_DBF.dbo.pedclit` estén vacíos obtener como creador al cliente.


- Al momento de que el cliente desde el sitio de NB realice la compra, guardar sus datos en `ccodageCreator` y `agentDescriptionCreator` de la tabla `NewBytes_DBF.dbo.pedclit`. Me pareció que esta era la opción más adecuada por lo que me tome la libertad de crear la tarea, pero lo dejo a tu criterio.
[[NBWEB-609] API - Refactor - Procesar carrito - Guardar creador de la orden](https://lioteam.atlassian.net/browse/NBWEB-609)





Si se opta por la segunda opción habría que considerar el tomar los datos del detalle de la orden de la tabla 

`NewBytes_DBF.dbo.pedclit` y no de la tabla `NewBytes_DBF.dbo.agentes` como se hace actualmente

---

Actualización 16/01/24
Aún no puedo visualizar el creador del pedido

[adjunto]
