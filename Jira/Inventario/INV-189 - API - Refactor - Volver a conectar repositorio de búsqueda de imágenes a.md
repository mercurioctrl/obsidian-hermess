---
jira_key: "INV-189"
aliases: ["INV-189"]
summary: "API - Refactor - Volver a conectar repositorio de búsqueda de imágenes a mercadolibre según research"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-13 08:21"
updated: "2025-06-30 10:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-189"
---

# INV-189: API - Refactor - Volver a conectar repositorio de búsqueda de imágenes a mercadolibre según research

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-13 08:21 |
| Actualizado | 2025-06-30 10:48 |
| Etiquetas | ninguna |
| Jira | [INV-189](https://bluinc.atlassian.net/browse/INV-189) |

## Relaciones

- **Padre:** [[INV-35 - Importadores Scrappers|INV-35]] Importadores/ Scrappers
- **action item from:** [[INV-188 - API - Research - Intentar obtener enlace de mercadolibre para una busqueda|INV-188]] API - Research - Intentar obtener enlace de mercadolibre para una busqueda determinada y luego para esa ficha de producto
- **relates to:** [[INV-192 - API - Refactor - NewEgg dejo de funcionar para obtener imagenes|INV-192]] API - Refactor - NewEgg dejo de funcionar para obtener imagenes
- **relates to:** [[INV-193 - API - Feat - Buscar precio mínimo para un item determinado en mercadolibre|INV-193]] API - Feat - Buscar precio mínimo para un item determinado en mercadolibre

## Descripcion

Según el reasearch realizado, volveremos a dotar de la capacidad de traer imágenes de mercadolibre al recurso

```
GET {API_URL}/getImages/string?title={string}
```

Se debe revisar que no se pierda la capacidad de traerlas tambien de neweeg, como se hizo desde siempre
