---
jira_key: "PED-873"
aliases: ["PED-873"]
summary: "API - Refactor - Al intentar editar (seleccionar para editar) una orden SUC 3, no me deja hacerlo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-14 14:59"
updated: "2024-11-20 22:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-873"
---

# PED-873: API - Refactor - Al intentar editar (seleccionar para editar) una orden SUC 3, no me deja hacerlo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-14 14:59 |
| Actualizado | 2024-11-20 22:02 |
| Etiquetas | ninguna |
| Jira | [PED-873](https://bluinc.atlassian.net/browse/PED-873) |

## Relaciones

- **Padre:** [[PED-34]] Generar / Editar ordenes
- **has action item:** [[SNB-2535]] no podemos generar pedido para uso internos

## Descripcion

Este concepto de la sucursal 3 para postventa, sirve para que puedan generar ordenes, pero solo con el stock de la columna de postventa.

```
GET {API_URL}/v1/getEditOrderData/0003-1
```

```
curl 'https://api.orders.lio.red/v1/getEditOrderData/0003-1' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MzE2OTMzODUsImF1ZCI6ImY4ODVmNzUyZmU3MDQ3M2JmOGEwMTQ5M2FlNWY0Nzk4M2EzYzQ3YzMiLCJ1c2VyIjp7ImlkIjo2MDc0MiwiY29kZUZQIjoiMDQ2MDE5IiwiYWdlbnRJZCI6NTIsInVzdUlkZW50aWZpY2FjaW9uIjoiSlRBTUEiLCJyb2xlRGVzY3JpcHRpb24iOiJKZWZlIGRlIHNlcnZpY2lvIHBvc3QgdmVudGEiLCJwZWRpZG9zIjoxLCJwbSI6MCwiZGlzY291bnRTaGlwcGluZyI6MSwicmViaWxsIjowfSwiaWF0IjoxNzMxNjA2OTg1LCJuYmYiOjE3MzE2MDY5ODV9.MLol-BQ4HblNx4EcSRs22IpoYDcTXFbvk2_CBdbmVss' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://www.pedidos.saftel.com' \
  -H 'Referer: https://www.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```

```
{
    "errors": {
        "status": 500,
        "title": "La orden no existe",
        "file": "\/var\/www\/app\/app\/Services\/Order\/OrderService.php",
        "line": 359
    }
}
```
