---
jira_key: "PED-765"
aliases: ["PED-765"]
summary: "API - Refactor ajuste en syncup de comprobante de pago entre LO y NB"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-07-02 11:57"
updated: "2024-07-07 23:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-765"
---

# PED-765: API - Refactor ajuste en syncup de comprobante de pago entre LO y NB

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-07-02 11:57 |
| Actualizado | 2024-07-07 23:50 |
| Etiquetas | ninguna |
| Jira | [PED-765](https://bluinc.atlassian.net/browse/PED-765) |

## Relaciones

- **is blocked by:** [[SNB-2052]] COMPROBANTES DE PAGO

## Descripcion

Aplicación de PEDIDOS.

`Route::patch('paymentVoucher/syncup', [PaymentVoucherController::class, 'syncup']);`

Cuando se cargan 2 comprobantes desde LO. y tiene el mismo numero de pedidoCabeceraID. el syncup solo registra 1 comprobante, debido a que lo tomaba como que ya tenia ese valor registrado. 

SyncUp:

`LO.dbo.pedidosCabeceraComprobantePago`  → `FROM NB_WEB.dbo.pedidosCabeceraComprobantePago`

Corrección. ahora contempla ademas de `pedidoCabeceraID` el `nroOperacion` y el `archivo`.
