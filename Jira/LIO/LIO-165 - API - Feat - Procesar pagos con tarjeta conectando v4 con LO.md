---
jira_key: "LIO-165"
aliases: ["LIO-165"]
summary: "API - Feat - Procesar pagos con tarjeta conectando v4 con LO"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-12-17 09:26"
updated: "2025-01-27 17:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-165"
---

# LIO-165: API - Feat - Procesar pagos con tarjeta conectando v4 con LO

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-12-17 09:26 |
| Actualizado | 2025-01-27 17:26 |
| Etiquetas | ninguna |
| Jira | [LIO-165](https://bluinc.atlassian.net/browse/LIO-165) |

## Relaciones

- **Padre:** [[LIO-8 - Proceso pago sencillo y competitiva a nivel financiamiento|LIO-8]] Proceso pago sencillo y competitiva a nivel financiamiento
- **blocks:** [[LIO-152 - APP - Feat - Integrar procesamiento de pago de MP con SDK (sin salir de la|LIO-152]] APP - Feat - Integrar procesamiento de pago de MP con SDK (sin salir de la plataforma)

## Descripcion

#### **Proceso de Pago** con tarjeta.

- **Endpoint**: `API_URL_LO/pedidos/checkout/confirmar`


- **Método**: **POST**



payload:

```
{
    "id": 656089,
    "bulk": {
        "weightKg": 0.06,
        "sizeCm": "5.89x5.89x5.89",
        "amount": 4
    }
}

```

Este recurso ejecuta el metodo **confirmar()** de la clase **PedidoModel, el cual dispara las siguientes acciones.**

- Generar órdenes de compra para productos nativos.


- Sincronizar el stock según el origen de los productos.


- Confirmar cupones y tarjetas de descuento con **DescuentoModel**.


- Confirmar conversiones como InstantFlash y envío gratis.


- Obtener detalles del pedido con **obtenerPedidoCheckout**.


- Revisar regalos y confirmarlos con **RegaloModel**.


- Actualizar el estado del pedido a "confirmado".


- Crear notificaciones y correos electrónicos para los vendedores.


- Crear notificaciones, mensajes y correos electrónicos para el comprador.



Una vez terminado de confirmarse la disponibilidad y generarse los registros internos necesarios, se ejecuta el pago utilizando como puente v4 para pasar el payload tal cual se genero en la pasarela de pago, que fue guardado en `LO.dbo.payment_gateway_transactions`

#### **Puente entre V4 y LO.**

Una vez confirmada la disponibilidad de stock y generados los registros internos, se debe ejecutar el pago utilizando **MercadoPago (v4)**.

Se debe enviar el payload en algun campo, que pasarela se quiere utilizar. mercadopago/getnet/payway …

- **Endpoint**: `URL_V4_API/v4/payment/mercadopago/process`


- **Método**: **POST**


- **Payload**.

```
{
    "token": "919bde1e761a5655c4b8cdfd05c937d7",
    "transactionAmount": "1000",
    "description": "varios",
    "installments": 1,
    "paymentMethodId": "master",
    "issuer": 3,
    "email": "ferreyraemanuel001@gmail.com",
    "identificationType": "DNI",
    "identificationNumber": "12345678",
    "cardholderName": "APRO"
}
```



#### **Validaciones y Detalles Importantes**

- **Validación del importe**:
El campo `transactionAmount` debe coincidir exactamente con el **total final del pedido**, calculado durante el proceso de confirmación.


- **Actualizar estado del pedido**:
La respuesta del recurso `/v4/payment/mercadopago/process` debe ser utilizada para cambiar el **estado** y el **detalle del estado** del pedido.
Ejemplo de respuesta esperada de MercadoPago:

```
{
    "id": "1328757049",
    "status": "approved",
    "statusDetail": "accredited",
    "message": "¡Listo! Se acreditó tu pago."
}
```




- **Estados y Detalles Posibles**:

**Estado**`status_detail`**Descripciónapproved**`accredited`¡Listo! Se acreditó tu pago. En tu resumen verás el cargo como `statement_descriptor`.**approved**`partially_refunded`El pago se realizó con al menos un reembolso parcial.**authorized**`pending_capture`El pago fue autorizado y está a la espera de ser capturado.**pending**`pending_waiting_transfer`Esperando que el usuario termine el proceso de pago en su banco (caso transferencia bancaria).**rejected**`cc_rejected_other_reason`El pago fue rechazado. **Permitir reintento de pago**.


- **Comportamiento en estados rechazados y pendientes**:

- Si el estado es `rejected`, se debe permitir al usuario **reintentar el pago**.


- Si el estado es `pending` o `authorized`, el sistema debe **esperar** al cambio de estado a `approved` antes de continuar.
