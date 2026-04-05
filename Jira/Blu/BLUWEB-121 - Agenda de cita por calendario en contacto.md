---
jira_key: "BLUWEB-121"
aliases: ["BLUWEB-121"]
summary: "Agenda de cita por calendario en contacto"
status: "LISTO"
type: "Historia"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2025-08-11 13:18"
updated: "2025-09-25 14:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-121"
---

# BLUWEB-121: Agenda de cita por calendario en contacto

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-11 13:18 |
| Actualizado | 2025-09-25 14:15 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-121](https://bluinc.atlassian.net/browse/BLUWEB-121) |

## Relaciones

- **Subtarea:** [[BLUWEB-122 - API - Feat - Ver disponibilidad (Time Slots) y Calendario|BLUWEB-122]] API - Feat - Ver disponibilidad (Time Slots) y Calendario
- **Subtarea:** [[BLUWEB-123 - API - Feta - Agendar cita (Time Slots)|BLUWEB-123]] API - Feta - Agendar cita (Time Slots)

## Descripcion

### **Objetivo general**

El sistema funcionará únicamente con **dos recursos principales** en la API REST:

- **GET **`/calendar/timeslots`
Devuelve un calendario mensual completo, indicando para cada día si hay disponibilidad o si ya se ha reservado la reunión del día.

- La configuración de **días hábiles** (lunes a viernes) y **hora fija de la reunión** se define en variables de entorno (`.env`).


- Si el día no es hábil o ya hay una reunión agendada, no se ofrece disponibilidad.


- El calendario se muestra siempre en formato de semanas (lunes a domingo), incluyendo días adyacentes fuera del mes para completar la grilla.




- **POST **`/calendar/meetings`
Permite a un visitante agendar una reunión seleccionando un día disponible.

- Solo se puede agendar **una reunión activa por día**.


- Al crear la reunión, se bloquea automáticamente la fecha para nuevas reservas.


- Se envía un correo de confirmación al visitante y al administrador, con:

- Detalles de la reunión.


- Archivo `.ics` adjunto compatible con Google Calendar, Outlook y Apple Calendar.


- Enlaces directos para añadir al calendario.


- Enlace único para cancelar la cita.







---

### **Lógica y reglas de negocio**

- **Una reunión por día**: al reservar, se valida que no exista otra reunión activa en esa fecha.


- **Días hábiles configurables**: por defecto lunes a viernes, definidos en `.env` como lista (`AVAILABLE_DAYS=mon,tue,wed,thu,fri`).


- **Hora fija de reunión**: definida en `.env` (`MEETING_START_TIME=09:00`, `MEETING_DURATION_MINUTES=30`).


- **Zona horaria**: definida en `.env` (`TIMEZONE=America/Argentina/Buenos_Aires`) y aplicada en toda la API.


- **Cancelación**: posible mediante enlace único enviado en el email de confirmación.


- **Visualización en calendario**: el GET retorna siempre el mes completo con semanas completas, aunque un día no esté disponible.



ABIERTO A SUGERENCIAS O REUTILIZAR LIBRERÍAS EXISTENTES QUE FUNCIONEN DIFERENTE PERO CUMPLAN EL MISMO FIN

[adjunto]
[adjunto]
