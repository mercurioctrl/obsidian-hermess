---
jira_key: "PED-1276"
aliases: ["PED-1276"]
summary: "API - Review - Para los BANCOS que tienen companyCode en NULL vienen siempre"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-22 08:16"
updated: "2026-01-26 10:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1276"
---

# PED-1276: API - Review - Para los BANCOS que tienen companyCode en NULL vienen siempre

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-22 08:16 |
| Actualizado | 2026-01-26 10:48 |
| Etiquetas | ninguna |
| Jira | [PED-1276](https://bluinc.atlassian.net/browse/PED-1276) |

## Relaciones

- **Padre:** [[PED-1257]] Repositorio Bancos y medios de pago

## Descripcion

En la misma linea de lo realizado en [link](https://bluinc.atlassian.net/browse/PED-1272)  haremos que los bancos del repositorio

```
GET v1/banks
```

Vengan filtrados por empresa, pero en el caso de tener `[NEW_BYTES].[dbo].[BA_BP_CAJA_CBANCARIAS].companyCode` en `NULL` se debe mostrar siempre.

El objetivo es  el mismo, lograr una transición ordenada hasta separar el concepto de empresa y empresa  de facturación, que se  dará posterior al empalme del MVP.

Ademas, sirve de *feature flag* para resolver rápido compatibilidades o inconvenientes de cobro.
