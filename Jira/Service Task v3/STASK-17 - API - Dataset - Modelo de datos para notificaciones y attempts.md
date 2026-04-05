---
jira_key: "STASK-17"
aliases: ["STASK-17"]
summary: "API - Dataset - Modelo de datos para notificaciones y attempts"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-13 08:47"
updated: "2026-02-24 21:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-17"
---

# STASK-17: API - Dataset - Modelo de datos para notificaciones y attempts

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-13 08:47 |
| Actualizado | 2026-02-24 21:16 |
| Etiquetas | ninguna |
| Jira | [STASK-17](https://bluinc.atlassian.net/browse/STASK-17) |

## Relaciones

- **Padre:** [[STASK-15 - Sistema de Notificaciones Multicanal (Queue + Workers)|STASK-15]] Sistema de Notificaciones Multicanal (Queue + Workers)

## Descripcion

Crear el modelo de persistencia que represente la intención de notificar y los intentos de envío por canal.
Debe permitir trazabilidad completa, reintentos y estados por usuario/canal.
El diseño debe soportar canales futuros sin cambios estructurales.

### Tablas

#### `notification_requests`

- id (uuid)


- type


- dedupe_key (nullable, unique)


- status (queued | processing | partial | sent | failed | canceled)


- channels_requested (json)


- channels_resolved (json)


- content (json)


- targets (json)


- data (json)


- created_at / updated_at



#### `notification_attempts`

- id


- request_id (uuid)


- channel (push | email | sms | whatsapp)


- target_type (users)


- target_id (userId)


- status (queued | sending | sent | delivered | failed | canceled)


- provider


- provider_message_id


- try_count


- error_code / error_message


- timestamps



### Criterios de aceptación

- `dedupe_key` permite idempotencia opcional.


- Existe un attempt por canal y por usuario.


- Los estados permiten reflejar envíos parciales.


- El modelo soporta agregar nuevos canales sin migraciones estructurales.
