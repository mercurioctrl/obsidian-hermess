---
jira_key: "POS-235"
aliases: ["POS-235"]
summary: "Postventa Proveedores Recepcion"
status: "En curso"
type: "Historia"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2023-03-08 12:05"
updated: "2023-03-14 12:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-235"
---

# POS-235: Postventa Proveedores Recepcion

| Campo | Valor |
|-------|-------|
| Estado | En curso (En curso) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-08 12:05 |
| Actualizado | 2023-03-14 12:02 |
| Etiquetas | ninguna |
| Jira | [POS-235](https://bluinc.atlassian.net/browse/POS-235) |

## Relaciones

- **Padre:** [[POS-230 - Postventa Proveedores|POS-230]] Postventa Proveedores
- **Subtarea:** [[POS-236 - API - Feat - Listar articulos pendientes de recepcion para postventa proveedores|POS-236]] API - Feat - Listar articulos pendientes de recepcion para postventa proveedores
- **Subtarea:** [[POS-239 - APP - Feat - Listar depósitos, pestaña depositos|POS-239]] APP - Feat - Listar depósitos, pestaña depositos
- **Subtarea:** [[POS-240 - APP - Feat - Modal crear deposito en la pestaña depositos.|POS-240]] APP - Feat - Modal crear deposito en la pestaña depositos.
- **Subtarea:** [[POS-241 - APP - Feat - Agregar pestaña y lista de articulos pendientes de recepcion para|POS-241]] APP - Feat - Agregar pestaña y lista de articulos pendientes de recepcion para postventa proveedores
- **Subtarea:** [[POS-243 - API - Feat - Mover items a un deposito|POS-243]] API - Feat - Mover items a un deposito
- **Subtarea:** [[POS-244 - API - Feat - Enviar items al proveedor|POS-244]] API - Feat - Enviar items al proveedor
- **Subtarea:** [[POS-246 - APP - Feat - Modal mover items a un deposito|POS-246]] APP - Feat - Modal mover items a un deposito
- **Subtarea:** [[POS-247 - APP - Refactor - Cambiar pestaña proveedores por Recuperos|POS-247]] APP - Refactor - Cambiar pestaña "proveedores" por "Recuperos"
- **Subtarea:** [[POS-250 - API - Refactor - Agregar statusId a cada item de la lista de recuperos|POS-250]] API - Refactor - Agregar statusId a cada item de la lista de "recuperos"
- **Subtarea:** [[POS-251 - API - Feat - Mandar productos a recupero|POS-251]] API - Feat - Mandar productos a recupero
- **Subtarea:** [[POS-252 - APP - Feat - Mandar productos a recupero|POS-252]] APP - Feat - Mandar productos a recupero
- **Subtarea:** [[POS-259 - API - Refactor - Cuando se listan los articulos pendientes no deben mostraste|POS-259]] API - Refactor - Cuando se listan los articulos pendientes no deben mostraste aquellos que ya estan en un deposito distinto a el de postventa 
- **Subtarea:** [[POS-260 - API - Feat - Mostrar listado de envios a proveedores|POS-260]] API - Feat - Mostrar listado de "envios a proveedores"
- **Subtarea:** [[POS-261 - APP - Feat - Mostrar listado de envios a proveedores|POS-261]] APP - Feat - Mostrar listado de "envios a proveedores"
- **Subtarea:** [[POS-263 - API - Refactor - Listar articulos - mostrar informacion del deposito actual|POS-263]] API - Refactor - Listar articulos -> mostrar informacion del deposito actual
- **Subtarea:** [[POS-264 - APP - Feat - Listar articulos - Mostrar informacion del deposito actual|POS-264]] APP - Feat - Listar articulos -> Mostrar informacion del deposito actual 
- **Subtarea:** [[POS-265 - APP - Feat - Mandar productos recuperados a proveedores|POS-265]] APP - Feat - Mandar productos recuperados a proveedores
- **Subtarea:** [[POS-266 - API - Feat - Generar planilla de los productos recuperados enviados a|POS-266]] API - Feat - Generar planilla de los productos recuperados enviados a proveedores
- **Subtarea:** [[POS-267 - API - Db - Dar de alta los proveedores especificos que estan en los depositos|POS-267]] API - Db - Dar de alta los proveedores especificos que estan en los depositos
- **Subtarea:** [[POS-268 - APP -Feat - Marcar rechazados en enviados a proveedores|POS-268]] APP -Feat - Marcar rechazados en enviados a proveedores

## Descripcion

La sección consiste en un listado de productos, particularizados por numero de serie que tienen que listarse para poder ser recepcionados por el sector correspondiente.

Los productos en cuestión, son aquellos productos que provienen de cambios/acreditaciones de los casos de postventa.

Y desde este listado es desde donde se les da un destino, ya sea un deposito nuevo o se hace un envió al proveedor.
