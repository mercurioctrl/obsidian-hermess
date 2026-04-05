---
jira_key: "PED-1217"
aliases: ["PED-1217"]
summary: "APP - Feat - Dashboard de Marcas (Totales por marca)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-05 08:03"
updated: "2026-01-19 14:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1217"
---

# PED-1217: APP - Feat - Dashboard de Marcas (Totales por marca)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 08:03 |
| Actualizado | 2026-01-19 14:10 |
| Etiquetas | ninguna |
| Jira | [PED-1217](https://bluinc.atlassian.net/browse/PED-1217) |

## Relaciones

- **Padre:** [[PED-1208]] Gestión de Aportes y Gastos de Marketing
- **action item from:** [[PED-1216]] API - Feat - Listar marcas con fondos (totales disponibles)

## Descripcion

Pantalla principal que lista marcas con fondos y muestra totales agregados por moneda: aportado, asignado, gastado y saldos disponibles. Es el “home” operativo para decidir dónde hay presupuesto.

**API**

```
GET /v1/marketing/brands?activeOnly=1&currencyId=&q=&currentPage=&itemsPerPage=
```

**Criterios de aceptación**

- Lista marcas con `totals[]` por moneda y muestra: `amountOriginalTotal`, `allocatedTotal`, `spentTotal`, `availableToAllocateTotal`, `availableCashTotal`.


- Incluye filtros: búsqueda `q`, moneda `currencyId` (opcional), y toggle `activeOnly`.


- Paginación por marca (`currentPage`, `itemsPerPage`).


- Al click en una marca navega a “Detalle de Fondos” pasando `brandId`.
