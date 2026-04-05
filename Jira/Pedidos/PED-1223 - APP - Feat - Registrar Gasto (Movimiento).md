---
jira_key: "PED-1223"
aliases: ["PED-1223"]
summary: "APP - Feat - Registrar Gasto (Movimiento)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-05 08:10"
updated: "2026-01-19 16:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1223"
---

# PED-1223: APP - Feat - Registrar Gasto (Movimiento)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 08:10 |
| Actualizado | 2026-01-19 16:05 |
| Etiquetas | ninguna |
| Jira | [PED-1223](https://bluinc.atlassian.net/browse/PED-1223) |

## Relaciones

- **Padre:** [[PED-1208 - Gestión de Aportes y Gastos de Marketing|PED-1208]] Gestión de Aportes y Gastos de Marketing
- **action item from:** [[PED-1214 - API - Feat - Registrar Movimiento Económico (gasto real + FX por movimiento)|PED-1214]] API - Feat - Registrar Movimiento Económico (gasto real + FX por movimiento)

## Descripcion

Formulario para cargar un gasto real, con moneda original y tipo de cambio por movimiento, y que calcule/visualice el impacto en la moneda del fondo.

**API**

```
POST /v1/marketing/movements
```

**Ejemplo payload**

```
{
  "fundId": 101,
  "actionId": 501,
  "allocationId": 9001,
  "conceptShort": "Meta Ads",
  "conceptLong": "Factura 0004-00001234",
  "originalCurrency": "ARS",
  "originalAmount": 300000,
  "fxRateToFund": 0.00125,
  "occurredAt": "2026-05-11T10:30:00-03:00"
}

```

**Criterios de aceptación**

- Campos requeridos: fondo, acción, concepto corto, moneda, monto, fecha; `allocationId` opcional.


- Si la moneda original coincide con la del fondo, el UI fuerza `fxRateToFund=1` (bloqueado o autocompletado).


- Muestra preview: `amountFinalFundCurrency = originalAmount * fxRateToFund` antes de enviar.


- Al éxito, refresca totales: `GET /v1/marketing/brands`, `GET /v1/marketing/actions` y grilla de movimientos.


- Maneja errores típicos: excede fondo, excede asignación, datos inválidos.
