---
jira_key: "BLUWEB-207"
aliases: ["BLUWEB-207"]
summary: "API - Feat - Recurso para formularios de contacto para landings de clientes (partner contact forms)"
status: "LISTO"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-14 08:33"
updated: "2025-12-05 10:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-207"
---

# BLUWEB-207: API - Feat - Recurso para formularios de contacto para landings de clientes (partner contact forms)

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-14 08:33 |
| Actualizado | 2025-12-05 10:59 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-207](https://bluinc.atlassian.net/browse/BLUWEB-207) |

## Relaciones

- **Padre:** [[BLUWEB-206]] Partner Services (Servicios para asociados)
- **has action item:** [[FB-91]] APP - Refactor - Conectar formulario de contacto utilizando el recurso y token de cliente

## Descripcion

Se aceptan cambios o mejoras a la idea origina y de llevarse adelante debe ser alterada la informacion de la historia con la solución tal cual fue realizada

Vamos a crear un recurso en la API que permita a las landings de nuestros clientes (sitios estáticos, sin backend propio) enviar formularios de contacto hacia nuestra API, para que:

- Se envíe un correo usando la configuración SMTP del cliente.


- Se registre el mensaje en una tabla interna para auditoría y seguimiento.


- Todo quede asociado al cliente que usa el servicio, de forma segura.



Cada cliente tendrá una configuración de correo en una tabla específica, y accederá al recurso usando una **apiKey** propia.

### Alcance funcional

- **Tabla de configuración de formularios de contacto** (ejemplo)

- Tabla: `contact_forms_config` (nombre a definir)


- Campos mínimos:

- `id` (PK)


- `clientId`


- `siteOrigin` (dominio / URL base autorizado, opcional pero deseable)


- `smtpHost`


- `smtpPort`


- `smtpUser`


- `smtpPassword` (encriptado)


- `smtpEncryption` (none / ssl / tls)


- `fromName`


- `fromEmail`


- `toEmail` (correo destino donde se reciben los formularios)


- `replyToEmail` (opcional)


- `isActive`






- **Tabla de registro de mensajes de contacto**

- Tabla: `contact_forms_messages` (nombre a definir)


- Campos mínimos:

- `id` (PK)


- `clientId`


- `siteOrigin` (dominio desde el que se envió)


- `formIdentifier` (opcional, por si el cliente tiene varios formularios)


- `senderName`


- `senderEmail`


- `senderPhone` (opcional)


- `subject` (opcional)


- `message`


- `extraData` (JSON opcional: campos adicionales)


- `status` (SENT / FAILED)


- `errorMessage` (nullable)


- `createdAt`






- **Autenticación / seguridad**

- Cada cliente tendrá una **apiKey** (por ejemplo en la tabla existente `clients`).


- La apiKey se enviará desde el front en un header, por ejemplo:

- `X-Client-ApiKey: {apiKey}`




- El backend:

- Valida la apiKey.


- Resuelve el `clientId` asociado.


- Opcional: valida `Origin` / `Referer` contra `siteOrigin` de la configuración.







---

```
POST {API_URL}/partner/contact-forms/submit
```

```
{
  "siteOrigin": "https://landing-cliente.com",
  "formIdentifier": "contacto-principal",
  "senderName": "Juan Pérez",
  "senderEmail": "juan@example.com",
  "senderPhone": "+54 11 1234-5678",
  "subject": "Consulta sobre producto",
  "message": "Hola, quería más información sobre el producto X.",
  "extraData": {
    "utm_source": "google-ads",
    "utm_campaign": "campania-abril"
  }
}

```

**Comportamiento**

- Valida la `apiKey`:

- Si no existe o está inactiva → 401.




- Determina el `clientId` asociado a la apiKey.


- Obtiene la configuración SMTP del cliente desde `contact_forms_config`.


- Opcional: valida que `siteOrigin` y/o el header `Origin` esté permitido para ese cliente.


- Envía el correo usando la configuración SMTP:

- `fromName` / `fromEmail` configurados.


- `toEmail` configurado en la tabla.


- `replyTo` con `senderEmail` cuando sea posible.




- Guarda un registro en `contact_forms_messages` con todos los datos, estado y eventual error.


- Devuelve una respuesta JSON amigable para el front.



**Respuesta de éxito (ejemplo)**

```
{
  "success": true,
  "message": "El mensaje fue enviado correctamente.",
  "status": "SENT"
}

```

**Respuesta de error SMTP (ejemplo)**

```
{
  "success": false,
  "message": "No se pudo enviar el mensaje.",
  "status": "FAILED",
  "errorCode": "SMTP_ERROR"
}

```

---

### Criterios de aceptación

- Si la `X-Client-ApiKey` es inválida o no está configurada, el endpoint devuelve **401** con un JSON indicando error de autenticación.


- Cuando la apiKey es válida y la configuración SMTP existe y está activa, el sistema:

- envía el correo al `toEmail` configurado,


- y registra el mensaje en la tabla `contact_forms_messages` con estado **SENT**.




- Si ocurre un error al enviar el correo (problema de SMTP, credenciales, etc.), el sistema:

- registra el mensaje con estado **FAILED** y el detalle del error,


- devuelve **500** con un código de error genérico (`SMTP_ERROR` o similar).




- El endpoint permite ser llamado desde un front de landing simple (sin backend propio), con soporte de CORS configurado por dominio por cliente.


- Existe un mecanismo básico de rate limiting por `clientId` y/o IP para evitar abuso masivo del recurso.
