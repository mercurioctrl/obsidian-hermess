---
jira_key: "COB-456"
aliases: ["COB-456"]
summary: "Refactor - Limitaciones para ingresar dinero \"a mano\" cuando no selecciono un pedido"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-07-10 09:01"
updated: "2023-07-27 18:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-456"
---

# COB-456: Refactor - Limitaciones para ingresar dinero "a mano" cuando no selecciono un pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-10 09:01 |
| Actualizado | 2023-07-27 18:39 |
| Etiquetas | ninguna |
| Jira | [COB-456](https://bluinc.atlassian.net/browse/COB-456) |

## Relaciones

- **Padre:** [[COB-33]] Cobrar
- **Subtarea:** [[COB-457]] API - Refactor - Observación justificativa obligatoria
- **Subtarea:** [[COB-458]] APP - Refactor - Nuevo modal emergente con formulario de ingreso de dinero "a mano" 

## Descripcion

Dado que “ingresar dinero a mano” sin seleccionar un pedido se volvió algo habitual, porque o es mas fácil, o bien requiere menos detalles de selección buscaremos desincentivar el comportamiento exigiendo algunos parámetros extra y resaltando el carácter incorrecto de este tipo de acción.
