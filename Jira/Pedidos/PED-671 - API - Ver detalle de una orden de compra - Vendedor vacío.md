---
jira_key: "PED-671"
aliases: ["PED-671"]
summary: "API - Ver detalle de una orden de compra - Vendedor vacío"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-04-15 20:10"
updated: "2024-04-17 18:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-671"
---

# PED-671: API - Ver detalle de una orden de compra - Vendedor vacío

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-15 20:10 |
| Actualizado | 2024-04-17 18:53 |
| Etiquetas | ninguna |
| Jira | [PED-671](https://bluinc.atlassian.net/browse/PED-671) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra
- **relates to:** [[PED-82 - API - Feat - Ver detalle de una orden de compra|PED-82]] API - Feat - Ver detalle de una orden de compra
- **relates to:** [[SNB-1763 - FALTANTE DE DATOS|SNB-1763]] FALTANTE DE DATOS

## Descripcion

- Resultado obtenido: 



[adjunto]
- Pasos para replicar error: 

- Buscar en producción el detalle de la orden 0002-10344602




- Datos de la prueba: 



```
curl 'https://api.orders.lio.red/v1/orders/0002-10344602' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTMzMDY3OTksImF1ZCI6IjY3OGU3YjliZDQxMmVkNTA4NDk2MjMzZDMzOGY1Njk1Y2NiZWQ0YjgiLCJ1c2VyIjp7ImlkIjo2MzY2OCwiY29kZUZQIjoiNTU1NTQiLCJhZ2VudElkIjo1OSwidXN1SWRlbnRpZmljYWNpb24iOm51bGwsInBlZGlkb3MiOjEsInBtIjowLCJkaXNjb3VudFNoaXBwaW5nIjoxLCJyZWJpbGwiOjB9LCJpYXQiOjE3MTMyMjAzOTksIm5iZiI6MTcxMzIyMDM5OX0.ka5IybphzhvWEUfkPAyWZ7cnWl8isryW7kBtNvZeqoI' \
  -H 'Connection: keep-alive' \
  -H 'Origin: http://pedidos.saftel.com' \
  -H 'Referer: http://pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```

- Resultado esperado: 

- Se visualicen los parámetros del vendedor




- Posible solución:

- Convertir a entero para desaparecer posible discrepancia `pedclit.ccodage = 8, agentes.ccodage = 08`





[adjunto]
