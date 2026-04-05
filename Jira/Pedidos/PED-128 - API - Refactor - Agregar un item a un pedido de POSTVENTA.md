---
jira_key: "PED-128"
aliases: ["PED-128"]
summary: "API - Refactor - Agregar un item a un pedido de POSTVENTA"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-10-09 14:32"
updated: "2024-11-25 02:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-128"
---

# PED-128: API - Refactor - Agregar un item a un pedido de POSTVENTA

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-09 14:32 |
| Actualizado | 2024-11-25 02:56 |
| Etiquetas | ninguna |
| Jira | [PED-128](https://bluinc.atlassian.net/browse/PED-128) |

## Relaciones

- **Padre:** [[PED-91 - APP - Feat - Generar pedido|PED-91]] APP - Feat - Generar pedido

## Descripcion

Haremos un refactor para el recurso que nos permite meter un ítem (o alterarlo) dentro de un pedido de POSTVENTA.

En este caso debemos validar que en una orden de POSTVENTA sucursal `0003`  solo pueden ingresar items que estén en stock de postventa (`[NewBytes_DBF].[dbo].[stocks]`.`nstock_postventa`)

```
PATCH /v1/orders/addItem
```

```
{
  "order":"10370978",
  "branch":"0003",
  "itemId":118990,
  "amount":1
}
```

Cuando se trate de un pedido de POSTVENTA (`0003`) entonces solo puedo meter tanta cantidad como exista en  `[NewBytes_DBF].[dbo].[stocks]`.`nstock_postventa` de lo contrario me dará un error especificado el motivo por el cual no se puede meter dentro del pedido (Para ingresar in ítem en un pedido de postventa primero deben hacer un pase desde deposito a postventa).

Solo se pueden tomar tanta cantidad de items/unidades como tenga en ese stock de postventa.
