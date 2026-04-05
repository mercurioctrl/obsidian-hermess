---
jira_key: "PEGA-113"
aliases: ["PEGA-113"]
summary: "API - Refactor - Filtro limites de precio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-09-13 09:06"
updated: "2024-09-16 11:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-113"
---

# PEGA-113: API - Refactor - Filtro limites de precio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-13 09:06 |
| Actualizado | 2024-09-16 11:12 |
| Etiquetas | ninguna |
| Jira | [PEGA-113](https://bluinc.atlassian.net/browse/PEGA-113) |

## Relaciones

- **Padre:** [[PEGA-6 - Feat - Listar productos|PEGA-6]] Feat - Listar productos
- **blocks:** [[PEGA-115 - APP - Refactor - Agregar filtro limite de precios|PEGA-115]] APP - Refactor - Agregar filtro limite de precios

## Descripcion

```
GET {API_URL}/v1/items?search=amd&priceLimit=0-344
```

Agregaremos un parámetro para filtrar in intervalo de precios….
