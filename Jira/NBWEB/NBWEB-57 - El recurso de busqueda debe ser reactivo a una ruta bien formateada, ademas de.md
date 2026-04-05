---
jira_key: "NBWEB-57"
aliases: ["NBWEB-57"]
summary: "El recurso de busqueda debe ser reactivo a una ruta bien formateada, ademas de funcionar por parametros"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-29 08:24"
updated: "2022-04-04 06:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-57"
---

# NBWEB-57: El recurso de busqueda debe ser reactivo a una ruta bien formateada, ademas de funcionar por parametros

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-29 08:24 |
| Actualizado | 2022-04-04 06:52 |
| Etiquetas | ninguna |
| Jira | [NBWEB-57](https://bluinc.atlassian.net/browse/NBWEB-57) |

## Relaciones

- **Padre:** [[NBWEB-50]] Sitio Web

## Descripcion

Se debe hacer una corrección en el recurso general de búsqueda. 

```
{{API_URL}}/v1/
```

El mismo debe ser reactivo a el siguiente formato

[https://www.nb.com.ar/brand/thermaltake](https://www.nb.com.ar/brand/thermaltake) o [https://www.nb.com.ar/brand/](https://www.nb.com.ar/brand/thermaltake){id_de_la_marca}

[https://www.nb.com.ar/categories/discos-hdd](https://www.nb.com.ar/categories/discos-hdd) o [https://www.nb.com.ar/categories/](https://www.nb.com.ar/categories/discos-hdd){categoria}

Es decir que la llamada al recurso, lista la categoría o la marca completa, en caso de matchear 100% (no usar wildcards)
