---
jira_key: "BLUWEB-29"
aliases: ["BLUWEB-29"]
summary: "API - Feat - Modificar usuario existente"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-05-19 08:07"
updated: "2025-05-19 16:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-29"
---

# BLUWEB-29: API - Feat - Modificar usuario existente

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-19 08:07 |
| Actualizado | 2025-05-19 16:10 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-29](https://bluinc.atlassian.net/browse/BLUWEB-29) |

## Relaciones

- **Padre:** [[BLUWEB-10 - Sistema de usuarios del BackOffice|BLUWEB-10]] Sistema de usuarios del BackOffice

## Descripcion

Permitir actualizar los datos de un usuario existente desde el back office

```
PATCH {API_URL}/backOffice/user/3
```

**Carga útil de ejemplo:**

```
{
  "job_title": "Ventas",
  "status": "inactive",
  "phone": "1198765432"
}
```

**Respuesta esperada (200 OK):**

```
{
   "success": true,
   "message": "Usuario actualizado exitosamente",
   "data": {
      "id": 3,
      "first_name": "Emanuel",
      "last_name": "Ferreyra",
      "email": "ferreyra@gmail.com",
      "roleId": 1,
      "role": "admin",
      "job_title": "Ventas",
      "phone": "1198765432",
      "whatsapp": "2235181919",
      "cbu": "2850590940090412345678",
      "alias": "emanuel.ferreyra",
      "status": "inactive"
   }
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
