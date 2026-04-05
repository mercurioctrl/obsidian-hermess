---
jira_key: "PED-768"
aliases: ["PED-768"]
summary: "API - Limites y Objetivos - Tiempo de espera excedido"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-07-08 01:11"
updated: "2024-07-10 10:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-768"
---

# PED-768: API - Limites y Objetivos - Tiempo de espera excedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-07-08 01:11 |
| Actualizado | 2024-07-10 10:39 |
| Etiquetas | ninguna |
| Jira | [PED-768](https://bluinc.atlassian.net/browse/PED-768) |

## Relaciones

- **Padre:** [[PED-469]] SyncUps e Importaciones
- **blocks:** [[PED-759]] API - Refactor - En el filtro de Trust, cuando no filtro por vendedor tarda bastante, pero ademas suele no traer nada, cuando hay vendedors que si cumplieron el objetivo

## Descripcion

Al obtener los objetivos el tiempo de espera sobrepasa lo establecido, ¿hay alguna forma de reducir esta cantidad?


```
{{API_URL}}/v1/objectives/capillarityIncentive
{{API_URL}}/v1/objectives/capillarityIncentive?&itemFilter=trust
```

[adjunto]
