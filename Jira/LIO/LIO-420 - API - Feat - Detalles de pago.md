---
jira_key: "LIO-420"
aliases: ["LIO-420"]
summary: "API - Feat - Detalles de pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-08-11 09:35"
updated: "2025-08-20 07:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-420"
---

# LIO-420: API - Feat - Detalles de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-11 09:35 |
| Actualizado | 2025-08-20 07:32 |
| Etiquetas | ninguna |
| Jira | [LIO-420](https://bluinc.atlassian.net/browse/LIO-420) |

## Relaciones

- **Padre:** [[LIO-419]] Mejoras de pagos
- **has action item:** [[LIO-429]] APP - Feat - Detalle de pago

## Descripcion

En la linea similar al recurso 

```
GET {API_URL}/v4/estados/pedidos/{pedidoLo}
```

que indica los estados generales debemos agregar un recurso para obtener mas detalles de algunas cuestiones especificas, en caso de ser necesario.

Para esto podremos agregar un recurso similar a 

```
GET {API_URL}/v4/estados/pedidos/{pedidoLo}/pago
```

```
{
  "paymentStatus": "Rechazado",
  "paymentStatusDetail": "Debes autorizar el pago con tu banco.",
  "paymentStatusCode": "cc_rejected_call_for_authorize",
  "paymentStatusTip": "La compra no pudo completarse. Llama al número del dorso de tu tarjeta para que el banco la autorice y vuelve a intentarlo.",
}

```

La idea es utilizando la clave de `paymentStatusDetail` cuando sea posible y la tabla `[LO].[dbo].[payment_status_detail]` entregar informacion detallada de lo sucedido y como proceder
