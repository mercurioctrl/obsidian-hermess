---
jira_key: "COB-555"
aliases: ["COB-555"]
summary: "API - Refactor - Al cobrar se debe registrar cotización en operaciones con cuenta corriente (billetera LO)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-04-08 08:12"
updated: "2025-04-23 04:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-555"
---

# COB-555: API - Refactor - Al cobrar se debe registrar cotización en operaciones con cuenta corriente (billetera LO)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-08 08:12 |
| Actualizado | 2025-04-23 04:01 |
| Etiquetas | ninguna |
| Jira | [COB-555](https://bluinc.atlassian.net/browse/COB-555) |

## Relaciones

- **Padre:** [[COB-115]] Feat - Realizar un cobro

## Descripcion

Actualmente, al realizar una operación de compra utilizando cuenta corriente (ya sea de forma manual o automática), **no se está registrando la cotización de la orden** en la tabla `[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]` Esto genera inconsistencias en el seguimiento financiero de las operaciones en dólares para el caso de la billetera de LO.

```
POST {API_URL}/v1/box
```

**Payload:**

```
[
  {
    "clientId": 26806,
    "pedido": ["X000200584142"],
    "finalAmount": 32.91,
    "payments": [
      {
        "paymentMethodId": 1,
        "amountPaid": 35,
        "bankAccountId": null,
        "isOrder": false,
        "quote": 1,
        "provinceId": null
      }
    ],
    "comment": ""
  }
]
```

- Se registre la cotización utilizada en la orden
