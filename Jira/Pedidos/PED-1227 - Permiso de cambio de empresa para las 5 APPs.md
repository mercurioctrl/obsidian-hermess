---
jira_key: "PED-1227"
aliases: ["PED-1227"]
summary: "Permiso de cambio de empresa para las 5 APPs"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-05 11:36"
updated: "2026-01-15 11:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1227"
---

# PED-1227: Permiso de cambio de empresa para las 5 APPs

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 11:36 |
| Actualizado | 2026-01-15 11:10 |
| Etiquetas | ninguna |
| Jira | [PED-1227](https://bluinc.atlassian.net/browse/PED-1227) |

## Relaciones

- **Padre:** [[PED-2]] Bases y repositorios
- **Subtarea:** [[PED-1228]] API - Refactor - Incluir en las 5 APPs el objeto user el permiso unlockedCompanyFilter
- **Subtarea:** [[PED-1229]] APP - Refactor - Incluir en las 5 APPs, el bloqueo del selector de empresa segun unlockedCompanyFilter

## Descripcion

Este Epic introduce un **mecanismo unificado de control de permisos** para el uso del filtro *Empresa* en todas las aplicaciones operativas del ecosistema.

El objetivo es **evitar que el usuario pueda cambiar arbitrariamente el contexto de empresa** salvo que tenga un permiso explícito para hacerlo, reduciendo errores operativos, confusión de datos y usos indebidos de información multiempresa.
