---
jira_key: "INV-66"
aliases: ["INV-66"]
summary: "API - Feat - Repositorio de marcas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-05 14:41"
updated: "2024-06-07 20:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-66"
---

# INV-66: API - Feat - Repositorio de marcas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-05 14:41 |
| Actualizado | 2024-06-07 20:53 |
| Etiquetas | ninguna |
| Jira | [INV-66](https://bluinc.atlassian.net/browse/INV-66) |

## Relaciones

- **Padre:** [[INV-65]] Marcas
- **blocks:** [[INV-67]] APP - Feat - Pestaña de marcas

## Descripcion

```
GET {{API_URL}}/v1/brands
```

```
[
  {
    "id": 1,
    "description": "PIONNER",
    "image": "https://static.nb.com.ar/img/5c1b4a2680cf7173307bebf745d227cf.jpeg",
    "hide": 0,
    "webSiteShow": "0"
  },
  {
    "id": 2,
    "description": "THERMALTAKE",
    "image": "https://static.nb.com.ar/img/cac8aeeceb0e35c116a9d045308fe9f1.png",
    "hide": 1,
    "webSiteShow": "1"
  },
  {
    "id": 3,
    "description": "SAMSUNG",
    "image": "https://static.nb.com.ar/img/a092ae5731dc904e0b8c1328992e0a9c.jpg",
    "hide": 1,
    "webSiteShow": "1"
  }
  
  ...
```

```
SELECT TOP (1000) [id]
      ,[referencia]
      ,[imagen]
      ,[oculto]
      ,[siteShow]
  FROM [NB_WEB].[dbo].[marcas]
 
```
