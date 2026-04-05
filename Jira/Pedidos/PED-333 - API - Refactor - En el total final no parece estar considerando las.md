---
jira_key: "PED-333"
aliases: ["PED-333"]
summary: "API - Refactor - En el total final no parece estar considerando las percpeciones, solo el iva"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-12-14 13:56"
updated: "2024-02-14 16:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-333"
---

# PED-333: API - Refactor - En el total final no parece estar considerando las percpeciones, solo el iva

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-14 13:56 |
| Actualizado | 2024-02-14 16:05 |
| Etiquetas | ninguna |
| Jira | [PED-333](https://bluinc.atlassian.net/browse/PED-333) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **relates to:** [[PED-342]] API - Listar ordenes de compra - Discrepancia en los totales finales

## Descripcion

Al ejecutar el siguiente recurso

```
curl 'https://api.orders.lio.red/v1/orders?currentPage=1&itemsPerPage=15&search=10334155&between=01-01-2023_14-12-2023' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDI1NzU2NTYsImF1ZCI6IjJjNDY0YjE5Yjg1ZDhlOTM1N2E4Yzc2ODFmZDUxMzBhMTE4MzZkYTQiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjB9LCJpYXQiOjE3MDI1NzIwNTYsIm5iZiI6MTcwMjU3MjA1Nn0.s1yokFCSAyc9dL6rmhXs1F88wZSc-sJf6yz3TBTMjvI' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://beta.pedidos.saftel.com' \
  -H 'Referer: https://beta.pedidos.saftel.com/orders?currentPage=1&itemsPerPage=15&search=10334155&between=01-01-2023_14-12-2023' \
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
    "response": [
        {
            "date": "2023-12-14 13:31:52",
            "orderNumber": "10334155",
            "branchNumber": "0002",
            "albnumNumber": "X000200569983",
            "realAlbumNumber": "00569983",
            "clientDescription": "SEGAL GABRIEL ALEJANDRO",
            "clientId": 32702,
            "orderTypeId": 2,
            "observation": "INTERNO",
            "status": "S",
            "statusDescription": "Remitido",
            "invoice": null,
            "token": null,
            "voucherId": null,
            "sellerId": 8,
            "seller": "Altamiranda Andrea",
            "totalInPesos": 1006792.5,
            "total": 958.85,
            "finalTotal": 1059.53,
            "shippingMethod": 0,
            "codePostal": "",
            "currency": 1050,
            "perception": 28.7655,
            "shippingLabel": false
        }
    ],
    "pagination": {
        "total": 1,
        "current": 1,
        "pageSize": 15
    }
}
```

El parametro `finalTotal` deberia ser 1088.29… Es decir hay que sumarle `perception` **siempre que no sea sucursal 10**
