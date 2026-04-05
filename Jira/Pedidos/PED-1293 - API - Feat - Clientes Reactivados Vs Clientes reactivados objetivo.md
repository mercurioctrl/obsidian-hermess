---
jira_key: "PED-1293"
aliases: ["PED-1293"]
summary: "API - Feat - Clientes Reactivados Vs Clientes reactivados objetivo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-02-02 12:10"
updated: "2026-02-03 17:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1293"
---

# PED-1293: API - Feat - Clientes Reactivados Vs Clientes reactivados objetivo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-02 12:10 |
| Actualizado | 2026-02-03 17:53 |
| Etiquetas | ninguna |
| Jira | [PED-1293](https://bluinc.atlassian.net/browse/PED-1293) |

## Relaciones

- **Padre:** [[PED-299 - Objetivos y Desafios|PED-299]] Objetivos y Desafios
- **action item from:** [[PED-1286 - API - Research - Clientes reactivados ¿cual es la mejor forma de obtener esta|PED-1286]] API - Research - Clientes reactivados ¿cual es la mejor forma de obtener esta métrica?

## Descripcion

```
GET /v1/objectives/reactivatedClients
```



Ejemplo de uso:

```
GET /v1/objectives/reactivatedClients?sellerId=41&sortBy=reactivatedClients&sortOrder=desc &months=
```



```json
{
    "response": [
        {
            "sellerId": 41,
            "sellerDescription": "Natalia Sheridaim",
            "reactivatedClients": 7,
            "targetAmount": 10,
            "percentageAchieved": 70
        }
        ...
    ],
    "pagination": {
        "total": 1,
        "current": 1,
        "pageSize": 15
    }
}

```
