---
jira_key: "PEGA-93"
aliases: ["PEGA-93"]
summary: "API - Feat - Agrupar por dia el resultado del histograma"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-06-25 10:06"
updated: "2024-06-26 01:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-93"
---

# PEGA-93: API - Feat - Agrupar por dia el resultado del histograma

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-25 10:06 |
| Actualizado | 2024-06-26 01:58 |
| Etiquetas | ninguna |
| Jira | [PEGA-93](https://bluinc.atlassian.net/browse/PEGA-93) |

## Relaciones

- **Padre:** [[PEGA-7]] Feat - Detalle del producto (Ficha)

## Descripcion

```
GET {API_URL}/v1/itemDetail/{id}
```

Sucede en casos como los del ejemplo siguiente, que el histograma devuelve varios valores para el mismo dia y entrega un histograma de menor utilidad, la idea seria solo devolver un precio por día (el ultimo).



[adjunto]
