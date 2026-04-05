---
jira_key: "BLUWEB-28"
aliases: ["BLUWEB-28"]
summary: "API - Feat - Crear nuevo usuario"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-05-19 08:05"
updated: "2025-05-19 16:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-28"
---

# BLUWEB-28: API - Feat - Crear nuevo usuario

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-19 08:05 |
| Actualizado | 2025-05-19 16:10 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-28](https://bluinc.atlassian.net/browse/BLUWEB-28) |

## Relaciones

- **Padre:** [[BLUWEB-10 - Sistema de usuarios del BackOffice|BLUWEB-10]] Sistema de usuarios del BackOffice

## Descripcion

Permitir registrar un nuevo usuario desde el back office

```
POST {API_URL}/backOffice/user
```

**Carga útil**

```
{
  "first_name": "Sofía",
  "last_name": "Gómez",
  "email": "sofia@example.com",
  "password": "clave1234",
  "roleId": 1,
  "job_title": "Compras",
  "phone": "1167894321",
  "whatsapp": "1167894321",
  "cbu": "2850590940090412345678",
  "alias": "sofia.cuenta.banco",
  "status": "active"
}

```

**Respuesta esperada (201 Created):**

```
{
  "id": 3,
  "first_name": "Sofía",
  "last_name": "Gómez",
  "email": "sofia@example.com",
  "roleId": 1,
  "role": "client",
  "job_title": "Compras",
  "phone": "1167894321",
  "whatsapp": "1167894321",
  "cbu": "2850590940090412345678",
  "alias": "sofia.cuenta.banco",
  "status": "active"
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
