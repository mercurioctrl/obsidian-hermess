---
jira_key: "LOCAPP-100"
summary: "API - Review - Problemas al emitir comprobantes luego del despliegue"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-27 07:59"
updated: "2026-02-11 13:38"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-100"
---

# LOCAPP-100: API - Review - Problemas al emitir comprobantes luego del despliegue

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-27 07:59 |
| Actualizado | 2026-02-11 13:38 |
| Etiquetas | esperandoDependencia |
| Jira | [LOCAPP-100](https://bluinc.atlassian.net/browse/LOCAPP-100) |

## Descripción

Error 500 al obtener tipos de comprobante al crear voucher (getVoucherType → ms-comprobantes)

**Descripción**
Al consumir el endpoint


```
GET /v1/getVoucherType?search={text}&clientId={id}
```


El backend responde **HTTP 500**.

El error se origina en una llamada interna al microservicio **ms-comprobantes**, específicamente al endpoint:

```
GET /v2/clientByCreateVoucher/{clientId}?voucherDescription={search}
```

La respuesta del microservicio devuelve un **500 Internal Server Error** con el mensaje:

```
syntax error, unexpected token "private"
```



El ejemplo en cuestión es (en este momento en produ o puede reproducirse porque volvimos a una versión anterior pero es lo que esta en development)

```
curl 'https://api.orders.lio.red/v1/getVoucherType?search=factura&clientId=95966' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3Njk1MTQzNTYsImF1ZCI6IjE2NWZhZjNlNjg1YTQzN2Y4NmU3MmQ4ODQwNGYzOTNmZDU4ODUyODMiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicm9sZURlc2NyaXB0aW9uIjoiQWRtaW5pc3RyYWRvciIsInBlZGlkb3MiOjEsInBtIjoxLCJkaXNjb3VudFNoaXBwaW5nIjoxLCJyZWJpbGwiOjEsImlzUG0iOjEsImlzR2VyZW5jaWEiOjEsImVkaXRDb3N0Rm9yU2FsZSI6MCwicGVkX2Z1bGxfYmVuZWZpdHMiOjEsImRlc2xpcXVpZGFyIjoxLCJ1bmxpbWl0ZWRSZXBvcnRzIjpudWxsLCJjcmVhdGVNYW51YWxWb3VjaGVyIjoxLCJiYW5MaXN0UHJpY2UiOiI1LDQsNiIsInVubG9ja2VkU2VsbGVyRmlsdGVyIjoxLCJ1c2VTdG9ja0luY29taW5nIjpudWxsLCJ1bmxvY2tlZENvbXBhbnlGaWx0ZXIiOjEsIm1hcmtldGluZ0Z1bmRzIjoxLCJjb21wYW55Q29kZSI6bnVsbH0sImlhdCI6MTc2OTQyNzk1NiwibmJmIjoxNzY5NDI3OTU2fQ.rhU_oml-Y56T9yVCdp6tDh0JAfX_eSVwugf9qKZqMCg' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://www.pedidos.saftel.com' \
  -H 'Referer: https://www.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```

```
{
    "errors": {
        "status": 500,
        "title": "Server error: `GET http:\/\/ms-comprobantes.lio.red\/v2\/clientByCreateVoucher\/95968?voucherDescription=factura` resulted in a `500 Internal Server Error` response:\n\"syntax error, unexpected token \\\"private\\\"\"\n",
        "file": "\/var\/www\/app\/vendor\/guzzlehttp\/guzzle\/src\/Exception\/RequestException.php",
        "line": 113
    }
}
```

---

Un problema similar (quizás el mismo) se observa al ejecutar (en este momento en produ o puede reproducirse porque volvimos a una versión anterior pero es lo que esta en development)

```
curl 'https://api.warehouse.lio.red/v1/makeVoucher' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3Njk5Mjk1NzQsImF1ZCI6ImFiNjYyYjlmNTRhMGZjYzRkMjVlMTBjNGRmMTRkYTVjN2MxMWQ0M2MiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImV4cGVkaWNpb24iOiIxIiwiZXhwZWRpY2lvbkFkbWluIjoiMSIsIm1hbmFnZW1lbnQiOiIxIiwiZXhwX3VwbG9hZF9zZXJpYWxzIjoiMSIsImV4cF9pdGVtcyI6IjEiLCJjb21wYW55Q29kZSI6bnVsbH0sImlhdCI6MTc2OTEwMTU3NCwibmJmIjoxNzY5MTAxNTc0fQ.qPn61WJcJFX8RXLhlrZYkDagUQPrvyURnCB3bQczGzU' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://expedicion.saftel.com' \
  -H 'Referer: https://expedicion.saftel.com/pickUp?currentPage=1&itemsPerPage=300&status=2,1' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"clientId":91245,"pedido":"X000200633172","iibbPerception":"0.00"}'
```

Que devuelve

```
<br />
<b>Warning</b>:  Undefined array key "voucherTypeId" in <b>/var/www/app/src/Controller/Voucher/MakeVoucher.php</b> on line <b>62</b><br />
<br />
<b>Warning</b>:  Attempt to read property "dataAfip" on string in <b>/var/www/app/src/Controller/Voucher/MakeVoucher.php</b> on line <b>75</b><br />
<br />
<b>Warning</b>:  Attempt to read property "CAE" on null in <b>/var/www/app/src/Controller/Voucher/MakeVoucher.php</b> on line <b>75</b><br />
"No se pudo crear el comprobante"
```
