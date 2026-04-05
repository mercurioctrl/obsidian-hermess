---
jira_key: "PED-146"
aliases: ["PED-146"]
summary: "API - Feat - Agregar / Editar usuario "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-10-18 09:06"
updated: "2023-10-19 10:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-146"
---

# PED-146: API - Feat - Agregar / Editar usuario 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-18 09:06 |
| Actualizado | 2023-10-19 10:09 |
| Etiquetas | ninguna |
| Jira | [PED-146](https://bluinc.atlassian.net/browse/PED-146) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes
- **blocks:** [[PED-147 - APP - Feat - Agregar Editar usuario|PED-147]] APP - Feat - Agregar / Editar usuario

## Descripcion

**Creación y edición de un usuario**

Objetivo: Desarrollar un recurso API que permita crear un nuevo usuario si el cliente no tiene uno o editar la información de un usuario existente.

**Especificación del recurso:**

```
PATCH {API_URL}/v1/user/{id cliente}
```

**Body de la petición:**

```
{
  "username": "Indica el nombre de usuario",
  "password": "Indica la contraseña (si se envía vacío, no se modifica)",
  "showName": "Nombre a mostrar del usuario",
  "disabled": "Indica si el usuario está activado (true/false)",
  "mail": "Correo electrónico del usuario"
}

```

**Notas:**

- Esta implementación se basa en la tabla de usuarios y sólo muestra la cuenta principal, es decir, aquellas donde `roleId = 1` y `subcuenta` es nula.


- Ademas el recurso debe ser lo suficientemente inteligente para que en el caso de que el cliente no posea un usuario, crearlo y en el caso de que si lo tenga, editarlo.



**Consulta SQL de referencia:**

```
ELECT *
FROM [NB_WEB].[dbo].[usuarios_nb]
WHERE roleId = 1 AND subcuenta IS NULL;
```
