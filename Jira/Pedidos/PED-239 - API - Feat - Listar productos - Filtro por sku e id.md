---
jira_key: "PED-239"
aliases: ["PED-239"]
summary: "API - Feat - Listar productos -> Filtro por sku e id"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-11-07 09:35"
updated: "2023-11-14 00:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-239"
---

# PED-239: API - Feat - Listar productos -> Filtro por sku e id

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-07 09:35 |
| Actualizado | 2023-11-14 00:26 |
| Etiquetas | ninguna |
| Jira | [PED-239](https://bluinc.atlassian.net/browse/PED-239) |

## Relaciones

- **Padre:** [[PED-65]] Listado de productos

## Descripcion

```
GET {API_URL}/v1/items?sku={sku}&id={itemId}
```

Agregaremos la posibilidad de buscar por SKU y por ID de producto
