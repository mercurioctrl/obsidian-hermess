---
jira_key: "PED-842"
aliases: ["PED-842"]
summary: "API - Editar cliente - Oportunidad de mejora en el mensaje de error"
status: "Finalizada"
type: "Tarea"
priority: "Lowest"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-10-05 08:45"
updated: "2024-10-09 22:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-842"
---

# PED-842: API - Editar cliente - Oportunidad de mejora en el mensaje de error

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Lowest |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-10-05 08:45 |
| Actualizado | 2024-10-09 22:24 |
| Etiquetas | ninguna |
| Jira | [PED-842](https://bluinc.atlassian.net/browse/PED-842) |

## Relaciones

- **Padre:** [[PED-15]] Clientes
- **relates to:** [[PED-19]] API - Feat - Editar cliente

## Descripcion

Al intentar editar los parámetros de un cliente, me apareció el error “Undefined array key 0”. 

Observé que el cliente no tenía añadido su número de WhatsApp, así que al agregarlo pude continuar con la edición. 

Sería útil que el mensaje de error indicara, en caso de que falte algún dato, que es necesario completarlo. De este modo, podríamos evitarnos un reporte futuro.

[adjunto]
