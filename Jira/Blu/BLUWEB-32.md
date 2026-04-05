---
jira_key: "BLUWEB-32"
summary: "API - Feat- Obtener listado de clientes"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-19 08:21"
updated: "2025-05-19 17:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-32"
---

# BLUWEB-32: API - Feat- Obtener listado de clientes

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-19 08:21 |
| Actualizado | 2025-05-19 17:10 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-32](https://bluinc.atlassian.net/browse/BLUWEB-32) |

## Descripción

```
GET {API_URL}/backOffice/client
```

```
[
  {
    "id": 1,
    "first_name": "Ana",
    "last_name": "Martínez",
    "companyName": "Cafe Martinez"
    "email": "ana@example.com",
    "phone": "1133445566",
    "whatsapp": "1133445566",
    "cbu": "2850590940090412345000",
    "alias": "ana.banco.cuenta",
    "status": "active"
  },
  {
    "id": 2,
    "first_name": "Carlos",
    "last_name": "Rey",
    "companyName": "Cafe Rey"
    "email": "carlos@example.com",
    "phone": "",
    "whatsapp": "",
    "cbu": "",
    "alias": "rey.cuenta.banco",
    "status": "inactive"
  }
]

```

## Criterios de aceptación generales para los 4 endpoints:

- **Autenticación obligatoria** para acceder a cualquiera de los endpoints y ser `admin` o `staff`


- **Validación correcta** del formato de email, campos obligatorios (`first_name`, `last_name`, `email`), y valores permitidos en `status`.


- **Errores claros y en formato JSON**, con código HTTP correspondiente (422, 404, etc.).


- **Consistencia en la estructura JSON** de las respuestas, tanto en éxito como en error.


- **Auditoría activa:** los campos `created_at` y `updated_at` deben mantenerse correctamente.
