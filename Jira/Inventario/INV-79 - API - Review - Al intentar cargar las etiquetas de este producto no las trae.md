---
jira_key: "INV-79"
aliases: ["INV-79"]
summary: "API - Review - Al intentar cargar las etiquetas de este producto no las trae"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-19 10:52"
updated: "2024-06-24 01:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-79"
---

# INV-79: API - Review - Al intentar cargar las etiquetas de este producto no las trae

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-19 10:52 |
| Actualizado | 2024-06-24 01:26 |
| Etiquetas | ninguna |
| Jira | [INV-79](https://bluinc.atlassian.net/browse/INV-79) |

## Relaciones

- **Padre:** [[INV-27]] Productos

## Descripcion

```
curl 'https://api.inventory.lio.red/item/111698' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTg4MDU5OTUsInVzdWFyaW8iOjU1fQ.V4RbPjsPb-MjoCyBXBxBiPQ800eNwl6mkP5KIZUQXl4' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://inventario.saftel.com' \
  -H 'Referer: https://inventario.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```



[adjunto]
