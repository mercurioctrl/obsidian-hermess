---
jira_key: "SNB-2336"
aliases: ["SNB-2336"]
summary: "LIO - API - No deja ver la reputación en \"mi cuenta\" para los vendedores"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-23 09:39"
updated: "2024-09-26 14:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-2336"
---

# SNB-2336: LIO - API - No deja ver la reputación en "mi cuenta" para los vendedores

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-23 09:39 |
| Actualizado | 2024-09-26 14:15 |
| Etiquetas | ninguna |
| Jira | [SNB-2336](https://bluinc.atlassian.net/browse/SNB-2336) |

## Relaciones

*Sin relaciones*

## Descripcion

Estoy teniendo algun problema para obtener la reputacion en la seccion “Mi cuenta” de libre opcion.
Tal vez solo se trate de que el usuario esta shadowbaneado o desactivado, pero igual debería poder verla, ya que una cosa no se relaciona a la otra. 

```
curl 'https://api.libreopcion.com/vendedores/ficha/22' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjp7ImlkIjoyLCJlbWFpbCI6Imhlcm1lc3M4N0BnbWFpbC5jb20iLCJub21icmUiOiJDYXRyaWVsIE1lcmN1cmlvIiwicGVyZmlsIjoidmVuZGVkb3IiLCJkb2N1bWVudG8iOiIzMzQ1Nzk2MiIsInRlbGVmb25vIjoiNC02MzYtMzQwNyIsImRpcmVjY2lvbiI6eyJjYWxsZSI6Ik1lZGluYSIsIm51bWVybyI6IjM1MSIsInBpc28iOiIxIiwiY2FzYUFwdG8iOiIzIn0sImNvZGlnb19wb3N0YWwiOiIxNDA4IiwiYXZhdGFyIjoxMiwiY2l1ZGFkIjp7ImlkIjoyMDgzMiwibm9tYnJlIjoiQ0FCQSIsInByb3ZpbmNpYV9pZCI6MSwidG90YWwiOjB9LCJwcm92aW5jaWEiOnsiaWQiOjEsImtleSI6MSwibm9tYnJlIjoiQ0FCQSIsInBhaXNfaWQiOjcsInRvdGFsIjowLCJjaXVkYWRfZGVmZWN0b19pZCI6MH0sInBhaXMiOnsiaWQiOjcsIm5vbWJyZSI6IkFSR0VOVElOQSIsInRvdGFsIjowfSwidGllbmRhX2lkIjoyNjgwNiwidmVuZGVkb3JfaWQiOjIyLCJ0b2tlblY0IjoiOEFDMDIwODgtODg2MS00MUMxLUE4NUUtMzQ1MkM0RUM0Q0E5In0sImlzcyI6ImxpYnJlb3BjaW9uLmNvbSIsImF1ZCI6ImxpYnJlb3BjaW9uLmNvbSIsImlhdCI6MTcyNTg5MzM4MiwibmJmIjoxNzI1ODkzMzgyfQ.Qqkxyce-wW9ZEr0GZ_wZI_IeifHr8mZIe3xb4CKtpuk' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://libreopcion.com' \
  -H 'Referer: https://libreopcion.com/compra/preguntas?p=1&estado=todas' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36' \
  -H 'ngrok-skip-browser-warning: true' \
  -H 'sec-ch-ua: "Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```
