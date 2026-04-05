---
jira_key: "PED-1265"
aliases: ["PED-1265"]
summary: "API - Refactor - Listar Acciones (con asignado/gastado por moneda) - Actualización objeto de respuesta y review de totalItems"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Franco Callipo"
reporter: "Guillermo Avila"
created: "2026-01-14 09:48"
updated: "2026-01-16 12:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1265"
---

# PED-1265: API - Refactor - Listar Acciones (con asignado/gastado por moneda) - Actualización objeto de respuesta y review de totalItems

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Franco Callipo |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-14 09:48 |
| Actualizado | 2026-01-16 12:03 |
| Etiquetas | ninguna |
| Jira | [PED-1265](https://bluinc.atlassian.net/browse/PED-1265) |

## Relaciones

- **Padre:** [[PED-1208]] Gestión de Aportes y Gastos de Marketing
- **clones:** [[PED-1213]] API - Feat - Listar Acciones (con asignado/gastado por moneda)

## Descripcion

Realizaremos un refactor para actualizar el objeto de respuesta, se agruparan los `totals` por `currencyId`, adicional a esto se agregara `currencyId` y modificaremos el nombre de la clave `currency` por `currencyDescription`.

```
GET /v1/marketing/actions?from={iso}&to={iso}&brandId={id}&currentPage=1&itemsPerPage=20
```



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



Adicionalmente te agrego algunas observaciones

- Al no filtrar por ninguna marca, la clave `totalItems` muestra cinco acciones, sin embargo, solo hay dos.



[adjunto]
