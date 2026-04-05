---
jira_key: "PED-1246"
aliases: ["PED-1246"]
summary: "API - Refactor - Mostrar/Guardar el forwarder en una orden especifica"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-08 10:01"
updated: "2026-01-21 19:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1246"
---

# PED-1246: API - Refactor - Mostrar/Guardar el forwarder en una orden especifica

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-08 10:01 |
| Actualizado | 2026-01-21 19:57 |
| Etiquetas | ninguna |
| Jira | [PED-1246](https://bluinc.atlassian.net/browse/PED-1246) |

## Relaciones

- **Padre:** [[PED-1237 - MVP - Forwarder|PED-1237]] MVP -  Forwarder
- **has action item:** [[PED-1240 - APP - Feat - Agregar un selector en el detalle de la orden de compra para|PED-1240]] APP - Feat - Agregar un selector en el detalle de la orden de compra para seleccionar el forwarder similar a incoterms (editable solo en pendiente)
- **has action item:** [[PED-1253 - API - MVP - Refactor edición de forwarder- si mandas null lo tiene que vaciar|PED-1253]] API - MVP - Refactor edición de forwarder-> si mandas null lo tiene que vaciar si la orden esta en pendiente

## Descripcion

```
PATCH /v1/orders/{branch}-{order}
```

```
{
  forwarderId: 2
}
```

Se agregara en la tabla `NewBytes_DBF.dbo.pedclit.forwarderId`

---

```
GET /v1/orders/{branch}-{order}
```

```
{
    "date": "2026-01-07 11:52:28",
    "makeSaleDate": null,
    "orderNumber": "10426421",
    "branchNumber": "0002",
    "incotermId": 2,
    "incotermCode": "CIF",
    "albnumNumber": null,
    "realAlbumNumber": null,
    "forwarderId": 2, 
    "forwarderName" "Nombre del forwarder"
...
```
