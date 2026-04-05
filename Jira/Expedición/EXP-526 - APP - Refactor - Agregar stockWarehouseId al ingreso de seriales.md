---
jira_key: "EXP-526"
aliases: ["EXP-526"]
summary: "APP - Refactor - Agregar stockWarehouseId al ingreso de seriales "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-28 08:23"
updated: "2026-01-29 14:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-526"
---

# EXP-526: APP - Refactor - Agregar stockWarehouseId al ingreso de seriales 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-28 08:23 |
| Actualizado | 2026-01-29 14:08 |
| Etiquetas | ninguna |
| Jira | [EXP-526](https://bluinc.atlassian.net/browse/EXP-526) |

## Relaciones

- **Padre:** [[EXP-11 - Feat - Serializar entrada de mercadería|EXP-11]] Feat - Serializar entrada de mercadería
- **action item from:** [[EXP-525 - API - Refactor - Agregar stockWarehouseId al ingreso de seriales|EXP-525]] API - Refactor - Agregar stockWarehouseId al ingreso de seriales 

## Descripcion

Agregaremos `stockWarehouseId` como un parámetro opcional, el mismo se obtiene de` /v1/providersOrders/{orderId}` que en ese punto ya lo tenemos en pantalla.

En caso de no estar disponible, lo enviamos NULL

[adjunto]
 

```
POST /v1/providersOrders/{id}/serials/{itemId}
```

```
{
"mode":"list",
"stockWarehouseId": 2, <-- Se agrega como parametro opcional
"serials":[
  "serial0001",
  "serial0002"
]

```
