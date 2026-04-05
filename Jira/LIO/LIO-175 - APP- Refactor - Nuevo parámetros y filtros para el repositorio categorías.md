---
jira_key: "LIO-175"
aliases: ["LIO-175"]
summary: "APP- Refactor - Nuevo parámetros y filtros para el repositorio categorías"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-01-19 19:37"
updated: "2025-01-27 04:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-175"
---

# LIO-175: APP- Refactor - Nuevo parámetros y filtros para el repositorio categorías

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-19 19:37 |
| Actualizado | 2025-01-27 04:35 |
| Etiquetas | ninguna |
| Jira | [LIO-175](https://bluinc.atlassian.net/browse/LIO-175) |

## Relaciones

- **Padre:** [[LIO-173 - Categorias|LIO-173]] Categorias

## Descripcion

Este refactor se divide en dos partes:

## 1 - El filtro que nos permite saber que secciones vamos a mostrar en el menu nuevo, reducido de la home

```
GET {API_URL}/v4/cabecera-categorias?homeShow={1|0|null}
```



## 2 - Cuando tengo presente la ruta explicita para el enlace (`directUrl`), que siempre es un enlace, mostrare esa en lugar de la composición común de la categoría

- directUrl: Parámetro para albergar directamente una url de búsqueda del tipo `https://libreopcion.com.ar/memorias-flash?ver_mas_vendedores=1&freeshipping=1` o cualquier otra



## Retorna

```
[
{
"id": 1732,
"nombre": "Accesorios y Periféricos",
"hijos": [
{
"id": 1,
"nombre": "Mouse",
"img": "icon-mouse.svg",
"directUrl": "https://libreopcion.com.ar/memorias-flash" <-- NUEVO
},
{
"id": 30,
"nombre": "Mousepad",
"img": "icon-mousepad.svg"
"directUrl": "https://libreopcion.com.ar/mousepad" <-- NUEVO
},
{
"id": 4,
"nombre": "Parlantes",
"img": "icon-parlantes.svg"
"directUrl": null <-- NUEVO
},
},
{
"id": 117,
"nombre": "Micrófonos",
"img": "icon-microfono.svg"
"directUrl": null <-- NUEVO
},
{
"id": 3,
"nombre": "Teclados",
"img": "icon-teclado.svg"
"directUrl": null <-- NUEVO
},
{
"id": 5,
"nombre": "Auriculares",
"img": "icon-auriculares.svg"
},
{
"id": 2,
"nombre": "Webcams",
"img": "icon-webcam.svg"
},
{
"id": 195,
"nombre": "Mochilas",
"img": "icon-mochilas.svg"
...
```
