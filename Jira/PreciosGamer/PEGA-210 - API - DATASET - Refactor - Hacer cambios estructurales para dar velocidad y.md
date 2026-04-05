---
jira_key: "PEGA-210"
aliases: ["PEGA-210"]
summary: "API - DATASET - Refactor - Hacer cambios estructurales para dar velocidad y estabilidad al utilizar el sitio"
status: "Tareas por hacer"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-09 08:40"
updated: "2026-01-09 08:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-210"
---

# PEGA-210: API - DATASET - Refactor - Hacer cambios estructurales para dar velocidad y estabilidad al utilizar el sitio

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-09 08:40 |
| Actualizado | 2026-01-09 08:45 |
| Etiquetas | ninguna |
| Jira | [PEGA-210](https://bluinc.atlassian.net/browse/PEGA-210) |

## Relaciones

- **Padre:** [[PEGA-209 - Optimización de Experiencia por Performance|PEGA-209]] Optimización de Experiencia por Performance

## Descripcion

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
