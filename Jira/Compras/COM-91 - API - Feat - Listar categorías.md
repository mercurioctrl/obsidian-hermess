---
jira_key: "COM-91"
aliases: ["COM-91"]
summary: "API - Feat - Listar categorías"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2024-05-14 17:11"
updated: "2024-05-15 17:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-91"
---

# COM-91: API - Feat - Listar categorías

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2024-05-14 17:11 |
| Actualizado | 2024-05-15 17:18 |
| Etiquetas | ninguna |
| Jira | [COM-91](https://bluinc.atlassian.net/browse/COM-91) |

## Relaciones

- **Padre:** [[COM-38 - Ver orden de compra|COM-38]] Ver orden de compra
- **blocks:** [[COM-75 - APP - Feact - Selector de posiciones arancelarias|COM-75]] APP - Feact - Selector de posiciones arancelarias

## Descripcion

Se necesita un recurso que liste las categorias para poder al crear un posicion arancelaria 



GET  {API_URL}/v1/categories

```
[
    {
        "id": 1,
        "name": "MEMORIAS"
    },
    {
        "id": 2,
        "name": "DISCOS HDD"
    },
    {
        "id": 3,
        "name": "PROCESADORES"
    }
    ....
]
```
