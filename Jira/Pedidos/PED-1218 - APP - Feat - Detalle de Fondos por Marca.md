---
jira_key: "PED-1218"
aliases: ["PED-1218"]
summary: "APP - Feat - Detalle de Fondos por Marca"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-05 08:04"
updated: "2026-01-20 09:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1218"
---

# PED-1218: APP - Feat - Detalle de Fondos por Marca

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 08:04 |
| Actualizado | 2026-01-20 09:47 |
| Etiquetas | ninguna |
| Jira | [PED-1218](https://bluinc.atlassian.net/browse/PED-1218) |

## Relaciones

- **Padre:** [[PED-1208]] Gestión de Aportes y Gastos de Marketing
- **action item from:** [[PED-1210]] API - Feat - Listar Fondos (con saldos)

## Descripcion

Vista de auditoría/operación que muestra fondos individuales de una marca y su estado (aportado, asignado, gastado, saldos). Sirve para entender el origen de los totales.

**API**

```
GET /v1/marketing/funds?brandId={id}&activeOnly=&currencyId=&currentPage=&itemsPerPage=
```

**Criterios de aceptación**

- Muestra listado con columnas: nombre, moneda, aportado, asignado, gastado, disponible para asignar, disponible cash, vencimiento.


- Permite filtrar por moneda y vigencia y mantiene paginación.


- Incluye botón “Crear Fondo” que abre el formulario ([link](https://bluinc.atlassian.net/browse/PED-1209) [link](https://bluinc.atlassian.net/browse/PED-1219) ).


- Desde cada fondo ofrece acción “Asignar a Acción” (abre modal de [link](https://bluinc.atlassian.net/browse/PED-1222)  [link](https://bluinc.atlassian.net/browse/PED-1212)  con `fundId` precargado).


- Maneja estados loading/vacío/error.
