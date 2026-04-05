---
jira_key: "BLUWEB-10"
summary: "Sistema de usuarios del BackOffice"
status: "LISTO"
type: "Historia"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2025-05-06 14:51"
updated: "2025-08-25 09:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-10"
---

# BLUWEB-10: Sistema de usuarios del BackOffice

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-06 14:51 |
| Actualizado | 2025-08-25 09:44 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-10](https://bluinc.atlassian.net/browse/BLUWEB-10) |

## Descripción

### Criterios de aceptación generales

- **Autenticación requerida**:
Todos los endpoints deben estar protegidos y requerir autenticación (por ejemplo, mediante token o sesión activa).


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
