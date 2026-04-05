---
jira_key: "NBWEB-38"
aliases: ["NBWEB-38"]
summary: "Listar Marcas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-16 11:12"
updated: "2022-03-29 08:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-38"
---

# NBWEB-38: Listar Marcas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-16 11:12 |
| Actualizado | 2022-03-29 08:10 |
| Etiquetas | ninguna |
| Jira | [NBWEB-38](https://bluinc.atlassian.net/browse/NBWEB-38) |

## Relaciones

- **Padre:** [[NBWEB-3]] Recursos de lista
- **relates to:** [[NBWEB-55]] Categorías / Marcas -  Barra Lateral

## Descripcion

```
GET {{API_URL}}/v1/brands
```

Se debe obtener el listado de marcas de `[NB_WEB].[dbo].[marcas]` y devolver un Array de objetos con la siguiente topologia.



```json
[
  {
  "description":"Nombre de la primer marca",
  "id": 1,
  "image":"url de la imagen",
  "initialC":5
  },
  {
  "description":"Nombre de la segunda marca",
  "id": 2,
  "image":"url de la imagen",
  }
]
```



Se deben excluir aquellas que estan marcadas como “ocultas”
