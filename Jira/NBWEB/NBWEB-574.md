---
jira_key: "NBWEB-574"
summary: "API - Feat - Recurso para leer precios"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-08-16 08:02"
updated: "2025-10-08 18:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-574"
---

# NBWEB-574: API - Feat - Recurso para leer precios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-16 08:02 |
| Actualizado | 2025-10-08 18:47 |
| Etiquetas | ninguna |
| Jira | [NBWEB-574](https://bluinc.atlassian.net/browse/NBWEB-574) |

## Descripción

Basandonos en el recurso [link](https://lioteam.atlassian.net/browse/NBWEB-4) crearemos un recurso especifico para actualizar precios, priorizando su velocidad de lectura.

```
GET [URL_PUNTERO]/prices/{terminos_de_busqueda}
```

```
[
{
    "id":"104964",
    "sku":"GP-P550B",
    "value":"53.56365",
    "iva":10.5,
    "finalPrice":59.187833250000004
},
{
    "id":"104964",
    "sku":"GP-P550B",
    "value":"53.56365",
    "iva":10.5,
    "finalPrice":59.187833250000004
]
```
