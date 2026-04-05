---
jira_key: "LIO-312"
aliases: ["LIO-312"]
summary: "APP - Refactor - Mostrar cuotas diferenciadas por medio de pago en la ficha del producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-04-03 09:10"
updated: "2025-04-09 23:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-312"
---

# LIO-312: APP - Refactor - Mostrar cuotas diferenciadas por medio de pago en la ficha del producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-03 09:10 |
| Actualizado | 2025-04-09 23:40 |
| Etiquetas | ninguna |
| Jira | [LIO-312](https://bluinc.atlassian.net/browse/LIO-312) |

## Relaciones

- **Padre:** [[LIO-119 - Inventario|LIO-119]] Inventario
- **action item from:** [[LIO-311 - API - Refactor del recurso de item para soportar intereses diferenciados por|LIO-311]] API - Refactor del recurso de item para soportar intereses diferenciados por cuota

## Descripcion

Actualizar la visualización de medios de pago para mostrar el desglose de cuotas con intereses diferenciados, cuando estén disponibles en el objeto del medio de pago. El objetivo es brindar al usuario una referencia clara del monto de cada cuota según el plan de financiación.

### 💡 Detalles funcionales

- En la sección de **medios de pago** de la ficha del producto:

- Detectar si un medio de pago tiene al menos uno de los campos `interes1`, `interes3`, `interes6`, `interes9`, `interes12` distinto de `null`.


- Por cada uno que tenga valor (incluso si es `0`), calcular el valor de la cuota y renderizarlo en el formato 

[adjunto]

- Mostrar el ícono de tarjeta en cada línea (como en el ejemplo adjunto).


- No se deben mostrar líneas si el interés para esa cuota es `null`.





### ✅ Criterios de aceptación

- Se muestran todas las opciones de cuotas que tengan `interesN` distinto de `null`.


- El cálculo del monto por cuota se realiza correctamente.


- El valor se formatea en pesos argentinos.


- Si no hay intereses diferenciados, se mantiene el comportamiento actual (retrocompatibilidad).


- Compatible con todos los medios de pago, no solo Mercado Pago.


- Mobile responsive.
