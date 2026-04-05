---
jira_key: "STASK-23"
aliases: ["STASK-23"]
summary: "API - Feat - Implementar Twilio configuracion e implemetancion de sms queue works."
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-02-13 17:34"
updated: "2026-03-19 19:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-23"
---

# STASK-23: API - Feat - Implementar Twilio configuracion e implemetancion de sms queue works.

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-02-13 17:34 |
| Actualizado | 2026-03-19 19:39 |
| Etiquetas | ninguna |
| Jira | [STASK-23](https://bluinc.atlassian.net/browse/STASK-23) |

## Relaciones

- **Padre:** [[STASK-20 - API - Workers - Preparación para SMS y WhatsApp (sin ejecución)|STASK-20]] API - Workers - Preparación para SMS y WhatsApp (sin ejecución)

## Descripcion

El sistema deberá incorporar soporte para envío de notificaciones **SMS** utilizando **Twilio SDK**, con procesamiento asíncrono mediante **Laravel Queue**.

**Se deberá implementar:**

- Un **TwilioService** como wrapper del SDK de Twilio, con manejo centralizado de errores y logging estructurado.


- Un **PhoneNumberResolver** que resuelva el número de teléfono del usuario con fallback entre fuentes y normalización a formato **E.164**, incluyendo fix para números móviles de Argentina.


- Un **SmsNotificationService** que actúe como worker encargado del envío de SMS, con lógica de reintentos y actualización de estados.


- Un **ProcessSmsNotification** como Job de Laravel Queue, configurado con hasta 3 intentos y backoff exponencial (1, 5 y 15 minutos).


- Configuración de credenciales y parámetros de Twilio mediante archivo `config/twilio.php` y variables de entorno.



**Flujo esperado**:

- El endpoint `/queueNotification` recibe un payload solicitando el canal `sms`.


- Se crean los registros `notification_request` y `notification_attempt`.


- El job se encola en la queue `sms`.


- El worker resuelve y normaliza el teléfono del usuario y envía el SMS vía Twilio.


- Se actualiza el estado del attempt (`sent` / `failed`) y del request según el resultado.



**Comando de ejecución del worker**:

```
php artisan queue:work --queue=sms --tries=3 --timeout=90
```
