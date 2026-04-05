---
jira_key: "NBWEB-883"
aliases: ["NBWEB-883"]
summary: "API - Refactor - Agregar a los csv y xlsx las medidas y peso de los preductos segun el esquema Producto > Categoria"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-19 10:02"
updated: "2024-09-25 00:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-883"
---

# NBWEB-883: API - Refactor - Agregar a los csv y xlsx las medidas y peso de los preductos segun el esquema Producto > Categoria

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-19 10:02 |
| Actualizado | 2024-09-25 00:14 |
| Etiquetas | ninguna |
| Jira | [NBWEB-883](https://bluinc.atlassian.net/browse/NBWEB-883) |

## Relaciones

- **Padre:** [[NBWEB-602 - Sitio Web|NBWEB-602]] Sitio Web

## Descripcion

Agregaremos las 3 medidas y el peso según el esquema que usamos donde de no existir en el articulo, usamos el de la categoría

```
GET {API_URL}/v1/priceListCsv
```

```
GET {API_URL}/v1/priceListExcel
```

```
GET {API_URL}/v1/priceListCsv/{token}
```

```
GET {API_URL}/v1/priceListExcel/{token}
```
