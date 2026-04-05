---
jira_key: "COM-279"
aliases: ["COM-279"]
summary: "APP - Refactor - Mandar filtro de companyCode en el recurso de proveedores dentro de \"Crear orden\" -> Añadir selector de empresa"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2026-01-29 10:12"
updated: "2026-02-11 13:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-279"
---

# COM-279: APP - Refactor - Mandar filtro de companyCode en el recurso de proveedores dentro de "Crear orden" -> Añadir selector de empresa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-29 10:12 |
| Actualizado | 2026-02-11 13:39 |
| Etiquetas | ninguna |
| Jira | [COM-279](https://bluinc.atlassian.net/browse/COM-279) |

## Relaciones

- **Padre:** [[COM-5 - Proveedores|COM-5]] Proveedores
- **clones:** [[COM-228 - APP -MVP - Mandar filtro de companyCode en el recurso de proveedores dentro de|COM-228]] APP -MVP - Mandar filtro de companyCode en el recurso de proveedores dentro de "Crear orden"

## Descripcion

Se realizará un refactor en el modal “Nueva orden de compra” para agregar un selector de Empresa, permitiendo al usuario filtrar los proveedores según la empresa asociada.

Obedeceremos también al parámetro `unlockedCompanyFilter` para determinar si es posible cambiar la selección.

```
{{API_URL}}/v1/providers
```

[adjunto]
