---
jira_key: "COM-66"
aliases: ["COM-66"]
summary: "API - Refactor - Extracción de datos - posición arancelaria e impuestos "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-03-06 10:21"
updated: "2024-04-21 18:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-66"
---

# COM-66: API - Refactor - Extracción de datos - posición arancelaria e impuestos 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-03-06 10:21 |
| Actualizado | 2024-04-21 18:52 |
| Etiquetas | ninguna |
| Jira | [COM-66](https://bluinc.atlassian.net/browse/COM-66) |

## Relaciones

- **Padre:** [[COM-1 - Bases y repositorios|COM-1]] Bases y repositorios
- **is blocked by:** [[COM-72 - API - Posición arancelaria e impuestos - Posiciones no encontradas|COM-72]] API - Posición arancelaria e impuestos - Posiciones no encontradas
- **is blocked by:** [[COM-73 - API - Posición arancelaria e impuestos - Resultados de búsqueda no coincidentes|COM-73]] API - Posición arancelaria e impuestos - Resultados de búsqueda no coincidentes

## Descripcion

Según lo comentado en la daily, se debe buscar el mejor camino para obtener los datos externos, sin afectar posteriormente el desempeño de las consultas.

- Se debe buscar por familia todas las posiciones.


- Se deben obtener todos los impuestos arancelarios por posición arancelaria. (considerando que se pueden quitar como agregar nuevos impuestos)





```
NEW_BYTES.dbo.ProductPosition
```

```
 NEW_BYTES.dbo.TaxPosition
```
