---
jira_key: "COB-225"
aliases: ["COB-225"]
summary: "API - Refactor - Agregar toleranca a los medios de pago"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-02 17:18"
updated: "2022-11-29 11:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-225"
---

# COB-225: API - Refactor - Agregar toleranca a los medios de pago

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-02 17:18 |
| Actualizado | 2022-11-29 11:33 |
| Etiquetas | ninguna |
| Jira | [COB-225](https://bluinc.atlassian.net/browse/COB-225) |

## Relaciones

- **Padre:** [[COB-222 - Refactor - Redondeo al cobrar|COB-222]] Refactor - Redondeo al cobrar
- **blocks:** [[COB-223 - APP - Refactor - Redondeo al cobrar|COB-223]] APP - Refactor - Redondeo al cobrar

## Descripcion

Lo primero es que agregaremos al recurso 

```
GET {{API_URL}}/v1/paymentMethods
```

el parametro `paymentTolerance` y quedara de la siguiente forma.

```
[
    {
        "id": 1,
        "description": "DOLARES",
        "increment": 0,
        "currencyAmount": 1,
        "isCheck": "NO",
        "paymentTolerance": 1
    },
    {
        "id": 2,
        "description": "PESOS",
        "increment": 0,
        "currencyAmount": 143,
        "isCheck": "NO",
        "paymentTolerance": 10
    },
    {
        "id": 14,
        "description": "CUENTA CORRIENTE",
        "increment": 0,
        "currencyAmount": 1,
        "isCheck": "NO",
        "paymentTolerance": 10
    },
    {
        "id": 15,
        "description": "CHEQUE",
        "increment": 0,
        "currencyAmount": 155,
        "isCheck": "SI",
        "paymentTolerance": 10
    }
]
```

El parámetro sale de la misma tabla y hay que agregar la columna en la tabla (recordar dejar la query).
