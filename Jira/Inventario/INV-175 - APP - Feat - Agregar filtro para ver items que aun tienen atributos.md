---
jira_key: "INV-175"
aliases: ["INV-175"]
summary: "APP - Feat - Agregar filtro para ver items que aun tienen atributos obligatorios sin satisfacer "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-01-20 12:57"
updated: "2025-01-23 02:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-175"
---

# INV-175: APP - Feat - Agregar filtro para ver items que aun tienen atributos obligatorios sin satisfacer 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-20 12:57 |
| Actualizado | 2025-01-23 02:13 |
| Etiquetas | ninguna |
| Jira | [INV-175](https://bluinc.atlassian.net/browse/INV-175) |

## Relaciones

- **Padre:** [[INV-27]] Productos
- **action item from:** [[INV-147]] API - Refactor - Filtrar productos que no cuentan con todos sus atributos obligatorios

## Descripcion

Basándonos en [link](https://lioteam.atlassian.net/browse/INV-147)  agregaremos un nuevo filtro para mostrar aquellos productos que aun tienen atributos obligatorios insatisfechos

```
GET {API_URL}/items?currentPage=1&itemsPerPage=300&hasAttributes=1
```

[adjunto]
