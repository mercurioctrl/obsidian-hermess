---
jira_key: PEGA-210
status: Tareas por hacer
assignee: Emanuel Jesus Ferreyra
assignee_email: null
reporter: Catriel Mercurio
priority: Medium
issuetype: Subtarea
project: PEGA
updated: "2026-01-09T08:45:23.383-0300"
created: "2026-01-09T08:40:51.050-0300"
url: "https://bluinc.atlassian.net/browse/PEGA-210"
tags: [jira, PEGA, tareas-por-hacer]
---

# PEGA-210 · API - DATASET - Refactor - Hacer cambios estructurales para dar velocidad y estabilidad al utilizar el sitio

[PEGA-210 en Jira](https://bluinc.atlassian.net/browse/PEGA-210)

## Descripción

El volumen de datos creció de forma sostenida y hoy el sistema opera con **datasets grandes y altamente consultados**.

Como consecuencia:

- La base de datos presenta degradación de performance en escenarios normales de uso.
- Los tiempos de respuesta se ven afectados en consultas críticas del sitio.
- El proceso de **sync-up de datos**, cuando se ejecuta, impacta negativamente en la experiencia general del sistema.

Este escenario genera fricción directa en la experiencia del usuario y limita la capacidad del producto para escalar.

---

### Objetivo

Investigar, analizar y **proponer cambios estructurales** en el backend y el modelo de datos que permitan:

- Mejorar la velocidad de respuesta del sitio.
- Aumentar la estabilidad del sistema bajo carga.
- Aislar o mitigar el impacto de los procesos de sincronización sobre el uso normal del sistema.

El foco está en **resolver problemas de fondo** para dar parte una una etapa final de consolidación operativa total que permita que el sitio este listo para escalar y tener dominio dentro del nicho sin requerir mantenimientos de emergencia o que la estrategia falle mas adelante porque no se hicieron los refactor a tiempo.

---
_Sincronizado por jira-sidecar el 2026-06-07 22:27:14 UTC._
