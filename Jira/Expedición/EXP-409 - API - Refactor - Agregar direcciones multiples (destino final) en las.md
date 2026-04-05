---
jira_key: "EXP-409"
aliases: ["EXP-409"]
summary: "API - Refactor - Agregar direcciones multiples (destino final) en las direcciones del cliente para UNA ORDEN DETERMINADA"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-04-19 12:13"
updated: "2024-04-21 22:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-409"
---

# EXP-409: API - Refactor - Agregar direcciones multiples (destino final) en las direcciones del cliente para UNA ORDEN DETERMINADA

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-19 12:13 |
| Actualizado | 2024-04-21 22:11 |
| Etiquetas | ninguna |
| Jira | [EXP-409](https://bluinc.atlassian.net/browse/EXP-409) |

## Relaciones

- **Padre:** [[EXP-13 - Feat - Etiquetas y seguimiento|EXP-13]] Feat - Etiquetas y seguimiento
- **blocks:** [[EXP-410 - APP - Refactor - Modificar el modal de generar etiqueta para el multidestino|EXP-410]] APP - Refactor - Modificar el modal de generar etiqueta para el multidestino

## Descripcion

Se refactorizara el recurso para poder obtener (solo cuando tiene ambas) la dirección inicial y la final.

La inicial, se marca igual que se marca ahora la favorita para la orden cuando tiene una sola ( "selectedInOrder": "1")

La secundaria, se marca como 2  ( "selectedInOrder": "2")

```
GET /v1/shipments/getAddress
```

```
[
    {
        "localidad": "CIUDAD DE BUENOS AIRES",
        "direccion": "alguna de prueba 124",
        "alphaCode": "BSAS",
        "telefono": "1530510267",
        "provincia": "CAPITAL FEDERAL ( CAP. FED. )",
        "codigoPostal": "1407",
        "idDirCli": "18063",
        "predeterminado": null,
        "selectedInOrder": "0"
    },
    {
        "localidad": "AGUA PINTADA",
        "direccion": "Direccion de prueba 234",
        "alphaCode": "0143",
        "telefono": "1540329485",
        "provincia": "CORDOBA",
        "codigoPostal": "5000",
        "idDirCli": "19140",
        "predeterminado": null,
        "selectedInOrder": "0"
    },
    {
        "localidad": "MAR DEL PLATA",
        "direccion": "Direccion de pruba",
        "alphaCode": "D470",
        "telefono": "423434",
        "provincia": "BUENOS AIRES ( BS. AS )",
        "codigoPostal": "4324",
        "idDirCli": "19149",
        "predeterminado": null,
        "selectedInOrder": "0"
    },
    {
        "localidad": "CIUDAD DE BUENOS AIRES",
        "direccion": "Medina 351",
        "alphaCode": "BSAS",
        "telefono": "1130510267",
        "provincia": "CAPITAL FEDERAL ( CAP. FED. )",
        "codigoPostal": "1407",
        "idDirCli": "25976",
        "predeterminado": null,
        "selectedInOrder": "0" <------------
    },
    {
        "localidad": "CIUDAD DE BUENOS AIRES",
        "direccion": "Prueba destino uno 145",
        "alphaCode": "BSAS",
        "telefono": "1130510267",
        "provincia": "CAPITAL FEDERAL ( CAP. FED. )",
        "codigoPostal": "1407",
        "idDirCli": "32541",
        "predeterminado": null,
        "selectedInOrder": "1" <------------
    },
    {
        "localidad": "ACOLLARADO",
        "direccion": "Prueba destino dos 123",
        "alphaCode": "0045",
        "telefono": "1130510267",
        "provincia": "CORDOBA",
        "codigoPostal": "3000",
        "idDirCli": "32542",
        "predeterminado": "32542",
        "selectedInOrder": "2" <------
    }
]
```

```
curl 'https://gamma.api.warehouse.lio.red/v1/shipments/getAddress?clientId=26806&branch=0002&order=10332720' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTM1NzM2NzksImF1ZCI6IjI1OGZlM2UwYjc4MTQwNjMzNzM3ZDM3OTkyMjQ1MTYzZTllYWYzMGMiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImV4cGVkaWNpb24iOiIxIiwiZXhwZWRpY2lvbkFkbWluIjoiMSIsIm1hbmFnZW1lbnQiOiIxIiwiZXhwX3VwbG9hZF9zZXJpYWxzIjoiMSJ9LCJpYXQiOjE3MTM1MzczNzksIm5iZiI6MTcxMzUzNzM3OX0.Pc4iNGpqkNaL5yfuUc0jc3r9j2i_7gjDI3zBP3p8xw4' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.expedicion.saftel.com' \
  -H 'Referer: https://gamma.expedicion.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```
