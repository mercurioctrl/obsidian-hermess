---
jira_key: "INV-188"
aliases: ["INV-188"]
summary: "API - Research - Intentar obtener enlace de mercadolibre para una busqueda determinada y luego para esa ficha de producto"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-05 12:13"
updated: "2025-06-13 08:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-188"
---

# INV-188: API - Research - Intentar obtener enlace de mercadolibre para una busqueda determinada y luego para esa ficha de producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-05 12:13 |
| Actualizado | 2025-06-13 08:35 |
| Etiquetas | ninguna |
| Jira | [INV-188](https://bluinc.atlassian.net/browse/INV-188) |

## Relaciones

- **Padre:** [[INV-35]] Importadores/ Scrappers
- **has action item:** [[INV-189]] API - Refactor - Volver a conectar repositorio de búsqueda de imágenes a mercadolibre según research

## Descripcion

Supongamos que deseo buscar las imágenes y el precio de un producto con el `SKU EP-T2510XBSGAR`

Para lo cual empezaremos construyendo un enlace del siguiente tipo o similar

```
https://listado.mercadolibre.com.ar/ep-t2510xbsgar#D[A:EP-T2510XBSGAR]
```

Y buscaremos obtener los enlaces que nos proveerán la ficha que contiene los datos objetivos

[adjunto]
Terminaremos obteniendo un enlace similar al siguiente


```
https://articulo.mercadolibre.com.ar/MLA-724650637-cargador-original-samsung-carga-rapida-a80-a20-a50-a30-a70-_JM?searchVariation=69105050201&highlight=false&headerTopBrand=true#polycard_client=search-nordic&searchVariation=69105050201&position=32&search_layout=stack&type=item&tracking_id=69d5af07-9e81-47ba-8f2e-d6af10e044fb
```

Una vez con el enlace, veremos si es posible obtener los siguiente datos (imagenes, precio y titulo)


[adjunto]
