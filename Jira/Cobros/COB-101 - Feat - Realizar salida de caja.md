---
jira_key: "COB-101"
aliases: ["COB-101"]
summary: "Feat - Realizar salida de caja"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2022-09-15 09:23"
updated: "2023-03-13 16:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-101"
---

# COB-101: Feat - Realizar salida de caja

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-15 09:23 |
| Actualizado | 2023-03-13 16:05 |
| Etiquetas | ninguna |
| Jira | [COB-101](https://bluinc.atlassian.net/browse/COB-101) |

## Relaciones

- **Padre:** [[COB-15 - Cajas|COB-15]] Cajas
- **Subtarea:** [[COB-102 - APP - Feat - Modal Salida|COB-102]] APP - Feat - Modal Salida
- **Subtarea:** [[COB-103 - API - Feat - Repositorio de conceptos de salida|COB-103]] API - Feat - Repositorio de conceptos de salida
- **Subtarea:** [[COB-104 - API - Feat - Realizar salida|COB-104]] API - Feat - Realizar salida
- **Subtarea:** [[COB-105 - API - Feat - Precargar salidas desde un pase|COB-105]] API - Feat - Precargar salidas desde un pase
- **Subtarea:** [[COB-207 - APP - Feat - Cuando se precarga la salida, desde un pase marcar cotizacion por|COB-207]] APP - Feat - Cuando se precarga la salida, desde un pase marcar cotizacion por parametro
- **Subtarea:** [[COB-246 - API - Refactor - Alterar saldo proveedor, en caso de que el concepto sea un|COB-246]] API - Refactor - Alterar saldo proveedor, en caso de que el concepto sea un "pago de factura" o "pago proveedor"
- **Subtarea:** [[COB-247 - APP - Refactor - Agregar al modal de salida un selector de proveedor si el id|COB-247]] APP - Refactor - Agregar al modal de salida un selector de proveedor si el id del concepto es 3 o 35
- **Subtarea:** [[COB-341 - API - Refactor - Ordenar alfabeticamente los conceptos de salida|COB-341]] API - Refactor - Ordenar alfabeticamente los conceptos de salida

## Descripcion

Se trata sobre una funcionalidad encargada de registrar una salida de caja.

Cuando un valor (por ej: cheque, dolar, peso) sale de una caja, tiene que hacer un movimiento de salida, y restarse al saldo de ese tipo de valor, siempre y cuando el mismo sea suficiente.
