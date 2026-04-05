---
jira_key: "NBWEB-961"
summary: "APP - Refactor - Agregar número de pedido y lista de ítems al generar token de tarjeta en MercadoPago para que se visualicen en cada pago de la plataforma"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-04-11 14:19"
updated: "2025-04-22 11:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-961"
---

# NBWEB-961: APP - Refactor - Agregar número de pedido y lista de ítems al generar token de tarjeta en MercadoPago para que se visualicen en cada pago de la plataforma

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-11 14:19 |
| Actualizado | 2025-04-22 11:00 |
| Etiquetas | ninguna |
| Jira | [NBWEB-961](https://bluinc.atlassian.net/browse/NBWEB-961) |

## Descripción

Actualmente, al generar el token de pago con tarjeta de crédito para MercadoPago, no se están incluyendo datos clave que nos permitirían mejorar el seguimiento y trazabilidad del pago.

[attachment]


Se requiere modificar el proceso de generación del token para que se incluyan adicionalmente:

- El número de pedido de Libre Opción (`orderId`)


- La lista completa de ítems del pedido (nombre, cantidad, precio unitario, etc.)



**Objetivo:**
Mejorar la trazabilidad de los pagos realizados con tarjeta de crédito en MercadoPago, asociando el token generado con la información del pedido en Libre Opción.

(Así era antes)

[attachment]
**Criterios de aceptación:**

- El `numero de pedido` de Libre Opción debe incluirse como parte del objeto o payload para poder visualizarlo desde mercadopago.


- La lista completa de ítems del pedido debe incluirse como parte del mismo payload.


- Los datos deben enviarse en un formato compatible con la API de MercadoPago, ya sea dentro del `additional_info` o un campo similar permitido.


- Debe mantenerse la compatibilidad con pagos ya existentes (no romper flujos actuales).
