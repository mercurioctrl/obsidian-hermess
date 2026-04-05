---
jira_key: "LIO-494"
aliases: ["LIO-494"]
summary: "API - Refactor - ajustar lectura de banners desde recurso API4"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2025-12-17 14:39"
updated: "2025-12-22 20:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-494"
---

# LIO-494: API - Refactor - ajustar lectura de banners desde recurso API4

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2025-12-17 14:39 |
| Actualizado | 2025-12-22 20:57 |
| Etiquetas | ninguna |
| Jira | [LIO-494](https://bluinc.atlassian.net/browse/LIO-494) |

## Relaciones

- **Padre:** [[LIO-485]] API - Feat - Migrar repositorio de banners desde legacy, con redis

## Descripcion

Es necesario que siempre que vengan todos los banners vengan incluso vacios es decir


```javascript
  {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    8: [],
  },
```

en lugar de: 



```
{
    "1": [
      …
    ],
    "2": [
        …
    ],
    "5": [
        {
            "orden": "1",
            "url": "",
            "checksum": "ff3649e27b42f7c7936ccdfb9bd76387.jpeg",
            "zone_id": "5"
        },
       ..
    ],
    "6": [
        {
            "orden": "1",
            "url": "",
            "checksum": "5bb093343670385a514400327e0b6fe3.jpeg",
            "zone_id": "6"
        },
       
    ]
}
```

 ya que falta el key del 3 y el 4

```javascript
 // id 1 Banner Home
  // id 2 Banner Home Mobile
  // id 3 Sub Banner
  // id 4 Sub Banner Mobile
  // id 5 Mini Banner Home
  // id 6 PR Fondo y Onomatopeya
  // id 8 Fondo sector personalizado home
```
