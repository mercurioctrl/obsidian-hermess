---
jira_key: "PEGA-162"
aliases: ["PEGA-162"]
summary: "API - Formulario de rastreo - Valores enviados y almacenados no coincidentes"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-01-03 00:33"
updated: "2025-01-03 20:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-162"
---

# PEGA-162: API - Formulario de rastreo - Valores enviados y almacenados no coincidentes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-01-03 00:33 |
| Actualizado | 2025-01-03 20:27 |
| Etiquetas | ninguna |
| Jira | [PEGA-162](https://bluinc.atlassian.net/browse/PEGA-162) |

## Relaciones

- **Padre:** [[PEGA-1 - Bases y repositorios|PEGA-1]] Bases y repositorios
- **relates to:** [[PEGA-38 - API - Feat - Formulario de rastreo|PEGA-38]] API - Feat - Formulario de rastreo

## Descripcion

Por alguna razón al no se están almacenando los datos de los siguientes parámetros:

- `siteUrl`


- `siteAPi`


- `apiDocumentationUrl`


- `storeName`





[adjunto]
[adjunto]
```
curl 'https://gamma.api.preciosgamer.com/v1/addMyInventory' -X POST -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: es-MX' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Content-Type: application/json' -H 'Referer: https://gamma.preciosgamer.com/' -H 'Origin: https://gamma.preciosgamer.com' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-site' -H 'Connection: keep-alive' -H 'Priority: u=0' --data-raw '{"email":"correoelectronico@nb.com.ar","name":"Nombre","siteUrl":"www.sitioweb.com","siteApi":"www.apiurl.com","apiDocumentationUrl":"www.documentacion.com","storeName":"tienda name","comment":"comentarios"}'
```
