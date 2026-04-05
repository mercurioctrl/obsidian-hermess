---
jira_key: "PED-516"
aliases: ["PED-516"]
summary: "API - Agregar/Editar cliente - Restricción de duplicados - Incidencias varias"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-01-26 02:33"
updated: "2024-02-01 19:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-516"
---

# PED-516: API - Agregar/Editar cliente - Restricción de duplicados - Incidencias varias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-01-26 02:33 |
| Actualizado | 2024-02-01 19:49 |
| Etiquetas | ninguna |
| Jira | [PED-516](https://bluinc.atlassian.net/browse/PED-516) |

## Relaciones

- **Padre:** [[PED-15]] Clientes
- **blocks:** [[PED-494]] API - Refactor - Agregar/Editar cliente - Restricción de duplicados 

## Descripcion

Al editar el número de identificación de un cliente, me lo permite aun cuando este ya existe en la base de datos junto con su misma categoría fiscal.

```
curl 'https://gamma.api.orders.lio.red/v1/clients/80600' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, /' \
  -H 'Accept-Language: es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDYyNTA4NTksImF1ZCI6ImZhNDg5NGU1YTFkMzMwYTIzNjljYzI3YzhmMTY5NGZmZjg4NTBiNjYiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjF9LCJpYXQiOjE3MDYyNDcyNTksIm5iZiI6MTcwNjI0NzI1OX0.Y8bFqPX9UduErl2_Utu20ybJrf7LDzkdMia7jO6iNT4' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0' \
  -H 'sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"cuil":"30712286896","clientName":"DI CARLO ESTEBAN OSCAR","commercialName":"DI CARLO ESTEBAN OSCAR","typeDocument":1,"category":1,"provinceId":1,"localityId":2564,"address":"SEGUI F J ALMTE. 560 Dpto:23","postalCode":"1407","telephone":"01154658991","telephone2":"01154658991","whaPhone":"5491154659915","email":"montenegrodiego@hotmail.com","clientId":80600,"companyCode":4,"profile":1,"currencyId":0,"salespersonId":41}' \
  --compressed
```

[adjunto]
---

Actualización 30/01/24
Realice la misma prueba, pero ahora en Postman y aún me permite actualizar el cliente.

[adjunto]
[adjunto]
Dato extra:
A simple vista, podría sugerir que el problema quizás está relacionado con el hecho de que se está filtrando por el mismo cliente. Esto podría conducir a un resultado verdadero solo si los datos a actualizar coinciden exactamente con los existentes en la base de datos.

[adjunto]
