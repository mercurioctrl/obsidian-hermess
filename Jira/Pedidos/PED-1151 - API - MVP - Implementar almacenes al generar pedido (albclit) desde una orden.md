---
jira_key: "PED-1151"
aliases: ["PED-1151"]
summary: "API - MVP - Implementar almacenes al generar pedido (albclit) desde una orden de compra (pedclit)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-08 09:11"
updated: "2025-11-11 14:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1151"
---

# PED-1151: API - MVP - Implementar almacenes al generar pedido (albclit) desde una orden de compra (pedclit)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-08 09:11 |
| Actualizado | 2025-11-11 14:02 |
| Etiquetas | ninguna |
| Jira | [PED-1151](https://bluinc.atlassian.net/browse/PED-1151) |

## Relaciones

- **Padre:** [[PED-1107]] Almacenes Multiples
- **action item from:** [[PED-90]] API - Feat- Generar pedido (albclit) desde una orden de compra (pedclit)

## Descripcion

Así como lo hicimos en [link](https://bluinc.atlassian.net/browse/PED-90)  hace mucho, lo que debemos hacer es que a la lógica de genear un pedido desde una orden, tambien lo alcance el refactor para contemplar distintos ALMACENES

Para esto nos enfocaremos en **Generar detalle (por cada ítem del pedido), recordemos que lo que hace es**

- Obtener el stock actual desde `[NewBytes_DBF].[dbo].stock` pero teniendo en cuenta `ID_ALMACEN` .


- Validar que `ncanped <= nstock` siempre respetando `ID_ALMACEN` tanto para pedclil.`ncanped` como para `stock.nstock`.

- Si no hay stock suficiente → eliminar cabecera y finalizar proceso.




- Si hay stock suficiente, **acumular las siguientes querys** sin ejecutarlas todavía:

- 🔹 **Update de stock:**
`UPDATE stock SET nstock = nstock - {cantidad} WHERE ID_ARTICULO = ? AND ID_ALMACEN = ?`


- 🔹 **Insert en registro de historial:**
Insert en `[NB_WEB].[dbo].[registro_stock]` con detalle del movimiento.
Aquí sera necesario agregar la columna `[NB_WEB].[dbo].[registro_stock].stockWarehouseId` que aun no existe, para marcar el movimiento con el `ID_ALMACEN` (lamentablemente tenemos que mantener el nombre viejo o nuevo para cada tabla donde ya existía)


- 🔹 **Insert del detalle del pedido:**
Insert en `[NewBytes_DBF].[dbo].[albclil]` con cantidad, precio, IVA, etc.
Acá debemos agregar tambien la columna `[NewBytes_DBF].[dbo].[albclil].stockWarehouseId` para poder marcarla correctamente.


- 🔹 **Update de stock posterior:**
Actualiza `sPosterior` en el historial con el nuevo valor total de stock en `registro_stock`.
