---
jira_key: "EXP-281"
aliases: ["EXP-281"]
summary: "APP - Refactor - Validar palabra clave, en el caso que exista"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-05-15 09:31"
updated: "2023-05-19 08:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-281"
---

# EXP-281: APP - Refactor - Validar palabra clave, en el caso que exista

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-15 09:31 |
| Actualizado | 2023-05-19 08:31 |
| Etiquetas | ninguna |
| Jira | [EXP-281](https://bluinc.atlassian.net/browse/EXP-281) |

## Relaciones

- **Padre:** [[EXP-258 - Feat - Autorizar Entrega mediante tarjeta de autorizacion|EXP-258]] Feat - Autorizar Entrega mediante tarjeta de autorizacion
- **is blocked by:** [[EXP-280 - API - Refactor - Validar palabra clave, en el caso que esta exista en la tabla|EXP-280]] API - Refactor - Validar palabra clave, en el caso que esta exista en la tabla pedclit

## Descripcion

Basándonos en [link](https://lioteam.atlassian.net/browse/EXP-280) agregaremos al modal que valida la tarjeta un campo extra, para ingresar la palabra clave.

Este campo solo aparece si el mismo se encuentra en la tabla pedclit

Solo es necesario validar en los casos que tengan `[NewBytes_DBF].[dbo].[pedclit].secret_key` distinto de NULL

Para esto se agregara al recurso [link](https://lioteam.atlassian.net/browse/EXP-280) 

```
GET {API_URL}/v1/orders/{pedido}
```

el parámetro `secretKey:true` cuando en pedclit no es nulo para poder saber si debemos o no mostrar el campo
