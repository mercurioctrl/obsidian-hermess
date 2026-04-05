---
jira_key: "PED-152"
aliases: ["PED-152"]
summary: "API - Feat - Desliquidar pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-10-18 22:09"
updated: "2025-02-20 10:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-152"
---

# PED-152: API - Feat - Desliquidar pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-18 22:09 |
| Actualizado | 2025-02-20 10:03 |
| Etiquetas | ninguna |
| Jira | [PED-152](https://bluinc.atlassian.net/browse/PED-152) |

## Relaciones

- **Padre:** [[PED-123]] Feat - Liquidar pedido
- **has action item:** [[PED-951]] API - Refactor - Validaciones necesarias para desliquidar

## Descripcion

Generaremos un recurso que sea para reabrir la venta (desliquidar) solo cuando el pedido aun no comenzó a serializarse segun la tabla `[NEW_BYTES].[dbo].[ST_REMITOS_VENTA_DETALLE_SALIDA]`

```
PATCH {API_URL}/v1/openSale
```

```
{
order
branch
}
```

```
DELETE FROM NEW_BYTES.dbo.MS_REMITO_CABECERA
WHERE REMITO_FP = ?		  AND SUCURSAL_REMITO = ?;

DELETE FROM
NEW_BYTES.dbo.MS_REMITO_DETALLE
WHERE REMITO_FP = ?		  AND SUCURSAL_REMITO = ?;

DELETE FROM  
NEW_BYTES.dbo.MS_VENTAS_REMITOS
WHERE REMITO_FP = ?		  AND SUCURSAL_REMITO = ?;

DELETE FROM
NEW_BYTES.dbo.MC_ENLACE_REMITOS_FORMASPAGO
WHERE REMITO_FP = ?		  AND SUCURSAL_REMITO = ?;

DELETE FROM  
NEW_BYTES.dbo.MS_REMITO_DETALLE_GANANCIA_ENLACE
WHERE REMITO_FP = ?		  AND SUCURSAL_REMITO = ?;

DELETE FROM
NEW_BYTES.dbo.MS_ENLACE_REMITOS_GANANCIAS
WHERE REMITO_FP = ?		  AND SUCURSAL_REMITO = ?;

DELETE FROM
NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS
WHERE REMITO_FP = ?		  AND SUCURSAL_REMITO = ?;

UPDATE NewBytes_DBF.dbo.albclit SET ntipoalb = 1, ID_ESTADOREMITOCLI=1 where cnumalb = ?		 AND cnumsuc = ?;
```
