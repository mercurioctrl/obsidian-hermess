---
jira_key: "COM-16"
aliases: ["COM-16"]
summary: "API - Feat - Repositorios Paises"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-13 16:33"
updated: "2024-02-14 09:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-16"
---

# COM-16: API - Feat - Repositorios Paises

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-13 16:33 |
| Actualizado | 2024-02-14 09:46 |
| Etiquetas | ninguna |
| Jira | [COM-16](https://bluinc.atlassian.net/browse/COM-16) |

## Relaciones

- **Padre:** [[COM-14 - Repositorios|COM-14]] Repositorios
- **blocks:** [[COM-19 - API - Feat - Filtrar por pais|COM-19]] API - Feat - Filtrar por pais
- **blocks:** [[COM-20 - APP - Feat - Filtrar por pais|COM-20]] APP - Feat - Filtrar por pais

## Descripcion

```
GET {API_URL}/v1/countries?searc={description o id}
```

```
[
  {
    "id": 2,
    "prefix": "ESPA ",
    "description": "Espa±a",
    "flag": "28",
    "id": 2,
    "defaultSet": null
  },
  {
    "id": 4,
    "prefix": "EURO ",
    "description": "Resto de Europa",
    "flag": "30",
    "id": 4,
    "defaultSet": null
  },
  {
    "id": 5,
    "prefix": "USA",
    "description": "Estados Unidos De AMERICA",
    "flag": "78",
    "id": 5,
    "defaultSet": null
  },
  {
    "id": 7,
    "prefix": "ARGE ",
    "description": "Argentina ",
    "flag": "1",
    "id": 7,
    "defaultSet": 1
  },
  {
    "id": 8,
    "prefix": "MEX",
    "description": "MexicoHH",
    "flag": "52",
    "id": 8,
    "defaultSet": null
  },
  {
    "id": 9,
    "prefix": "POR",
    "description": "Porugal",
    "flag": "65",
    "id": 9,
    "defaultSet": null
  },
  {
    "id": 10,
    "prefix": "CAN",
    "description": "Canada",
    "flag": "16",
    "id": 10,
    "defaultSet": null
  },
  {
    "id": 11,
    "prefix": "BRA",
    "description": "Brasil",
    "flag": "13",
    "id": 11,
    "defaultSet": null
  }
]
```
