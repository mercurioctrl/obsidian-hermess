---
jira_key: "PED-238"
aliases: ["PED-238"]
summary: "API - Refactor - Precios para sucursal 10"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-11-07 09:10"
updated: "2023-11-07 13:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-238"
---

# PED-238: API - Refactor - Precios para sucursal 10

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-07 09:10 |
| Actualizado | 2023-11-07 13:38 |
| Etiquetas | ninguna |
| Jira | [PED-238](https://bluinc.atlassian.net/browse/PED-238) |

## Relaciones

- **Padre:** [[PED-237]] Precios

## Descripcion

Cuando estoy editando un pedido de sucursal 10, los precios se calculan de manera diferente.

En principio, el IVA siempre es 0. Osea que el IVA para ese producto se marca en cero en pedclil (y posteriormente se pasa de la misma forma a albclil).

Por otro lado, el precio base, tiene un sobrecargo obtenido desde el repositorio de clientes para ese cliente en base al IVA del producto. ` [NewBytes_DBF].[dbo].[clientes].superOfertaDto` 

### Conecpto:

Si `superOfertaDto` = `50`, entonces eso quiere decir que solo tomare en consideración el `50%` del IVA.

Entonces, si para ese item el IVA es `21`, mi nuevo IVA es `10.5`. Pero no se agrega como IVA, sino como un incremento al producto.

### Ejemplo:

**Prrecio producto:** 100

**Iva producto: **10.5

**superOfertaDto: **50

**precioFinal** =  100 + (100×(10,5* 50/100)÷100)

**ivaFinal**= 0
