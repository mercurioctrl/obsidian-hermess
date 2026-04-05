---
jira_key: "PED-496"
aliases: ["PED-496"]
summary: "APP - Feat - Mostrar modal con info de comprobante de pago - Visualización del accionable"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-01-17 20:14"
updated: "2024-01-18 11:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-496"
---

# PED-496: APP - Feat - Mostrar modal con info de comprobante de pago - Visualización del accionable

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-01-17 20:14 |
| Actualizado | 2024-01-18 11:15 |
| Etiquetas | ninguna |
| Jira | [PED-496](https://bluinc.atlassian.net/browse/PED-496) |

## Relaciones

- **blocks:** [[PED-485]] APP - Feat - Mostrar modal con info de comprobante de pago

## Descripcion

1. Además de considerar el habilitar el botón para ver el comprobante de pago cuando la orden tenga `idLo` habría que considerar también el estado de la orden, es decir, si está ya fue pagada y así como también si ésta ya tiene un tipo de pago establecido.

[adjunto]
Dato extra
Estas son los parámetros que encontré en un pedido que contiene un comprobante de pago

```
{
  "status": "s", 
  "statusId": 13, 
  "statusDescription": "Entregado Cobrado", 
  "idLo": 568627, 
  "paymentMethodId": 3, 
  "paymentMethodDescription": "Dep\u00f3sito en Banco",
}
```
