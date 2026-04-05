---
jira_key: "BLUWEB-122"
aliases: ["BLUWEB-122"]
summary: "API - Feat - Ver disponibilidad (Time Slots) y Calendario"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-11 13:20"
updated: "2025-08-29 09:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-122"
---

# BLUWEB-122: API - Feat - Ver disponibilidad (Time Slots) y Calendario

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-11 13:20 |
| Actualizado | 2025-08-29 09:58 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-122](https://bluinc.atlassian.net/browse/BLUWEB-122) |

## Relaciones

- **Padre:** [[BLUWEB-121 - Agenda de cita por calendario en contacto|BLUWEB-121]] Agenda de cita por calendario en contacto

## Descripcion

Este endpoint permite obtener la **disponibilidad de horarios organizada en formato calendario mensual**. Está diseñado para que el frontend pueda renderizar un calendario interactivo con todas las semanas del mes, mostrando tanto los días con disponibilidad como los días sin turnos asignados.

El objetivo es entregar un formato que incluya:

- **Grilla semanal completa** (de lunes a domingo) que cubra el mes consultado, extendida para incluir los días adyacentes que completan las semanas.


- Información por día sobre si pertenece o no al mes, si es el día actual, su número de día de la semana y los turnos disponibles o reservados.


- **Filtrado opcional** para mostrar únicamente los horarios con disponibilidad (`onlyAvailable=true`) o todos los slots creados (`onlyAvailable=false`).



Este recurso es la base para construir la vista de calendario en el sitio público y también puede ser reutilizado en el panel de administración para visualizar la agenda.

```
GET /calendar/timeslots?month=YYYY-MM&onlyAvailable=true|false
```

**Query params:**

- `month` *(YYYY-MM)* → mes que se quiere consultar.


- `onlyAvailable` *(true|false)* → si `true` devuelve solo los slots con disponibilidad; si `false` devuelve todos.



---

## **Respuesta esperada**

- **month** → mes solicitado.


- **timezone** → zona horaria en que se generan los slots.


- **weeks** → array de semanas, cada semana es un array de 7 días (lunes a domingo).


- Cada día tiene:

- `date` → fecha en formato YYYY-MM-DD


- `inMonth` → si pertenece o no al mes consultado


- `isToday` → si es el día actual


- `weekday` → 1 a 7 (lunes a domingo)





```
{
  "month": "2025-09",
  "timezone": "America/Argentina/Buenos_Aires",
  "weeks": [
    [
      {
        "date": "2025-09-01",
        "inMonth": true,
        "isToday": false,
        "weekday": 1,
        "timeSlots": [
          {"id": 101, "start": "09:00", "end": "09:30", "available": true} <-- Solo devuelvo un slot, porque solo se puede agandar una por dia
        ]
      },
      {
        "date": "2025-09-02",
        "inMonth": true,
        "isToday": false,
        "weekday": 2,
        "timeSlots": [
              {"id": 102, "start": "09:30", "end": "10:00", "available": false} <-- Solo devuelvo un slot, porque solo se puede agandar una por dia
        ]
      },
      { "date": "2025-09-03", "inMonth": true, "isToday": false, "weekday": 3, "timeSlots": [] },
      { "date": "2025-09-04", "inMonth": true, "isToday": false, "weekday": 4, "timeSlots": [] },
      { "date": "2025-09-05", "inMonth": true, "isToday": false, "weekday": 5, "timeSlots": [] },
      { "date": "2025-09-06", "inMonth": true, "isToday": false, "weekday": 6, "timeSlots": [] },
      { "date": "2025-09-07", "inMonth": true, "isToday": false, "weekday": 7, "timeSlots": [] }
    ],
    [
      { "date": "2025-09-08", "inMonth": true, "isToday": false, "weekday": 1, "timeSlots": [] },
      { "date": "2025-09-09", "inMonth": true, "isToday": false, "weekday": 2, "timeSlots": [] },
      { "date": "2025-09-10", "inMonth": true, "isToday": false, "weekday": 3, "timeSlots": [] },
      { "date": "2025-09-11", "inMonth": true, "isToday": false, "weekday": 4, "timeSlots": [] },
      { "date": "2025-09-12", "inMonth": true, "isToday": false, "weekday": 5, "timeSlots": [] },
      { "date": "2025-09-13", "inMonth": true, "isToday": false, "weekday": 6, "timeSlots": [] },
      { "date": "2025-09-14", "inMonth": true, "isToday": false, "weekday": 7, "timeSlots": [] }
    ]
    // ...resto de semanas hasta completar el mes
  ]
}
```

## **SQL base para este endpoint**

Asumiendo tabla `timeslots`:

```
CREATE TABLE timeslots (
  id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  is_available BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NULL,
  updated_at TIMESTAMP NULL,
  UNIQUE KEY uq_date_start (date, start_time),
  KEY idx_date (date),
  KEY idx_available_date (is_available, date)
);
```

Nota: 

```
use Carbon\Carbon;
use Carbon\CarbonPeriod;
```

### **Variables de entorno clave (**`.env`**)**

```
AVAILABLE_DAYS=mon,tue,wed,thu,fri
MEETING_START_TIME=09:00
MEETING_DURATION_MINUTES=30
TIMEZONE=America/Argentina/Buenos_Aires
```
