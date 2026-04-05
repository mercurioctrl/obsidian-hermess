---
jira_key: "PED-244"
aliases: ["PED-244"]
summary: "API - Refactor - Ver detalle de una orden de compra -> Agregar \"Letra\" de item, rentabilidad porcentual y ganancia"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-11-08 09:20"
updated: "2024-01-04 19:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-244"
---

# PED-244: API - Refactor - Ver detalle de una orden de compra -> Agregar "Letra" de item, rentabilidad porcentual y ganancia

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-08 09:20 |
| Actualizado | 2024-01-04 19:31 |
| Etiquetas | ninguna |
| Jira | [PED-244](https://bluinc.atlassian.net/browse/PED-244) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra
- **blocks:** [[PED-245 - APP - Refactor - Modal Ver pedido Agregar Letra de item, rentabilidad|PED-245]] APP - Refactor - Modal Ver pedido > Agregar "Letra" de item, rentabilidad porcentual y ganancia

## Descripcion

### Criterios de aceptación

- Agregar letra correspondiente al precio seleccionado


- Mostrar la rentabilidad porcentual


- Mostrar la ganancia nominal (En dolares)



1- Es la que surge de la clase precios, si es a mano, tambien se debe mostrar PM, etc.

2 y 3 - Este punto funciona de la siguiente manera, tanto para obtener la ganancia como la rentabilidad es necesario saber el costo. El costo es dinámico hasta el momento de la liquidación. Por lo tanto, en un pedido que aun no fue liquidado el costo se tomara de `[NewBytes_DBF].[dbo].[articulo].ncosteprom` 
En cambio si el mismo ya fue liquidado, se toma el estado congelado de ese costo al momento de la liquidación, es decir:  `[NEW_BYTES].[dbo].[MS_REMITO_DETALLE_GANANCIA_ENLACE].COSTO`

Recordar multiplicar por la cantidad
