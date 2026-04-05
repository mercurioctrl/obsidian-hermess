---
jira_key: "COM-104"
aliases: ["COM-104"]
summary: "APP - Refactor - Agregar totales impositivos al modal de la orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-06-06 10:24"
updated: "2024-06-13 22:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-104"
---

# COM-104: APP - Refactor - Agregar totales impositivos al modal de la orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-06 10:24 |
| Actualizado | 2024-06-13 22:25 |
| Etiquetas | ninguna |
| Jira | [COM-104](https://bluinc.atlassian.net/browse/COM-104) |

## Relaciones

- **Padre:** [[COM-38]] Ver orden de compra
- **is blocked by:** [[COM-103]] API - Refactor - Calcular totales de impuestos por linea y subtotales

## Descripcion

Basándonos en el recurso [link](https://lioteam.atlassian.net/browse/COM-103) 

[adjunto]
La idea es mostrar a la derecha de la linea (detras de los impuestos) el subtotal para esa liena, osea el ítem.

Y debajo, el subtotal para cada impuesto sumando todas las lineas.

El recurso se carga tanto al abrirl el modal, como al alterar el contenido de alguna manera (incluida posicion arancelaria)
