---
jira_key: "COM-248"
aliases: ["COM-248"]
summary: "APP - MVP - Review - Generar ingreso -> envió de parámetro de depósito vacío"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2025-11-14 17:12"
updated: "2025-12-05 05:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-248"
---

# COM-248: APP - MVP - Review - Generar ingreso -> envió de parámetro de depósito vacío

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2025-11-14 17:12 |
| Actualizado | 2025-12-05 05:29 |
| Etiquetas | ninguna |
| Jira | [COM-248](https://bluinc.atlassian.net/browse/COM-248) |

## Relaciones

- **Padre:** [[COM-77 - Editar orden de compra|COM-77]] Editar orden de compra
- **relates to:** [[COM-201 - APP - MVP - Refactor - Se debe poder modificar y cambiar un nuevo atributo|COM-201]] APP - MVP - Refactor - Se debe poder modificar y cambiar un nuevo atributo warehousesId asociado a las ordenes

## Descripcion

- Al intentar generar un ingreso después de haber seleccionado por primera vez un depósito, parece no enviarse dicha selección.


- Los nombres de Depósito se visualizan distintos, al seleccionar el depósito y reabrir la orden.



```
GET {API_URL]}/v1/makeProviderOrderInbound
```

[adjunto]
[adjunto]
