---
jira_key: "NBWEB-936"
aliases: ["NBWEB-936"]
summary: "API - Refactor - Al XLSX general, tanto con como sin token, le agregaremos una columna con la galeria completa de imagenes"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-20 07:20"
updated: "2024-12-27 06:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-936"
---

# NBWEB-936: API - Refactor - Al XLSX general, tanto con como sin token, le agregaremos una columna con la galeria completa de imagenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-20 07:20 |
| Actualizado | 2024-12-27 06:29 |
| Etiquetas | ninguna |
| Jira | [NBWEB-936](https://bluinc.atlassian.net/browse/NBWEB-936) |

## Relaciones

- **Padre:** [[NBWEB-602 - Sitio Web|NBWEB-602]] Sitio Web

## Descripcion

```
GET {API_URL}/v1/priceListExcel/{token}
```

```
GET {API_URL}/v1/priceListExcel
```

Así como existe la columna “IMAGEN” agregaremos detrás de todo una columna extra llamada “GALERIA” donde ademas de estar la imagen principal, estén tambien las demás pero separadas por “,”


Se debe buscar el metodo que retrase el recurso lo menos posible. En caso de presentarse retrasos importantes, es posible que necesitemos agregar un parámetro para activar o no la feature en nuestras variables de entorno (Se necesita mas que nada para NBE, aunque estaria bueno tambien para NB)
