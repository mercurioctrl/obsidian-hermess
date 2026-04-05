---
jira_key: "BLUWEB-33"
aliases: ["BLUWEB-33"]
summary: "API - Feat - Alta de nuevo cliente"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-19 08:23"
updated: "2025-05-19 16:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-33"
---

# BLUWEB-33: API - Feat - Alta de nuevo cliente

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-19 08:23 |
| Actualizado | 2025-05-19 16:36 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-33](https://bluinc.atlassian.net/browse/BLUWEB-33) |

## Relaciones

- **Padre:** [[BLUWEB-11]] Sistema de clientes del BackOffice

## Descripcion

Registrar un nuevo cliente desde el back office

```
POST {API_URL}/backOffice/client
```

**Carga útil**

```
{
  "first_name": "Laura",
  "last_name": "Domínguez",
  "companyName": "Cafe Domínguez"
  "email": "laura@example.com",
  "phone": "1144556677",
  "whatsapp": "1144556677",
  "cbu": "2850590940090412345999",
  "alias": "laura.dominguez.banco",
  "status": "active"
}

```

Respuesta esperda

```
{
  "id": 3,
  "first_name": "Laura",
  "last_name": "Domínguez",
  "companyName": "Cafe Domínguez"
  "email": "laura@example.com",
  "phone": "1144556677",
  "whatsapp": "1144556677",
  "cbu": "2850590940090412345999",
  "alias": "laura.dominguez.banco",
  "status": "active"
}

```

## Criterios de aceptación generales para los 4 endpoints:

- **Autenticación obligatoria** para acceder a cualquiera de los endpoints y ser `admin` o `staff`


- **Validación correcta** del formato de email, campos obligatorios (`first_name`, `last_name`, `email`), y valores permitidos en `status`.


- **Errores claros y en formato JSON**, con código HTTP correspondiente (422, 404, etc.).


- **Consistencia en la estructura JSON** de las respuestas, tanto en éxito como en error.


- **Auditoría activa:** los campos `created_at` y `updated_at` deben mantenerse correctamente.
