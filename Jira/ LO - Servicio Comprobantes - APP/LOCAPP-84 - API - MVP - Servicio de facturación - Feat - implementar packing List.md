---
jira_key: "LOCAPP-84"
aliases: ["LOCAPP-84"]
summary: "API - MVP - Servicio de facturación - Feat - implementar packing List"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2025-10-01 17:54"
updated: "2026-03-05 10:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-84"
---

# LOCAPP-84: API - MVP - Servicio de facturación - Feat - implementar packing List

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-01 17:54 |
| Actualizado | 2026-03-05 10:02 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-84](https://bluinc.atlassian.net/browse/LOCAPP-84) |

## Relaciones

- **Padre:** [[LOCAPP-80]] MVP - Vouchers para LASET (eticket, efactura,packingList "PL", SLI)
- **action item from:** [[LOCAPP-82]] APP - MVP - Feat - Crear maquetacion para packing List
- **has action item:** [[LOCAPP-85]] APP - MVP - Feat - Conectar packing List  con la api
- **is blocked by:** [[PED-1321]] API - Feat - Ver detalle pedido -> Agregar nro proforma (ver/editar)

## Descripcion

Se deben agregar como datos extra el shipTo que seríá el forwarder, y agregar `proformaInvoice` de la orden de venta ya que el resto de datos se tienen dentro del get actual


GET: [https://gamma.ms-comprobantes.lio.red/v2/FUy/754/deef6ac5351b0677f90a0783cf9f80](https://gamma.ms-comprobantes.lio.red/v2/FUy/754/deef6ac5351b0677f90a0783cf9f80)

el forwarder viene atado al pedido

ej:
[https://gamma.api.orders.lio.red/v1/orders/0002-10426782](https://gamma.api.orders.lio.red/v1/orders/0002-10426782)

Si no se entiende algo avisame
