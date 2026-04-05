---
jira_key: "PED-413"
aliases: ["PED-413"]
summary: "API - Refactor - Actualizaremos la columna nstock_reserva_pedidos para todos aquellos casos donde hay movimientos entre pedidos pendientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-29 11:25"
updated: "2024-01-09 00:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-413"
---

# PED-413: API - Refactor - Actualizaremos la columna nstock_reserva_pedidos para todos aquellos casos donde hay movimientos entre pedidos pendientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-29 11:25 |
| Actualizado | 2024-01-09 00:23 |
| Etiquetas | ninguna |
| Jira | [PED-413](https://bluinc.atlassian.net/browse/PED-413) |

## Relaciones

- **Padre:** [[PED-34 - Generar Editar ordenes|PED-34]] Generar / Editar ordenes
- **blocks:** [[PED-423 - API - Filtrado por stock no coincidente|PED-423]] API - Filtrado por stock no coincidente

## Descripcion

Utilizaremos un query similar a la siguiente, para poder actualizar el valor de la columna de cada item para los siguientes casos

```
UPDATE A SET nstock_reserva_pedidos = ISNULL((SELECT SUM(ncanped) FROM [NewBytes_DBF].[dbo].pedclil pl_sub
LEFT JOIN NewBytes_DBF.dbo.pedclit pt_sub ON
pl_sub.cnumsuc = pt_sub.cnumsuc
AND pl_sub.cnumped = pt_sub.cnumped
WHERE
(pt_sub.cobserv = 'INTERNO' OR  pt_sub.cobserv = 'DESCARGADO')
AND pt_sub.cestado = 'P'
AND (pl_sub.cref = A.cRef or pl_sub.ID_Articulo = A.ID_ARTICULO)  ),0)
FROM [NewBytes_DBF].[dbo].[stocks] A;
```

- Agregar / quitar unidades de un pedido


- Movimiento de unidades entre pedidos


- Eliminacion de una orden


- Generacion de pedido


- Eliminacion de un pedido
