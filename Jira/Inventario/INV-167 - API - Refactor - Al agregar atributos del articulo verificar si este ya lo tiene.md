---
jira_key: "INV-167"
aliases: ["INV-167"]
summary: "API - Refactor - Al agregar atributos del articulo verificar si este ya lo tiene"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-10-24 02:14"
updated: "2024-10-30 03:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-167"
---

# INV-167: API - Refactor - Al agregar atributos del articulo verificar si este ya lo tiene

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-10-24 02:14 |
| Actualizado | 2024-10-30 03:24 |
| Etiquetas | ninguna |
| Jira | [INV-167](https://bluinc.atlassian.net/browse/INV-167) |

## Relaciones

- **Padre:** [[INV-27 - Productos|INV-27]] Productos
- **relates to:** [[INV-168 - APP - Refactor - Al agregar atributos al articulo actualizar el modal de|INV-168]] APP - Refactor - Al agregar atributos al articulo actualizar el modal de atributos

## Descripcion

Realizaremos una mejora para que se valide si el atributo que estamos agregando ya existe. Si existe editarlo, sino existe agregarlo.

De esta manera evitamos duplicidad.

```
curl "https://gamma.api.inventory.lio.red/item/attribute/117549" -X POST -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0" -H "Accept: application/json, text/plain, */*" -H "Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3Mjk3NDgxMjksInVzdWFyaW8iOjc0NjN9.7ossM-3PaAFFJz_68WMzjEo8-yV1SIkLyjqRkHRCWmg" -H "Content-Type: application/json" -H "Origin: https://gamma.inventario.saftel.com" -H "Connection: keep-alive" -H "Referer: https://gamma.inventario.saftel.com/" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: cross-site" -H "Priority: u=0" --data-raw "{""name"":""Tipo de RAM"",""value"":""DDR4 U-DIMM""}"
```

[adjunto]
