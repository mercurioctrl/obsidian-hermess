---
jira_key: "NBWEB-710"
aliases: ["NBWEB-710"]
summary: "API - Registrar usuario - Fecha no guardada"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-04-15 17:41"
updated: "2024-04-17 20:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-710"
---

# NBWEB-710: API - Registrar usuario - Fecha no guardada

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-15 17:41 |
| Actualizado | 2024-04-17 20:08 |
| Etiquetas | ninguna |
| Jira | [NBWEB-710](https://bluinc.atlassian.net/browse/NBWEB-710) |

## Relaciones

- **Padre:** [[NBWEB-602 - Sitio Web|NBWEB-602]] Sitio Web
- **relates to:** [[NBWEB-676 - API - Agregar agregar direccion, codigo postal y whatsapp en el registro de un|NBWEB-676]] API - Agregar agregar direccion, codigo postal y whatsapp en el registro de un cliente y que se pueda levantar en PED
- **relates to:** [[NBWEB-709 - APP - Registrar usuario - Teléfono invalido|NBWEB-709]] APP - Registrar usuario - Teléfono invalido

## Descripcion

- Resultado obtenido: 



[adjunto]
- Pasos para replicar error: 



Registrar un usuario en el sitio de NB.

- Datos de la prueba: 



```
curl 'https://gamma.api.orders.lio.red/v1/clientsRequests?full=true' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTMyMTUzMTYsImF1ZCI6IjZjMTg3OTIzY2NiZTdlNTJiNWQyZThkNDhiYTFjZDg5M2YzZjY2MGEiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MX0sImlhdCI6MTcxMzIxMTcxNiwibmJmIjoxNzEzMjExNzE2fQ.t9qhIrG66S3EGXVYYndYV74_qcbQ-R5NU33BoyOexMQ' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```

- Resultado esperado: 



Poder visualizar la fecha en que se realizo la solicitud en el sistema de Pedidos.

- Posible solución:



Guardar la fecha al registrar al usuario desde el sitio de NB y agregar el parámetro al recurso del listado de solicitudes de clientes.
