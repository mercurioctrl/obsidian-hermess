---
jira_key: "PEGA-67"
aliases: ["PEGA-67"]
summary: "API - Listar productos - Orden alfabético "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-05-06 13:42"
updated: "2024-05-22 16:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-67"
---

# PEGA-67: API - Listar productos - Orden alfabético 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-05-06 13:42 |
| Actualizado | 2024-05-22 16:48 |
| Etiquetas | ninguna |
| Jira | [PEGA-67](https://bluinc.atlassian.net/browse/PEGA-67) |

## Relaciones

- **Padre:** [[PEGA-2]] Catalogos y Buscador
- **blocks:** [[PEGA-15]] API - Feat - Listar productos filtros

## Descripcion

Al filtrar por orden alfabético me aparecen resultados distintos a los esperados.

[adjunto]
```
curl 'https://gamma.api.pega.lio.red/v1/items?search=amd&offset=0&order=asc_a_z' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.preciosgamer.com' \
  -H 'Referer: https://gamma.preciosgamer.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```
