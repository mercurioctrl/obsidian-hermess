---
jira_key: "COB-171"
aliases: ["COB-171"]
summary: "API - Feat - Realizar entrada"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-10-17 10:05"
updated: "2022-10-27 08:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-171"
---

# COB-171: API - Feat - Realizar entrada

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-17 10:05 |
| Actualizado | 2022-10-27 08:37 |
| Etiquetas | ninguna |
| Jira | [COB-171](https://bluinc.atlassian.net/browse/COB-171) |

## Relaciones

- **Padre:** [[COB-170 - Feat - Realizar entrada de caja|COB-170]] Feat - Realizar entrada de caja

## Descripcion

```
POST {URL_API}/v1/cashIn
```

```
[
    {
        "amount": 2,
        "paymentMethodId": 1,
        "inputConceptId": 8,
        "reference": "Comentario 1",
        "currencyQuote": 140.5
    },
    {
        "amount": 2,
        "paymentMethodId": 1,
        "inputConceptId": 8,
        "reference": "Comentario 2",
        "currencyQuote": 140.5
    },
    {
        "amount": 2,
        "paymentMethodId": 1,
        "inputConceptId": 8,
        "reference": "Comentario 3",
        "currencyQuote": 140.5
    }
]
```
