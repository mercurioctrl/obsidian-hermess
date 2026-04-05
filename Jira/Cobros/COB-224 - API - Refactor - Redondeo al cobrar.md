---
jira_key: "COB-224"
aliases: ["COB-224"]
summary: "API - Refactor - Redondeo al cobrar"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-02 17:04"
updated: "2022-11-29 11:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-224"
---

# COB-224: API - Refactor - Redondeo al cobrar

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-02 17:04 |
| Actualizado | 2022-11-29 11:33 |
| Etiquetas | ninguna |
| Jira | [COB-224](https://bluinc.atlassian.net/browse/COB-224) |

## Relaciones

- **Padre:** [[COB-222 - Refactor - Redondeo al cobrar|COB-222]] Refactor - Redondeo al cobrar

## Descripcion

Al cobrar se debe verificar que no tenga un saldo negativo que sea SUPERIOR al paymentTolerance de el objeto DOLARES.

Siempre el calculo lo hacemos en dolares.

De darte el caso, interrumpo el proceso y envió la notificación correspondiente.
