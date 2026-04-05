---
jira_key: "COB-223"
aliases: ["COB-223"]
summary: "APP - Refactor - Redondeo al cobrar"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-11-02 17:04"
updated: "2022-11-29 11:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-223"
---

# COB-223: APP - Refactor - Redondeo al cobrar

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-02 17:04 |
| Actualizado | 2022-11-29 11:33 |
| Etiquetas | ninguna |
| Jira | [COB-223](https://bluinc.atlassian.net/browse/COB-223) |

## Relaciones

- **Padre:** [[COB-222 - Refactor - Redondeo al cobrar|COB-222]] Refactor - Redondeo al cobrar
- **is blocked by:** [[COB-225 - API - Refactor - Agregar toleranca a los medios de pago|COB-225]] API - Refactor - Agregar toleranca a los medios de pago

## Descripcion

Al cobrar se debe verificar que no tenga un saldo negativo que sea SUPERIOR al paymentTolerance  en [link](https://lioteam.atlassian.net/browse/COB-225) de el objeto DOLARES.

Siempre el calculo lo hacemos en dolares.

De darte el caso, interrumpo el proceso y envió la notificación correspondiente.
