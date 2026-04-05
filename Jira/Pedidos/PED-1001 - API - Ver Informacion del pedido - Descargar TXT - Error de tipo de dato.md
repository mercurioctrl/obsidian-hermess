---
jira_key: "PED-1001"
aliases: ["PED-1001"]
summary: "API - Ver Informacion del pedido -> Descargar TXT - Error de tipo de dato"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-05-08 11:26"
updated: "2025-05-09 09:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1001"
---

# PED-1001: API - Ver Informacion del pedido -> Descargar TXT - Error de tipo de dato

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-05-08 11:26 |
| Actualizado | 2025-05-09 09:46 |
| Etiquetas | ninguna |
| Jira | [PED-1001](https://bluinc.atlassian.net/browse/PED-1001) |

## Relaciones

- **relates to:** [[PED-77]] API - Feat - Descargar txt en Ver Informacion del pedido

## Descripcion

Al intentar descargar el archivo de texto, me aparece el siguiente error:

```
curl 'https://gamma.api.orders.lio.red/v1/download/0002-10356467/txt' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: es-MX' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDY3MTQwNDIsImF1ZCI6ImM2YmNhZTQzMDJlNTU0ZDVjZjc2NmEwOWJmMDRjZDdlMzM1ZWQ3NTQiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicm9sZURlc2NyaXB0aW9uIjoiUHJvZHVjdCBNYW5hZ2VyIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MSwiaXNQbSI6MCwiaXNHZXJlbmNpYSI6MCwiZWRpdENvc3RGb3JTYWxlIjoxLCJwZWRfZnVsbF9iZW5lZml0cyI6MCwiZGVzbGlxdWlkYXIiOjEsInVubGltaXRlZFJlcG9ydHMiOjB9LCJpYXQiOjE3NDY3MTA0NDIsIm5iZiI6MTc0NjcxMDQ0Mn0.NheSF7uZYRBLBrt9Q8jvTj3LBhmQRWoBX51lSIrLa3I' -H 'Origin: https://gamma.pedidos.saftel.com' -H 'Connection: keep-alive' -H 'Referer: https://gamma.pedidos.saftel.com/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: cross-site' -H 'Priority: u=0'
```

[adjunto]
