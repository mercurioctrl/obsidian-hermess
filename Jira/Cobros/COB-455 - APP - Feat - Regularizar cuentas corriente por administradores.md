---
jira_key: "COB-455"
aliases: ["COB-455"]
summary: "APP - Feat - Regularizar cuentas corriente por administradores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-07-07 23:11"
updated: "2023-07-24 09:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-455"
---

# COB-455: APP - Feat - Regularizar cuentas corriente por administradores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-07 23:11 |
| Actualizado | 2023-07-24 09:07 |
| Etiquetas | ninguna |
| Jira | [COB-455](https://bluinc.atlassian.net/browse/COB-455) |

## Relaciones

- **Padre:** [[COB-453 - Feat - Regularizar cuenta para administradores|COB-453]] Feat - Regularizar cuenta para administradores
- **is blocked by:** [[COB-454 - API - Feat - Regularizar cuenta corriente|COB-454]] API - Feat - Regularizar cuenta corriente

## Descripcion

Basándonos en el recurso de la historia [https://lioteam.atlassian.net/browse/COB-454](https://lioteam.atlassian.net/browse/COB-454) agregaremos un botón con la leyenda “Regularizar cuenta corriente” al modal de cuenta corriente.

[adjunto]
Al accionarlo abriremos un modal con un formulario que posee los siguientes elementos:

- Saldo correcto del cliente: Puede tener números decimales positivos o negativos y es obligatorio.


- Justificación, es un texto con un mínimo de 50 caracteres (esto debe indicarse para que se entienda que es obligatorio un minimo) es obligatorio.


- Cuando se presiona el botón “Regularizar” pide confirmación por SI o por NO
