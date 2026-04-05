---
jira_key: "EXP-169"
aliases: ["EXP-169"]
summary: "Feat - Alertar pedidos"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-01-24 09:09"
updated: "2023-03-07 19:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-169"
---

# EXP-169: Feat - Alertar pedidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-24 09:09 |
| Actualizado | 2023-03-07 19:17 |
| Etiquetas | ninguna |
| Jira | [EXP-169](https://bluinc.atlassian.net/browse/EXP-169) |

## Relaciones

- **Padre:** [[EXP-1]] Base y Repositorios
- **Subtarea:** [[EXP-176]] API - Feat - Alertar pedidos
- **Subtarea:** [[EXP-177]] APP - Feat - Alertar pedido
- **Subtarea:** [[EXP-178]] API - Refactor - Cambiar el orden de las listas "retiros" y "envios" para priorizar los pedidos alertados
- **Subtarea:** [[EXP-211]] API - Refactor - Al despachar quitar alerta
- **Subtarea:** [[EXP-506]] API - Refactor - Des-alertar pedido
- **is blocked by:** [[EXP-212]] Alertar pedido - Alertar pedido ya despachado
- **is blocked by:** [[EXP-211]] API - Refactor - Al despachar quitar alerta

## Descripcion

Para poder preparar los pedidos prioritarios mas rápido, se deben poder alertar. Esto es simplemente marcarles una flag para destacarles.

No solo los destacaremos, sino que ademas los moveremos al principio de la lista “a la fuerza” de modo tal que no pudieran pasar desapercibidos al encontrarse fuera de la primer pagina. Recién una vez despachado se ira la flag de alerta.

 

- Deben realmente destacar en el front para no pasar desapercibidos


- La acción de “alertar” debe ser inmediata a nivel visual, osea que al darle clic a “alertar pedido” debo verlo como cambia de posición y destaque en el acto desde el front.


- Recién una vez que se despacha, el alerta se va.
