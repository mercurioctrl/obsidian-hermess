---
jira_key: "LIO-445"
aliases: ["LIO-445"]
summary: "API - Refactor - Al procesar la compra, comprobar y descontar monto de billetera en caso de ser utilizado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-09 08:47"
updated: "2025-09-15 20:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-445"
---

# LIO-445: API - Refactor - Al procesar la compra, comprobar y descontar monto de billetera en caso de ser utilizado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-09 08:47 |
| Actualizado | 2025-09-15 20:32 |
| Etiquetas | ninguna |
| Jira | [LIO-445](https://bluinc.atlassian.net/browse/LIO-445) |

## Relaciones

- **Padre:** [[LIO-419 - Mejoras de pagos|LIO-419]] Mejoras de pagos
- **has action item:** [[LIO-450 - API - Refactor - Al confirmar un pedido que usa plata en wallet o billetera,|LIO-450]] API - Refactor - Al confirmar un pedido que usa plata en wallet o billetera, agregar parametro idLo a la linea de cuenta corriente

## Descripcion

**Confirmación del pedido**

- Cuando se ejecuta la confirmación de un pedido (`POST {API_URL}/pedidos/checkout/confirmar`), **antes de hacer**:

```
UPDATE [LO].[dbo].[pedidosCabecera] 
SET [confirmado] = 1 …
```



```
POST {API_URL}/pedidos/checkout/confirmar
```

**Imputación en cuenta corriente**

- Insertar un registro en `[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]`.


- Este registro debe incluir el **HMAC**.


- Usar `TR_CODE = 32` (“DEBITOS VARIOS”).


- En el campo de “concepto alternativo” colocar: **“Uso de dinero en compras”**.



---

**Detalle del pedido**

- Al generar los registros en `[NewBytes_DBF].[dbo].[pedclil]`, los montos que se guardan en `npreunit` deben estar ya con el **descuento del wallet aplicado**, similar a como se aplican los descuentos.


- A esta lógica se debe agregar también el **prorrateo del **`usedHere`** de la wallet** en cada ítem, según su importe.


- Ejemplo: actualmente ya se descuenta con la siguiente lógica (ver query existente):



```
((([PD].precio - [PD].precio * [PD].descuento / 100 ) * (1 / [PC].cotizacion) / (0.01 * [PD].iva + 1)) - (([PD].descuentoLO / [PD].cantidad) * (1 / [PC].cotizacion) / (0.01 * [PD].iva + 1))) AS precioDolarSinIVA,
```

### Criterios de aceptación

- Si el usuario no usa wallet, no se imputa nada adicional.


- Si el usuario usa wallet parcial o total, debe:

- Generarse un movimiento en `MC_CCORRIENTES_MOVIMIENTOS` con HMAC y TR_CODE 32.


- Aplicarse el descuento correspondiente en cada `npreunit` de `pedclil`, prorrateado entre los ítems.




- La confirmación del pedido solo se completa si la imputación fue exitosa.
