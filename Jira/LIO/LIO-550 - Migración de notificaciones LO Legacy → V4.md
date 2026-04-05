---
jira_key: "LIO-550"
aliases: ["LIO-550"]
summary: "Migración de notificaciones LO Legacy → V4"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-02-23 17:27"
updated: "2026-03-16 13:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-550"
---

# LIO-550: Migración de notificaciones LO Legacy → V4

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-02-23 17:27 |
| Actualizado | 2026-03-16 13:51 |
| Etiquetas | ninguna |
| Jira | [LIO-550](https://bluinc.atlassian.net/browse/LIO-550) |

## Relaciones

- **Subtarea:** [[LIO-552 - API - Feat - Envío de notificaciones pendientes por canal|LIO-552]] API - Feat -  Envío de notificaciones pendientes por canal
- **Subtarea:** [[LIO-553 - API - Feat - Contador de notificaciones pendientes website|LIO-553]] API - Feat - Contador de notificaciones pendientes website
- **Subtarea:** [[LIO-554 - API - Feat - Últimas notificaciones pendientes website|LIO-554]] API - Feat - Últimas notificaciones pendientes website
- **Subtarea:** [[LIO-555 - API - Feat - Listado paginado de notificaciones website|LIO-555]] API - Feat -  Listado paginado de notificaciones website
- **Subtarea:** [[LIO-556 - API - Feat - Marcar notificación como vista por token|LIO-556]] API - Feat - Marcar notificación como vista por token
- **Subtarea:** [[LIO-563 - API - LO - V4 - Feat - Procesar y despachar las notificaciones pendientes|LIO-563]] API -  LO - V4 - Feat - Procesar y despachar las notificaciones pendientes actuando como proxy 
- **Subtarea:** [[LIO-570 - APP - Refactor - Migrar de v3 a v4 - notificaciones|LIO-570]] APP - Refactor -  Migrar de v3 a v4 - notificaciones

## Descripcion

### Descripción

Se requiere migrar los endpoints de notificaciones actualmente implementados en **LO Legacy Notificaciones** hacia **LO V4**, centralizando la lógica en un único servicio y manteniendo la compatibilidad con el sistema actual de envío de emails.

El objetivo es que **LO V4** sea responsable de la creación, gestión y envío de notificaciones multicanal, incluyendo website y email, permitiendo además la futura extensión a otros canales.

Actualmente el endpoint de creación de notificaciones ya se encuentra implementado en V4, pero **no se está enviando el template de email correspondiente**. Como parte de esta migración, se deberá integrar la tabla de templates de email desde la base legacy (MariaDB) para mantener el comportamiento actual de envío de notificaciones por email.

Además, se deben migrar los endpoints asociados a notificaciones website (pendientes, listado, contador y marcado como vistas), asegurando compatibilidad funcional con legacy.

---

### Alcance

Migración de los siguientes endpoints desde legacy hacia V4:

- `POST /notifications`
Creación de notificación multicanal:

- Creación de cabecera de notificación


- Generación de token


- Acortamiento de URL


- Creación de registros por canal


- Integración con templates de email legacy




- `POST /notifications/send/pendings/{channel}`
Envío de notificaciones pendientes por canal.


- `GET /notifications/website/number/pending`
Obtención del total de notificaciones pendientes (no vistas) para un usuario.


- `GET /notifications/website/last/pending`
Obtención de las últimas notificaciones pendientes según límite.


- `GET /notifications/website/paginate`
Listado paginado de notificaciones website.


- `POST /notifications/{token}/mark-view`
Marcado de notificación como vista mediante token.



---

### Objetivos

- Centralizar la lógica de notificaciones en V4


- Mantener compatibilidad con templates de email legacy


- Permitir envío multicanal


- Unificar la lógica de notificaciones website


- Facilitar futuras extensiones de canales



---

### Consideraciones técnicas

- Los templates de email se obtendrán desde la base legacy (MariaDB).


- Se debe mantener compatibilidad con el formato actual de templates.


- El envío de emails debe continuar funcionando como en legacy.


- El offset del paginado website se mantiene en 20.


- El token de notificación debe seguir siendo válido para marcado como vista.
