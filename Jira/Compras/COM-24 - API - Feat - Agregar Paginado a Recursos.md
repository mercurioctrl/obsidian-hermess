---
jira_key: "COM-24"
aliases: ["COM-24"]
summary: "API - Feat - Agregar Paginado a Recursos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-02-15 11:39"
updated: "2024-02-15 12:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-24"
---

# COM-24: API - Feat - Agregar Paginado a Recursos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-02-15 11:39 |
| Actualizado | 2024-02-15 12:58 |
| Etiquetas | ninguna |
| Jira | [COM-24](https://bluinc.atlassian.net/browse/COM-24) |

## Relaciones

- **Padre:** [[COM-6 - Listar proveedores|COM-6]] Listar proveedores

## Descripcion

Agregar estructura de respuesta a todos los recurso que deban ser paginados.

Ej:

```
{
  "response": [
    {},
    {}
  ],
  "pagination": {
    "total": 59715,
    "limit": 15,
    "offset": 0
  }
}
```



Nota: En esta tarea se incluye el dato Total: como contador .
