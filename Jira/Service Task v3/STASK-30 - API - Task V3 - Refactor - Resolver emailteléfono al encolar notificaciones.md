---
jira_key: "STASK-30"
aliases: ["STASK-30"]
summary: "API - Task V3 - Refactor - Resolver email/teléfono al encolar notificaciones"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-03-02 18:54"
updated: "2026-03-03 13:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-30"
---

# STASK-30: API - Task V3 - Refactor - Resolver email/teléfono al encolar notificaciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-03-02 18:54 |
| Actualizado | 2026-03-03 13:15 |
| Etiquetas | ninguna |
| Jira | [STASK-30](https://bluinc.atlassian.net/browse/STASK-30) |

## Relaciones

- **Padre:** [[STASK-15]] Sistema de Notificaciones Multicanal (Queue + Workers)

## Descripcion

Actualmente, los campos `email_address` y `phone_number` en `notification_attempts` quedan en `NULL` al momento de encolar la notificación. Estos valores recién se resuelven cuando el job se ejecuta, lo que dificulta la auditoría y el debugging.

Se requiere modificar este comportamiento para que los datos queden resueltos desde el momento de la creación del attempt.

---

##  Alcance de la tarea

###  Resolver datos al momento de encolar

- Resolver `email_address` y `phone_number` en el momento de crear los `notification_attempts`.


- El comportamiento debe ser consistente con lo que ya ocurre con `device_token` en push.


- Los valores deben persistirse directamente en la tabla `notification_attempts`.



---

###  Crear resolvers centralizados

Crear dos componentes reutilizables:

- `EmailResolver`


- `PhoneResolver`



Estos deberán:

- Encapsular la lógica de resolución.


- Poder reutilizarse desde el repository o desde los workers.


- Evitar duplicación de lógica.



---

###  Actualizar Services / Workers

Actualizar:

- `EmailNotificationService`


- `SmsNotificationService`


- `WhatsAppNotificationService`



Para que:

- Lean el `email_address` o `phone_number` directamente desde el `notification_attempt`.


- Implementen un **fallback por compatibilidad**:

- Si el campo viene `NULL` (attempts antiguos), usar el resolver como mecanismo de respaldo.





---

###  Logging

Agregar logs que indiquen claramente el origen del dato utilizado:

- `"source=attempt"` cuando el dato proviene del attempt.


- `"source=resolver"` cuando se use el fallback.



---

##  Resultado esperado

- `notification_attempts` debe tener `email_address` y `phone_number` completos desde su creación.


- No debe resolverse el mismo dato múltiples veces en reintentos.


- El comportamiento debe ser consistente con push notifications.
