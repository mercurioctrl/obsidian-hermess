---
jira_key: "NBWEB-989"
aliases: ["NBWEB-989"]
summary: "API - Feat - Repositorio de challenges para NB Travel"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-28 12:42"
updated: "2025-07-31 10:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-989"
---

# NBWEB-989: API - Feat - Repositorio de challenges para NB Travel

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-28 12:42 |
| Actualizado | 2025-07-31 10:53 |
| Etiquetas | ninguna |
| Jira | [NBWEB-989](https://bluinc.atlassian.net/browse/NBWEB-989) |

## Relaciones

- **Padre:** [[NBWEB-978 - NB TRAVEL|NBWEB-978]] NB TRAVEL

## Descripcion

Crearemos un repositorio para almacenar y mostrar los challenges (premios por acciones concretas, como compartir en redes o cosas asi) que se irán realizando. El fin del recurso es que se puedan visualizar en la landing page

```
GET {API_URL}/v1/miCuenta/challenges?status={completed/current}
```

Para esto crearemos la tabla `[NB_WEB].[dbo].[challenges]`con la siguiente estructura:

- id (auto)


- description (Este es un texto que explica en que consiste el challenge)


- startDate (fecha de inicio)


- endDate (Fecha de finalizacion )



Con la misma logica que los aceleradores, mostraremos los actuales cuando es `current`y si recibo `completed`los que ya finalizaron
