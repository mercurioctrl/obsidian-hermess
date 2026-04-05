---
jira_key: "COB-531"
aliases: ["COB-531"]
summary: "APP - Refactor - Incoporar el cobro total a los clientes y las descripciones"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-07-23 17:05"
updated: "2024-07-24 16:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-531"
---

# COB-531: APP - Refactor - Incoporar el cobro total a los clientes y las descripciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-23 17:05 |
| Actualizado | 2024-07-24 16:42 |
| Etiquetas | ninguna |
| Jira | [COB-531](https://bluinc.atlassian.net/browse/COB-531) |

## Relaciones

- **Padre:** [[COB-506]] Logistica

## Descripcion

```
GET {{API_URL}}/v1/statistics/logisticsExpenses
```

```
{
    "expenseAmount": 5232199.076355001,
    "chargedAmount": 3649961.0875375997, <<---- NUEVO
    "intervals": [
        {
            "date": "01-07-2024",
            "expense": 311478.6375850001,
            "charged": 458636.73651014996
        },
        {
            "date": "02-07-2024",
            "expense": 330800.24218999996,
            "charged": 210511.67466230007
        },
....
],
    "descriptions": {
        "expenseAmount": "Importe que pagaron los clientes por los envíos", <<----NUEVO
        "chargedAmount": "Importe cobrado por los envíos" <<----NUEVO
    }
}
        
```



[adjunto]
