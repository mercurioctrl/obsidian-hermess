---
jira_key: "COM-288"
aliases: ["COM-288"]
summary: "APP - Feat - agregar descuento a la orden de compra"
status: "Tareas por hacer"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2026-03-04 09:08"
updated: "2026-03-09 09:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-288"
---

# COM-288: APP - Feat - agregar descuento a la orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2026-03-04 09:08 |
| Actualizado | 2026-03-09 09:39 |
| Etiquetas | ninguna |
| Jira | [COM-288](https://bluinc.atlassian.net/browse/COM-288) |

## Relaciones

- **Padre:** [[COM-8]] Ordenes de compra
- **has action item:** [[COM-289]] API - Feat - agregar descuento a la orden de compra

## Descripcion

Esperar a la reunión con LASET

Idea:
Agregar una columna que se llame descuento al lado del costo

| **Costo** | **Descuento** |
| --- | --- |
| 100 | 0 |

si se agrega descuento de 10 quedaría

| **Costo** | **Descuento** |
| --- | --- |
| 90 | 10 |

y cada que se edite el descuento modifica al costo y se envia por separado ambos parametros

y si se modifica el costo no modifica al descuento
