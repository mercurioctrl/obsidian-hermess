---
jira_key: "SNB-2088"
aliases: ["SNB-2088"]
summary: "cambio en pendings soporte"
status: "Finalizada"
type: "Nueva función"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Ezequiel manzano"
created: "2024-07-10 10:16"
updated: "2024-07-10 17:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-2088"
---

# SNB-2088: cambio en pendings soporte

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Nueva función |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Ezequiel manzano |
| Creado | 2024-07-10 10:16 |
| Actualizado | 2024-07-10 17:38 |
| Etiquetas | ninguna |
| Jira | [SNB-2088](https://bluinc.atlassian.net/browse/SNB-2088) |

## Relaciones

- **relates to:** [[PED-769]] API - Refactor - Ajustar las notificaciones para cada usuario

## Descripcion

Se requiere agregar en las distintas API’S a la request de pendings para soporte el parametro

**?reportUser=andi**

quedando asi la request final

`{{API_URL}}/v1/pendings?reportUser=andi`
