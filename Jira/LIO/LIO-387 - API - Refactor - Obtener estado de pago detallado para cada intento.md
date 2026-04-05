---
jira_key: "LIO-387"
aliases: ["LIO-387"]
summary: "API - Refactor - Obtener estado de pago detallado para cada intento"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-07-21 14:52"
updated: "2025-08-05 19:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-387"
---

# LIO-387: API - Refactor - Obtener estado de pago detallado para cada intento

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-21 14:52 |
| Actualizado | 2025-08-05 19:27 |
| Etiquetas | ninguna |
| Jira | [LIO-387](https://bluinc.atlassian.net/browse/LIO-387) |

## Relaciones

- **Padre:** [[LIO-8]] Proceso pago sencillo y competitiva a nivel financiamiento
- **blocks:** [[PED-1058]] API - Feat - Crear un recurso para obtener los intentos de pago de un usuario determinado
- **has action item:** [[LIO-389]] API - Refactor - Obtener estado de pago detallado para un usuario determinado

## Descripcion

Lo que queremos es sumar el parámetro que suele llamarse `mp_payment_status_detail`

Que suele tener estados mas específicos tipo 

```
accredited
bpp_refunded
by_admin
by_collector
by_payer
cc_amount_rate_limit_exceeded
cc_rejected_3ds_challenge
cc_rejected_bad_filled_card_number
cc_rejected_bad_filled_date
cc_rejected_bad_filled_other
cc_rejected_bad_filled_security_code
cc_rejected_blacklist
cc_rejected_call_for_authorize
cc_rejected_card_disabled
cc_rejected_high_risk
cc_rejected_insufficient_amount
cc_rejected_invalid_installments
cc_rejected_other_reason
expired
in_process
partially_refunded
refunded
reimbursed
rejected_high_risk
settled
```

Para esto agregaremos una columna extra en la tabla `[payment_gateway_transactions]`, junto a la que usamos para operar llamda `status` y la llamaremos `status_detail`
