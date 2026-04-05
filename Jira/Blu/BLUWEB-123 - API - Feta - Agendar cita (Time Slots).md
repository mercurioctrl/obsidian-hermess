---
jira_key: "BLUWEB-123"
aliases: ["BLUWEB-123"]
summary: "API - Feta - Agendar cita (Time Slots)"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-11 13:33"
updated: "2025-08-29 10:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-123"
---

# BLUWEB-123: API - Feta - Agendar cita (Time Slots)

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-11 13:33 |
| Actualizado | 2025-08-29 10:03 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-123](https://bluinc.atlassian.net/browse/BLUWEB-123) |

## Relaciones

- **Padre:** [[BLUWEB-121 - Agenda de cita por calendario en contacto|BLUWEB-121]] Agenda de cita por calendario en contacto

## Descripcion

Este endpoint permite **crear una reserva de reunión** sobre un horario previamente disponible en el calendario. El visitante selecciona un `timeslot` y envía sus datos de contacto para confirmar la cita.

El objetivo es:

- Verificar que el `timeslot` esté disponible en el momento de la reserva.


- Bloquear el horario (`is_available=false`) para evitar dobles reservas.


- Guardar la información de la reunión y generar un token único que permita su cancelación posterior sin login.


- Enviar un correo electrónico al usuario y al administrador con la confirmación de la cita, incluyendo archivo `.ics` adjunto y links para añadir al calendario (Google, Outlook, Apple).



Este recurso es clave para la funcionalidad central de la agenda, tanto en el sitio público como en integraciones externas.

```
POST {API_URL}/calendar/meetings
```

```
{
  "client_name": "Ezequiel Manzano",
  "client_email" : "ezequielm789@gmail.com",
  "service_id": 1,
  "time_slot_id": 3,
  "client_notes": "Primera consulta"
}

```

**Campos obligatorios:**

- `name` *(string)* → nombre de la persona que agenda.


- `email` *(string, formato válido)* → email de contacto.


- `timeslot_id` *(int)* → ID del horario a reservar.


- `timezone` *(string, opcional con default)* → zona horaria del usuario.



**Campos opcionales:**

- `phone` *(string)* → teléfono de contacto.


- `notes` *(string)* → comentarios adicionales.



### **Respuesta esperada**

**201 Created** – cita creada correctamente.

```
{
    "success": true,
    "message": "Cita creada exitosamente.",
    "data": {
        "appointment": {
            "id": 3,
            "client": {
                "name": "Ezequiel Manzano",
                "email": "ezequielm789@gmail.com"
            },
            "service": {
                "id": 1,
                "name": "Consulta General",
                "description": "Consulta general",
                "duration_minutes": 30
            },
            "time_slot": {
                "id": 3,
                "status": "booked"
            },
            "appointment_date": "2025-08-25",
            "start_time": "10:00",
            "end_time": "10:30",
            "status": null,
            "client_notes": "Primera consulta",
            "duration_minutes": 30,
            "is_upcoming": true,
            "cancel_token": "DgEhmTi7dz4eNyAWASuzUO69bftfH0rn",
            "created_at": "2025-08-14 10:41:05",
            "confirmed_at": null,
            "cancelled_at": null
        }
    }
}
```

### **Flujo interno**

- Validar que el `timeslot_id` exista y `is_available=true`.


- Crear la reunión (`meetings`) y generar `cancel_token` único.


- Marcar el `timeslot` como `is_available=false`.


- Enviar email de confirmación:

- Adjuntar archivo `.ics` con cita.


- Incluir links para Google Calendar, Outlook y Yahoo.


- Incluir link único para cancelar.





---

### **Errores**

- **404 Not Found** → `timeslot_id` inexistente.


- **409 Conflict** → el horario ya fue reservado.


- **422 Unprocessable Entity** → datos inválidos (formato de email, campos faltantes).



Ejemplo de error 409:

```
{
  "error": "El horario seleccionado ya no está disponible."
}

```

### **SQL base**

```
CREATE TABLE meetings (
  id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  timeslot_id BIGINT UNSIGNED NOT NULL,
  name VARCHAR(120) NOT NULL,
  email VARCHAR(190) NOT NULL,
  phone VARCHAR(40) NULL,
  notes TEXT NULL,
  timezone VARCHAR(64) NOT NULL DEFAULT 'America/Argentina/Buenos_Aires',
  cancel_token CHAR(64) NOT NULL,
  canceled_at DATETIME NULL,
  created_at TIMESTAMP NULL,
  updated_at TIMESTAMP NULL,
  UNIQUE KEY uq_cancel_token (cancel_token),
  UNIQUE KEY uq_timeslot_id (timeslot_id),
  CONSTRAINT fk_meetings_timeslot
    FOREIGN KEY (timeslot_id) REFERENCES timeslots(id)
    ON UPDATE CASCADE ON DELETE RESTRICT
);
```

### **Nota técnica**

```
use Illuminate\Support\Str;
use Carbon\Carbon;
```

- `Str::random(32)` → para generar `cancel_token` único (puede ser hash + UUID).


- Validar disponibilidad en transacción DB para evitar condiciones de



```
AVAILABLE_DAYS=mon,tue,wed,thu,fri
MEETING_START_TIME=09:00
MEETING_DURATION_MINUTES=30
TIMEZONE=America/Argentina/Buenos_Aires
```
