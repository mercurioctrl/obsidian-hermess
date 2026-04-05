---
jira_key: "NBWEB-646"
summary: "API - Feat - Listas de precio -> Agregar nueva utilidad y mascara de Categoria"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-03-15 08:46"
updated: "2024-03-18 15:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-646"
---

# NBWEB-646: API - Feat - Listas de precio -> Agregar nueva utilidad y mascara de Categoria

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-15 08:46 |
| Actualizado | 2024-03-18 15:20 |
| Etiquetas | ninguna |
| Jira | [NBWEB-646](https://bluinc.atlassian.net/browse/NBWEB-646) |

## Descripción

Agregaremos al recurso items (catalogo), en caso de existir la vinculación con la tabla de categorías [link](https://lioteam.atlassian.net/browse/NBWEB-644) 

los siguientes parametros

```
[
{
"title": "DISCO SSD M.2 500GB WD BLACK SN770 NVME PCIe Gen4 x4",
"sku": "WDS500G3XE",
"id": 117262,
"category": "DISCOS SSD",
"categoryId": 56,
"categoryUserId": 45455,  <---
"categoryDescriptionUser": 'Mother varias marcas', <---
"utility": 2.5, <---
"brand": "WD",
"brandId": 62,
"mainImage": "https://static.nb.com.ar/i/nb_DISCO-SSD-M.2-500GB-WD-BLACK-SN770-NVME-PCIe-Gen4-x4_ver_c3ac1f866bcda2e0d33e77f590df7047.jpg",
"brandImage": "https://static.nb.com.ar/img/c6ab87d63363e40dfe3338023b5838c6.jpg",
"initialB": 5,
"initialC": 10,
"stock": "Sin stock",
"amountInCart": 0,
"amountStock": null,
"price": null,
"warranty": "12 meses",
"cotizacion": 869
},
```
