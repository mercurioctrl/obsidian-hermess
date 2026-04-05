---
jira_key: "COB-426"
aliases: ["COB-426"]
summary: "API - Oportunidad de mejora - Mejorar la latencia del recurso para que sea mas instantáneo en produ (mas o menos 1 seg)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-04-28 09:00"
updated: "2023-05-08 10:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-426"
---

# COB-426: API - Oportunidad de mejora - Mejorar la latencia del recurso para que sea mas instantáneo en produ (mas o menos 1 seg)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-28 09:00 |
| Actualizado | 2023-05-08 10:35 |
| Etiquetas | ninguna |
| Jira | [COB-426](https://bluinc.atlassian.net/browse/COB-426) |

## Relaciones

- **Padre:** [[COB-218]] Feat - Movimientos bancarios

## Descripcion

Se trata del recurso en producción, que tiene una demora de alrededor de 5 segundos y produce una sensación no tan buena al acceder varias veces al día para chequear informacion

```
GET {API_RUL}/v1/currentBankAccount/{BankId}
```

```shell
curl 'https://api.cashbox.lio.red/v1/currentBankAccount/7?itemsPerPage=15&currentPage=1&currency=1'   -H 'Accept: application/json, text/plain, */*'   -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6'   -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODI2OTM1NDIsImF1ZCI6ImY1M2UwMjU4ZDM1ZjY2MThjZjY1NDZiYTZlOTQ5MGMwZWU2YzQwNGUiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImNvYnJvIjoiMSIsImNvYnJvQWRtaW4iOiIxIiwiYWdlbnRJZCI6IjEyIiwiYm94IjoiU2ViYSIsIm1hbmFnZW1lbnQiOiIxIiwiZWRpdF9jcmVkaXQiOiIxIn0sImlhdCI6MTY4MjY4Mjc0MiwibmJmIjoxNjgyNjgyNzQyfQ.NuuKVLI33mrQ5NigoG-tVjW-y-cTIGrtQdqCRJxEB0Q'   -H 'Connection: keep-alive'   -H 'Origin: https://caja.saftel.com'   -H 'Referer: https://caja.saftel.com/banks'   -H 'Sec-Fetch-Dest: empty'   -H 'Sec-Fetch-Mode: cors'   -H 'Sec-Fetch-Site: cross-site'   -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'   -H 'sec-ch-ua: "Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"'   -H 'sec-ch-ua-mobile: ?0'   -H 'sec-ch-ua-platform: "Linux"'   --compressed
```
