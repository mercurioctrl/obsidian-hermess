---
jira_key: "PED-382"
aliases: ["PED-382"]
summary: "API - Review - Eliminar albclit, problema con algunos articulos"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-12-22 15:17"
updated: "2023-12-22 17:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-382"
---

# PED-382: API - Review - Eliminar albclit, problema con algunos articulos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-22 15:17 |
| Actualizado | 2023-12-22 17:07 |
| Etiquetas | ninguna |
| Jira | [PED-382](https://bluinc.atlassian.net/browse/PED-382) |

## Relaciones

- **Padre:** [[PED-4 - Pedidos|PED-4]] Pedidos

## Descripcion

```
curl 'https://api.orders.lio.red/v1/removeSale' \
  -X 'DELETE' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDMzMzM3MDksImF1ZCI6IjJjNDY0YjE5Yjg1ZDhlOTM1N2E4Yzc2ODFmZDUxMzBhMTE4MzZkYTQiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjB9LCJpYXQiOjE3MDMyNDczMDksIm5iZiI6MTcwMzI0NzMwOX0.ESQfK8WOeYwkMrtqApYRax62wb3Y6noHNwUNxrieycA' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://beta.pedidos.saftel.com' \
  -H 'Referer: https://beta.pedidos.saftel.com/orders?currentPage=1&itemsPerPage=15&search=00570569' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"order":"10334941","branch":"0002"}' \
  --compressed
```

Devuelve:

```
{
    "errors": {
        "status": 500,
        "title": "SQLSTATE[HY000]: General error: 20018 Invalid column name 'ARMADO_PC'. [20018] (severity 16) [  DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 111454\n                                AND ID_ARTICULO = 111454; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 116698\n                                AND ID_ARTICULO = 116698; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 101267\n                                AND ID_ARTICULO = 101267; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 116787\n                                AND ID_ARTICULO = 116787; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 103041\n                                AND ID_ARTICULO = 103041; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 117826\n                                AND ID_ARTICULO = 117826; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 118520\n                                AND ID_ARTICULO = 118520; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 117789\n                                AND ID_ARTICULO = 117789; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 118336\n                                AND ID_ARTICULO = 118336; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = ARMADO_PC\n                                AND ID_ARTICULO = 22; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 102048\n                                AND ID_ARTICULO = 102048;] (SQL:   DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 111454\n                                AND ID_ARTICULO = 111454; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 116698\n                                AND ID_ARTICULO = 116698; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 101267\n                                AND ID_ARTICULO = 101267; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 116787\n                                AND ID_ARTICULO = 116787; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 103041\n                                AND ID_ARTICULO = 103041; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 117826\n                                AND ID_ARTICULO = 117826; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 118520\n                                AND ID_ARTICULO = 118520; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 117789\n                                AND ID_ARTICULO = 117789; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 118336\n                                AND ID_ARTICULO = 118336; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = ARMADO_PC\n                                AND ID_ARTICULO = 22; DELETE FROM [NewBytes_DBF].[dbo].[albclil]\n                                WHERE CNUMALB = '00570569'\n                                AND CREF = 102048\n                                AND ID_ARTICULO = 102048;)",
        "file": "\/var\/www\/app\/vendor\/laravel\/framework\/src\/Illuminate\/Database\/Connection.php",
        "line": 760
    }
}
```
