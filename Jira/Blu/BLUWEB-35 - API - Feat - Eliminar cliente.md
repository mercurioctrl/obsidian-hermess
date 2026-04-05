---
jira_key: "BLUWEB-35"
aliases: ["BLUWEB-35"]
summary: "API - Feat - Eliminar cliente"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-19 08:27"
updated: "2025-05-19 16:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-35"
---

# BLUWEB-35: API - Feat - Eliminar cliente

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-19 08:27 |
| Actualizado | 2025-05-19 16:31 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-35](https://bluinc.atlassian.net/browse/BLUWEB-35) |

## Relaciones

- **Padre:** [[BLUWEB-11]] Sistema de clientes del BackOffice

## Descripcion

Eliminar un cliente específico por ID desde back office

```
DELETE {API_URL}/backOffice/client/3
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

## Criterios de aceptación generales para los 4 endpoints:

- **Autenticación obligatoria** para acceder a cualquiera de los endpoints y ser `admin` o `staff`


- **Validación correcta** del formato de email, campos obligatorios (`first_name`, `last_name`, `email`), y valores permitidos en `status`.


- **Errores claros y en formato JSON**, con código HTTP correspondiente (422, 404, etc.).


- **Consistencia en la estructura JSON** de las respuestas, tanto en éxito como en error.


- **Auditoría activa:** los campos `created_at` y `updated_at` deben mantenerse correctamente.
