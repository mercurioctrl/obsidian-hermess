---
jira_key: "COB-453"
aliases: ["COB-453"]
summary: "Feat - Regularizar cuenta para administradores"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-07-07 23:04"
updated: "2023-09-05 15:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-453"
---

# COB-453: Feat - Regularizar cuenta para administradores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-07 23:04 |
| Actualizado | 2023-09-05 15:18 |
| Etiquetas | ninguna |
| Jira | [COB-453](https://bluinc.atlassian.net/browse/COB-453) |

## Relaciones

- **Padre:** [[COB-20]] Cuentas Corrientes
- **Subtarea:** [[COB-454]] API - Feat - Regularizar cuenta corriente
- **Subtarea:** [[COB-455]] APP - Feat - Regularizar cuentas corriente por administradores
- **Subtarea:** [[COB-477]] APP - Review - Regularizar cuentas corrientes -> Error en el mensaje "succes"
- **blocks:** [[SNB-953]] se liquidó un pedido y se autorizó sólo / OTRO MÁS
- **blocks:** [[SNB-929]] regularizar cuenta
- **is caused by:** [[SNB-929]] regularizar cuenta
- **is blocked by:** [[COB-473]] APP - Regularizar cuenta para administradores - Incidencias varias
- **is blocked by:** [[COB-474]] API - Regularizar cuenta para administradores - Incidencias varias

## Descripcion

Se busca introducir una funcionalidad, solo para administradores, que se encargue de ajustar la cuenta corriente del cliente a un valor determinado introducido por el usuario.

Al ingresar el valor correcto del subtotal, el sistema analiza la situación actual de la cuenta corriente del cliente, incluyendo los movimientos registrados y los saldos pendientes. A continuación, se calculan las transacciones necesarias para igualar el subtotal deseado y se agrega una linea con la leyenda regularización, indicando quien fue el usuario que la realizo y una justificacion de este movimiento administrativo.

Ademas, al realizar dicha “regularizacion” es obligatorio reintroducir la contraseña del usuario administrativo y una justificacion del al menos 20 caracteres.
