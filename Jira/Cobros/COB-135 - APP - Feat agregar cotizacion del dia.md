---
jira_key: "COB-135"
aliases: ["COB-135"]
summary: "APP - Feat agregar cotizacion del dia"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2022-10-04 13:42"
updated: "2022-10-25 09:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-135"
---

# COB-135: APP - Feat agregar cotizacion del dia

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2022-10-04 13:42 |
| Actualizado | 2022-10-25 09:05 |
| Etiquetas | ninguna |
| Jira | [COB-135](https://bluinc.atlassian.net/browse/COB-135) |

## Relaciones

*Sin relaciones*

## Descripcion

```
{{API_URL}}/v1/paymentMethods
```

```
[
    {
        "id": 1,
        "description": "DOLARES",
        "increment": 0,
        "currencyAmount": 1,
        "isCheck": "NO"
    },
    {
        "id": 2,
        "description": "PESOS",// --->ESTA
        "increment": 0,
        "currencyAmount": 143,
        "isCheck": "NO"
    },
    {
        "id": 14,
        "description": "CUENTA CORRIENTE",
        "increment": 0,
        "currencyAmount": 1,
        "isCheck": "NO"
    },
    {
        "id": 15,
        "description": "CHEQUE",
        "increment": 0,
        "currencyAmount": 155,
        "isCheck": "SI"
    }
]
```
