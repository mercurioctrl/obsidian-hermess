---
jira_key: "EXP-219"
aliases: ["EXP-219"]
summary: "API - Feat- Crear etiqueta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-02-27 09:58"
updated: "2023-03-27 08:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-219"
---

# EXP-219: API - Feat- Crear etiqueta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-02-27 09:58 |
| Actualizado | 2023-03-27 08:42 |
| Etiquetas | ninguna |
| Jira | [EXP-219](https://bluinc.atlassian.net/browse/EXP-219) |

## Relaciones

- **Padre:** [[EXP-218 - Etiquetas para envíos que no las generan (genericas de ahora en mas)|EXP-218]] Etiquetas para envíos que no las generan (genericas de ahora en mas)
- **blocks:** [[EXP-222 - APP - Feat - Modal para crear etiqueta de envío generica|EXP-222]] APP - Feat - Modal para crear etiqueta de envío generica

## Descripcion

Con el objetivo de registrar los datos que nos permitan generar una ‘etiqueta genérica’ para los medios de envío.

Para esto crearemos una tabla para ese proposito.

El recurso a ejecutarse se puede ubicar tanto en la ruta existente

```
POST {{API_URL}}/v1/shipments/addTrackingOrder
```



La carga útil que recibe el recurso es

```
{
  name: {string}, 
  address: {string},
  localityId: {int el id de la localidad}, 
  provinceId: {int el id de la localidad},
  postalCode: {numero},
  comment {string},
  packages: {int, por defecto 1}
}
```
