---
jira_key: "LIO-390"
aliases: ["LIO-390"]
summary: "API - Refactor -  registrar status como rejected al disparar exception en error de pago v4"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-07-24 17:46"
updated: "2025-08-05 20:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-390"
---

# LIO-390: API - Refactor -  registrar status como rejected al disparar exception en error de pago v4

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-07-24 17:46 |
| Actualizado | 2025-08-05 20:49 |
| Etiquetas | ninguna |
| Jira | [LIO-390](https://bluinc.atlassian.net/browse/LIO-390) |

## Relaciones

- **Padre:** [[LIO-8 - Proceso pago sencillo y competitiva a nivel financiamiento|LIO-8]] Proceso pago sencillo y competitiva a nivel financiamiento

## Descripcion

Al procesar el pagos desde V4.

```
POST /payment/mercadopago/process
```

payload:

```
{
   "id": 741653
}
```



response:

```json
{
    "errors": {
        "status": 500,
        "title": "Error al procesar el pago: bad_request: Card Token not found",
        "file": "/var/www/app/app/Support/PaymentProviders/MercadoPago/MercadoPagoPayment.php",
        "line": 48
    }
}
```



Al dispararse un excepción como la siguente por un precargar incorrecta de un digito de la tarjeta por ejemplo, se debera marcar como `rejected` en las tablas `payment_gateway_transactions`  y `LO`.`dbo.pedidosCabecera `registrando tanto status como `status_detail.`

Esto permite que si el estado es `rejected`, se cancele el pedido y el stock se restaure.
