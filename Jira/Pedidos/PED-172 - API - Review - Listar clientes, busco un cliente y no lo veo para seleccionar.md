---
jira_key: "PED-172"
aliases: ["PED-172"]
summary: "API - Review - Listar clientes, busco un cliente y no lo veo para seleccionar"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-10-26 06:58"
updated: "2023-10-26 10:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-172"
---

# PED-172: API - Review - Listar clientes, busco un cliente y no lo veo para seleccionar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-26 06:58 |
| Actualizado | 2023-10-26 10:13 |
| Etiquetas | ninguna |
| Jira | [PED-172](https://bluinc.atlassian.net/browse/PED-172) |

## Relaciones

- **Padre:** [[PED-16]] Listar clientes

## Descripcion

En el recurso [link](https://lioteam.atlassian.net/browse/PED-17)  al filtrar por cliente 

Realizo la siguiente busqueda 

```
curl 'https://gamma.api.orders.lio.red/v1/clients?search=mercurio&currentPage=1&itemsPerPage=15' \
  -X 'OPTIONS' \
  -H 'Accept: */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Access-Control-Request-Headers: authorization' \
  -H 'Access-Control-Request-Method: GET' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36' \
  --compressed
```

Esperando encontrar en el listado al cliente 

| 26806 - MERCURIO CATRIEL EDUARDO |
| --- |

Pero no aparece… ¿es posible que quede detrás del paginado?
