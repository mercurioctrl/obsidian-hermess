---
jira_key: "LIO-398"
aliases: ["LIO-398"]
summary: "API - Review - Verificar ganancia de meses anteriores en cuentas de vendedores, parecen no traer resultados"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-30 08:30"
updated: "2025-08-13 10:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-398"
---

# LIO-398: API - Review - Verificar ganancia de meses anteriores en cuentas de vendedores, parecen no traer resultados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-30 08:30 |
| Actualizado | 2025-08-13 10:46 |
| Etiquetas | ninguna |
| Jira | [LIO-398](https://bluinc.atlassian.net/browse/LIO-398) |

## Relaciones

- **Padre:** [[LIO-397]] Pagos de Ganancias y Comisiones

## Descripcion

Revisando algunas cuentas note que dejo de reportar meses pasado al consultar el recurso de legacy de la siguiente manera 

```
curl 'https://omega-api.libreopcion.com.ar/liquidaciones/meses-previos' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjp7ImlkIjo0ODQ1LCJlbWFpbCI6IkdlYXJzU3RvcmVTYW50YWZlQGdtYWlsLmNvbSIsIm5vbWJyZSI6IkdlYXJzIFN0b3JlIiwicGVyZmlsIjoidmVuZGVkb3IiLCJkb2N1bWVudG8iOiIzNTgzMjcxOCIsInRlbGVmb25vIjoiMzQyNTc4OTUyMyIsImRpcmVjY2lvbiI6eyJjYWxsZSI6InNhbnRpYWdvIGRlbCBlc3Rlcm8iLCJudW1lcm8iOiIyOTUxIiwicGlzbyI6IlVuaWNhIGNhc2EiLCJjYXNhQXB0byI6IkNhc2EifSwiY29kaWdvX3Bvc3RhbCI6IjE0MDciLCJhdmF0YXIiOjQ1LCJjaXVkYWQiOnsiaWQiOjE4MjE3LCJub21icmUiOiJTQU5UTyBUT01FIiwicHJvdmluY2lhX2lkIjoxNywidG90YWwiOjB9LCJwcm92aW5jaWEiOnsiaWQiOjE3LCJrZXkiOjE3LCJub21icmUiOiJTQU5UQSBGRSIsInBhaXNfaWQiOjcsInRvdGFsIjowLCJjaXVkYWRfZGVmZWN0b19pZCI6MH0sInBhaXMiOnsiaWQiOjcsIm5vbWJyZSI6IkFSR0VOVElOQSIsInRvdGFsIjowfSwidGllbmRhX2lkIjoyNTI3MiwidmVuZGVkb3JfaWQiOjQ0NywidG9rZW5WNCI6IjQ2N0E3QkMyLUJCQUUtNDU1Qy04M0RGLTlCQzY0QkNBOERDNiIsImNvZGlnb19wb3N0YWxfZGVmYXVsdCI6MTIyOSwiYWN0aXZlV2FsbGV0IjpmYWxzZX0sImlzcyI6ImxpYnJlb3BjaW9uLmNvbSIsImF1ZCI6ImxpYnJlb3BjaW9uLmNvbSIsImlhdCI6MTc1Mzg3NDc0NCwibmJmIjoxNzUzODc0NzQ0fQ.ZeJGcTuDhcbsEtYKYoEKMiPf8zDEpdXaK2RCiCwCsfw' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://libreopcion.com.ar' \
  -H 'Referer: https://libreopcion.com.ar/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```

Estoy seguro que debe tener que ver con algo de la query o algún cambio de como estas se marcan.

Por ejemplo, en el caso de Squaglia, las unicas que veo son de Febreroo 2020

[adjunto]
