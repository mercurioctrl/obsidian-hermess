---
jira_key: "NBWEB-69"
summary: "Cambio de url de la imagen por checkshum correcto y url completa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-30 16:36"
updated: "2022-06-21 21:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-69"
---

# NBWEB-69: Cambio de url de la imagen por checkshum correcto y url completa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-30 16:36 |
| Actualizado | 2022-06-21 21:35 |
| Etiquetas | ninguna |
| Jira | [NBWEB-69](https://bluinc.atlassian.net/browse/NBWEB-69) |

## Descripción

Para obtener la columna `[checksum]` que contiene un string de la imagen en nuestro servidor de imágenes, del siguiente tipo “8fdb2f87975f3835eb0c41e08a82f133.jpeg”.

Tiene que existir una variable en el archivo .env y .env-example llamada “CACHE_STATIC_BASE_URL” que en este caso tendrá el valor “[https://static.nb.com.ar/i/](https://static.nb.com.ar/i/)” y debe retornarse dentro del parametro de la siguiente forma

`"imagen_principal":" https://static.nb.com.ar/i/nb_nombre-del-producto_ver_b65cd71de19e10c27d8c357cd99cded9.png"`

La clave para obtener la columna de la tabla `[PRODUCTOS].[dbo].[fotos]` seria:

```sql
    LEFT JOIN 
        [NB_WEB].[dbo].[fotos_productos] 
    ON 
        [NB_WEB].[dbo].[fotos_productos].id_nb_producto = [NewBytes_DBF].[dbo].[articulo].id_articulo AND [NB_WEB].[dbo].[fotos_productos].portada = 1
    LEFT JOIN 
        [PRODUCTOS].[dbo].[fotos]
    ON 
        [NB_WEB].[dbo].[fotos_productos].id_productos_fotos = [PRODUCTOS].[dbo].[fotos].id
```
