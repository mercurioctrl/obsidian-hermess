---
jira_key: "SNB-3184"
aliases: ["SNB-3184"]
summary: "SISTEMAS - Modificar zonas horarias"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2025-06-24 19:04"
updated: "2026-01-22 06:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3184"
---

# SNB-3184: SISTEMAS - Modificar zonas horarias

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2025-06-24 19:04 |
| Actualizado | 2026-01-22 06:48 |
| Etiquetas | ninguna |
| Jira | [SNB-3184](https://bluinc.atlassian.net/browse/SNB-3184) |

## Relaciones

- **blocks:** [[PEGA-193 - API - Feat - Registro de nuevo reseller|PEGA-193]] API - Feat - Registro de nuevo reseller

## Descripcion

Actualmente las fechas se están guardando incorrectamente en la base de datos debido a una configuración diferente de la zona horaria actual en los servidores de pruebas y desarrollo.

Solicito actualizar la configuración de timezone en ambos entornos para que coincida con la zona horaria correcta ([[UTC-3]]).
