---
jira_key: "PED-1146"
aliases: ["PED-1146"]
summary: "APP - MVP – Refactor – addItem con depósito específico"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-10-07 09:24"
updated: "2025-11-10 13:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1146"
---

# PED-1146: APP - MVP – Refactor – addItem con depósito específico

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-07 09:24 |
| Actualizado | 2025-11-10 13:08 |
| Etiquetas | ninguna |
| Jira | [PED-1146](https://bluinc.atlassian.net/browse/PED-1146) |

## Relaciones

- **Padre:** [[PED-1107]] Almacenes Multiples
- **action item from:** [[PED-1145]] API - MVP – Refactor – addItem con depósito específico y reserva por almacén
- **has action item:** [[PED-1145]] API - MVP – Refactor – addItem con depósito específico y reserva por almacén

## Descripcion

Actualizar la llamada al endpoint


```
PATCH /v1/orders/addItem
```


para que siempre incluya el campo `stockWarehouseId` en el payload.
Este valor debe obtenerse desde el **repositorio de ítems**, utilizando el depósito asociado al producto que el usuario selecciona (por ejemplo, el almacén actual o el predeterminado del vendedor).

**Payload**

```
{
  "order": "10425810",
  "branch": "0002",
  "itemId": 119555,
  "amount": 1,
  "stockWarehouseId": 3 <-- Se agrega
}
```

**Criterios de aceptación:**

- El payload siempre incluye `stockWarehouseId` obtenido del repositorio de ítems.


- Si el ítem no tiene depósito asociado, mostrar error o impedir la acción.


- El flujo de agregar ítem funciona igual visualmente (sin cambios en UI).


- El backend recibe correctamente el `stockWarehouseId` y responde con el formato esperado (`msg`, `success`, `item`).
