---
jira_key: "LIO-56"
summary: "API - PED - Refactor - Al hacer una autorizacion (ID_STATUS = 2) para un PEDIDO DE LIBRE OPCION debe marcarse como cobrado tambien en libre opcion"
status: "Backlog"
type: "Subtarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2024-06-26 12:20"
updated: "2024-06-26 12:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-56"
---

# LIO-56: API - PED - Refactor - Al hacer una autorizacion (ID_STATUS = 2) para un PEDIDO DE LIBRE OPCION debe marcarse como cobrado tambien en libre opcion

| Campo | Valor |
|-------|-------|
| Estado | Backlog (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-26 12:20 |
| Actualizado | 2024-06-26 12:35 |
| Etiquetas | ninguna |
| Jira | [LIO-56](https://bluinc.atlassian.net/browse/LIO-56) |

## Descripción

Lo que haremos sera marcar `cobrado=1` en `LO.dbo.pedidosCabecera` cuando lo marco como autorizado o pagado . Esta feature solo afecta pedidos de libreopcion.

```
SELECT 
cobrado
FROM
LO.dbo.pedidosCabecera A
LEFT JOIN
LO.dbo.pedidosCabeceraPaquete B
ON 
B.pedidoCabeceraID = A.id
LEFT JOIN
LO.dbo.pedidosCabeceraVendedor C
ON
C.pedidoCabeceraID = A.id
LEFT JOIN
NewBytes_DBF.dbo.pedclit D
ON
D.cnumped = C.pedclitID
WHERE D.cnumped = ?
```
