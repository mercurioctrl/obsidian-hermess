---
jira_key: "SNB-2654"
aliases: ["SNB-2654"]
summary: "Numero de operación MP al liquidar no funciona correctamente"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Pedidos Jira"
created: "2024-12-17 22:11"
updated: "2024-12-23 15:22"
labels: ["Sistemas"]
jira_url: "https://bluinc.atlassian.net/browse/SNB-2654"
---

# SNB-2654: Numero de operación MP al liquidar no funciona correctamente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Pedidos Jira |
| Creado | 2024-12-17 22:11 |
| Actualizado | 2024-12-23 15:22 |
| Etiquetas | Sistemas |
| Jira | [SNB-2654](https://bluinc.atlassian.net/browse/SNB-2654) |

## Relaciones

- **has action item:** [[PED-906 - API - Refactor - validacion al liquidar por banco id de operacion unico|PED-906]] API - Refactor - validacion al liquidar por banco id de operacion unico

## Descripcion

Al procesar una venta de hoy 675270 de SCUAGLIA  el cupón difería del importe al buscar mas ventas del cliente  tiene otra del día 15/12, si con el importe correcto 675138 , el cliente subió el mismo cupón en ambas compras , al probar liquidar la del día de hoy el sistema tomo y no advirtió que el numero de operación ya estaba asignado a otro pedido por favor revisar 
Usuario: jdebello
