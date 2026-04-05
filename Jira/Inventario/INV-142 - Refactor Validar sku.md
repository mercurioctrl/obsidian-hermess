---
jira_key: "INV-142"
aliases: ["INV-142"]
summary: "Refactor: Validar sku"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Ezequiel manzano"
created: "2024-09-23 15:26"
updated: "2024-09-24 23:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-142"
---

# INV-142: Refactor: Validar sku

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Ezequiel manzano |
| Creado | 2024-09-23 15:26 |
| Actualizado | 2024-09-24 23:46 |
| Etiquetas | ninguna |
| Jira | [INV-142](https://bluinc.atlassian.net/browse/INV-142) |

## Relaciones

- **Subtarea:** [[INV-144 - Validar SKU - Observaciones al validar sin completar los datos|INV-144]] Validar SKU - Observaciones al validar sin completar los datos
- **relates to:** [[INV-135 - API - Refactor - Siempre que lo que se edita es un sku, debe chequearse que el|INV-135]] API - Refactor - Siempre que lo que se edita es un sku, debe chequearse que el mismo no exista en otro producto
- **blocks:** [[INV-136 - API - Refactor - Al editar y crear un producto tambien alterar los parametros|INV-136]] API - Refactor - Al editar y crear un producto tambien alterar los parametros viejos en string

## Descripcion

Buenas! se debe modificar que al enviar el get para validar el sku, se debe mandar el companyCode si es q esta tiene asignada.

Si necesitas algun cambio del back avisame pero creo qno es necesario.
