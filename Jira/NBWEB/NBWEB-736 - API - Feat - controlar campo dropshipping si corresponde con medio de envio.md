---
jira_key: "NBWEB-736"
aliases: ["NBWEB-736"]
summary: "API - Feat - controlar campo dropshipping si corresponde con medio de envio habilitado"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-05-21 17:02"
updated: "2024-05-22 17:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-736"
---

# NBWEB-736: API - Feat - controlar campo dropshipping si corresponde con medio de envio habilitado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-05-21 17:02 |
| Actualizado | 2024-05-22 17:39 |
| Etiquetas | ninguna |
| Jira | [NBWEB-736](https://bluinc.atlassian.net/browse/NBWEB-736) |

## Relaciones

- **is blocked by:** [[SNB-1836 - MOTO DROPSHIPPING|SNB-1836]] MOTO DROPSHIPPING
- **causes:** [[NBWEB-737 - APP - Refactor Al procesar el carrito y recibir el error debe ser posible|NBWEB-737]] APP - Refactor: Al procesar el carrito y recibir el error debe ser posible mostrar el mensaje con el nuevo objeto entregado por la api

## Descripcion

Si se procesa una compra como dropshipping, controlar si existe campo “dropshipping“:”true” , con el fin de verificar si el medio de envio es permitido en este caso. 

En caso de ser moto o camioneta.

deberia retornar una excepcion aclarando que es posible seleccionar estos medios de envios.



Ejemplo de response, en caso de que se intente asignar un transportista no valido para Dropshipping.

```
{
    "success": false,
    "message": "De seleccionar dropShipping, el medio de envío solo puede ser: OCA, Andreani, Entregar",
    "code": 400
}
```



Los Transportista en el `"message",` son los asignados como `activoDropshipping = 1` en la tabla `LO.[dbo].[mediosEnvio]`   los cuales se pueden activar o desactivar desde CMS.
