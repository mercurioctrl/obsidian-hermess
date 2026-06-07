---
jira_key: STASK-21
status: Tareas por hacer
assignee: null
assignee_email: null
reporter: Catriel Mercurio
priority: Medium
issuetype: Historia
project: STASK
updated: "2026-01-13T08:51:17.635-0300"
created: "2026-01-13T08:51:12.384-0300"
url: "https://bluinc.atlassian.net/browse/STASK-21"
tags: [jira, STASK, tareas-por-hacer]
---

# STASK-21 · API - Readme - Documentacion y reglas operativas

[STASK-21 en Jira](https://bluinc.atlassian.net/browse/STASK-21)

## Descripción

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

1. El equipo entiende cuándo usar dedupeKey y cuándo no.
2. No hay ambigüedad sobre qué canales están activos.
3. El flujo de ejecución es claro para debugging.
4. La documentación queda asociada al EPIC.

---
_Sincronizado por jira-sidecar el 2026-06-07 22:26:32 UTC._
