---
jira_key: "INV-68"
aliases: ["INV-68"]
summary: "API - Feat - Editar / Crear marcas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-05 14:45"
updated: "2024-08-27 03:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-68"
---

# INV-68: API - Feat - Editar / Crear marcas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-05 14:45 |
| Actualizado | 2024-08-27 03:24 |
| Etiquetas | ninguna |
| Jira | [INV-68](https://bluinc.atlassian.net/browse/INV-68) |

## Relaciones

- **Padre:** [[INV-65]] Marcas
- **blocks:** [[INV-67]] APP - Feat - Pestaña de marcas
- **is blocked by:** [[INV-74]] API - Refactor - Editar / Crear marcas - Guardar datos adicionales
- **relates to:** [[INV-103]] API - Editar / Crear marcas - Error al subir imagen 

## Descripcion

```
POST {{API_URL}}/v1/brands
```

```
[
  {
    "description": "PIONNER",
  }
 ] 
```

```
PATCH {{API_URL}}/v1/brands
```

```
[
  {
    "id": 1,
    "description": "PIONNER",
    "image": "https://static.nb.com.ar/img/5c1b4a2680cf7173307bebf745d227cf.jpeg",
    "hide": 0,
    "webSiteShow": "0"
  }
]
```

```
SELECT TOP (1000) [id]
      ,[referencia]
      ,[imagen]
      ,[oculto]
      ,[siteShow]
  FROM [NB_WEB].[dbo].[marcas]
 
```
