---
jira_key: "POS-172"
aliases: ["POS-172"]
summary: "APP - Feat agregar cotizacion del dia"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2022-10-04 14:14"
updated: "2022-10-18 14:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-172"
---

# POS-172: APP - Feat agregar cotizacion del dia

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2022-10-04 14:14 |
| Actualizado | 2022-10-18 14:21 |
| Etiquetas | ninguna |
| Jira | [POS-172](https://bluinc.atlassian.net/browse/POS-172) |

## Relaciones

*Sin relaciones*

## Descripcion

```
{{API_URL}}/v1/cotization
```

```
[
    {
        "id": 1,
        "description": "DOLARES",
        "isCheck": "NO",
        "increment": 0,
        "currencyAmount": 1
    },
    {
        "id": 2,
        "description": "PESOS",// --> ESTE
        "isCheck": "NO",
        "increment": 0,
        "currencyAmount": 143.25
    },
    {
        "id": 14,
        "description": "CUENTA CORRIENTE",
        "isCheck": "NO",
        "increment": 0,
        "currencyAmount": 1
    },
    {
        "id": 15,
        "description": "CHEQUE",
        "isCheck": "SI",
        "increment": 0,
        "currencyAmount": 155.02
    }
]
```
