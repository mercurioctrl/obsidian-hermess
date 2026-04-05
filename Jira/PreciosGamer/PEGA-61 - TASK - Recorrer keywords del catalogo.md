---
jira_key: "PEGA-61"
aliases: ["PEGA-61"]
summary: "TASK - Recorrer keywords del catalogo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-07 09:23"
updated: "2024-05-10 11:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-61"
---

# PEGA-61: TASK - Recorrer keywords del catalogo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-07 09:23 |
| Actualizado | 2024-05-10 11:51 |
| Etiquetas | ninguna |
| Jira | [PEGA-61](https://bluinc.atlassian.net/browse/PEGA-61) |

## Relaciones

- **Padre:** [[PEGA-26 - API - Feat - Recoger catalogos por resellermarketplace|PEGA-26]] API - Feat - Recoger catalogos por reseller/marketplace

## Descripcion

### Crearemos una nueva tabla

llamada `keywordTracker` con las siguiente columnas (poneles nombre cancheros en ingles)

- id


- keywords


- tracked (true/false, indica si ya fueron trackeadas)


- date


- dateTracked


- delayDate (sirve para retrasas el rastreo hasta despues de ese momento)



Esta tabla funcionara como una cola, para que podamos meter las cosas que queremos que se trackeen de manera mas flexible. Podemos vaciarla cada tanto, pero nos sirve para ir contabilizando (dps arrojaremos eso en otro repo).

### Que debe hacer la ejecución de la tarea

Debe recorrer keywordTracker, mostrando solo aquellos con `tracked` en `false` y cuando `delayDate` sea anterior a el momento actual. Realizar la búsqueda en los distintos rastreadores con una ejecución

- Ml


- Tm


- Lo


- Hg



Cada vez que se completa un rastreo, se marca el parámetro `tracked` de la tabla en true, así como `dateTracked`

En las próximas historias hablaremos sobre el llenado de la tabla `keywordTracker`
