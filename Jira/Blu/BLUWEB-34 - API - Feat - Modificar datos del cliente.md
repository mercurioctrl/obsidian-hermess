---
jira_key: "BLUWEB-34"
aliases: ["BLUWEB-34"]
summary: "API - Feat - Modificar datos del cliente"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-19 08:25"
updated: "2025-05-19 16:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-34"
---

# BLUWEB-34: API - Feat - Modificar datos del cliente

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-19 08:25 |
| Actualizado | 2025-05-19 16:31 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-34](https://bluinc.atlassian.net/browse/BLUWEB-34) |

## Relaciones

- **Padre:** [[BLUWEB-11 - Sistema de clientes del BackOffice|BLUWEB-11]] Sistema de clientes del BackOffice

## Descripcion

Actualizar información parcial de un cliente existente.

```
PATCH {API_URL}/backOffice/client/3
```

**Carga útil de ejemplo (puedo alterar todos los campos menos id)**

```
{
  "status": "inactive",
  "phone": "1155667788"
}
```

Respuesta esperada de ejemplo

```
{
  "id": 3,
  "first_name": "Laura",
  "last_name": "Domínguez",
  "email": "laura@example.com",
  "phone": "1155667788",
  "whatsapp": "1144556677",
  "cbu": "2850590940090412345999",
  "alias": "laura.dominguez.banco",
  "status": "inactive"
}

```

## Criterios de aceptación generales para los 4 endpoints:

- **Autenticación obligatoria** para acceder a cualquiera de los endpoints y ser `admin` o `staff`


- **Validación correcta** del formato de email, campos obligatorios (`first_name`, `last_name`, `email`), y valores permitidos en `status`.


- **Errores claros y en formato JSON**, con código HTTP correspondiente (422, 404, etc.).


- **Consistencia en la estructura JSON** de las respuestas, tanto en éxito como en error.


- **Auditoría activa:** los campos `created_at` y `updated_at` deben mantenerse correctamente.
