---
jira_key: "LIO-234"
aliases: ["LIO-234"]
summary: "API - Refactor - Usar backgrounds personalizados para los sectores personalizados de productos"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-02-26 06:36"
updated: "2025-02-27 21:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-234"
---

# LIO-234: API - Refactor - Usar backgrounds personalizados para los sectores personalizados de productos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-26 06:36 |
| Actualizado | 2025-02-27 21:13 |
| Etiquetas | ninguna |
| Jira | [LIO-234](https://bluinc.atlassian.net/browse/LIO-234) |

## Relaciones

- **Padre:** [[LIO-105 - Home|LIO-105]] Home
- **has action item:** [[LIO-239 - APP - Refactor - Conectar los mini banners de productos destacados con el CMS|LIO-239]] APP - Refactor - Conectar los mini banners de productos destacados con el CMS unificando la obtencion de los banners con una sola peticion

## Descripcion

Agregaremos primero (temporalmente harcodeado el fondo para una muestra)

[adjunto]
[adjunto]
Y luego lo leeremos directamente de una zona de banners una vez finalizada la refactorizacion [link](https://lioteam.atlassian.net/browse/LIO-235) .

Esta refactorizacion trae como idea que si voy a generar la home, por ahí puede ser mas rápido traer todo un recurso que incluso se puede cachear, una sola vez y adicionalmente guardarlo en local storage
