---
jira_key: "LIO-326"
aliases: ["LIO-326"]
summary: "API - Review - Opciones de compra con salida de error"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-22 09:02"
updated: "2025-04-22 13:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-326"
---

# LIO-326: API - Review - Opciones de compra con salida de error

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-22 09:02 |
| Actualizado | 2025-04-22 13:04 |
| Etiquetas | ninguna |
| Jira | [LIO-326](https://bluinc.atlassian.net/browse/LIO-326) |

## Relaciones

- **Padre:** [[LIO-119 - Inventario|LIO-119]] Inventario

## Descripcion

```
curl 'https://omega-api4.libreopcion.com.ar/v4/buyingOption' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NTc5ODMyMDYsImF1ZCI6IjhlMmUzZWNkZmMyZjZmYmQ5MWEyMDQ2OGU0Y2E3NmU4ZTM3ZmUyNWYiLCJ1c2VyIjp7ImlkIjoyLCJlbWFpbCI6Imhlcm1lc3M4N0BnbWFpbC5jb20iLCJub21icmUiOiJDYXRyaWVsIE1lcmN1cmlvbyIsInBlcmZpbCI6InZlbmRlZG9yIiwiZG9jdW1lbnRvIjoiMzM0NTc5NjIiLCJ0ZWxlZm9ubyI6IjQtNjM2LTM0MDciLCJkaXJlY2Npb24iOnsiY2FsbGUiOiJNZWRpbmEiLCJudW1lcm8iOiIzNTEiLCJwaXNvIjoiMSIsImNhc2FBcHRvIjoiMyJ9LCJjb2RpZ29Qb3N0YWwiOiIxNDA4IiwiYXZhdGFyIjoxMiwiY2l1ZGFkIjp7ImlkIjoyMDgzMiwibm9tYnJlIjoiQ0FCQSIsInByb3ZpbmNpYUlkIjoxfSwicHJvdmluY2lhIjp7ImlkIjoxLCJub21icmUiOiJDQUJBIiwicGFpc0lkIjo3LCJjaXVkYWREZWZlY3RvSWQiOjIwODMyfSwicGFpcyI6eyJpZCI6Nywibm9tYnJlIjoiQVJHRU5USU5BIn0sInRpZW5kYUlkIjoyNjgwNiwidmVuZGVkb3JJZCI6MjIsInRva2VuVjMiOiJleUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpJVXpJMU5pSjkuZXlKMWMzVmhjbWx2SWpwN0ltbGtJam95TENKbGJXRnBiQ0k2SW1obGNtMWxjM000TjBCbmJXRnBiQzVqYjIwaUxDSnViMjFpY21VaU9pSkRZWFJ5YVdWc0lFMWxjbU4xY21sdmJ5SXNJbkJsY21acGJDSTZJblpsYm1SbFpHOXlJaXdpWkc5amRXMWxiblJ2SWpvaU16TTBOVGM1TmpJaUxDSjBaV3hsWm05dWJ5STZJalF0TmpNMkxUTTBNRGNpTENKa2FYSmxZMk5wYjI0aU9uc2lZMkZzYkdVaU9pSk5aV1JwYm1FaUxDSnVkVzFsY204aU9pSXpOVEVpTENKd2FYTnZJam9pTVNJc0ltTmhjMkZCY0hSdklqb2lNeUo5TENKamIyUnBaMjlmY0c5emRHRnNJam9pTVRRd09DSXNJbUYyWVhSaGNpSTZNVElzSW1OcGRXUmhaQ0k2ZXlKcFpDSTZNakE0TXpJc0ltNXZiV0p5WlNJNklrTkJRa0VpTENKd2NtOTJhVzVqYVdGZmFXUWlPakVzSW5SdmRHRnNJam93ZlN3aWNISnZkbWx1WTJsaElqcDdJbWxrSWpveExDSnJaWGtpT2pFc0ltNXZiV0p5WlNJNklrTkJRa0VpTENKd1lXbHpYMmxrSWpvM0xDSjBiM1JoYkNJNk1Dd2lZMmwxWkdGa1gyUmxabVZqZEc5ZmFXUWlPakI5TENKd1lXbHpJanA3SW1sa0lqbzNMQ0p1YjIxaWNtVWlPaUpCVWtkRlRsUkpUa0VpTENKMGIzUmhiQ0k2TUgwc0luUnBaVzVrWVY5cFpDSTZNalk0TURZc0luWmxibVJsWkc5eVgybGtJam95TWl3aWRHOXJaVzVXTkNJNklrSXlNek0wUTBaRExUaEJRVFV0TkVaRlJDMDRPVFEyTFVRM056QTJRMEUxT0RSQlFpSXNJbU52WkdsbmIxOXdiM04wWVd4ZlpHVm1ZWFZzZENJNk1UUXdOMzBzSW1semN5STZJbXhwWW5KbGIzQmphVzl1TG1OdmJTSXNJbUYxWkNJNklteHBZbkpsYjNCamFXOXVMbU52YlNJc0ltbGhkQ0k2TVRjME5UQXlNekl3Tml3aWJtSm1Jam94TnpRMU1ESXpNakEyZlEuRk5ZRndWY1ZRS1kzWlNreHB6T0pjUTNaNi1iZnphbUVjTmY2SmVVcVQzUSIsImNvZGlnb1Bvc3RhbERlZmF1bHQiOjE0MDd9LCJpYXQiOjE3NDUwMjMyMDYsIm5iZiI6MTc0NTAyMzIwNn0.YiFX_inivi57-KQy6HDW2cmWFCPs-OfhiSv9_9TKkTc' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://libreopcion.com.ar' \
  -H 'Referer: https://libreopcion.com.ar/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"order":"asc","limit":50,"offset":0,"payload":[103094],"about":1}'
```

[adjunto]
