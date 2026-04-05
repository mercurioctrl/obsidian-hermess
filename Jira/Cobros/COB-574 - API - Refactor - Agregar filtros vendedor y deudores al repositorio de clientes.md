---
jira_key: "COB-574"
aliases: ["COB-574"]
summary: "API - Refactor - Agregar filtros \"vendedor\" y \"deudores\" al repositorio de clientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-20 07:51"
updated: "2025-08-25 11:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-574"
---

# COB-574: API - Refactor - Agregar filtros "vendedor" y "deudores" al repositorio de clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-20 07:51 |
| Actualizado | 2025-08-25 11:02 |
| Etiquetas | ninguna |
| Jira | [COB-574](https://bluinc.atlassian.net/browse/COB-574) |

## Relaciones

- **Padre:** [[COB-573]] Clientes
- **has action item:** [[COB-576]] APP - Refactor - Agregar filtros "vendedor" y "deudores" al repositorio de clientes
- **relates to:** [[COB-577]] API - Propuesta de mejora - Repositorio de clientes -> Decimales visibles en el saldo

## Descripcion

En principio agregaremos dos filtros nuevos al recurso `sellerId` y `balanceState`

```
GET /v1/clients?currentPage=1&itemsPerPage=15&sellerId=42&balanceState=debt
```

`sellerId`: Se trata de un filtro por vendedor que ya hemos utilizado otras veces, el mismo esta basado en el repositorio de vendedores [link](https://bluinc.atlassian.net/browse/COB-575)  el mismo se vincula a los clientes a traves del parametro `ID_VENDEDOR` de la tabla de clientes

`balanceState:` Este parámetro opera sobre el atributo `usedBalanceAmount` de este mismo recurso. Y puede cursar los siguientes valores:

- `debt` → `usedBalanceAmount < 0`


- `credit` → `usedBalanceAmount > 0`


- `none` → `usedBalanceAmount = 0`


- `null` (default si no se envía) → no filtra por estado de saldo.



Adicionalmente y ya que incorporamos esa dimension, agregaremos el vendedor como nuevos parametros a la salida del objeto de la siguiente manera

```
{
    "response": [
        {
            "clientId": 92282,
            "clientName": "Ariel matias Callisto",
            "clientBusinessName": "Ariel matias Callisto",
            "clientTaxNumber": "33286685",
            "clientPerception": 0,
            "limitCheckBalanceAmount": 0,
            "usedCheckBalanceAmount": 0,
            "limitBalanceAmount": 0,
            "usedBalanceAmount": 0,
            "desactive": false,
            "salespersonName": "Natalia Sheridaim", <--SE AGREGA
            "sellerId": 41 <-- SE AGREA
        },
        {
            "clientId": 92281,
            "clientName": "Misael Comba",
            "clientBusinessName": "Misael Comba",
            "clientTaxNumber": "44348164",
            "clientPerception": 0,
            "limitCheckBalanceAmount": 0,
            "usedCheckBalanceAmount": 0,
            "limitBalanceAmount": 0,
            "usedBalanceAmount": 0,
            "desactive": false
            "salespersonName": "Natalia Sheridaim", <--SE AGREGA
            "sellerId": 41 <-- SE AGREA
        },
    ...
    ],
    "pagination": {
        "total": 87755,
        "current": 1,
        "pageSize": 15
    }
}
```
