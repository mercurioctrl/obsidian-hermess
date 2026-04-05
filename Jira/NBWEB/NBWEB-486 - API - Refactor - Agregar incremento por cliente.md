---
jira_key: "NBWEB-486"
aliases: ["NBWEB-486"]
summary: "API - Refactor - Agregar incremento por cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-09-15 12:51"
updated: "2022-09-19 09:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-486"
---

# NBWEB-486: API - Refactor - Agregar incremento por cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-15 12:51 |
| Actualizado | 2022-09-19 09:23 |
| Etiquetas | ninguna |
| Jira | [NBWEB-486](https://bluinc.atlassian.net/browse/NBWEB-486) |

## Relaciones

- **Padre:** [[NBWEB-4 - API - Catalogos de productos|NBWEB-4]] API - Catalogos de productos
- **blocks:** [[SNB-308 - Incrementos para clientes de misiones|SNB-308]] Incrementos para clientes de misiones
- **is caused by:** [[NBWEB-487 - API - Feat - Modificar en el sistema de pedidos|NBWEB-487]] API - Feat - Modificar en el sistema de pedidos

## Descripcion

Agregar incremento por cliente.

Vamos a agregar una columnar dentro de la tabla `newbytes_dbf.dbo.clientes` que contiene un decimal porcentual.

El mismo altera el precio calculado para cada cliente, incrementándolo y decrementandolo según sea positivo o negativo
