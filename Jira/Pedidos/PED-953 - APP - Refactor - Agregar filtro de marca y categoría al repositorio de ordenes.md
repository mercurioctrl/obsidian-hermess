---
jira_key: "PED-953"
aliases: ["PED-953"]
summary: "APP - Refactor - Agregar filtro de marca y categoría al repositorio de ordenes"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-02-21 09:38"
updated: "2025-02-21 21:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-953"
---

# PED-953: APP - Refactor - Agregar filtro de marca y categoría al repositorio de ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-21 09:38 |
| Actualizado | 2025-02-21 21:19 |
| Etiquetas | ninguna |
| Jira | [PED-953](https://bluinc.atlassian.net/browse/PED-953) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **action item from:** [[PED-952]] API - Refactor - Agregar filtro de marca y categoría al repositorio de ordenes

## Descripcion

Basándonos en el refactor [link](https://lioteam.atlassian.net/browse/PED-952) agregaremos dos filtros nuevos al área de filtros “ocultos” para poder mostrar ordenes que poseen dentro determinada marca y categoría

[adjunto]
Para esto utilizaremos los repositorios

```
GET {API_URL}/v1/brands 
```

```
GET {API_URL}/v1/categories 
```

para agaragar ambos selectores
