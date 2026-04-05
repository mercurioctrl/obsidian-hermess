---
jira_key: "INV-308"
aliases: ["INV-308"]
summary: "APP - Refactor - Marcar articulo como kit -> Considerar companyCode al buscar en items"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2025-12-26 12:08"
updated: "2026-01-08 11:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-308"
---

# INV-308: APP - Refactor - Marcar articulo como kit -> Considerar companyCode al buscar en items

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2025-12-26 12:08 |
| Actualizado | 2026-01-08 11:30 |
| Etiquetas | ninguna |
| Jira | [INV-308](https://bluinc.atlassian.net/browse/INV-308) |

## Relaciones

- **Padre:** [[INV-253 - Crear y modificar Kits|INV-253]] Crear y modificar Kits
- **relates to:** [[INV-271 - APP - Feat - Pestaña “Kits”, listado y acción “Marcar como kit”|INV-271]] APP - Feat - Pestaña “Kits”, listado y acción “Marcar como kit”

## Descripcion

Al buscar un producto para marcarlo como kit, debe ser posible filtrarlo por compañía, permitiendo seleccionar la empresa correspondiente o, en su defecto, tomando automáticamente la empresa definida en la configuración.

```
{{API_URL}}/items
```

[adjunto]
[adjunto]
