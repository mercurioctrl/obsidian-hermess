---
jira_key: "PED-865"
aliases: ["PED-865"]
summary: "API - Refactor - Descargar listado de precios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-04 10:16"
updated: "2024-11-19 16:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-865"
---

# PED-865: API - Refactor - Descargar listado de precios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-04 10:16 |
| Actualizado | 2024-11-19 16:29 |
| Etiquetas | ninguna |
| Jira | [PED-865](https://bluinc.atlassian.net/browse/PED-865) |

## Relaciones

- **Padre:** [[PED-191 - Descargar Listado de precios|PED-191]] Descargar Listado de precios

## Descripcion

Refactorizar el recurso para descargar los listados de precios para incluir el internal tax en la ultima columna, tanto del excel como el txt

```
GET {API_URL}/v1/download/priceList?type=xlsx
```

```
GET {API_URL}/v1/download/priceList?type=text
```
