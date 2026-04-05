---
jira_key: "PED-1220"
aliases: ["PED-1220"]
summary: "APP - Feat - Listado de Acciones (con estado por moneda)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-05 08:08"
updated: "2026-01-20 09:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1220"
---

# PED-1220: APP - Feat - Listado de Acciones (con estado por moneda)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 08:08 |
| Actualizado | 2026-01-20 09:56 |
| Etiquetas | ninguna |
| Jira | [PED-1220](https://bluinc.atlassian.net/browse/PED-1220) |

## Relaciones

- **Padre:** [[PED-1208]] Gestión de Aportes y Gastos de Marketing
- **action item from:** [[PED-1213]] API - Feat - Listar Acciones (con asignado/gastado por moneda)

## Descripcion

**Descripción**
Pantalla para ver acciones y sus totales (asignado, gastado, restante) por moneda. Permite entender ejecución y consumo de presupuesto.

**API**

```
GET /v1/marketing/actions?brandId=&from=&to=&currentPage=&itemsPerPage=
```

**Criterios de aceptación**

- Lista acciones mostrando totales por moneda (`totals[]`) y `remaining`.


- Filtros: rango de fechas (`from/to`) y filtro opcional por marca (`brandId`).


- CTA “Crear Acción” (historia #5).


- CTA por acción: “Ver Movimientos” (historia [link](https://bluinc.atlassian.net/browse/PED-1224)  con `actionId`) y “Asignar Presupuesto” (historia [link](https://bluinc.atlassian.net/browse/PED-1222)  con `actionId`).


- Estados loading/vacío/error.
