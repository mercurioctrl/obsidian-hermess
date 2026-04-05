---
jira_key: "EXP-29"
aliases: ["EXP-29"]
summary: "APP - Feat -Procesar pases de mercadería"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-11-01 12:33"
updated: "2023-03-13 15:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-29"
---

# EXP-29: APP - Feat -Procesar pases de mercadería

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-01 12:33 |
| Actualizado | 2023-03-13 15:57 |
| Etiquetas | ninguna |
| Jira | [EXP-29](https://bluinc.atlassian.net/browse/EXP-29) |

## Relaciones

- **Padre:** [[EXP-19]] Feat -Procesar pases de mercadería

## Descripcion

Basándonos en [link](https://lioteam.atlassian.net/browse/EXP-82) haremos el formulario para poder procesar el pase de mercadería.

Es similar a cuando hicimos el formulario para hacerlo via web, pero esta vez estara integrado a la aplicaion en un modal.

Enviaremos un objeto del siguiente tipo 

```
{
       "statusId":1,
        "passId":11,
        autorizaUser: {token},
        "items": [
        {
            "productId": 100,
            "productDescription": "Placa de video",
            "serial": "sn8907433987"
        }
        ]
}
```

[adjunto]
Agregaremos a partir de ahora, un parámetro extra, que es el token que valida quien realizo en definitiva la operación, mas allá de quien es el usuario logueado. Ademas, el autorizante, debe tener un permiso especifico para autorizar ese tipo de accion en la tabla de permisos.
