---
jira_key: "COB-71"
aliases: ["COB-71"]
summary: "API - Refactor - Agregar tabla de estados para los pases para mejorar el sistema viejo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-29 15:26"
updated: "2022-10-20 17:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-71"
---

# COB-71: API - Refactor - Agregar tabla de estados para los pases para mejorar el sistema viejo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-29 15:26 |
| Actualizado | 2022-10-20 17:11 |
| Etiquetas | ninguna |
| Jira | [COB-71](https://bluinc.atlassian.net/browse/COB-71) |

## Relaciones

- **Padre:** [[COB-12 - Feat - Procesar pases de caja|COB-12]] Feat - Procesar pases de caja

## Descripcion

Esta historia se trata sobre crear una tabla donde almacenar los estados de los pases. Es una refactorizacion sobre la base del sistema viejo, pero para mejorarlo.

Se busca dotar a la tabla `MC_LOG_OPERACIONES` con una columna exclusiva `passesSatusId` que nos sirva para poder tener un indice numérico vinculado a otra tabla (que tambien crearemos) llamada passesSatus.



La misma debe contar con al menos dos columnas

- id


- description
