---
jira_key: "PED-906"
aliases: ["PED-906"]
summary: "API - Refactor - validacion al liquidar por banco id de operacion unico"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-12-18 17:17"
updated: "2024-12-27 06:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-906"
---

# PED-906: API - Refactor - validacion al liquidar por banco id de operacion unico

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-12-18 17:17 |
| Actualizado | 2024-12-27 06:14 |
| Etiquetas | ninguna |
| Jira | [PED-906](https://bluinc.atlassian.net/browse/PED-906) |

## Relaciones

- **action item from:** [[SNB-2654]] Numero de operación MP al liquidar no funciona correctamente

## Descripcion

Se debe ajutar validación  para evitar tener duplicados de nro operacion unico, en cualquier instancia.

Endpoint:  POST /v1/paymentForBank

Metodo a ajustar.

`BankTransferRepository::uniqueOperationId($branch, $numOrder): bool`

- Verifica si el `nroOperacion` ya existe en cualquier orden


- Subconsulta para obtener el `nroOperacion` de la orden actual
