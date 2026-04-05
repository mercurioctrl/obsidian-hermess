---
jira_key: "EXP-318"
aliases: ["EXP-318"]
summary: "API - Refactor - Listar direcciones de envio por cliente y por pedido especifico"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-06-23 13:46"
updated: "2023-07-17 06:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-318"
---

# EXP-318: API - Refactor - Listar direcciones de envio por cliente y por pedido especifico

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-23 13:46 |
| Actualizado | 2023-07-17 06:28 |
| Etiquetas | ninguna |
| Jira | [EXP-318](https://bluinc.atlassian.net/browse/EXP-318) |

## Relaciones

- **Padre:** [[EXP-218 - Etiquetas para envíos que no las generan (genericas de ahora en mas)|EXP-218]] Etiquetas para envíos que no las generan (genericas de ahora en mas)
- **blocks:** [[EXP-319 - APP - Refactor - Listar direcciones de envio, en el modal enviar al revisar la|EXP-319]] APP - Refactor - Listar direcciones de envio, en el modal enviar al revisar la direccion agregaremos order y branch a la consulta

## Descripcion

Dado que en el front, al momento de generar la etiqueta, vemos un cuadro de dialogo del siguiente tipo

[adjunto]
Necesito poder setear por default la dirección del pedido. Con ese propósito entre otros se creo [link](https://lioteam.atlassian.net/browse/EXP-221)  al que refactorizaremos para lograr

```
{{API_URL}}/v1/shipments/getAddress?clientId=25955&branch=0002&order=10318145
```

para que tambien tenga branch y order

De esta forma daremos prioridad a la columna `idDirCliNbWeb` seteada en `[NewBytes_DBF].[dbo].[pedclit]` y mostrando esa direccion.

Si la misma no estuviera, ahí si mostramos las otras opciones.
