---
jira_key: "LIO-423"
aliases: ["LIO-423"]
summary: "API - Feat - Completar intención de pago"
status: "Backlog"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-08-12 13:01"
updated: "2025-08-13 15:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-423"
---

# LIO-423: API - Feat - Completar intención de pago

| Campo | Valor |
|-------|-------|
| Estado | Backlog (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-12 13:01 |
| Actualizado | 2025-08-13 15:51 |
| Etiquetas | ninguna |
| Jira | [LIO-423](https://bluinc.atlassian.net/browse/LIO-423) |

## Relaciones

- **Padre:** [[LIO-416 - Intenciones de pago - checkout|LIO-416]] Intenciones de pago - checkout

## Descripcion

```
PATCH {API_URL}/payment-intents/{id}
```


Para completar la información de una intención de pago previamente creada, actualizando su monto, moneda, métodos de pago y datos del cliente. 

**Objetivo**:
Permitir que una intención de pago creada de forma incompleta pueda ser completada con toda la información necesaria para su procesamiento.

**Requerimientos funcionales**:

- **Entrada esperada**

- `amount` *(decimal, requerido si no estaba definido antes)* — Monto final a cobrar.


- `currency` *(string, requerido)* — Moneda de la operación.


- `paymentMethodType` *(string, requerido)* — Ej: `tarjeta`, `transferencia`, `wallet`.
**Para mas adelantes (no hace falta resolver ahora):**


- `details` *(JSON, opcional)* — Datos específicos del método (ej. token de tarjeta, CBU, ID externo, etc.).


- `clientData` *(JSON, opcional)* — Información del cliente (nombre, email, etc.).




- **Proceso**

- Verificar que la intención exista en `PaymentIntents`.


- Validar que el estado actual sea `pending`.

- Si no lo es → responder `409 Conflict`.




- Actualizar `PaymentIntents` con los nuevos valores (`amount`, `currency`, `updatedAt`, `status = pending`).


- Insertar un registro en `PaymentIntentMethods` con el medio de pago y su importe.


- Registrar en `PaymentLogs` el evento `"Payment intent updated"` con estado `pending`.




- **Salida esperada** (HTTP 200 OK):



```
{
  "id": "uuid",
  "status": "pending",
  "updatedAt": "2025-08-12T10:15:00Z"
}
```

**Respuestas de error**

- 400 Bad Request: Parámetros faltantes o inválidos.


- 404 Not Found: Intención no encontrada.


- 409 Conflict: Estado no permite completar la intención.


- 500 Internal Server Error: Fallo interno en la actualizació



**Tablas involucradas**:

- `PaymentIntents` (update).


- `PaymentIntentMethods` (insert del método de pago).


- `PaymentLogs` (insert log de completado).



**Notas técnicas**:

- Usar transacciones para asegurar consistencia entre la actualización de `PaymentIntents` y la inserción en `PaymentIntentMethods` y `PaymentLogs`.


- Validar que el monto en `PaymentIntentMethods.amount` sea igual al total de la intención (`PaymentIntents.amount`) para pagos completos o sumarizado en caso de pagos mixtos (en fases futuras).


- Manejar la serialización y deserialización del campo `details` en formato JSON.
