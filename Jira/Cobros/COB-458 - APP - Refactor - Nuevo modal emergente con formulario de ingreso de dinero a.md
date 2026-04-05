---
jira_key: "COB-458"
aliases: ["COB-458"]
summary: "APP - Refactor - Nuevo modal emergente con formulario de ingreso de dinero \"a mano\" "
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-07-10 09:06"
updated: "2023-07-10 18:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-458"
---

# COB-458: APP - Refactor - Nuevo modal emergente con formulario de ingreso de dinero "a mano" 

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-10 09:06 |
| Actualizado | 2023-07-10 18:16 |
| Etiquetas | ninguna |
| Jira | [COB-458](https://bluinc.atlassian.net/browse/COB-458) |

## Relaciones

- **Padre:** [[COB-456 - Refactor - Limitaciones para ingresar dinero a mano cuando no selecciono un|COB-456]] Refactor - Limitaciones para ingresar dinero "a mano" cuando no selecciono un pedido
- **is blocked by:** [[COB-457 - API - Refactor - Observación justificativa obligatoria|COB-457]] API - Refactor - Observación justificativa obligatoria

## Descripcion

Al ingresar dinero a mano y apretar el accionable “Cobrar” se debe desplegar un nuevo modal con la leyenda:

Estas a punto de realizar una acción imprudente sobre la cuenta del cliente. Si lo que deseas es cobrarle al mismo, debes seleccionar primero el pedido que quieres cobrar.

Si continuas con esta acción, marcaremos este movimiento para su revisión y avisaremos a la gerencia de esta operación.

Accionable “Cancelar” y Accionable “Confirmar imprudencia”
