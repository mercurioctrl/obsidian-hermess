---
jira_key: "PED-511"
aliases: ["PED-511"]
summary: "API - Review - Error en query al eliminar un pedido"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-01-24 08:10"
updated: "2024-01-26 05:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-511"
---

# PED-511: API - Review - Error en query al eliminar un pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-24 08:10 |
| Actualizado | 2024-01-26 05:43 |
| Etiquetas | ninguna |
| Jira | [PED-511](https://bluinc.atlassian.net/browse/PED-511) |

## Relaciones

- **Padre:** [[PED-4 - Pedidos|PED-4]] Pedidos

## Descripcion

```
curl 'https://api.orders.lio.red/v1/orders/0000-10335650' \
  -X 'DELETE' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDYxNzcwODIsImF1ZCI6IjgyMGE2YTM0NjZhYjY2NWVlMDJlMzhlYTQzNDk2OTIzN2NkNWU0YTciLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjF9LCJpYXQiOjE3MDYwOTA2ODIsIm5iZiI6MTcwNjA5MDY4Mn0.wf4AMYjMEIo-UPzfe4R6i07nsbyrXwy0diXfUNMEEzM' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://www.pedidos.saftel.com' \
  -H 'Referer: https://www.pedidos.saftel.com/orders?currentPage=1&itemsPerPage=15&sellerId=12' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```

```
{
    "errors": {
        "status": 500,
        "title": "SQLSTATE[HY000]: General error: 20018 Incorrect syntax near ')'. [20018] (severity 15) [  UPDATE A\n        SET\n        nstock_reserva_pedidos = ISNULL((SELECT SUM(ncanped) FROM [NewBytes_DBF].[dbo].pedclil pl_sub\n        LEFT JOIN NewBytes_DBF.dbo.pedclit pt_sub ON\n        pl_sub.cnumsuc = pt_sub.cnumsuc\n        AND pl_sub.cnumped = pt_sub.cnumped\n\n        WHERE\n\n        (pt_sub.cobserv = 'INTERNO' OR  pt_sub.cobserv = 'DESCARGADO')\n        AND pt_sub.cestado = 'P'\n        AND (pl_sub.cref = A.cRef or pl_sub.ID_Articulo = A.ID_ARTICULO)\n        AND pl_sub.anulado <> 1 and pt_sub.lanula <> 1  ),0)\n        FROM [NewBytes_DBF].[dbo].[stocks] A WHERE A.ID_ARTICULO IN ();] (SQL:   UPDATE A\n        SET\n        nstock_reserva_pedidos = ISNULL((SELECT SUM(ncanped) FROM [NewBytes_DBF].[dbo].pedclil pl_sub\n        LEFT JOIN NewBytes_DBF.dbo.pedclit pt_sub ON\n        pl_sub.cnumsuc = pt_sub.cnumsuc\n        AND pl_sub.cnumped = pt_sub.cnumped\n\n        WHERE\n\n        (pt_sub.cobserv = 'INTERNO' OR  pt_sub.cobserv = 'DESCARGADO')\n        AND pt_sub.cestado = 'P'\n        AND (pl_sub.cref = A.cRef or pl_sub.ID_Articulo = A.ID_ARTICULO)\n        AND pl_sub.anulado <> 1 and pt_sub.lanula <> 1  ),0)\n        FROM [NewBytes_DBF].[dbo].[stocks] A WHERE A.ID_ARTICULO IN ();)",
        "file": "\/var\/www\/app\/vendor\/laravel\/framework\/src\/Illuminate\/Database\/Connection.php",
        "line": 760
    }
}
```
