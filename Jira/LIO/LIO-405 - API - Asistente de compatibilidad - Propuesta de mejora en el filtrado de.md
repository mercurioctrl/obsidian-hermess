---
jira_key: "LIO-405"
aliases: ["LIO-405"]
summary: "API - Asistente de compatibilidad - Propuesta de mejora en el filtrado de productos enviados"
status: "Finalizada"
type: "Tarea"
priority: "Low"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-08-04 14:20"
updated: "2025-09-03 19:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-405"
---

# LIO-405: API - Asistente de compatibilidad - Propuesta de mejora en el filtrado de productos enviados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Low |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-08-04 14:20 |
| Actualizado | 2025-09-03 19:11 |
| Etiquetas | ninguna |
| Jira | [LIO-405](https://bluinc.atlassian.net/browse/LIO-405) |

## Relaciones

- **Padre:** [[LIO-391 - Desarrollos IA para LIO (Aleph)|LIO-391]] Desarrollos IA para LIO (Aleph)
- **relates to:** [[LIO-400 - API - Refactor - Ajustes para el asistente de compatibilidad, ejecutar la|LIO-400]] API - Refactor - Ajustes para el asistente de compatibilidad, ejecutar la consulta solo si parece ser relevante

## Descripcion

Como propuesta de mejora, realizaremos un refactor del recurso del asistente de compatibilidad para que solo se active si hay al menos dos productos relevantes en el carrito.

Esto se implementará mediante la coincidencia con las palabras clave mencionadas en la historia: [https://bluinc.atlassian.net/browse/LIO-400](https://bluinc.atlassian.net/browse/LIO-400)

El objetivo es ajustar el payload y enviar únicamente los productos coincidentes a la IA:

```
POST /aleph/compatibility
```
