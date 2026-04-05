---
jira_key: "PED-564"
aliases: ["PED-564"]
summary: "Agregar permiso - All comissions"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Ezequiel manzano"
created: "2024-02-21 14:55"
updated: "2024-02-21 18:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-564"
---

# PED-564: Agregar permiso - All comissions

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Ezequiel manzano |
| Creado | 2024-02-21 14:55 |
| Actualizado | 2024-02-21 18:09 |
| Etiquetas | ninguna |
| Jira | [PED-564](https://bluinc.atlassian.net/browse/PED-564) |

## Relaciones

- **relates to:** [[SNB-1512 - COMISIONES|SNB-1512]] COMISIONES

## Descripcion

```
update NB_WEB.dbo.permisos_agente  set all_comissions = 1 where agente_fp = 8

ALTER TABLE NB_WEB.dbo.permisos_agente  
add all_comissions INT DEFAULT 0 

```
