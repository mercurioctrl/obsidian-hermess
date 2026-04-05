---
jira_key: "PED-1213"
aliases: ["PED-1213"]
summary: "API - Feat - Listar Acciones (con asignado/gastado por moneda)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-01-05 07:21"
updated: "2026-01-16 10:03"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/PED-1213"
---

# PED-1213: API - Feat - Listar Acciones (con asignado/gastado por moneda)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 07:21 |
| Actualizado | 2026-01-16 10:03 |
| Etiquetas | esperandoDependencia |
| Jira | [PED-1213](https://bluinc.atlassian.net/browse/PED-1213) |

## Relaciones

- **Padre:** [[PED-1208 - Gestión de Aportes y Gastos de Marketing|PED-1208]] Gestión de Aportes y Gastos de Marketing
- **has action item:** [[PED-1220 - APP - Feat - Listado de Acciones (con estado por moneda)|PED-1220]] APP - Feat - Listado de Acciones (con estado por moneda)
- **is cloned by:** [[PED-1265 - API - Refactor - Listar Acciones (con asignadogastado por moneda) -|PED-1265]] API - Refactor - Listar Acciones (con asignado/gastado por moneda) - Actualización objeto de respuesta y review de totalItems

## Descripcion

**Qué hay que hacer**

- Listar acciones y devolver sus totales desde `Marketing_ActionStats` (sin vistas).


- Permitir filtrar por `brandId` (acciones que tengan asignaciones desde fondos de esa marca).



**Endpoint**

```
GET /v1/marketing/actions?from={iso}&to={iso}&brandId={id}&currentPage=1&itemsPerPage=20
```

**Ejemplo request (llamada)**

```
GET /v1/marketing/actions?brandId=12&currentPage=1&itemsPerPage=20
```

**Ejemplo response (200)**

```
{
  "currentPage": 1,
  "itemsPerPage": 20,
  "totalItems": 1,
  "list": [
    {
      "id": 501,
      "name": "Hot Sale 2026",
      "startAt": "2026-05-11T00:00:00-03:00",
      "endAt": "2026-05-13T23:59:59-03:00",
      "totals": [
        { "currency": "USD", "allocatedTotal": 1200.00, "spentTotal": 600.00, "remaining": 600.00 }
      ]
    }
  ]
}

```

**SQL Server**

- `Marketing_Actions`


- `Marketing_ActionStats`


- joins para filtro `brandId`: `Marketing_Allocations` → `Marketing_Funds(BrandId)`



**Criterios de aceptación**

- Devuelve acciones paginadas y ordenadas.


- Incluye totales por moneda (ARS/USD) desde `Marketing_ActionStats`.


- Soporta filtro `brandId` (solo acciones relacionadas a fondos de esa marca).


- Soporta `from/to` según la regla definida (por fechas de acción).


- No usa vistas ni cálculos agregados pesados para listar.



---

Se actualiza el objeto de respuesta

```
{
  "currentPage": 1,
  "itemsPerPage": 20,
  "totalItems": 1,
  "list": [
    {
      "id": 501,
      "name": "Hot Sale 2026",
      "startAt": "2026-05-11T00:00:00-03:00",
      "endAt": "2026-05-13T23:59:59-03:00",
      "totals": {
        "1": { <------------------------------------------- SE AGREGA
          "currencyId": 1, <------------------------------- SE AGREGA
          "currencyDescription": "USD", <------------------ SE MODIFICA
          "amountOriginalTotal": 1200.00,
          "allocatedTotal": 1200.00,
          "spentTotal": 600.00,
          "availableToAllocateTotal": 0.00,
          "availableCashTotal": 600.00
        }
      }
    }
  ]
}
```
