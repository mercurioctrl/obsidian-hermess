---
jira_key: "BLUWEB-27"
aliases: ["BLUWEB-27"]
summary: "API - Feat - Obtener listado de usuarios"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-05-19 08:04"
updated: "2025-05-19 16:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-27"
---

# BLUWEB-27: API - Feat - Obtener listado de usuarios

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-19 08:04 |
| Actualizado | 2025-05-19 16:10 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-27](https://bluinc.atlassian.net/browse/BLUWEB-27) |

## Relaciones

- **Padre:** [[BLUWEB-10]] Sistema de usuarios del BackOffice

## Descripcion

Permitir obtener el listado completo de usuarios registrados.

```
GET {API_URL}/backOffice/user
```

```
{
   "success": true,
   "message": "Listado de usuarios obtenido exitosamente",
   "data": [
      {
         "id": 1,
         "first_name": "Test",
         "last_name": "User",
         "email": "test@example.com",
         "role": "admin",
         "role_id": 1,
         "job_title": null,
         "phone": null,
         "whatsapp": null,
         "cbu": null,
         "alias": null,
         "status": "active"
      },
      {
         "id": 2,
         "first_name": "Sofía",
         "last_name": "Gómez",
         "email": "sofia@example.com",
         "role": "admin",
         "role_id": 1,
         "job_title": "Compras",
         "phone": "1167894321",
         "whatsapp": "1167894321",
         "cbu": "2850590940090412345678",
         "alias": "sofia.cuenta.banco",
         "status": "active"
      }
   ]
}

```

### Criterios de aceptación generales

- **Autenticación requerida**:
Todos los endpoints deben estar protegidos y requerir autenticación (por ejemplo, mediante token o sesión activa) y ser `admin` o `staff`


- **Validación de datos**:
Los campos deben validarse correctamente:

- `email` debe ser único y tener formato válido.


- `role` debe ser uno de: `admin`, `staff`, `client`.


- `status` debe ser `active` o `inactive`.


- Campos obligatorios como `first_name`, `last_name`, `email` y `password` (en POST) deben ser requeridos.




- **Manejo de errores consistente**:
Ante errores de validación o recursos inexistentes, debe devolverse un mensaje claro en formato JSON con código de estado HTTP apropiado (422, 404, etc.).


- **Formato de respuesta uniforme**:
Todas las respuestas deben seguir un formato JSON uniforme y estructurado, tanto en éxito como en error.


- **Auditoría (opcional si aplica)**:
Todas las acciones de alta, modificación y eliminación deben dejar trazabilidad (logs o timestamps actualizados), especialmente si el modelo ya tiene `created_at` y `updated_at`.
