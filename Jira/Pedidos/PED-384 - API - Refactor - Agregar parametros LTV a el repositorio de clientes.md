---
jira_key: "PED-384"
aliases: ["PED-384"]
summary: "API - Refactor - Agregar parametros LTV a el repositorio de clientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-12-22 16:00"
updated: "2023-12-27 21:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-384"
---

# PED-384: API - Refactor - Agregar parametros LTV a el repositorio de clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-22 16:00 |
| Actualizado | 2023-12-27 21:15 |
| Etiquetas | ninguna |
| Jira | [PED-384](https://bluinc.atlassian.net/browse/PED-384) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes
- **blocks:** [[PED-387 - APP - Refactor - Agregaremos informacion del cliente al listado|PED-387]] APP - Refactor - Agregaremos informacion del cliente al listado
- **is blocked by:** [[PED-396 - API - Agregar parámetros LTV al repositorio clientes - Incidencias varias|PED-396]]   API - Agregar parámetros LTV al repositorio clientes - Incidencias varias

## Descripcion

Agregaremos al recurso que se encarga de listar los clientes los parametros

- [average_purchase_value]


- [purchase_frequency]


- [relationship_duration_month]


- [ltv] 



La tabla correspondiente es `[NewBytes_DBF].[dbo].[clientesLtv]`


Se debe mostrar siempre el ultimo registro para cada cliente
