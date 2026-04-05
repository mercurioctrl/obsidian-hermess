---
jira_key: "POS-276"
aliases: ["POS-276"]
summary: "APP - Feat - Rechazar pase desde expedicion"
status: "CodeReview"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-12-28 15:48"
updated: "2023-12-28 17:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-276"
---

# POS-276: APP - Feat - Rechazar pase desde expedicion

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-28 15:48 |
| Actualizado | 2023-12-28 17:59 |
| Etiquetas | ninguna |
| Jira | [POS-276](https://bluinc.atlassian.net/browse/POS-276) |

## Relaciones

- **Padre:** [[POS-23 - Pases de mercaderia|POS-23]] Pases de mercaderia

## Descripcion

Existe un caso donde nos pueden hacer un pase por error, el cual deseamos rechazar y revertir el procesos a su instancia inicial.

Para eso agregaremos un “accionable” a el modal que diga “rechazar pase” en rojo.

El mismo ejecutara el recurso a continuacion

[adjunto]
```
PATCH {{API_URL}}/v1/passes
```

```
{
    "statusId":3,
    "passId":1882,
    "items": [
            {
            "productDescription": "MEMORIA PATRIOT DDR4 V4S 8GB 3200MHZ CL16 VIPER 4 STEEL PE000638",
            "productId": "118343 ",
            "serial": "UW2310202800"
            }
        ]
}
```
