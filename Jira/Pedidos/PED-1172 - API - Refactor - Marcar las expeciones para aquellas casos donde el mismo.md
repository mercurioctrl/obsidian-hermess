---
jira_key: "PED-1172"
aliases: ["PED-1172"]
summary: "API - Refactor - Marcar las expeciones para aquellas casos donde el mismo itemId colisiona con el que un Kit contiene cuando quiere agregarse, o si ya esta dentro de la orden"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-28 15:09"
updated: "2025-12-15 10:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1172"
---

# PED-1172: API - Refactor - Marcar las expeciones para aquellas casos donde el mismo itemId colisiona con el que un Kit contiene cuando quiere agregarse, o si ya esta dentro de la orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-28 15:09 |
| Actualizado | 2025-12-15 10:59 |
| Etiquetas | ninguna |
| Jira | [PED-1172](https://bluinc.atlassian.net/browse/PED-1172) |

## Relaciones

- **Padre:** [[PED-1170 - Kits|PED-1170]] Kits

## Descripcion

Según lo acordado, se incorporará una excepción específica para estos casos, diseñada para ser lo más eficiente y poco invasiva posible.

Además, cuando ocurra la situación, el sistema mostrará un mensaje identificando el ítem que genera el conflicto y sugerirá crear un nuevo pedido para incluirlo allí.
