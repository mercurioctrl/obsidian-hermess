---
jira_key: "COM-260"
aliases: ["COM-260"]
summary: "API - MVP - Refactor - al crear/editar un depósito se debe respetar el companyCode que se envía"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-12-16 14:15"
updated: "2025-12-17 13:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-260"
---

# COM-260: API - MVP - Refactor - al crear/editar un depósito se debe respetar el companyCode que se envía

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-12-16 14:15 |
| Actualizado | 2025-12-17 13:14 |
| Etiquetas | ninguna |
| Jira | [COM-260](https://bluinc.atlassian.net/browse/COM-260) |

## Relaciones

- **Padre:** [[COM-178]] Depositos
- **has action item:** [[COM-261]] APP - MVP - Refactor - agregar selector de companyCode cuando se crea/edita un depósito

## Descripcion

Hice una prueba enviando 


```
curl 'https://gamma.api.purchases.lio.red/v1/warehouses' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9,es-ES;q=0.8,es;q=0.7' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjU5MDY3NTIsImF1ZCI6ImY3MjQ3NTBhZjIzMGJiODc5M2EwODE1MmE3NGRiMmIxZTdjOTQ4YjgiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImNvbXByYXMiOiIxIiwicG0iOiIxIiwiY29tcGFueUNvZGUiOiI0In0sImlhdCI6MTc2NTkwMzE1MiwibmJmIjoxNzY1OTAzMTUyfQ.fTb2RnRuv1cnfVeITiMlRIOgGObGkMQ-avLqQflmbp8' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: http://localhost:3003' \
  -H 'Pragma: no-cache' \
  -H 'Referer: http://localhost:3003/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"name":"prueba electric","code":"ELE","address":"asdasdasd","countryId":8,"provinceId":null,"cityId":null,"default":true,"phone":"","companyCode":4}'
```

envie el companyCode 4 y recibí como respuesta del POST


```
{
    "success": true,
    "message": "Almacén creado correctamente",
    "data": {
        "id": 26,
        "code": "ELE",
        "name": "prueba electric",
        "address": "asdasdasd",
        "phone": "",
        "default": true,
        "cityCode": "",
        "cityId": 0,
        "cityName": "",
        "provinceId": 0,
        "provinceCode": 0,
        "provinceName": "",
        "countryDescription": "MexicoHH",
        "countryId": 8,
        "prefixFlag": "MX",
        "companyCode": 0 //-------------> no respeta el codigo
    }
}
```
