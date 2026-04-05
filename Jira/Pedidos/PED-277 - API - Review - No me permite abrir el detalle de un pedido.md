---
jira_key: "PED-277"
aliases: ["PED-277"]
summary: "API - Review - No me permite abrir el detalle de un pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-11-23 08:02"
updated: "2023-11-23 09:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-277"
---

# PED-277: API - Review - No me permite abrir el detalle de un pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-23 08:02 |
| Actualizado | 2023-11-23 09:25 |
| Etiquetas | ninguna |
| Jira | [PED-277](https://bluinc.atlassian.net/browse/PED-277) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra

## Descripcion

```
curl 'https://api.orders.lio.red/v1/orders/0002-10332631' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDA3NDA2MzYsImF1ZCI6IjJjNDY0YjE5Yjg1ZDhlOTM1N2E4Yzc2ODFmZDUxMzBhMTE4MzZkYTQiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjB9LCJpYXQiOjE3MDA3MzcwMzYsIm5iZiI6MTcwMDczNzAzNn0.Iocdryc-9oiCHZVkqA5-qooQEqh_3Z1ZB_ln0y_V0OY' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://beta.pedidos.saftel.com' \
  -H 'Referer: https://beta.pedidos.saftel.com/orders?search=mercurio' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```

```
{
    "errors": {
        "status": 500,
        "title": "Undefined array key 0",
        "file": "\/var\/www\/app\/app\/Dto\/Order\/OrderDetailDto.php",
        "line": 31
    }
}
```
