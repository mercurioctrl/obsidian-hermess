---
jira_key: "INV-299"
aliases: ["INV-299"]
summary: "API - Refactor - Agregar permiso para la seccion kits y su crecion"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-23 08:40"
updated: "2025-12-29 12:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-299"
---

# INV-299: API - Refactor - Agregar permiso para la seccion kits y su crecion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-23 08:40 |
| Actualizado | 2025-12-29 12:23 |
| Etiquetas | ninguna |
| Jira | [INV-299](https://bluinc.atlassian.net/browse/INV-299) |

## Relaciones

- **Padre:** [[INV-253 - Crear y modificar Kits|INV-253]] Crear y modificar Kits

## Descripcion

Se debe agregar un nuevo permiso a nivel de agente en la tabla `NB_WEB.dbo.permisos_agente` que permita habilitar o restringir el acceso a los recursos de **itemsKits**.

Para ello, se incorporará el campo/permiso:

- `NB_WEB.dbo.permisos_agente.itemsKits`



Cuando este permiso **no esté habilitado**, el agente **no podrá utilizar** los siguientes endpoints:

- `GET {API_URL}/itemsKits`


- `POST {API_URL}/itemsKits`


- `PATCH {API_URL}/itemsKits`



**Comportamiento esperado**

- Si el agente intenta acceder a cualquiera de los endpoints sin el permiso correspondiente:

- Se debe devolver el **código HTTP adecuado** (403 Forbidden).


- La respuesta debe incluir un **mensaje claro** indicando que el agente no posee permisos para operar sobre `itemsKits`.





**Notas**

- El control debe aplicarse de forma consistente a todos los métodos listados.


- No debe ejecutarse ninguna lógica del recurso si el permiso es inválido.
