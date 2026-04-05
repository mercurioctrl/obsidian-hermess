---
jira_key: "COM-249"
aliases: ["COM-249"]
summary: "APP - Refactor - Detalle de la orden -> Agregar filtro por empresa al obtener los impuestos/gastos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2025-11-14 18:00"
updated: "2025-11-17 12:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-249"
---

# COM-249: APP - Refactor - Detalle de la orden -> Agregar filtro por empresa al obtener los impuestos/gastos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2025-11-14 18:00 |
| Actualizado | 2025-11-17 12:13 |
| Etiquetas | ninguna |
| Jira | [COM-249](https://bluinc.atlassian.net/browse/COM-249) |

## Relaciones

- **Padre:** [[COM-77]] Editar orden de compra
- **relates to:** [[COM-147]] APP - Feat - Agregar / Editar / Eliminar impuestos distribuidos
- **relates to:** [[COM-232]] APP - MVP - Agregar filtro de empresa a la pestaña de impuestos/gasto (tariffTax)

## Descripcion

Realizaremos un refactor al recurso para obtener los impuestos/gastos, para agregar el filtro por `companyCode`

```
GET {{API_URL}}/v1/tariffTax?companyCode={id}
```

[adjunto]
