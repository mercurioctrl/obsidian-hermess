---
jira_key: "NBWEB-60"
summary: "API - Esquema de Roles y permisos"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-29 16:00"
updated: "2022-06-26 20:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-60"
---

# NBWEB-60: API - Esquema de Roles y permisos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-29 16:00 |
| Actualizado | 2022-06-26 20:17 |
| Etiquetas | ninguna |
| Jira | [NBWEB-60](https://bluinc.atlassian.net/browse/NBWEB-60) |

## Descripción

Montar un esquema tipo Middleware para asegurar los recursos de la api según el siguiente criterio. 

Se deben utilizar las tablas `[NB_WEB].[dbo].[userRoles]` y `[NB_WEB].[dbo].[userPermissions]`

Todos los recursos deben ser validados para ver si se tiene los permisos correctos para su ejecucion.
