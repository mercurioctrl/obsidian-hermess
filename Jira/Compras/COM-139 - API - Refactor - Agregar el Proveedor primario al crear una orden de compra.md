---
jira_key: "COM-139"
aliases: ["COM-139"]
summary: "API - Refactor - Agregar el Proveedor primario al crear una orden de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-09-02 08:15"
updated: "2024-09-04 03:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-139"
---

# COM-139: API - Refactor - Agregar el Proveedor primario al crear una orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-02 08:15 |
| Actualizado | 2024-09-04 03:22 |
| Etiquetas | ninguna |
| Jira | [COM-139](https://bluinc.atlassian.net/browse/COM-139) |

## Relaciones

- **Padre:** [[COM-138]] Crear orden de compra
- **blocks:** [[COM-140]] APP - Refactor - Agregar el proveedor primario al crear una orden de compra

## Descripcion

Dado que muchas veces el proveedor para nosotros es en realidad una empresa intermediaria, entonces debemos dejar cuenta de cual es el proveedor original (esto se hace con fines de tramitar garantías y demás).

Para esto, refactorizaremos el recurso 

```
POST {API_URL}/v1/providerOrder
```

```
{
"provider":13175
"primaryProvider": 3456 <<< -NUEVO PARAMETRO
}
```

el mismo se guardara en la tabla `pedprol` y `albprol` (cuando se genera el ingreso)
