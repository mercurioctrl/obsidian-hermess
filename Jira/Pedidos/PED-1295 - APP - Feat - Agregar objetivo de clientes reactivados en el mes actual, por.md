---
jira_key: "PED-1295"
aliases: ["PED-1295"]
summary: "APP - Feat - Agregar objetivo de clientes reactivados en el mes actual, por vendedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-02-03 08:23"
updated: "2026-02-12 14:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1295"
---

# PED-1295: APP - Feat - Agregar objetivo de clientes reactivados en el mes actual, por vendedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-03 08:23 |
| Actualizado | 2026-02-12 14:01 |
| Etiquetas | ninguna |
| Jira | [PED-1295](https://bluinc.atlassian.net/browse/PED-1295) |

## Relaciones

- **Padre:** [[PED-299]] Objetivos y Desafios

## Descripcion

Usaremos la feature [link](https://bluinc.atlassian.net/browse/PED-1293)  para agregar debajo de el objetivo mensual de venta

[adjunto]
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
