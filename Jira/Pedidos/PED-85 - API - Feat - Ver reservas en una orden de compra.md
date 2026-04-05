---
jira_key: "PED-85"
aliases: ["PED-85"]
summary: "API - Feat - Ver reservas en una orden de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-21 09:50"
updated: "2025-12-15 12:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-85"
---

# PED-85: API - Feat - Ver reservas en una orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-21 09:50 |
| Actualizado | 2025-12-15 12:25 |
| Etiquetas | ninguna |
| Jira | [PED-85](https://bluinc.atlassian.net/browse/PED-85) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra
- **blocks:** [[PED-86 - APP - Feat - Ver reservas de una orden de compra|PED-86]] APP - Feat - Ver reservas de una orden de compra
- **action item from:** [[PED-1192 - API - Refactor - Ver reservas en una orden de compra|PED-1192]] API - Refactor - Ver reservas en una orden de compra

## Descripcion

Este recurso sirve para saber quien tiene disponible stock de un producto determinado, que aun esta disponible. Siempre se trata de casos “reservados” es decir que el vendedor lo tiene en un pedido para un cliente, pero la función es justamente que sus compañeros puedan ver esto para solicitarle stock en caso de que sea necesario para cerrar una orden.

```
GET {API_URL}/v1/itemReservations/{itemId}
```

```json
[
    {
        "dateOrder": "2023-09-13 09:24:25",
        "branch": "0002",
        "order": "10328182",
        "clientDescription": "COMPUGARDEN S.R.L.",
        "amount": "3.000",
        "agentDescription": "Andrea Altamiranda"
    },
    {
        "dateOrder": "2023-09-15 17:42:04",
        "branch": "0002",
        "order": "10328538",
        "clientDescription": "SOFTROCKS",
        "amount": "1.000",
        "ncanent": null,
        "agentDescription": "Soto Lautaro"
    },
    {
        "dateOrder": "2023-09-15 17:58:12",
        "branch": "0002",
        "order": "10328540",
        "clientDescription": "FONTANINI PACHER FRANCISCO MARIANO",
        "amount": "1.000",
        "ncanent": null,
        "agentDescription": "Patricio Contardi"
    },
    {
        "dateOrder": "2023-09-18 11:28:31",
        "branch": "0002",
        "order": "10328598",
        "clientDescription": "NUNEZ MARIA ALEJANDRA",
        "amount": "1.000",
        "ncanent": null,
        "agentDescription": "Patricio Contardi"
    }
]
```

Consulta orientativa

```sql
SELECT
CONVERT(VARCHAR,A.dfecped, 20) AS dfecped,
A.cnumsuc,
A.cnumped,
D.cnomcli,
B.ncanped,
B.ncanent,
E.cnbrage,
E.capeage
FROM [NewBytes_DBF].[dbo].[pedclit] A
LEFT JOIN [NewBytes_DBF].[dbo].[pedclil] B
ON A.cnumsuc = B.cnumsuc AND A.cnumped = B.cnumped AND A.cnumsuc = B.cnumsuc
LEFT JOIN NewBytes_DBF.dbo.articulo C ON C.cRef = B.cref
LEFT JOIN NewBytes_DBF.dbo.clientes D ON D.ccodcli = A.ccodcli
LEFT JOIN NewBytes_DBF.dbo.agentes E ON E.ccodage = D.ccodage
WHERE B.cref = ? AND (A.cobserv = 'INTERNO' OR A.cobserv = 'DESCARGADO') AND A.cestado = 'P' and ncanped >0
GROUP BY
A.dfecped,
B.ncanent,
A.cnumsuc,
A.cnumped,
D.cnomcli,
B.ncanped,
E.cnbrage,
E.capeage
```
