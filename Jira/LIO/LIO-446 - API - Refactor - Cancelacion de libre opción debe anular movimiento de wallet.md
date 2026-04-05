---
jira_key: "LIO-446"
aliases: ["LIO-446"]
summary: "API - Refactor - Cancelacion de libre opción debe anular movimiento de wallet si este existe"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-09 12:13"
updated: "2025-09-18 21:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-446"
---

# LIO-446: API - Refactor - Cancelacion de libre opción debe anular movimiento de wallet si este existe

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-09 12:13 |
| Actualizado | 2025-09-18 21:31 |
| Etiquetas | ninguna |
| Jira | [LIO-446](https://bluinc.atlassian.net/browse/LIO-446) |

## Relaciones

- **Padre:** [[LIO-419]] Mejoras de pagos

## Descripcion

**Quiero** que, al cancelar un pedido que había usado dinero de la wallet, se genere el movimiento de devolución correspondiente (haremos un movimiento igual y contrario)
**Para** mantener consistencia en la cuenta corriente y restituir el saldo del usuario.

### Flujo esperado

- **Cancelación de la orden**


- Cuando se recibe la petición:

```
PATCH {API_URL}/v4/purchase/{pedidoId}/cancel
```

**Movimiento en cuenta corriente**

- Si la orden tenía imputación de dinero en wallet:

- Se debe generar un registro en `[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]`.


- El registro debe ser **igual y contrario** al que se creó al momento de confirmar la compra.




- En este caso:

- Usar `TR_CODE = 30` (“CRÉDITOS VARIOS”).


- Concepto alternativo: **“Devolución de compra”**.


- Incluir también el **HMAC** como en los movimientos de débito.







### Criterios de aceptación

- Si la orden **no** tenía uso de wallet → no se genera ningún movimiento extra.


- Si la orden **sí** tenía uso de wallet → debe:

- Generarse un movimiento con `TR_CODE = 30` y concepto “Devolución de compra”.


- El importe debe ser **exactamente el mismo** que se descontó en el TR_CODE = 32 al confirmar la compra.


- El saldo en la wallet del usuario debe quedar como si nunca se hubiese usado en esa orden.




- La cancelación del pedido solo será válida si la devolución se imputó correctamente en la tabla de movimientos.





Dato complementario

La forma en la que este recurso identifica que linea de cta cte hacer referencia es mediante el campo idLo agregado en `MC_CCORRIENTES_MOVIMIENTOS`

```
-- ALTER TABLE [NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]
--     ADD showWallet bit DEFAULT 0,
--         idLo int DEFAULT null
```
