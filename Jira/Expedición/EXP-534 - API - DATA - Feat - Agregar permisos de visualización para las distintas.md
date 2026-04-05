---
jira_key: "EXP-534"
aliases: ["EXP-534"]
summary: "API - DATA - Feat - Agregar permisos de visualización para las distintas pestañas de expedicion"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-03-27 10:05"
updated: "2026-03-27 15:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-534"
---

# EXP-534: API - DATA - Feat - Agregar permisos de visualización para las distintas pestañas de expedicion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-27 10:05 |
| Actualizado | 2026-03-27 15:12 |
| Etiquetas | ninguna |
| Jira | [EXP-534](https://bluinc.atlassian.net/browse/EXP-534) |

## Relaciones

- **Padre:** [[EXP-533]] Permisos de visualizacion
- **has action item:** [[EXP-535]] APP - Refactor - Mostrar o no pestañas segun el permiso de visualización de la misma para ese usuario
- **has action item:** [[LAW-56]] Mostrar / Ocultar pestañas 

## Descripcion

Similar a como se trabajo en cobros, agermanamos permisos en la tabla `permisos_agentes` para que puedan o no visualizar las distintas pestañas

[adjunto]
Estos permisos a su vez, deben llegar para cada usuario en el objeto `user`
