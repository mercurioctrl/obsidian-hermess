---
jira_key: "PED-69"
summary: "API - Feat - Listar productos -> Filtros"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-12 09:56"
updated: "2023-10-04 10:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-69"
---

# PED-69: API - Feat - Listar productos -> Filtros

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-12 09:56 |
| Actualizado | 2023-10-04 10:08 |
| Etiquetas | ninguna |
| Jira | [PED-69](https://bluinc.atlassian.net/browse/PED-69) |

## Descripción

```
GET {API_URL}/v1/items?search={string match}&categorieId={filtraPorId}&brandId={filtraPorId}&inStock=true
```

- `search` es un string que filtra por el titulo del producto


- `categorieId` muestra productos dentro de la categoría


- `brandId` muestra productos dentro de la marca


- `inStock` muestra o no los productos en stock, según el criterio ` AND (S.nstock - S.nstock_reserva_pedidos > 0) `
