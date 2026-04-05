---
jira_key: "NBWEB-881"
aliases: ["NBWEB-881"]
summary: "EXTENSION - Woocomerce - Agregar ruta especifica para las imágenes de exportación "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-09-18 12:53"
updated: "2024-09-23 02:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-881"
---

# NBWEB-881: EXTENSION - Woocomerce - Agregar ruta especifica para las imágenes de exportación 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-18 12:53 |
| Actualizado | 2024-09-23 02:22 |
| Etiquetas | ninguna |
| Jira | [NBWEB-881](https://bluinc.atlassian.net/browse/NBWEB-881) |

## Relaciones

- **Padre:** [[NBWEB-682 - Productos|NBWEB-682]] Productos

## Descripcion

Basandonos en el arreglo realizado en [link](https://github.com/New-Bytes/sitio-api-rest-v3/pull/495)  

Usaremos los parametros de las variables de entorno
CACHE_STATIC_BASE_URL=[https://static.nb.com.ar/i/](https://static.nb.com.ar/i/)
SUBFIX_IMG_URL=_export_

para entregar un parametro especifico en la API

```

{
"title": "ACCESORIOS ADATA CARRY GABINETE P/SSD ED600 BLACK",
"sku": "AED600-U31-CBK",
"id": 103314,
"category": "ACCESORIOS",
"categoryId": 20,
"brand": "ADATA",
"brandId": 91,
"mainImage": "https://static.nb.com.ar/i/nb_ACCESORIOS-ADATA-CARRY-GABINETE-P/SSD-ED600-BLACK_ver_7fef69ca98c61857f106c6eda8fda6d8.jpeg",
"mainImageExp": "https://static.nb.com.ar/i/nb_ACCESORIOS-ADATA-CARRY-GABINETE-PSSD-ED600-BLACK_export_7fef69ca98c61857f106c6eda8fda6d8.jpeg",
"brandImage": "https://static.nb.com.ar/img/c2e0fde53fb8cc3bb7c5afd089671af1.jpg",
"initialB": 5,

```
