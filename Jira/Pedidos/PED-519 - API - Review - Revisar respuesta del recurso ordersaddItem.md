---
jira_key: "PED-519"
aliases: ["PED-519"]
summary: "API - Review - Revisar respuesta del recurso /orders/addItem"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2024-01-30 09:53"
updated: "2024-02-08 13:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-519"
---

# PED-519: API - Review - Revisar respuesta del recurso /orders/addItem

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2024-01-30 09:53 |
| Actualizado | 2024-02-08 13:43 |
| Etiquetas | ninguna |
| Jira | [PED-519](https://bluinc.atlassian.net/browse/PED-519) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **relates to:** [[PED-518]] APP - Refactor - Ver detalle de una orden de compra - Actualizar subtotales
- **is blocked by:** [[PED-522]] API - Revisar respuesta del recurso addItem - Precio a mano no guardado

## Descripcion

Al actualizar cantidad de un producto, no devuelve correctamente la letra ni la lista de precio
ejemplo: 0010-10332228


```
{
  letra:null
  pricedList:null
}
```

[adjunto]
[adjunto]
Por otro lado revisar tambien cuando hay un precio a mano y se cambia la cantidad, lo que devuelve el recurso no es el precio a mano ejemplo: 0002-10332470


[adjunto]
