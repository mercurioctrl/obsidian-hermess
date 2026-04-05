---
jira_key: "COM-109"
aliases: ["COM-109"]
summary: "Generar INGRESO o pedido (a partir de una orden de compra)"
status: "Tareas por hacer"
type: "Historia"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2024-06-18 09:13"
updated: "2024-06-18 09:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-109"
---

# COM-109: Generar INGRESO o pedido (a partir de una orden de compra)

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-18 09:13 |
| Actualizado | 2024-06-18 09:45 |
| Etiquetas | ninguna |
| Jira | [COM-109](https://bluinc.atlassian.net/browse/COM-109) |

## Relaciones

- **Padre:** [[COM-8 - Ordenes de compra|COM-8]] Ordenes de compra
- **Subtarea:** [[COM-110 - API - Generar un ingreso|COM-110]] API - Generar un ingreso
- **Subtarea:** [[COM-129 - APP - Refactor - Generar un ingreso en base a una orden|COM-129]] APP - Refactor - Generar un ingreso en base a una orden
- **Subtarea:** [[COM-151 - API - Review - Problemas al generar un registro cuando hago el INGRESO|COM-151]] API - Review - Problemas al generar un registro cuando hago el INGRESO
- **Subtarea:** [[COM-170 - API - Refactor - Cambiar de estado la orden, cuando ya se hicieron todos los|COM-170]] API - Refactor - Cambiar de estado la orden, cuando ya se hicieron todos los ingresos posible
- **Subtarea:** [[COM-171 - APP - Refactor - Sacar opcion de ingresar, ya que con partial quedo disfuncional|COM-171]] APP - Refactor - Sacar opcion de ingresar, ya que con "partial" quedo disfuncional
- **Subtarea:** [[COM-173 - API - Refactor - Modificar valor iniciar de lfacturado|COM-173]] API - Refactor - Modificar valor iniciar de lfacturado
- **Subtarea:** [[COM-190 - API -MVP - Refactor - Elegir si altera o no el costo promedio del item para|COM-190]] API -MVP - Refactor - Elegir si altera o no el costo promedio del item para cada item
- **Subtarea:** [[COM-191 - APP -MVP - Refactor - Elegir si altera o no el costo promedio del item para|COM-191]] APP -MVP - Refactor - Elegir si altera o no el costo promedio del item para cada item
- **Subtarea:** [[COM-202 - API - MVP - Refactor - Al generar un PEDIDO DE COMPRA o ingreso, se deben|COM-202]] API - MVP - Refactor - Al generar un PEDIDO DE COMPRA o ingreso, se deben enviar las cosas al deposito corresponiente warehousesId (ID_ALMACEN)
- **Subtarea:** [[COM-216 - API - MVP - Refactor - Cada que se haga un ingreso revisar para cambiar el|COM-216]] API - MVP - Refactor  - Cada que se haga un ingreso revisar para cambiar el estado de la orden en caso que sean iguales la cantidad ingresadas que las totales para todos los items
- **Subtarea:** [[COM-251 - API - MVP - Review - Generar ingreso - Diferencia de IVA al finalizar la orden|COM-251]] API - MVP - Review - Generar ingreso -> Diferencia de IVA al finalizar la orden
- **Subtarea:** [[COM-271 - APP - MVP - Review - Cuando se hace un ingreso parcial los productos que no|COM-271]] APP - MVP - Review - Cuando se hace un ingreso parcial los productos que no tienen cantidad o carga, no hay que agregarlos al objeto, caso contrario da error si el mismo esta completo
- **Subtarea:** [[COM-272 - API - MVP - Review - Cuando una orden genera un ingreso que no tiene marcado el|COM-272]] API - MVP - Review - Cuando una orden genera un ingreso que no tiene marcado el costo promedio, el costo debe ser el mismo que lleva la orden directo
- **Subtarea:** [[COM-273 - API - MVP - Review - Al realizar ingresos de compra, los agrega bien a su stock|COM-273]] API - MVP - Review - Al realizar ingresos de compra, los agrega bien a su stock segun deposito, pero no marca en los detalles el deposito en si

## Descripcion

Así como pasa en compras, existe un proceso mediante el cual la “orden de compra” pasa a nuestro inventario (suma stock) y este proceso es cuando se genera un “ingreso” a partir de una orden de compra.
