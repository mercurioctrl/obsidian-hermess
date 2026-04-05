---
jira_key: "NBWEB-546"
aliases: ["NBWEB-546"]
summary: "API - Refactor - Precio especial MarketPlaces"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-05-29 06:04"
updated: "2023-08-04 09:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-546"
---

# NBWEB-546: API - Refactor - Precio especial MarketPlaces

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-29 06:04 |
| Actualizado | 2023-08-04 09:42 |
| Etiquetas | ninguna |
| Jira | [NBWEB-546](https://bluinc.atlassian.net/browse/NBWEB-546) |

## Relaciones

- **Padre:** [[NBWEB-544 - Refactor - Precios especiales por cliente y para marketplace|NBWEB-544]] Refactor - Precios especiales por cliente y para marketplace
- **blocks:** [[SNB-783 - Integracion - Producteca|SNB-783]] Integracion - Producteca

## Descripcion

Esta es una modalidad similar a la anterior (pero distinta :p). Se trata de poder aplicar un precio especial, pero en lugar de atarlo al costo, lo atamos al precio mayorista de un producto. 

Esta parte sucede por detrás al momento de cambiar el precio, por eso solo debemos modificar en `getPrice` lo logica de cuando/donde leer este precio

Se hace de la siguiente manera:

Cuando el cliente tiene marcado `[NewBytes_DBF].[dbo].[clientes].ntarifapp = 2` entonces asumimos que el precio asignado para ese cliente es el de marketplace que se encuentra en `[NewBytes_DBF].[dbo].[articulo].npvp2`

Por las dudas, en este momento `[NewBytes_DBF].[dbo].[articulo].npvp2` se encuentra todo en cero, porque es la primera vez que se utiliza.

Este precio tiene la misma jerarquia que `[NewBytes_DBF].[dbo].[clientes].ntarifapp = 5`
