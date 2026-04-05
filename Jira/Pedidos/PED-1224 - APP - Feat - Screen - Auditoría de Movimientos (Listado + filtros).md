---
jira_key: "PED-1224"
aliases: ["PED-1224"]
summary: "APP - Feat - Screen - Auditoría de Movimientos (Listado + filtros)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-05 08:11"
updated: "2026-01-20 10:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1224"
---

# PED-1224: APP - Feat - Screen - Auditoría de Movimientos (Listado + filtros)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 08:11 |
| Actualizado | 2026-01-20 10:08 |
| Etiquetas | ninguna |
| Jira | [PED-1224](https://bluinc.atlassian.net/browse/PED-1224) |

## Relaciones

- **Padre:** [[PED-1208]] Gestión de Aportes y Gastos de Marketing
- **action item from:** [[PED-1215]] API - Feat - Listar Movimientos (auditoría + filtros)

## Descripcion

Pantalla de auditoría que lista movimientos y permite filtrar por marca, fondo, acción y fechas. Enfocada en trazabilidad: original + FX + impacto final.

**API**

```
GET /v1/marketing/movements?brandId=&fundId=&actionId=&from=&to=&currentPage=&itemsPerPage=
```

**Criterios de aceptación**

- Muestra columnas: fecha, marca/fondo/acción (si aplica), concepto, moneda original+monto, FX, monto final.


- Filtros combinables: `brandId`, `fundId`, `actionId`, `from/to`.


- Paginación y orden por fecha descendente.


- Permite navegar desde un movimiento a su contexto (fondo o acción) si están disponibles en UI.


- Estados loading/vacío/error con retry.
