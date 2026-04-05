---
jira_key: "COM-59"
aliases: ["COM-59"]
summary: "API - Alta de proveedores - Datos no obligatorios"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-02-20 18:29"
updated: "2024-02-21 15:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-59"
---

# COM-59: API - Alta de proveedores - Datos no obligatorios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-20 18:29 |
| Actualizado | 2024-02-21 15:39 |
| Etiquetas | ninguna |
| Jira | [COM-59](https://bluinc.atlassian.net/browse/COM-59) |

## Relaciones

- **Padre:** [[COM-5]] Proveedores
- **blocks:** [[COM-43]] API - Feat - Alta de proveedores

## Descripcion

Considerando la tarea [link](https://lioteam.atlassian.net/browse/COM-44), la cual señala que al dar de alta un proveedor no es necesario incluir la provincia (`provinceId`) y la localidad (`locateId`), sino solamente el país, procederemos a eliminar la obligatoriedad de estos parámetros en el recurso.

```
POST {{API_URL}}/v1/providers
```
