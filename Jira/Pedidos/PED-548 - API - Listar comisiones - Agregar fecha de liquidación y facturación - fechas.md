---
jira_key: "PED-548"
aliases: ["PED-548"]
summary: "API - Listar comisiones -> Agregar fecha de liquidación y facturación - fechas de facturación y remito faltantes"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-02-08 16:53"
updated: "2024-02-14 14:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-548"
---

# PED-548: API - Listar comisiones -> Agregar fecha de liquidación y facturación - fechas de facturación y remito faltantes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-08 16:53 |
| Actualizado | 2024-02-14 14:37 |
| Etiquetas | ninguna |
| Jira | [PED-548](https://bluinc.atlassian.net/browse/PED-548) |

## Relaciones

- **Padre:** [[PED-6 - Comisiones|PED-6]] Comisiones
- **blocks:** [[PED-529 - API - Feat - Listar comisiones - Agregar fecha de liquidacion y facturacion|PED-529]] API - Feat - Listar comisiones -> Agregar fecha de liquidacion y facturacion
- **relates to:** [[PED-559 - APP - Listar comisiones - Agregar fecha de remito|PED-559]] APP - Listar comisiones - Agregar fecha de remito

## Descripcion

- He encontrado casos en los que las fechas de facturación de pedidos con sucursal 10 no se están mostrando. 



[adjunto]
[adjunto]


Dato extra:

Esto puede deberse a que en una de las consultas para obtener las comisiones de los pedidos con sucursal 10, no se están relacionando con `[NewBytes_DBF].[dbo].[FP_FactWebCliEncabezado]`



2. Se que no está especificado en la tarea original, pero hay que agregar al recurso la fecha del remito.
