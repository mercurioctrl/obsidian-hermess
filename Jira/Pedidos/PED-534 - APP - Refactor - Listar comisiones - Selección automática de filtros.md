---
jira_key: "PED-534"
aliases: ["PED-534"]
summary: " APP - Refactor - Listar comisiones - Selección automática de filtros"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-02-06 13:56"
updated: "2024-02-14 13:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-534"
---

# PED-534:  APP - Refactor - Listar comisiones - Selección automática de filtros

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-06 13:56 |
| Actualizado | 2024-02-14 13:23 |
| Etiquetas | ninguna |
| Jira | [PED-534](https://bluinc.atlassian.net/browse/PED-534) |

## Relaciones

- **Padre:** [[PED-174 - Listar comisiones|PED-174]] Listar comisiones
- **relates to:** [[PED-176 - APP - Feat - Listar comisiones|PED-176]] APP - Feat - Listar comisiones
- **relates to:** [[PED-533 - APP - Accionable para ver las comisiones directamente - Fechas no coincidentes|PED-533]] APP - Accionable para ver las comisiones directamente - Fechas no coincidentes

## Descripcion

Cuando accedo a la pestaña de Comisiones, la solicitud a `{{API_URL}}/v1/comissions` no se realiza automáticamente sino hasta después de seleccionar los filtros. Propongo que sigamos el mismo enfoque que utilizamos en el Dashboard, donde los filtros de vendedor y fecha se seleccionan automáticamente al ingresar. Podemos platicarlo en la daily para decidir si la consideramos o no.

[adjunto]
