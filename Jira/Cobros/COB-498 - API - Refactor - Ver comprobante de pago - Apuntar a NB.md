---
jira_key: "COB-498"
aliases: ["COB-498"]
summary: "API - Refactor - Ver comprobante de pago - Apuntar a NB"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-03-19 11:50"
updated: "2024-05-06 20:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-498"
---

# COB-498: API - Refactor - Ver comprobante de pago - Apuntar a NB

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-03-19 11:50 |
| Actualizado | 2024-05-06 20:42 |
| Etiquetas | ninguna |
| Jira | [COB-498](https://bluinc.atlassian.net/browse/COB-498) |

## Relaciones

- **Padre:** [[COB-487 - Feat - Cobrables - Comprobantes de pago|COB-487]] Feat - Cobrables -> Comprobantes de pago
- **relates to:** [[PED-585 - API - Feat - Agregar comprobantes de pago|PED-585]] API - Feat - Agregar comprobantes de pago
- **relates to:** [[COB-489 - API - Feat - Ver comprobante de pago|COB-489]] API - Feat - Ver comprobante de pago
- **is blocked by:** [[COB-500 - API - Ver comprobante de pago - No se encuentra el comprobante|COB-500]] API - Ver comprobante de pago - No se encuentra el comprobante
- **is blocked by:** [[COB-502 - API - Ver comprobante de pago - No se visualiza la imagen|COB-502]] API - Ver comprobante de pago - No se visualiza la imagen

## Descripcion

Vamos a llevar a cabo una refactorización en el recurso para que en lugar de hacer referencia a `[LO].[dbo].[pedidosCabeceraComprobantePago]` haga referencia a `[NB_WEB].[dbo].[pedidosCabeceraComprobantePago]`

Siguiendo el mismo enfoque que se utiliza en el sistema de Pedidos.

```
GET {API_URL}/v1/paymentVoucher/{branch-order}
```
