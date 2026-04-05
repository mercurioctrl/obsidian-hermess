---
jira_key: "LAW-48"
aliases: ["LAW-48"]
summary: "API - PED - Refector - Filtro companyCode + includeNull en PaymentMethods"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-03-10 09:37"
updated: "2026-03-13 18:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-48"
---

# LAW-48: API - PED - Refector - Filtro companyCode + includeNull en PaymentMethods

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-10 09:37 |
| Actualizado | 2026-03-13 18:50 |
| Etiquetas | ninguna |
| Jira | [LAW-48](https://bluinc.atlassian.net/browse/LAW-48) |

## Relaciones

- **Padre:** [[LAW-44]] LASET FUSSY ISSUES - Limpieza da informacion que no es del contexto para una empresa determinada
- **has action item:** [[LAW-49]] APP - PED - Feat- Filtro companyCode + includeNull en PaymentMethods

## Descripcion

## Contexto

El repositorio ya tiene soporte parcial de `companyCode`, pero con un comportamiento incorrecto: cuando se filtra por `companyCode` **siempre incluye los registros con **`companyCode IS NULL`, sin que el llamador pueda controlarlo.

```
GET v1/paymentMethods
```

El nuevo esquema separa esa lógica en un parámetro explícito `includeNull`.

### Comportamiento esperado

| Parámetros recibidos | Resultado |
| --- | --- |
| Sin parámetros | Todos sin filtro |
| `companyCode=11` | Solo los que tienen `companyCode = 11` |
| `companyCode=11&includeNull=true` | Los de `companyCode = 11` más los que tienen `companyCode IS NULL` |

## ⚠️ Cambio de comportamiento

El comportamiento actual (cuando llega `companyCode`) **siempre incluía los NULL**. Con este cambio, el filtrado por `companyCode` **excluye los NULL por defecto**. Verificar que ningún llamador existente dependa del comportamiento anterior.
