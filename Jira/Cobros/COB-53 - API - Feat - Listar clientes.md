---
jira_key: "COB-53"
aliases: ["COB-53"]
summary: "API - Feat - Listar clientes"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-09 15:35"
updated: "2022-10-20 17:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-53"
---

# COB-53: API - Feat - Listar clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-09 15:35 |
| Actualizado | 2022-10-20 17:09 |
| Etiquetas | ninguna |
| Jira | [COB-53](https://bluinc.atlassian.net/browse/COB-53) |

## Relaciones

- **Padre:** [[COB-20]] Cuentas Corrientes
- **Subtarea:** [[COB-64]] API - Feat - Filtros listar clientes
- **Subtarea:** [[COB-271]] API - Refactor - Se debe poder ingresar nombres con la letra ñ, al menos como un comodin
- **Subtarea:** [[COB-437]] API - Refactor - Agregar parametro y filtro para clientes activos/inactivos/todos
- **blocks:** [[COB-54]] APP - Feat - Listar clientes

## Descripcion

```
GET {API_RUL}/v1/clients
```

```json
  [{
    "clientId": "026870",
    "clientName": "CRIVELLI DIEGO GASPAR",
    "clientBusinessName": "CRIVELLI DIEGO GASPAR",
    "clientTaxNumber": "20-32107683-2",
    "clientPerception": 0.0,
    "checkBalanceAmount": 2004252.04,
    "limitBalanceAmount": 2000.0,
    "usedBalanceAmount": 122.06,
  },
  {
    "clientId": "026887",
    "clientName": "PIGNANI MATIAS NICOLAS",
    "clientBusinessName": "PIGNANI MATIAS NICOLAS",
    "clientTaxNumber": "20-33947793-1",
    "clientPerception": 0.0,
    "limitCheckBalanceAmount": 2004252.04,
    "usedCheckBalanceAmount": 2004252.04,
    "limitBalanceAmount": 2000.0,
    "usedBalanceAmount": 122.06,
    }
  ]
```
