---
jira_key: "INV-61"
aliases: ["INV-61"]
summary: "API - Refactor - Atributos -> Eliminar atributo - Respuesta ambigua"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-04-11 15:26"
updated: "2024-04-17 19:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-61"
---

# INV-61: API - Refactor - Atributos -> Eliminar atributo - Respuesta ambigua

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-11 15:26 |
| Actualizado | 2024-04-17 19:09 |
| Etiquetas | ninguna |
| Jira | [INV-61](https://bluinc.atlassian.net/browse/INV-61) |

## Relaciones

- **Padre:** [[INV-27]] Productos
- **blocks:** [[SNB-1658]] INVENTARIO 

## Descripcion

Al intentar eliminar el atributo de un producto me aparece lo siguiente:

- Código de estado no coincidente con el estatus


- Mensaje no descriptivo del error



```
{{API_URL}}/item/attribute?attribute_id={}
```

[adjunto]
Dato extra:

Parece ser que el atributo si se elimina.
