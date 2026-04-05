---
jira_key: "PED-627"
aliases: ["PED-627"]
summary: "  API - Generar reporte de stock y ventas por producto - Filtrado por fechas no coincidente "
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-03-21 15:15"
updated: "2024-04-18 21:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-627"
---

# PED-627:   API - Generar reporte de stock y ventas por producto - Filtrado por fechas no coincidente 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-03-21 15:15 |
| Actualizado | 2024-04-18 21:18 |
| Etiquetas | ninguna |
| Jira | [PED-627](https://bluinc.atlassian.net/browse/PED-627) |

## Relaciones

- **Padre:** [[PED-149 - Reportes|PED-149]] Reportes
- **relates to:** [[PED-215 - API - Feat - Generar reporte de stock y ventas por producto|PED-215]] API - Feat - Generar reporte de stock y ventas por producto
- **relates to:** [[SNB-1653 - datos faltantes en reportes|SNB-1653]] datos faltantes en reportes

## Descripcion

Al filtrar por fechas y marca, no se aplica el filtrado de fechas.

[adjunto]
[adjunto]
```
curl 'https://gamma.api.orders.lio.red/v1/reports/stocks?sellerId=12&brandId=65&currentPage=1&between=20-2-2024_21-3-2024' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,es-MX;q=0.4' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTEwNDc2NTQsImF1ZCI6ImQ3MzUwMjI3ZDRjN2FmMTUyMWIxY2Y2YTIxZTY0ZDUwODkwZDI2YjkiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjF9LCJpYXQiOjE3MTEwNDQwNTQsIm5iZiI6MTcxMTA0NDA1NH0.4F5wMS_FNsJRmUpTA-jJ4U4sD3joU7-gD7ZZTO7fbqk' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0' \
  -H 'sec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```

---

Actualización 05/04/24
No aparece ningún registro

[adjunto]
[adjunto]
