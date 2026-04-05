---
jira_key: "INV-180"
aliases: ["INV-180"]
summary: "APP - Refactor - Listar productos (Pestaña productos) - Portada no visible tras selección"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2025-02-25 20:42"
updated: "2025-02-27 20:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-180"
---

# INV-180: APP - Refactor - Listar productos (Pestaña productos) - Portada no visible tras selección

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2025-02-25 20:42 |
| Actualizado | 2025-02-27 20:25 |
| Etiquetas | ninguna |
| Jira | [INV-180](https://bluinc.atlassian.net/browse/INV-180) |

## Relaciones

- **Padre:** [[INV-27]] Productos
- **relates to:** [[INV-28]] APP - Feat - Listar productos (Pestaña productos)
- **blocks:** [[SNB-2825]] Ni bien cargo una imagen desde un repositorio (por ejemplo meli) al marcarla como portada no funciona, parece no tener el id

## Descripcion

Al cargar una imagen e inmediatamente seleccionarla como portada, al revisar el sitio web, la imagen no aparece como portada. Este inconveniente puede deberse al orden en el que se completan las peticiones dentro del flujo de trabajo, específicamente el hecho de que la imagen es marcada como portada antes de establecer la relación con los productos.



**Flujo de Proceso:**

1. Carga de la Imagen:

```
https://api.inventory.lio.red/uploadfile/file
```



2. Marcado de la Imagen como Portada:

```
https://api.inventory.lio.red/item/{itemId}
```



3. Relación del Producto con las Imágenes:

```
https://api.inventory.lio.red/item/{itemId}
```



[adjunto]
