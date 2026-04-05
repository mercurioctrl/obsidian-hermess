---
jira_key: "PEGA-167"
aliases: ["PEGA-167"]
summary: "APP - Refactor - Agregar \"fecha de cambio\" en los repositorios de baja de precio de la home"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-01-08 13:03"
updated: "2025-01-20 11:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-167"
---

# PEGA-167: APP - Refactor - Agregar "fecha de cambio" en los repositorios de baja de precio de la home

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-08 13:03 |
| Actualizado | 2025-01-20 11:25 |
| Etiquetas | ninguna |
| Jira | [PEGA-167](https://bluinc.atlassian.net/browse/PEGA-167) |

## Relaciones

- **Padre:** [[PEGA-2]] Catalogos y Buscador
- **action item from:** [[PEGA-165]] API - Refactor - Nuevo parámetro para filtrar limite de días desde la ultima modificación de precio

## Descripcion

Utilizaremos el parámetro introducido en el refactor [link](https://lioteam.atlassian.net/browse/PEGA-165) 

para poder evaluar la baja de precios en periodos mas cortos.

Para esto habilitaremos el parámetro para ser recibido por el front y para que este a su vez lo envié al back si esta presente

Para los repositorios enlazados en la home lo fijaremos en 2 dias


```
https://preciosgamer.com/bajaron_de_precio?rate=down&t=1&search=Bajaron%20de%20precio&changedate=2
```

```
https://preciosgamer.com/memoria?rate=down&order=asc_price&search=memoria&changedate=2
```

etc
