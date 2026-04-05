---
jira_key: "NBWEB-37"
aliases: ["NBWEB-37"]
summary: "Listar Categorias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-16 11:12"
updated: "2022-04-04 06:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-37"
---

# NBWEB-37: Listar Categorias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-16 11:12 |
| Actualizado | 2022-04-04 06:36 |
| Etiquetas | ninguna |
| Jira | [NBWEB-37](https://bluinc.atlassian.net/browse/NBWEB-37) |

## Relaciones

- **Padre:** [[NBWEB-3 - Recursos de lista|NBWEB-3]] Recursos de lista
- **relates to:** [[NBWEB-55 - Categorías Marcas - Barra Lateral|NBWEB-55]] Categorías / Marcas -  Barra Lateral

## Descripcion

Se debe obtener el listado de categorias de `[NewBytes_DBF].[dbo].[familias]` y devolver un Array de objetos con la siguiente topologia.



```json
[
  {
  "description":"Nombre de la primer categorias",
  "id": 1,
  "initialB":4,
  "initialC":5
  },
  {
  "description":"Nombre de la segunda categorias",
  "id": 2,
  "initialB":5,
  "initialC":3,
  }
]
```
