---
jira_key: "LIO-386"
aliases: ["LIO-386"]
summary: "API - Feat - Evaluar integridad de una compra respecto a su envio, pago y descuentos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-07-14 13:24"
updated: "2025-09-12 16:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-386"
---

# LIO-386: API - Feat - Evaluar integridad de una compra respecto a su envio, pago y descuentos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-14 13:24 |
| Actualizado | 2025-09-12 16:08 |
| Etiquetas | ninguna |
| Jira | [LIO-386](https://bluinc.atlassian.net/browse/LIO-386) |

## Relaciones

- **Padre:** [[LIO-373]] Seguridad del checkout y protección de transacciones
- **has action item:** [[LIO-452]] API - Refactor - Se debe sumar a el analisis de integridad los nuevos parametros de uso de dinero en wallet

## Descripcion

Lo que haremos es evaluar la integridad del pedido en tres aspecto diferentes

```
POST {API_LEGACY}/pedidos/checkout/confirmar
```

Medio de pago, se evalúa el interés aplicado y el total pagadoMedio de envío, se evalúa que la cotización de envío sea igual a la del pedido confirmadoDescuentos, se evalúa que el descuento aplicado, sea el mismo que el del cupón de la tabla de cuponesCada uno de estos apartados tendrá un parámetro en `[LO].[dbo].[pedidosCabecera]` de modo tal que podamos ubicar rápidamente donde esta la diferencia para buscarla.

`[LO].[dbo].[pedidosCabecera].paymentIntegrity`

`[LO].[dbo].[pedidosCabecera].shippingIntegrity`

`[LO].[dbo].[pedidosCabecera].discountIntegrity`

Avisame como la ves o si cambiarías algo



Actualización:

La logica se agerga sobre el endpoint en V4.

```
POST /v4/payment/mercadopago/process
```

previo a procesar el pago se marcan los campos correspondiente para comprobar la integridad de la transacción.



Extra:

Si bien la tarea no menciona esto, cree un recurso llamado 

```
GET /v4/verifyTransactionIntegrity/{id_pedido}
```

Muestra claramente la diferencia entre el checkout precargador desde el front, y el construido por el back tomando la información capturada en cada recurso, (cotización, cupones descuento, interes de pagos, precio original de items).

Esto muestra a simple vista sin tener que ejecutar nuevamente el proceso de pago, cuales son las diferencias si es que existen en el pedido.

Ejemplo real en Prod. pedido: `737975`

response:

```json
{
    "checkoutFront": {
        "quote": {
            "id": 4041,
            "price": 0,
            "cost": 13961
        },
        "payment": {
            "installments": 1,
            "installment_rate": 0
        },
        "discount": 10000,
        "interest": 0,
        "total": 143127
    },
    "checkoutBack": {
        "quote": {
            "id": 4041,
            "price": 0,
            "cost": 13961
        },
        "payment": {
            "installments": 1,
            "installment_rate": 0
        },
        "discount": 10000,
        "interest": 0,
        "total": 143127
    },
    "integrity": {
        "payment": true,
        "shipping": true,
        "discount": true,
        "overall": true
    }
}
```



En `integrity`  si alguno es false se debe a que los valores podrian haber sido manipulados, o algún otro error que requiere atención.
