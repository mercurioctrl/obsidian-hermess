---
jira_key: "PED-1046"
aliases: ["PED-1046"]
summary: "APP - Refactor - Cuando una orden cuenta con el atributo MLA se debe marcar como una compra de mercadolibre"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-07-13 20:21"
updated: "2025-07-15 10:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1046"
---

# PED-1046: APP - Refactor - Cuando una orden cuenta con el atributo MLA se debe marcar como una compra de mercadolibre

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-13 20:21 |
| Actualizado | 2025-07-15 10:30 |
| Etiquetas | ninguna |
| Jira | [PED-1046](https://bluinc.atlassian.net/browse/PED-1046) |

## Relaciones

- **Padre:** [[PED-915]] MercadoLibre
- **action item from:** [[PED-1043]] API - Refactor - Agregar MLA al recurso de las ordenes

## Descripcion

Simplemente cuando ingresa un pedido que cuenta con `mla`, cambiaremos el texto a nivel visual que dice “INTERNO” por “MERCADOLIBRE”

Esto lo haremos por front, ya que no vale la pena cambiar como interactua el sistema solo por un indicador visual (el tipo de pedido afecta su funcinamiento.)

[adjunto]
