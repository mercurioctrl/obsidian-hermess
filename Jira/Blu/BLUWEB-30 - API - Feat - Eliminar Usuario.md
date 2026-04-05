---
jira_key: "BLUWEB-30"
aliases: ["BLUWEB-30"]
summary: "API - Feat - Eliminar Usuario"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-05-19 08:13"
updated: "2025-05-19 17:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-30"
---

# BLUWEB-30: API - Feat - Eliminar Usuario

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-19 08:13 |
| Actualizado | 2025-05-19 17:30 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-30](https://bluinc.atlassian.net/browse/BLUWEB-30) |

## Relaciones

- **Padre:** [[BLUWEB-10 - Sistema de usuarios del BackOffice|BLUWEB-10]] Sistema de usuarios del BackOffice

## Descripcion

Permitir eliminar un usuario por ID desde el back office

```
DELETE {API_URL}/backOffice/user/3
```

### **Respuestas esperadas (correctas):**

| Código | Significado | Descripción |
| --- | --- | --- |
| **200 OK** | ✅ Eliminación exitosa, con contenido | El usuario fue eliminado y se devuelve un mensaje o el objeto eliminado en el cuerpo. |

---

### ❌ **Respuestas de error:**

| Código | Significado | Descripción |
| --- | --- | --- |
| **400 Bad Request** | ❌ Solicitud mal formada | Por ejemplo, si el ID no es válido (ej. una cadena en lugar de número). |
| **401 Unauthorized** | ❌ No autenticado | No se envió token de autenticación o es inválido. |
| **403 Forbidden** | ❌ No autorizado | El usuario no tiene permisos para eliminar. |
| **404 Not Found** | ❌ No encontrado | No existe un usuario con ID = 3. |
| **500 Internal Server Error** | ❌ Error interno | Fallo inesperado del servidor al procesar la eliminación. |

Es un soft Delete, osea que se marca como eliminado pero no se elimina el registro



Criterios de aceptación generales

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
