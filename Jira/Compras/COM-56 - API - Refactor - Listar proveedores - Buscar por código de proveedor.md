---
jira_key: "COM-56"
aliases: ["COM-56"]
summary: "API - Refactor - Listar proveedores -> Buscar por código de proveedor "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-02-20 11:22"
updated: "2024-02-21 16:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-56"
---

# COM-56: API - Refactor - Listar proveedores -> Buscar por código de proveedor 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-20 11:22 |
| Actualizado | 2024-02-21 16:36 |
| Etiquetas | ninguna |
| Jira | [COM-56](https://bluinc.atlassian.net/browse/COM-56) |

## Relaciones

- **Padre:** [[COM-6]] Listar proveedores
- **relates to:** [[COM-7]] API - Feat - Listar proveedores

## Descripcion

Basándonos en el recurso 

```
GET {{API_URL}}/v1/providers?search={name, id o businessName}
```

Ampliaremos la búsqueda general para incluir la opción de buscar por `providerCode`.

[adjunto]
