---
jira_key: "PED-995"
aliases: ["PED-995"]
summary: "APP - Refactor - Agregar percepciones ARBA al \"pedido + INFO\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-04-25 08:25"
updated: "2025-05-12 13:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-995"
---

# PED-995: APP - Refactor - Agregar percepciones ARBA al "pedido + INFO"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-25 08:25 |
| Actualizado | 2025-05-12 13:31 |
| Etiquetas | ninguna |
| Jira | [PED-995](https://bluinc.atlassian.net/browse/PED-995) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra
- **action item from:** [[PED-994 - API - Refactor - Agregar percepciones ARBA al pedido + INFO|PED-994]] API - Refactor - Agregar percepciones ARBA al "pedido + INFO"

## Descripcion

Al igual que hicimos en el detalle de la orden se debe incorporar el concepto de percepciones de ARBA como un elemento extra de la siguiente manera

[adjunto]
Basándonos en el recurso [link](https://bluinc.atlassian.net/browse/PED-994) para obtener el porcentual, sera necesario no solo mostrarlo como un elemento diferenciado “Percepción ARBA”, sino ademas sumarlo a los totales como venimos haciendo (Solo totales finales).

Adicionalmente tambien debe estar en el resto de los formatos PDF, TXT, COPIAR, WAA

Y ese total a su vez funcional con la calculadora de cheques.
