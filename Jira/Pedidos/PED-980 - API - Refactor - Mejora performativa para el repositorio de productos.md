---
jira_key: "PED-980"
aliases: ["PED-980"]
summary: "API - Refactor - Mejora performativa para el repositorio de productos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-03-28 10:38"
updated: "2025-04-03 08:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-980"
---

# PED-980: API - Refactor - Mejora performativa para el repositorio de productos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-28 10:38 |
| Actualizado | 2025-04-03 08:38 |
| Etiquetas | ninguna |
| Jira | [PED-980](https://bluinc.atlassian.net/browse/PED-980) |

## Relaciones

- **Padre:** [[PED-65 - Listado de productos|PED-65]] Listado de productos

## Descripcion

Despues de hacer algunas pruebas se nota que el repositorio comenzo a ponerse mas lentos, menos performativo.

```
GET {API_URL}/v1/items?search={terminos de busqueda}&between={fecha}&stock={stock}
```

Se deben buscar estrategias y métodos para agilizar lo mas posible el recurso ya que es uno de los mas utilizados en la aplicacion.
