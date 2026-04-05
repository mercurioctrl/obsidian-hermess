---
jira_key: "NBWEB-727"
aliases: ["NBWEB-727"]
summary: "API - Catálogos de productos - Oportunidad de mejora en el buscador del sitio"
status: "Finalizada"
type: "Tarea"
priority: "Low"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-04-30 15:34"
updated: "2024-05-02 22:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-727"
---

# NBWEB-727: API - Catálogos de productos - Oportunidad de mejora en el buscador del sitio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Low |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-30 15:34 |
| Actualizado | 2024-05-02 22:12 |
| Etiquetas | ninguna |
| Jira | [NBWEB-727](https://bluinc.atlassian.net/browse/NBWEB-727) |

## Relaciones

- **Padre:** [[NBWEB-602]] Sitio Web
- **relates to:** [[NBWEB-4]] API - Catalogos de productos
- **blocks:** [[SNB-1835]] No busca en la web NB celular samsung

## Descripcion

Al buscar en el sitio de NB, por ejemplo, “Celular samsung“ no devuelve resultados. 

[adjunto]
```
curl 'https://gamma.api.nb.com.ar/v1/celular-samsung?available_stock=0' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.nb.com.ar' \
  -H 'Referer: https://gamma.nb.com.ar/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```
