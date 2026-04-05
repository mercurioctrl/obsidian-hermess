---
jira_key: "EXP-177"
aliases: ["EXP-177"]
summary: "APP - Feat - Alertar pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-01-25 08:54"
updated: "2023-02-23 17:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-177"
---

# EXP-177: APP - Feat - Alertar pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-25 08:54 |
| Actualizado | 2023-02-23 17:18 |
| Etiquetas | ninguna |
| Jira | [EXP-177](https://bluinc.atlassian.net/browse/EXP-177) |

## Relaciones

- **Padre:** [[EXP-169]] Feat - Alertar pedidos
- **is blocked by:** [[EXP-176]] API - Feat - Alertar pedidos

## Descripcion

Cuando estoy viendo un pedido en las pestañas Envios o Retiros y el mismo aun no esta despachado, tengo que poder alertarlo mediante un enlace o boton en la fila. (Creo que dijimos que esto era mejor que el boton derecho, pero por ahi en este caso podriamos evaluarlo por el tipo de accion).

Usaremos 

```
PATCH {API_URL}/v1/alertOrder/{pedidoAAlertar}
```

Que esta descrito aca: [link](https://lioteam.atlassian.net/browse/EXP-176) 

Es importante que al realizar la acción, el usuario vea como en tiempo real los cambio suceden, y que no necesite recargar una parte del sitio.

La idea era mover el ítem al primer lugar de la lista y destacarle con un color, un borde o algo que llame la atención.
