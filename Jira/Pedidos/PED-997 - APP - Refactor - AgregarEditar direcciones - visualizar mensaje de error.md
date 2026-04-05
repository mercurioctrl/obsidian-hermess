---
jira_key: "PED-997"
aliases: ["PED-997"]
summary: "APP - Refactor - Agregar/Editar direcciones -> visualizar mensaje de error"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2025-05-06 10:30"
updated: "2025-07-15 10:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-997"
---

# PED-997: APP - Refactor - Agregar/Editar direcciones -> visualizar mensaje de error

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2025-05-06 10:30 |
| Actualizado | 2025-07-15 10:31 |
| Etiquetas | ninguna |
| Jira | [PED-997](https://bluinc.atlassian.net/browse/PED-997) |

## Relaciones

- **relates to:** [[SNB-3207]] BORRAR DOMICILIO DE ENVIO
- **relates to:** [[PED-30]] APP - Feat - Agregar/Editar direcciones

## Descripcion

Realizaremos una refactorización para poder visualizar el mensaje del back al intentar eliminar una dirección comprometida con un pedido en curso.

[adjunto]
```
curl ^"https://gamma.api.orders.lio.red/v1/shippingAddress/75980/39509^" ^
  -X DELETE ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: es-MX^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NTE0NzA2MDQsImF1ZCI6IjUwNTQ1YjgxYjk0YjZlNDk3NjhkZGEzZmM2ZTBjOTZiN2UzNTRmZTQiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicm9sZURlc2NyaXB0aW9uIjoiUHJvZHVjdCBNYW5hZ2VyIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MSwiaXNQbSI6MCwiaXNHZXJlbmNpYSI6MCwiZWRpdENvc3RGb3JTYWxlIjoxLCJwZWRfZnVsbF9iZW5lZml0cyI6MCwiZGVzbGlxdWlkYXIiOjEsInVubGltaXRlZFJlcG9ydHMiOjB9LCJpYXQiOjE3NTE0NjcwMDQsIm5iZiI6MTc1MTQ2NzAwNH0.jGTeUJZWYxBNInn-ZD6RQzD2XWSEGGZrNIMDUHG1WsE^" ^
  -H ^"Origin: https://gamma.pedidos.saftel.com^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://gamma.pedidos.saftel.com/^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: cross-site^" ^
  -H ^"Priority: u=0^"
```
