---
jira_key: "PED-221"
aliases: ["PED-221"]
summary: "APP - Mover item entre ordenes de compra - Incidencias varias"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2023-11-03 01:29"
updated: "2023-11-14 18:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-221"
---

# PED-221: APP - Mover item entre ordenes de compra - Incidencias varias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2023-11-03 01:29 |
| Actualizado | 2023-11-14 18:40 |
| Etiquetas | ninguna |
| Jira | [PED-221](https://bluinc.atlassian.net/browse/PED-221) |

## Relaciones

- **blocks:** [[PED-189]] APP - Feat - Mover item entre ordenes de compra
- **clones:** [[PED-230]] APP - Feat - Editar precio, se debe poder ingresar un precio a mano para un item determinado

## Descripcion

- **Agregar opción de crear una nueva orden**
De acuerdo a la tarea [link](https://lioteam.atlassian.net/browse/PED-189) es necesario agregar la opción de crear una nueva orden y que los productos seleccionados se muevan a esa orden recién creada.



[adjunto]
- **No es posible** **seleccionar este producto para moverlo** entre ordenes, aunque debería poder ya que el estado de la orden es pendiente y no tiene un pedido asignado.



`0002-10314844` 

[adjunto]
- **Se visualiza el código** en el campo precio, tal vez debe ser porque viene vacío en el back
`0002-10314782`



[adjunto]
- Me permite **mover un producto aun cuando la cantidad es cero**.



[adjunto]
---

Actualización 13/11/23

- Al crear la nueva orden los productos no se mueven a esa nueva orden creada.


- Me sigue permitiendo mover productos con cantidad en cero



[adjunto]
- Me aparece el siguiente código al mover productos a una orden



[adjunto]
