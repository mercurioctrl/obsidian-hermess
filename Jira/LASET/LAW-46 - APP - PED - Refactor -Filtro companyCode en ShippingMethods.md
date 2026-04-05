---
jira_key: "LAW-46"
aliases: ["LAW-46"]
summary: "APP - PED - Refactor -Filtro companyCode en ShippingMethods"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-03-10 08:33"
updated: "2026-03-13 16:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-46"
---

# LAW-46: APP - PED - Refactor -Filtro companyCode en ShippingMethods

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-10 08:33 |
| Actualizado | 2026-03-13 16:05 |
| Etiquetas | ninguna |
| Jira | [LAW-46](https://bluinc.atlassian.net/browse/LAW-46) |

## Relaciones

- **Padre:** [[LAW-44]] LASET FUSSY ISSUES - Limpieza da informacion que no es del contexto para una empresa determinada
- **action item from:** [[LAW-45]] API - PED -  Refactor - Filtro companyCode en ShippingMethods

## Descripcion

La idea según lo que conversamos ayer, es poder sacarles de contexto informacion que les parece irrelevante para ellos para evitar confusiones y distracciones.

Para esto alteraremos el funcionamiento del filtro de ShippingMethods

## Descripción

Modificar las actions del store `orders` para que puedan enviar los parámetros `companyCode` e `includeNull` al backend al consultar los medios de envío.

### Comportamiento esperado

- Si no se pasan parámetros → comportamiento actual (sin cambios).


- Si se pasa `companyCode` → filtra por ese código.


- Si se pasa `companyCode` + `includeNull: true` → filtra por ese código más los que tienen `companyCode` nulo.



---

##
