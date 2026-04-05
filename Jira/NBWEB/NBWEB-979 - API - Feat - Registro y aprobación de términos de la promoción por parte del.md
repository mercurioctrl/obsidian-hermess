---
jira_key: "NBWEB-979"
aliases: ["NBWEB-979"]
summary: "API - Feat - Registro y aprobación de términos de la promoción por parte del cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-25 11:42"
updated: "2025-07-02 11:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-979"
---

# NBWEB-979: API - Feat - Registro y aprobación de términos de la promoción por parte del cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-25 11:42 |
| Actualizado | 2025-07-02 11:24 |
| Etiquetas | ninguna |
| Jira | [NBWEB-979](https://bluinc.atlassian.net/browse/NBWEB-979) |

## Relaciones

- **Padre:** [[NBWEB-978 - NB TRAVEL|NBWEB-978]] NB TRAVEL
- **has action item:** [[NBWEB-980 - APP - Feat - Registro y aprobación de términos de la promoción por parte del|NBWEB-980]] APP - Feat - Registro y aprobación de términos de la promoción por parte del cliente

## Descripcion

Crearemos un pequeño formulario para las promociones de viaje que nos permitirá saber quienes se inscribieron para participar aceptando los términos y con que cuits se inscribieron, ademas de datos de contacto de la persona vinculada a la promoción. 

```
POST /v1/travel/registrations
```

```
{
  "mail": "user@ejemplo.com",
  "phone": "+541112345678",
  "documents": "30-70924663-8",
  "accept_terms": true
}
```

- Todos los campos son obligatorios


- Se deberá controlar que al menos tenga un cuit ingresado



Crearemos una tabla `[NB_WEB].[dbo].travel`

- id (auto)


- userId (esta en los claims)


- phone


- documents (varchar255)


- registrationDate (datetime)



Dado que se requiere el userId el formulario solo puede ser procesado cuando esta logueado

**Devuelve:**

```
{
succes:true,
commnet: "Registro exitoso"
payload: [
    {
      "id": 123,
      "userId": 456,
      "mail": "user@ejemplo.com",
      "phone": "+541112345678",
      "documents": "30-70924663-8",
      "accept_terms": true,
      "registration_date": "2025-06-26T10:45:00-03:00"
    }
  ]
}
```
