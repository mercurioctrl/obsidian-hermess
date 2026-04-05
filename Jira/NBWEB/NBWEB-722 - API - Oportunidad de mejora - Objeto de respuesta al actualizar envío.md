---
jira_key: "NBWEB-722"
aliases: ["NBWEB-722"]
summary: "API - Oportunidad de mejora - Objeto de respuesta al actualizar envío"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-04-23 23:12"
updated: "2024-05-08 12:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-722"
---

# NBWEB-722: API - Oportunidad de mejora - Objeto de respuesta al actualizar envío

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-23 23:12 |
| Actualizado | 2024-05-08 12:55 |
| Etiquetas | ninguna |
| Jira | [NBWEB-722](https://bluinc.atlassian.net/browse/NBWEB-722) |

## Relaciones

- **Padre:** [[NBWEB-498 - Oportunidades de mejora|NBWEB-498]] Oportunidades de mejora
- **relates to:** [[NBWEB-720 - API - Refactor - cms permitir actualizar en shipping method dropshipping|NBWEB-720]] API - Refactor - cms permitir actualizar en shipping method dropshipping
- **relates to:** [[NBWEB-730 - APP - CMS - Actualización de objeto de respuesta al actualizar envío|NBWEB-730]] APP - CMS - Actualización de objeto de respuesta al actualizar envío

## Descripcion

Oportunidad de mejora al objeto de respuesta al actualizar el medio de envío.

[adjunto]
```
curl 'https://gamma.api.nb.com.ar/v1/cms/shippingMethods' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTM5NjAyMjMsImF1ZCI6ImU2MjZjN2JkODM1MjI3ODNhMTljNzg5M2YwNTNiMWU3YjQyMjM1MTQiLCJ1c2VyIjp7ImlkIjoiNTMiLCJ1c3VhcmlvQWRtaW4iOiJzaXN0ZW1hcyIsInBhc3NBZG1pbiI6ImYzMzYzMGJjNTczODg5YWQwNGJmMjUxY2Y2NTMyZDI5IiwiY29ycmVvIjoiZW1hbnphbm9AbGlicmVvcGNpb24uY29tIiwidGlwbyI6ImFkbWluaXN0cmFkb3IiLCJjY29kYWdlIjoiMCIsIlVzdWFyaW9jYWphIjpudWxsLCJpcCI6bnVsbCwib3MiOm51bGwsImJyb3dzZXIiOm51bGwsInZlcnNpb24iOm51bGwsInVzZXJfYWdlbnQiOm51bGwsImNtc19sbyI6IjEiLCJjbXNfbmIiOm51bGwsImlkX2FkbWluIjoiNTMiLCJyZWd1bGFyaXphcl9zdG9jayI6IjEiLCJicmFuZCI6IjEiLCJiYW5uZXIiOiIxIiwicGF5bWVudE1ldGhvZHMiOiIxIiwiY2F0ZWdvcmllcyI6IjEiLCJzaGlwcGluZ01ldGhvZHMiOiIxIiwiY3VycmVuY3lRdW90ZSI6IjEiLCJkZWZhdWx0UGFyYW1ldGVycyI6IjEiLCJzdGFmZiI6IjEiLCJwYXltZW50TWV0aG9kVHJhZGUiOiIxIiwiY3VzdG9tZXIiOiIwIiwiY2FydCI6IjAiLCJwYXltZW50TWV0aG9kc0xPIjoiMSIsInNoaXBwaW5nTWV0aG9kc0xPIjoiMSIsImJhbm5lcnNMTyI6IjEiLCJjb3Vwb25zTE8iOiIxIiwiaGVscExPIjoiMSIsImdpZnRDYXJkc0xPIjoiMSIsImluc3RhbnRGbGFzaExPIjoiMSIsImNvZWZmaWNpZW50UmFua2luZ0xPIjoiMSJ9LCJpYXQiOjE3MTM5MjQyMjMsIm5iZiI6MTcxMzkyNDIyMywiY21zIjp0cnVlfQ.8MR06CotU_4UnwwxsNNle_wb_EtmSbHj7L95ku3j03I' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.cms-nbweb.saftel.com' \
  -H 'Referer: https://gamma.cms-nbweb.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"id":"4041","name":"OCA","description":"OCA a domicilio","active":1,"extraDayMin":"1","extraDayMax":"3","kmPrice":null,"minFee":null,"maxDistance":null,"insuredLimit":null,"activoDropshipping":false}'
```

Como sugerencias:

```
{"success": true, "message": ""}
```

```
{"status": "success", "message": ""}
```
