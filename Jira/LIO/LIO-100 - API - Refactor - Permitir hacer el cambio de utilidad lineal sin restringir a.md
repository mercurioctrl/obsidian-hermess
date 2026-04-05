---
jira_key: "LIO-100"
aliases: ["LIO-100"]
summary: "API - Refactor - Permitir hacer el cambio de utilidad lineal sin restringir a minUtility"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-23 09:52"
updated: "2024-10-04 12:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-100"
---

# LIO-100: API - Refactor - Permitir hacer el cambio de utilidad lineal sin restringir a minUtility

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-23 09:52 |
| Actualizado | 2024-10-04 12:17 |
| Etiquetas | ninguna |
| Jira | [LIO-100](https://bluinc.atlassian.net/browse/LIO-100) |

## Relaciones

- **Padre:** [[LIO-98]] Inventario resellers
- **has action item:** [[LIO-101]] APP - Refactor - Cambios de precio y utilidad en el inventario
- **relates to:** [[LIO-104]] API - Refactor - Guardar precio exacto de mi artículo 

## Descripcion

```
curl 'https://api.libreopcion.com/inventories/products/677552/list' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjp7ImlkIjoyLCJlbWFpbCI6Imhlcm1lc3M4N0BnbWFpbC5jb20iLCJub21icmUiOiJDYXRyaWVsIE1lcmN1cmlvIiwicGVyZmlsIjoidmVuZGVkb3IiLCJkb2N1bWVudG8iOiIzMzQ1Nzk2MiIsInRlbGVmb25vIjoiNC02MzYtMzQwNyIsImRpcmVjY2lvbiI6eyJjYWxsZSI6Ik1lZGluYSIsIm51bWVybyI6IjM1MSIsInBpc28iOiIxIiwiY2FzYUFwdG8iOiIzIn0sImNvZGlnb19wb3N0YWwiOiIxNDA4IiwiYXZhdGFyIjoxMiwiY2l1ZGFkIjp7ImlkIjoyMDgzMiwibm9tYnJlIjoiQ0FCQSIsInByb3ZpbmNpYV9pZCI6MSwidG90YWwiOjB9LCJwcm92aW5jaWEiOnsiaWQiOjEsImtleSI6MSwibm9tYnJlIjoiQ0FCQSIsInBhaXNfaWQiOjcsInRvdGFsIjowLCJjaXVkYWRfZGVmZWN0b19pZCI6MH0sInBhaXMiOnsiaWQiOjcsIm5vbWJyZSI6IkFSR0VOVElOQSIsInRvdGFsIjowfSwidGllbmRhX2lkIjoyNjgwNiwidmVuZGVkb3JfaWQiOjIyLCJ0b2tlblY0IjoiOEFDMDIwODgtODg2MS00MUMxLUE4NUUtMzQ1MkM0RUM0Q0E5In0sImlzcyI6ImxpYnJlb3BjaW9uLmNvbSIsImF1ZCI6ImxpYnJlb3BjaW9uLmNvbSIsImlhdCI6MTcyNTg5MzM4MiwibmJmIjoxNzI1ODkzMzgyfQ.Qqkxyce-wW9ZEr0GZ_wZI_IeifHr8mZIe3xb4CKtpuk' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://libreopcion.com' \
  -H 'Referer: https://libreopcion.com/catalogo?stockAvailability=1&statusActive=1&page=1&search=intel' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36' \
  -H 'ngrok-skip-browser-warning: true' \
  -H 'sec-ch-ua: "Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"utility":"24"}'
```
