---
jira_key: "POS-81"
summary: "API - Test - Revisar el fallo al intentar definir una solucion tecnica"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-23 16:32"
updated: "2022-10-11 10:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-81"
---

# POS-81: API - Test - Revisar el fallo al intentar definir una solucion tecnica

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-23 16:32 |
| Actualizado | 2022-10-11 10:21 |
| Etiquetas | ninguna |
| Jira | [POS-81](https://bluinc.atlassian.net/browse/POS-81) |

## Descripción

Al hacer

```
curl 'https://gamma.api.aftersale.lio.red/v1/afterSales/32124/49548' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjEzNjczNDIsImF1ZCI6IjkyZjlhNmRhZTBhYzRkNDE1YTBjMzRhMTdjMjE1NjFjYmVhYTcxNDAiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjI1NDMzIiwicG9zdHZlbnRhIjoiMSIsInBvc3R2ZW50YV9jcmVkaXRvcyI6IjEiLCJhZ2VudElkIjoiMTIiLCJwb3N0dmVudGFfc29sdWNpb24iOiIwIiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIn0sImlhdCI6MTY2MTI4MDk0MiwibmJmIjoxNjYxMjgwOTQyfQ.2vPH0I9rZkJr_7L-XPqzo5V96CsXmFuJpSpkPYEldSE' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: http://gamma.postventa.saftel.com' \
  -H 'Referer: http://gamma.postventa.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"testProductStatusId":2}' \
  --compressed
```

Me retorna 

```json
{
    "message": "Slim Application Error",
    "exception": [
        {
            "type": "Error",
            "code": 0,
            "message": "Class \"App\\Controller\\Exception\" not found",
            "file": "/var/www/app/src/Controller/AfterSaleController.php",
            "line": 477
        }
    ]
}
```
