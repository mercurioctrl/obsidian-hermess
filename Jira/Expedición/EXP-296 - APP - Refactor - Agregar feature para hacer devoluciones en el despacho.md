---
jira_key: "EXP-296"
aliases: ["EXP-296"]
summary: "APP - Refactor - Agregar feature para hacer devoluciones en el despacho"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-05-28 20:54"
updated: "2023-06-12 08:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-296"
---

# EXP-296: APP - Refactor - Agregar feature para hacer devoluciones en el despacho

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-28 20:54 |
| Actualizado | 2023-06-12 08:04 |
| Etiquetas | ninguna |
| Jira | [EXP-296](https://bluinc.atlassian.net/browse/EXP-296) |

## Relaciones

- **Padre:** [[EXP-294]] Refactor - Devoluciones (pre-despacho)

## Descripcion

Agregaremos un botón “hacer devolución” en el modal 

[adjunto]
de esta forma abriremos el modal 

[adjunto]
que nos permitirá usar el recurso 

```
POST {{API_URL}}/v1/ordersRefund/{pedido}
```

que fue refactorizado para este fin [link](https://lioteam.atlassian.net/browse/EXP-295)
