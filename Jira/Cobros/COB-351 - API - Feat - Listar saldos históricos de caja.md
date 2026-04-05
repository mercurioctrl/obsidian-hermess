---
jira_key: "COB-351"
aliases: ["COB-351"]
summary: "API - Feat - Listar saldos históricos de caja"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-03-10 08:31"
updated: "2024-04-16 12:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-351"
---

# COB-351: API - Feat - Listar saldos históricos de caja

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-10 08:31 |
| Actualizado | 2024-04-16 12:17 |
| Etiquetas | ninguna |
| Jira | [COB-351](https://bluinc.atlassian.net/browse/COB-351) |

## Relaciones

- **Padre:** [[COB-347]] Poder ver saldo inicial y final de caja en cada día
- **blocks:** [[COB-352]] APP - Feat - Listar saldos históricos de caja

## Descripcion

Crearemos un recurso para poder mostrar el historial de saldos registrados para una caja determinada.

Para esto utilizaremos la tabla `[NEW_BYTES].[dbo].[MC_SALDOS_INICIO]`

Para esto usaremos el recurso

```
GET {API_URL}/v1/boxBalance/{caja}/balanceHistory?between=03-2022_03-2023&itemsPerPage=15&currentPage=1
```

Obtendremos algo similar al siguiente array de objetos

```
[
    {
        "date": "2022-03-02",
        "dolar": {
            "scAmount": 1422.77000000003,
            "scAmountManual": 0,
            "paymentId": 1,
            "paymentDescription": "DOLARES"
        },
        "peso": {
            "scAmount": 164868.630000026,
            "scAmountManual": 0,
            "paymentId": 2,
            "paymentDescription": "PESOS"
        },
        "cheque": {
            "scAmount": -130227499.2,
            "scAmountManual": 0,
            "paymentId": 15,
            "paymentDescription": "CHEQUE"
        }
    }
]
```

Este recurso debe tener un mecanismo de paginacion similar a los otros listados
