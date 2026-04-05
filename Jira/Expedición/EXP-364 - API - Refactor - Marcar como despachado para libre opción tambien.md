---
jira_key: "EXP-364"
aliases: ["EXP-364"]
summary: "API - Refactor - Marcar como despachado para libre opción tambien"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-01 14:47"
updated: "2023-09-04 16:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-364"
---

# EXP-364: API - Refactor - Marcar como despachado para libre opción tambien

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-01 14:47 |
| Actualizado | 2023-09-04 16:02 |
| Etiquetas | ninguna |
| Jira | [EXP-364](https://bluinc.atlassian.net/browse/EXP-364) |

## Relaciones

- **Padre:** [[EXP-258]] Feat - Autorizar Entrega mediante tarjeta de autorizacion
- **blocks:** [[SNB-1153]] NO SE MARCAN COMO DESPACHADOS LOS PEDIDOS EN LA GRILLA DE LIBRE OPCION

## Descripcion

Cuando ejecutamos el recurso 

```
PATCH {API_URL}/v1/orders/{pedido}/hand
```

y es un **pedido de libre opción** entonces tengo que marcar tambien en `B.despachado, A.despachado`

```
SELECT 
B.despachado, A.despachado
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

LEFT JOIN NewBytes_DBF.dbo.pedclil ON pedclil.cnumped = d.cnumped
    WHERE confirmado = 1 
AND D.cnumped = 10327157
```
