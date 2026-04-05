---
jira_key: "INV-293"
aliases: ["INV-293"]
summary: "API - Review - Filtro por nombre de kit"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-19 09:03"
updated: "2025-12-26 12:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-293"
---

# INV-293: API - Review - Filtro por nombre de kit

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-19 09:03 |
| Actualizado | 2025-12-26 12:02 |
| Etiquetas | ninguna |
| Jira | [INV-293](https://bluinc.atlassian.net/browse/INV-293) |

## Relaciones

- **Padre:** [[INV-253]] Crear y modificar Kits

## Descripcion

Parece no estar filtrando por el atributo `search`

```
GET {API_URL}/itemsKits?currentPage=1&itemsPerPage=10&stockWarehouseId=2&companyCode=4&search=kit_mother_memoria_y_micro_testing_catri
```
