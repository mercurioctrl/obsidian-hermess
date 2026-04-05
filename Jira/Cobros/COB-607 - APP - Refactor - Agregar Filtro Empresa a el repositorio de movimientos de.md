---
jira_key: "COB-607"
aliases: ["COB-607"]
summary: "APP - Refactor - Agregar Filtro Empresa a el repositorio de movimientos de bancos y mostrarlo en el listado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-02-04 07:09"
updated: "2026-02-12 23:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-607"
---

# COB-607: APP - Refactor - Agregar Filtro Empresa a el repositorio de movimientos de bancos y mostrarlo en el listado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-04 07:09 |
| Actualizado | 2026-02-12 23:19 |
| Etiquetas | ninguna |
| Jira | [COB-607](https://bluinc.atlassian.net/browse/COB-607) |

## Relaciones

- **Padre:** [[COB-9 - API - Feat - Listar bancos|COB-9]] API - Feat - Listar bancos
- **action item from:** [[COB-606 - API - Refactor - Refactorizar el repositorio de movimientos de bancos para|COB-606]] API - Refactor - Refactorizar el repositorio de  movimientos de bancos para agregar atributos y filtros referidos a companyCode

## Descripcion

Agregar soporte de **companyCode** en el listado de movimientos bancarios.

**Cambios**

- Enviar `companyCode` al endpoint `/v1/currentBankAccount`.


- Agregar filtro de **Empresa** en la UI.


- Mostrar nueva columna **Empresa** usando `companyDescription`.



**Aceptación**

- El filtro recarga el listado correctamente.


- Se visualiza la empresa en cada registro sin afectar paginación ni filtros actuales.
