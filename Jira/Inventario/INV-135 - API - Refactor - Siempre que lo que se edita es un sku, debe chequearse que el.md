---
jira_key: "INV-135"
aliases: ["INV-135"]
summary: "API - Refactor - Siempre que lo que se edita es un sku, debe chequearse que el mismo no exista en otro producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-13 18:20"
updated: "2024-09-24 23:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-135"
---

# INV-135: API - Refactor - Siempre que lo que se edita es un sku, debe chequearse que el mismo no exista en otro producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-13 18:20 |
| Actualizado | 2024-09-24 23:03 |
| Etiquetas | ninguna |
| Jira | [INV-135](https://bluinc.atlassian.net/browse/INV-135) |

## Relaciones

- **Padre:** [[INV-27]] Productos
- **relates to:** [[INV-142]] Refactor: Validar sku

## Descripcion

Cuando editas los productos en el listado, me paso que pude repetir un sku que ya existia en otro producto, eso no debe estar permitido en ninguna instancia, a menos que el producto sea de una distribuidora o empresa diferente

```
curl 'https://api.inventory.lio.red/item/119025' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjYyNjQwNjgsInVzdWFyaW8iOjc0NjN9.ZQWDvCQW-vDNa5Yf56mgM_M0DjaXShuN6SDVnPuSUOM' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://inventario.saftel.com' \
  -H 'Referer: https://inventario.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36' \
  -H 'ngrok-skip-browser-warning: true' \
  -H 'sec-ch-ua: "Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"sku":"B550I AORUS PRO AX 1.3"}'
```
