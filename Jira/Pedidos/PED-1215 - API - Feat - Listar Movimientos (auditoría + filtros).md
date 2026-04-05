---
jira_key: "PED-1215"
aliases: ["PED-1215"]
summary: "API - Feat - Listar Movimientos (auditoría + filtros)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-01-05 07:25"
updated: "2026-01-19 16:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1215"
---

# PED-1215: API - Feat - Listar Movimientos (auditoría + filtros)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 07:25 |
| Actualizado | 2026-01-19 16:27 |
| Etiquetas | ninguna |
| Jira | [PED-1215](https://bluinc.atlassian.net/browse/PED-1215) |

## Relaciones

- **Padre:** [[PED-1208]] Gestión de Aportes y Gastos de Marketing
- **has action item:** [[PED-1224]] APP - Feat - Screen - Auditoría de Movimientos (Listado + filtros)

## Descripcion

**Qué hay que hacer**

- Listar movimientos con filtros por fondo, acción, marca y fechas; mostrar original + conversión + impacto.



**Endpoint**

```
GET /v1/marketing/movements?fundId={id}&actionId={id}&brandId={id}&from={iso}&to={iso}&currentPage=1&itemsPerPage=50
```

**Ejemplo request (llamada)**

```
GET /v1/marketing/movements?brandId=12&from=2026-05-01T00:00:00-03:00&to=2026-05-31T23:59:59-03:00&currentPage=1&itemsPerPage=50

```

**Ejemplo response (200)**

```
{
  "currentPage": 1,
  "itemsPerPage": 50,
  "totalItems": 1,
  "list": [
    {
      "id": 70001,
      "fundId": 101,
      "actionId": 501,
      "allocationId": 9001,
      "conceptShort": "Meta Ads - campaña Hot Sale",
      "originalCurrency": "ARS",
      "originalAmount": 300000.00,
      "fxRateToFund": 0.00125,
      "amountFinalFundCurrency": 375.00,
      "occurredAt": "2026-05-11T10:30:00-03:00"
    }
  ]
}

```

**SQL Server**

- `Marketing_Movements` + join a `Marketing_Funds` para filtrar por `BrandId`.



**Criterios de aceptación**

- Devuelve paginado y ordenado por `OccurredAt DESC`.


- Filtros combinables: `fundId`, `actionId`, `brandId`, `from/to`.


- Incluye campos de conversión (`fxRateToFund`, `amountFinalFundCurrency`).


- No usa vistas.


- Query estable y performante con índices (`FundId/ActionId/OccurredAt`).
