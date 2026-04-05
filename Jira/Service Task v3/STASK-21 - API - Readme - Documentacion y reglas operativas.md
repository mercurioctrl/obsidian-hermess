---
jira_key: "STASK-21"
aliases: ["STASK-21"]
summary: "API - Readme - Documentacion y reglas operativas"
status: "Tareas por hacer"
type: "Historia"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2026-01-13 08:51"
updated: "2026-01-13 08:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-21"
---

# STASK-21: API - Readme - Documentacion y reglas operativas

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-13 08:51 |
| Actualizado | 2026-01-13 08:51 |
| Etiquetas | ninguna |
| Jira | [STASK-21](https://bluinc.atlassian.net/browse/STASK-21) |

## Relaciones

- **Padre:** [[STASK-15]] Sistema de Notificaciones Multicanal (Queue + Workers)

## Descripcion

## Documentación y reglas operativas

### Descripción

Documentar el flujo completo del sistema para backend y mobile.
Definir reglas claras sobre dedupeKey, estados y alcance del MVP.

### Tareas

- Documentar `dedupeKey` (opcional, recomendado)


- Documentar estados de requests y attempts


- Documentar flujo: API → DB → Queue → Worker → Provider


- Aclarar alcance MVP (push + email)



### Criterios de aceptación

- El equipo entiende cuándo usar dedupeKey y cuándo no.


- No hay ambigüedad sobre qué canales están activos.


- El flujo de ejecución es claro para debugging.


- La documentación queda asociada al EPIC.
