---
jira_key: "LIO-164"
aliases: ["LIO-164"]
summary: "API - Feat - Migrar recurso para actualizar punto de entrega"
status: "Backlog"
type: "Subtarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2024-12-10 16:26"
updated: "2024-12-10 16:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-164"
---

# LIO-164: API - Feat - Migrar recurso para actualizar punto de entrega

| Campo | Valor |
|-------|-------|
| Estado | Backlog (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-10 16:26 |
| Actualizado | 2024-12-10 16:30 |
| Etiquetas | ninguna |
| Jira | [LIO-164](https://bluinc.atlassian.net/browse/LIO-164) |

## Relaciones

- **Padre:** [[LIO-162 - Mejoras generales para envios|LIO-162]] Mejoras generales para envios
- **has action item:** [[LIO-163 - APP - Refactor - Cambiar herramienta para cotizacion|LIO-163]] APP - Refactor - Cambiar herramienta para cotizacion

## Descripcion

Migraremos el recurso directamente a v4

```
PATCH {API_V4}/{{API_URL}}/v4/user/deliveryAddress
```

```
{
  "zipCode":"1407" <-- puede enviar solo ete parametro
}
```

```
curl 'https://api.libreopcion.com.ar/auth/update-data' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjp7ImlkIjoyLCJlbWFpbCI6Imhlcm1lc3M4N0BnbWFpbC5jb20iLCJub21icmUiOiJDYXRyaWVsIE1lcmN1cmlvIiwicGVyZmlsIjoidmVuZGVkb3IiLCJkb2N1bWVudG8iOiIzMzQ1Nzk2MiIsInRlbGVmb25vIjoiNC02MzYtMzQwNyIsImRpcmVjY2lvbiI6eyJjYWxsZSI6Ik1lZGluYSIsIm51bWVybyI6IjM1MSIsInBpc28iOiIxIiwiY2FzYUFwdG8iOiIzIn0sImNvZGlnb19wb3N0YWwiOiIxNDA3IiwiYXZhdGFyIjoxMiwiY2l1ZGFkIjp7ImlkIjoyMDgzMiwibm9tYnJlIjoiQ0FCQSIsInByb3ZpbmNpYV9pZCI6MSwidG90YWwiOjB9LCJwcm92aW5jaWEiOnsiaWQiOjEsImtleSI6MSwibm9tYnJlIjoiQ0FCQSIsInBhaXNfaWQiOjcsInRvdGFsIjowLCJjaXVkYWRfZGVmZWN0b19pZCI6MH0sInBhaXMiOnsiaWQiOjcsIm5vbWJyZSI6IkFSR0VOVElOQSIsInRvdGFsIjowfSwidGllbmRhX2lkIjoyNjgwNiwidmVuZGVkb3JfaWQiOjIyLCJ0b2tlblY0IjoiQzMzRDM2RDktMDQyMS00MUE0LTlENUQtMENFRDhENkFCQTcwIn0sImlzcyI6ImxpYnJlb3BjaW9uLmNvbSIsImF1ZCI6ImxpYnJlb3BjaW9uLmNvbSIsImlhdCI6MTczMzQxMzA5MSwibmJmIjoxNzMzNDEzMDkxfQ.r3usPJpr8EXRi4gHamapb0W_2sHEjcgpGj16JvXOhU0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://libreopcion.com.ar' \
  -H 'Referer: https://libreopcion.com.ar/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"codigo_postal":"1407","calle":"Medina","numero":"351","piso":"1","casaApto":"3","ciudad":20832,"provincia":1,"tienda_id":26806}'
```
