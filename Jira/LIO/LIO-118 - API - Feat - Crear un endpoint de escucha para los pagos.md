---
jira_key: "LIO-118"
aliases: ["LIO-118"]
summary: "API - Feat - Crear un endpoint de escucha para los pagos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-10-29 09:07"
updated: "2024-11-06 15:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-118"
---

# LIO-118: API - Feat - Crear un endpoint de escucha para los pagos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-29 09:07 |
| Actualizado | 2024-11-06 15:36 |
| Etiquetas | ninguna |
| Jira | [LIO-118](https://bluinc.atlassian.net/browse/LIO-118) |

## Relaciones

- **Padre:** [[LIO-8 - Proceso pago sencillo y competitiva a nivel financiamiento|LIO-8]] Proceso pago sencillo y competitiva a nivel financiamiento

## Descripcion

- **Recurso**:

- Crear un endpoint `POST` que recibirá notificaciones de pago de Getnet sobre el estado de una transacción, ya sea "autorizado" o "rechazado".




- **Endpoint Requerido**:

- URL: `POST API_URL/v4/webhook/getnet`


- Función: Recibir y procesar la información enviada desde Getnet con respecto al estado de pago.




- **Doc de Referencia**:

- Consulta la [link](https://developer.getnetworld.com/en/products/checkout-web-based?tab=documentation&documentationId=webhook-notifications-checkout-web-based)  para detalles sobre el formato de las notificaciones y sus parámetros.




- **Estructura de la Tabla de Almacenamiento**:

- La información recibida de Getnet debe almacenarse en la tabla `LO.dbo.logGetNetNotification` en la base de datos.


- Esta tabla almacenará tanto detalles individuales como el JSON completo de la notificación para referencia futura.


- Extraer los campos requeridos de la notificación de Getnet, incluyendo `payment_intent_id`, `checkout_id`, `order_id`, `payment_status`, y `payment_amount`.


- Guardar el JSON completo en el campo `payload` para futuras referencias o auditorías.



```
CREATE TABLE LO.dbo.logGetNetNotification (
    id INT PRIMARY KEY IDENTITY(1,1),
    payment_intent_id NVARCHAR(255) NOT NULL,
    checkout_id NVARCHAR(255) NOT NULL,
    order_id NVARCHAR(255) NOT NULL,
    payment_status NVARCHAR(255) NOT NULL,
    payment_amount DECIMAL(18, 2) NOT NULL,
    payload NVARCHAR(MAX) NOT NULL, 
    created_at DATETIME NOT NULL DEFAULT GETDATE(),
    updated_at DATETIME NOT NULL DEFAULT GETDATE()
);

```
