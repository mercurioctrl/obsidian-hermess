---
jira_key: "PED-26"
summary: "API - Repository - Divisas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-08-08 10:08"
updated: "2023-08-10 12:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-26"
---

# PED-26: API - Repository - Divisas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-08 10:08 |
| Actualizado | 2023-08-10 12:16 |
| Etiquetas | ninguna |
| Jira | [PED-26](https://bluinc.atlassian.net/browse/PED-26) |

## Descripción

Se trata del repositorio para obtener divisas

```
{API_URL}/V1/currency
```

```
[
  {
    "id": 1,
    "description": "DOLAR               ",
    "defaultCurrency": 1,
    "ccoddiv": "DOL ",
    "afipId": "DOL",
    "sign": "u$s       "
  },
  {
    "id": 2,
    "description": "PESOS               ",
    "defaultCurrency": null,
    "ccoddiv": "PSO ",
    "afipId": "PES",
    "sign": "$         "
  }
]
```

Repositorio

```
[NewBytes_DBF].[dbo].[FP_Monedas]
```
