---
jira_key: "PED-510"
aliases: ["PED-510"]
summary: "API - Review- Colision entre numeros generados por libreopcion y pedidos que vienen (de) o son presupuestos "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-01-23 10:16"
updated: "2024-01-30 11:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-510"
---

# PED-510: API - Review- Colision entre numeros generados por libreopcion y pedidos que vienen (de) o son presupuestos 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-23 10:16 |
| Actualizado | 2024-01-30 11:49 |
| Etiquetas | ninguna |
| Jira | [PED-510](https://bluinc.atlassian.net/browse/PED-510) |

## Relaciones

- **Padre:** [[PED-328]] Libre Opcion

## Descripcion

Paso varias veces en los ultimos días que se había algún problema con un pedido y siempre el problema es que teníamos un presupuesto colisionado con un pedido de libre opción

Es decir, tenias el mismo pedclit.cnumped

Hay que buscar la raiz del problema que puede estar tanto en la api legacy como en la generacion del presupuesto y mitigarla para que no se mezclen
