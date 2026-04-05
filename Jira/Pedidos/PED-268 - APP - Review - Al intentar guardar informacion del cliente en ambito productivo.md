---
jira_key: "PED-268"
aliases: ["PED-268"]
summary: "APP - Review - Al intentar guardar informacion del cliente en ambito productivo se produce un fallo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-11-15 09:41"
updated: "2023-11-15 10:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-268"
---

# PED-268: APP - Review - Al intentar guardar informacion del cliente en ambito productivo se produce un fallo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-15 09:41 |
| Actualizado | 2023-11-15 10:20 |
| Etiquetas | ninguna |
| Jira | [PED-268](https://bluinc.atlassian.net/browse/PED-268) |

## Relaciones

- **Padre:** [[PED-16]] Listar clientes

## Descripcion

[adjunto]
```
{
    "errors": {
        "status": 500,
        "title": "Undefined array key \"clientCode\"",
        "file": "\/var\/www\/app\/app\/Services\/Client\/ClientUpdateService.php",
        "line": 141
    }
}
```

```
curl 'https://api.orders.lio.red/v1/clients/26806' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDAwNTUxMzUsImF1ZCI6IjMxODljYTgwZjYyNjNlZjljNTZhYzMzYTI4NWU3NGI1NTk1ZjNiZGQiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjB9LCJpYXQiOjE3MDAwNTE1MzUsIm5iZiI6MTcwMDA1MTUzNX0.UGfdstz9TIdEirey9r5Lz9uEHcBGk-_hF--QNDQMMfY' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://beta.pedidos.saftel.com' \
  -H 'Referer: https://beta.pedidos.saftel.com/clients?currentPage=1&itemsPerPage=100&search=mercurio' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"profile":3,"salespersonId":12,"currencyId":1,"companyCode":4}' \
  --compressed
```
