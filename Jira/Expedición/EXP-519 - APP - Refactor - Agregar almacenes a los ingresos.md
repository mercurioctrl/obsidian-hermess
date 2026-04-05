---
jira_key: "EXP-519"
aliases: ["EXP-519"]
summary: "APP - Refactor - Agregar almacenes a los ingresos"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-10-13 07:37"
updated: "2025-11-12 10:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-519"
---

# EXP-519: APP - Refactor - Agregar almacenes a los ingresos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-13 07:37 |
| Actualizado | 2025-11-12 10:45 |
| Etiquetas | ninguna |
| Jira | [EXP-519](https://bluinc.atlassian.net/browse/EXP-519) |

## Relaciones

- **Padre:** [[EXP-512 - Almacenes multiples|EXP-512]] Almacenes multiples
- **action item from:** [[EXP-518 - API - Refactor - Agregar parámetros de almacén en los ingresos|EXP-518]] API - Refactor - Agregar parámetros de almacén en los ingresos 

## Descripcion

Actualmente, en el modal de detalle de ingresao de cuna orden de compra (vista utilizada para ingresar seriales) se muestran datos básicos como nombre, SKU y estado de serialización.
Para mejorar la trazabilidad, se debe agregar la información del **almacén de origen del ítem** (depósito) tal como en el sistema de pedidos.

---

Visualizar en el modal de detalle de la orden una referencia clara del **depósito al que pertenece cada ítem**, combinando el prefijo o código del almacén junto con su identificador.
Esto permite identificar de forma rápida el origen del producto dentro del flujo de serialización.

Ejemplo:

```
2 - SAF
```

Donde:

- **SAF** → `stockWarehouseCode`


- **2** → `stockWarehouseId`



### **Criterios de aceptación** ✅

- El modal de detalle de orden debe mostrar los nuevos campos provenientes del backend:

- `stockWarehouseCode`


- `stockWarehouseId`


- `stockWarehouseDescription` *(opcional, puede mostrarse como tooltip o texto secundario)*




- El formato visible debe seguir la convención: **{stockWarehouseCode} ({stockWarehouseId})**, tal como se aplica en la vista de pedidos.


- Si los valores vienen `null`, no se muestra el bloque de depósito.


- El diseño debe mantener la jerarquía visual actual: los datos del depósito se ubican debajo del SKU y antes de la información de serialización.


- Se valida correctamente la información con la respuesta del endpoint GET {API_URL}/v1/providersOrders/{providerOrder}.
