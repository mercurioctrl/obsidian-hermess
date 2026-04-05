---
jira_key: "PED-853"
aliases: ["PED-853"]
summary: "API - Refactor - Al crear/editar una orden se debe agregar el internalTax si corresponde en pedclil"
status: "Tareas por hacer"
type: "Subtarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2024-10-28 14:12"
updated: "2026-01-20 16:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-853"
---

# PED-853: API - Refactor - Al crear/editar una orden se debe agregar el internalTax si corresponde en pedclil

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-28 14:12 |
| Actualizado | 2026-01-20 16:55 |
| Etiquetas | ninguna |
| Jira | [PED-853](https://bluinc.atlassian.net/browse/PED-853) |

## Relaciones

- **Padre:** [[PED-34 - Generar Editar ordenes|PED-34]] Generar / Editar ordenes
- **has action item:** [[PED-851 - API - Refactor - Modificar los totales del pedido para incluir el internalTax|PED-851]] API - Refactor - Modificar los totales del pedido para incluir el internalTax
- **has action item:** [[PED-854 - API - Refactor - Guardar internalTax en albclil al generar el pedido|PED-854]] API - Refactor - Guardar internalTax en albclil al generar el pedido
- **has action item:** [[PED-1271 - API - Feat - Ver reservas en una orden de compra, en casos puntuales no|PED-1271]] API - Feat - Ver reservas en una orden de compra, en casos puntuales no coincide la cantidad de afuera, con el resultado del modal

## Descripcion

Agregaremos a la tabla de la db el parametro `[NewBytes_DBF].[dbo].[pedclil].internalTax`

```
PATCH {API_URL}/v1/orders/addItem
```

Cuando creamos o editamos una orden con un item que tiene `[NewBytes_DBF].[dbo].[articulo]`.`internalTax` entonces trasladamos el mismo dato a `[NewBytes_DBF].[dbo].[pedclil].internalTax` para dejar guardado cual era en ese momento.
