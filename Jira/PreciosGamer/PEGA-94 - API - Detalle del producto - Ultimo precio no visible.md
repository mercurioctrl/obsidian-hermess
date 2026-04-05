---
jira_key: "PEGA-94"
aliases: ["PEGA-94"]
summary: "API - Detalle del producto - Ultimo precio no visible"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-06-26 14:23"
updated: "2024-06-28 18:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-94"
---

# PEGA-94: API - Detalle del producto - Ultimo precio no visible

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-26 14:23 |
| Actualizado | 2024-06-28 18:07 |
| Etiquetas | ninguna |
| Jira | [PEGA-94](https://bluinc.atlassian.net/browse/PEGA-94) |

## Relaciones

- **Padre:** [[PEGA-2]] Catalogos y Buscador
- **blocks:** [[PEGA-19]] API - Feat - Detalle del producto

## Descripcion

El objeto no trae consigo el ultimo precio, sin embargo, en el histograma si aparece.

[adjunto]
```
curl 'https://gamma.api.pega.lio.red/v1/itemDetail/31777' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.preciosgamer.com' \
  -H 'Referer: https://gamma.preciosgamer.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0' \
  -H 'sec-ch-ua: "Chromium";v="124", "Opera";v="110", "Not-A.Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```
