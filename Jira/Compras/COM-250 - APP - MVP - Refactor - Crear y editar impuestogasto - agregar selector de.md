---
jira_key: "COM-250"
aliases: ["COM-250"]
summary: "APP - MVP - Refactor - Crear y editar impuesto/gasto -> agregar selector de empresa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2025-11-17 11:36"
updated: "2025-12-05 05:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-250"
---

# COM-250: APP - MVP - Refactor - Crear y editar impuesto/gasto -> agregar selector de empresa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2025-11-17 11:36 |
| Actualizado | 2025-12-05 05:30 |
| Etiquetas | ninguna |
| Jira | [COM-250](https://bluinc.atlassian.net/browse/COM-250) |

## Relaciones

- **Padre:** [[COM-98]] Repositorio de impuestos por posicionar arancelaria
- **relates to:** [[COM-232]] APP - MVP - Agregar filtro de empresa a la pestaña de impuestos/gasto (tariffTax)
- **relates to:** [[COM-233]] API - MVP - Agregar filtro de empresa a la pestaña de impuestos/gasto (tariffTax)

## Descripcion

Realizaremos una refactorización en los modales "Agregar impuesto/gasto" y "Editar impuesto/gasto" para adicionar el selector de empresa. Algunas referencias mencionadas al respecto fueron:

Al crear:

- El selector debe tener preseleccionada la empresa a la que pertenece.


- Si no tiene empresa, debe mostrar el estado "Por seleccionar".


- Es un campo obligatorio.



```
POST {{API_URL}}/v1/tariffTax
```

```
PATCH {{API_URL}}/v1/tariffTax
```

[adjunto]
[adjunto]
