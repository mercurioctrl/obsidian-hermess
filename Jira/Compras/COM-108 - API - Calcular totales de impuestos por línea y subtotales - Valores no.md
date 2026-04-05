---
jira_key: "COM-108"
aliases: ["COM-108"]
summary: "API - Calcular totales de impuestos por línea y subtotales - Valores no coincidentes"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-06-13 22:29"
updated: "2024-06-27 17:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-108"
---

# COM-108: API - Calcular totales de impuestos por línea y subtotales - Valores no coincidentes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-13 22:29 |
| Actualizado | 2024-06-27 17:03 |
| Etiquetas | ninguna |
| Jira | [COM-108](https://bluinc.atlassian.net/browse/COM-108) |

## Relaciones

- **Padre:** [[COM-8]] Ordenes de compra
- **blocks:** [[COM-103]] API - Refactor - Calcular totales de impuestos por linea y subtotales

## Descripcion

Algunos valores no coinciden

- `iibb` → 5 % de $100 = $5 


- `ganancias` → 10 % de $100 = $10


- `percentageItemTax` → 10 % + 5 % + 10 % + 5 % + 10 % + 5 %  + 10 %  + 5 %  = 60 %



```
GET {{API_URL}}/v1/totalTaxesProviderOrder
```

[adjunto]
```
curl 'https://gamma.api.purchases.lio.red/v1/totalTaxesProviderOrder/11071' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTgzMzAxMzAsImF1ZCI6ImE1YTMyZTRhYjk0NDVlMTJjMDAzZWVkNmZkZGZkYzU4ZDA1YmNjNjMiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsInBlZGlkb3MiOiIxIiwicG0iOiIxIn0sImlhdCI6MTcxODMyNjUzMCwibmJmIjoxNzE4MzI2NTMwfQ.1YEBPmCzEn3aPCjtoGy8BCejHuTx5xg53OvXWw0_Lj4' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.compras.saftel.com' \
  -H 'Referer: https://gamma.compras.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0' \
  -H 'sec-ch-ua: "Chromium";v="124", "Opera";v="110", "Not-A.Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```

---

- Realice de nuevo la prueba pero ahora agregando un nuevo articulo



- `iibb` → 10 % + 10 % = 20 %


- `ganancias` → 10 % + 10 % = 20 %


- `percentageItemTax` → 10 % + 10 % + 10 % + 10 % + 10 % + 10 %  + 10 %  + 10 %  = 80 %


- `totalItemTax` →  $10 + $10 + $10 + $10 + $10 + $10  + $10 + $10  = $80



[adjunto]
---

Actualización 25/06/24

Al realizar de nuevo la prueba

[adjunto]
