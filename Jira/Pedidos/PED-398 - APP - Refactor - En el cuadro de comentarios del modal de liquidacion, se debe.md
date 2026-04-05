---
jira_key: "PED-398"
aliases: ["PED-398"]
summary: "APP - Refactor - En el cuadro de comentarios del modal de liquidacion, se debe sostener los comentarios del pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-12-27 09:25"
updated: "2023-12-28 16:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-398"
---

# PED-398: APP - Refactor - En el cuadro de comentarios del modal de liquidacion, se debe sostener los comentarios del pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-27 09:25 |
| Actualizado | 2023-12-28 16:21 |
| Etiquetas | ninguna |
| Jira | [PED-398](https://bluinc.atlassian.net/browse/PED-398) |

## Relaciones

- **Padre:** [[PED-123]] Feat - Liquidar pedido

## Descripcion

Debemos usar el recurso

```
{API_URL}/v1/sellerComments/{pedido}
```

Tanto para mostrar, como para guardar siempre y cuando no se liquide todavia para evitar cargar lo mismo varias veces

[adjunto]
