---
jira_key: "PED-982"
aliases: ["PED-982"]
summary: "API - Refactor - Guardar cotización al autorizar un pago de Libre Opción con comprobante (Billetera Lo)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-04-08 08:16"
updated: "2025-04-23 04:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-982"
---

# PED-982: API - Refactor - Guardar cotización al autorizar un pago de Libre Opción con comprobante (Billetera Lo)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-08 08:16 |
| Actualizado | 2025-04-23 04:04 |
| Etiquetas | ninguna |
| Jira | [PED-982](https://bluinc.atlassian.net/browse/PED-982) |

## Relaciones

- **Padre:** [[PED-5 - Comprobantes|PED-5]] Comprobantes
- **action item from:** [[PED-691 - API - Autorizar pedido (cobrar) liquidado si tiene el comprobante guardado y si|PED-691]] API - Autorizar pedido (cobrar) liquidado si tiene el comprobante guardado y si es de libre opcion

## Descripcion

Actualmente, al realizar una operación de compra utilizando cuenta corriente (ya sea de forma manual o automática), **no se está registrando la cotización de la orden** en la tabla `[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]` Esto genera inconsistencias en el seguimiento financiero de las operaciones en dólares para el caso de la billetera de LO.

```
POST {API_URL}/v1/paymentForBank
```

**Payload:**

```
{
  "pedido": "X000200584145",
  "transferAmount": 324
}
```

- Se registre la cotización utilizada en la orden
