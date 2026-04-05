---
jira_key: "LIO-561"
aliases: ["LIO-561"]
summary: "API - Review - Verificar al crear/actualizar un cliente de libre opción parámetros iniciales "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-02-27 08:37"
updated: "2026-03-02 14:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-561"
---

# LIO-561: API - Review - Verificar al crear/actualizar un cliente de libre opción parámetros iniciales 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-27 08:37 |
| Actualizado | 2026-03-02 14:54 |
| Etiquetas | ninguna |
| Jira | [LIO-561](https://bluinc.atlassian.net/browse/LIO-561) |

## Relaciones

- **Padre:** [[LIO-402]] Clientes

## Descripcion

- Verificar si se esta guardando para NB el parámetro `[NewBytes_DBF].[dbo].[clientes].voucherCompanyCode` al creal un nuevo cliente (no se si esto ya lo habiamos cubierto, pero releyendo esto me surgio la duda [link](https://bluinc.atlassian.net/browse/SNB-3681) ).



Al mismo tiempo surgió otra duda, respecto a la resignación de clientes y habría que verificar lo siguiente

- Cuando se hace un pedido de libre opcion, y el cliente matchea con uno que existe ya en NB, no debe cambiar nunca el vendedor que ya tiene asignado (para no robarle clientes). Osea que `[NewBytes_DBF].[dbo].[clientes].ID_VENDEDOR`, ni `[NewBytes_DBF].[dbo].[clientes].ccodage` deben cambiar en ese caso. Solo si no existia el cliente o esos parametros eran `NULL`. 


- Por otro lado en el caso de la orden si debera figurar como que es de libreopcion aunque no lo sea el cliente, es decir  en `[NewBytes_DBF].[dbo].[pedclit]`
