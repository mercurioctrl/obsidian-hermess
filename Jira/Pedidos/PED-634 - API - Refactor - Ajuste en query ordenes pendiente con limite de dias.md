---
jira_key: "PED-634"
aliases: ["PED-634"]
summary: "API - Refactor - Ajuste en query ordenes pendiente con limite de dias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-03-25 10:03"
updated: "2024-04-05 06:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-634"
---

# PED-634: API - Refactor - Ajuste en query ordenes pendiente con limite de dias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-03-25 10:03 |
| Actualizado | 2024-04-05 06:50 |
| Etiquetas | ninguna |
| Jira | [PED-634](https://bluinc.atlassian.net/browse/PED-634) |

## Relaciones

- **Padre:** [[PED-123]] Feat - Liquidar pedido

## Descripcion

Metodo 

`$this->checkOrderPending($codeAgent)`

- tambien excluye aquellos pedidos que fueron anulados



utilizando: `pedclit.lanula = 0`
