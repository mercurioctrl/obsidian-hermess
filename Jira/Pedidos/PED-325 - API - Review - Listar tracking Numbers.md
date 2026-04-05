---
jira_key: "PED-325"
aliases: ["PED-325"]
summary: "API - Review - Listar tracking Numbers"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-12-12 10:16"
updated: "2023-12-14 16:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-325"
---

# PED-325: API - Review - Listar tracking Numbers

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-12 10:16 |
| Actualizado | 2023-12-14 16:46 |
| Etiquetas | ninguna |
| Jira | [PED-325](https://bluinc.atlassian.net/browse/PED-325) |

## Relaciones

- **Padre:** [[PED-58 - Agregar Editar Envío en las ordenes de compra|PED-58]] Agregar / Editar Envío en las ordenes de compra

## Descripcion

Existen pedidos que tienen seguimiento, pero que al ejecutar el recurso para mostrarlo, no los trae.

Se deja un ejemplo a continuación.

```
curl 'https://api.orders.lio.red/v1/orders/X000200569795/trackingNumbers' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDIzOTA0NDAsImF1ZCI6IjJjNDY0YjE5Yjg1ZDhlOTM1N2E4Yzc2ODFmZDUxMzBhMTE4MzZkYTQiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjB9LCJpYXQiOjE3MDIzODY4NDAsIm5iZiI6MTcwMjM4Njg0MH0.NPoWoG8PJdahFKWNIzXjYUoKvLrZWruxDJ9IB9NJzsA' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://beta.pedidos.saftel.com' \
  -H 'Referer: https://beta.pedidos.saftel.com/orders?currentPage=1&itemsPerPage=15&search=00569795' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```
