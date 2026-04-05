---
jira_key: "COB-503"
aliases: ["COB-503"]
summary: "API fix retorna dato duplicado en movimientos de caja"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-04-23 18:55"
updated: "2024-04-29 01:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-503"
---

# COB-503: API fix retorna dato duplicado en movimientos de caja

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-04-23 18:55 |
| Actualizado | 2024-04-29 01:58 |
| Etiquetas | ninguna |
| Jira | [COB-503](https://bluinc.atlassian.net/browse/COB-503) |

## Relaciones

*Sin relaciones*

## Descripcion

[https://lioteam.atlassian.net/issues/[[SNB-1820]]](https://lioteam.atlassian.net/issues/[[SNB-1820]]) 

Retorna movimientos duplicados.

Esto se debe a que cuando se realizan cobros con pedidos multiples, se registra un Id de Log_operaciones para 2 filas en nonTaxVoucher. 

se dio solucion ajustando la query.
