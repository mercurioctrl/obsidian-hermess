---
jira_key: "COM-277"
aliases: ["COM-277"]
summary: "APP - Refactor - Alta/Edición de Proveedores -> Añadir selector de empresa"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2026-01-29 09:53"
updated: "2026-02-04 10:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-277"
---

# COM-277: APP - Refactor - Alta/Edición de Proveedores -> Añadir selector de empresa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-29 09:53 |
| Actualizado | 2026-02-04 10:35 |
| Etiquetas | ninguna |
| Jira | [COM-277](https://bluinc.atlassian.net/browse/COM-277) |

## Relaciones

- **Padre:** [[COM-5 - Proveedores|COM-5]] Proveedores
- **clones:** [[COM-246 - APP - MVP - Mandar companyCode al crear un proveedor|COM-246]] APP - MVP - Mandar companyCode al crear un proveedor
- **relates to:** [[COM-44 - APP - Feat - Alta de proveedores|COM-44]] APP - Feat - Alta de proveedores
- **relates to:** [[COM-45 - API - Feat - Modificar un provedor|COM-45]] API - Feat - Modificar un provedor

## Descripcion

Realizaremos un refactor para agregar en el modal “Agregar proveedor” Y “Editar proveedor“ un selector de Empresa que permita al usuario elegir la empresa asociada al proveedor.

El valor seleccionado debe enviarse como `companyCode` tanto en la creación como en la edición del proveedor.

```
POST/PATCH /v1/providers
```

[adjunto]
