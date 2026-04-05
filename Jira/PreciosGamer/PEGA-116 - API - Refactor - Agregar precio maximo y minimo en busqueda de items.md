---
jira_key: "PEGA-116"
aliases: ["PEGA-116"]
summary: "API - Refactor - Agregar precio maximo y minimo en busqueda de items"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-09-16 15:49"
updated: "2024-09-20 07:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-116"
---

# PEGA-116: API - Refactor - Agregar precio maximo y minimo en busqueda de items

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-09-16 15:49 |
| Actualizado | 2024-09-20 07:46 |
| Etiquetas | ninguna |
| Jira | [PEGA-116](https://bluinc.atlassian.net/browse/PEGA-116) |

## Relaciones

- **Padre:** [[PEGA-7]] Feat - Detalle del producto (Ficha)

## Descripcion

```
{
  "response":[....],
  "pagination": {
        "total": 115,
        "offset": 0,
        "limit": 30,
        "order": "asc_price",
        "maxPrice": 719714, --> nuevo maximo precio
        "minPrice": 84729 --> nuevo minimo precio
    }
}
```
