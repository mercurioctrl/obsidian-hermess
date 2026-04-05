---
jira_key: "LIO-176"
aliases: ["LIO-176"]
summary: "API - CMS - Feat - Repositorio de Lectura / Escritura para categorias en el CMS"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-01-19 19:48"
updated: "2025-01-27 17:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-176"
---

# LIO-176: API - CMS - Feat - Repositorio de Lectura / Escritura para categorias en el CMS

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-19 19:48 |
| Actualizado | 2025-01-27 17:03 |
| Etiquetas | ninguna |
| Jira | [LIO-176](https://bluinc.atlassian.net/browse/LIO-176) |

## Relaciones

- **Padre:** [[LIO-173 - Categorias|LIO-173]] Categorias
- **has action item:** [[LIO-177 - APP - CMS - Feat - Sección categorías en el CMS|LIO-177]] APP - CMS - Feat - Sección categorías en el CMS
- **has action item:** [[LIO-184 - API - CMS - Refactor - Sección categorías en el CMS - Adición de categoría hija|LIO-184]] API - CMS - Refactor - Sección categorías en el CMS -> Adición de categoría hija

## Descripcion

Agregaremos los recursos necesario para trabajar con el repositorio de categorías

```
GET {API_URL}/v1/categories?active={1|0|null}&parent={1|0}
```

```
[
...
  {
    "id": 1,
    "active": 1,
    "name": "Mouse",
    "icon": "mouse",
    "keywords": "mouses",
    "id_nb": 25,
    "profit": null,
    "deleted": 0,
    "parentCategory": 0,
    "searchName": "mouse",
    "countItems": 590,
    "homeShow": 1, <-- NUEVO
    "directUrl": "https://libreopcion.com.ar/mouse" <-- NUEVO
  },
  {
    "id": 2,
    "active": 1,
    "name": "Webcams",
    "icon": "webcam",
    "keywords": "webcam",
    "id_nb": 24,
    "profit": null,
    "deleted": 0,
    "parentCategory": 0,
    "searchName": "webcams webcam",
    "countItems": 30,
    "homeShow": 1, <-- NUEVO
    "directUrl": "https://libreopcion.com.ar/mouse" <-- NUEVO
  },
...
]
```

```
PATCH {API_URL}/v1/categories
```

```
[
  {
    "id": 1,
    "active": 1,
    "name": "Mouse",
    "icon": "mouse",
    "keywords": "mouses",
    "id_nb": 25,
    "profit": null,
    "deleted": 0,
    "parentCategory": 0 || {id_categoria},
    "searchName": "mouse",
    "countItems": 590,
    "homeShow": 1, <-- NUEVO
    "directUrl": "https://libreopcion.com.ar/mouse" <-- NUEVO,
  }
]
```

```
DELETE {API_URL}/v1/categories/{id}
```

```
POST {API_URL}/v1/categories
```

```
[
  {
    "active": 1,
    "name": "Mouse",
    "keywords": "mouses",
    "parentCategory": 0 || {id_categoria},
    "homeShow": 1, <-- NUEVO
    "directUrl": "https://libreopcion.com.ar/mouse" <-- NUEVO
  }
]
```
