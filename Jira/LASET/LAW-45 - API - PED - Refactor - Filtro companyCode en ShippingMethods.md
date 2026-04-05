---
jira_key: "LAW-45"
aliases: ["LAW-45"]
summary: "API - PED -  Refactor - Filtro companyCode en ShippingMethods"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-03-10 08:33"
updated: "2026-03-13 16:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-45"
---

# LAW-45: API - PED -  Refactor - Filtro companyCode en ShippingMethods

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-10 08:33 |
| Actualizado | 2026-03-13 16:04 |
| Etiquetas | ninguna |
| Jira | [LAW-45](https://bluinc.atlassian.net/browse/LAW-45) |

## Relaciones

- **Padre:** [[LAW-44 - LASET FUSSY ISSUES - Limpieza da informacion que no es del contexto para una|LAW-44]] LASET FUSSY ISSUES - Limpieza da informacion que no es del contexto para una empresa determinada
- **has action item:** [[LAW-46 - APP - PED - Refactor -Filtro companyCode en ShippingMethods|LAW-46]] APP - PED - Refactor -Filtro companyCode en ShippingMethods

## Descripcion

La idea según lo que conversamos ayer, es poder sacarles de contexto informacion que les parece irrelevante para ellos para evitar confusiones y distracciones.

Para esto alteraremos el funcionamiento del filtro de ShippingMethods

## Descripción

Agregar soporte de filtrado por `companyCode` en los endpoints de medios de envío:

```
GET /v1/shippingMethods?companyCode={companyCode}&includeNull={includeNull}
```

### Comportamiento esperado

| Parámetros recibidos | Resultado |
| --- | --- |
| Sin parámetros | Devuelve todos sin filtro |
| `companyCode=11` | Solo los que tienen `companyCode = 11` |
| `companyCode=11&includeNull=true` | Los de `companyCode = 11` más los que tienen `companyCode IS NULL` |

---

## Verificación

```
# Todos
GET /v1/shippingMethods
​
# Solo 11
GET /v1/shippingMethods?companyCode=11
​
# 11 + sin companyCode
GET /v1/shippingMethods?companyCode=11&includeNull=true
```
