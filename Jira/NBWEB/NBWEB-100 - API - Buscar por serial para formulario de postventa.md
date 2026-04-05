---
jira_key: "NBWEB-100"
aliases: ["NBWEB-100"]
summary: "API - Buscar por serial para formulario de postventa"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-06 14:40"
updated: "2022-07-01 17:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-100"
---

# NBWEB-100: API - Buscar por serial para formulario de postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-06 14:40 |
| Actualizado | 2022-07-01 17:59 |
| Etiquetas | ninguna |
| Jira | [NBWEB-100](https://bluinc.atlassian.net/browse/NBWEB-100) |

## Relaciones

- **Padre:** [[NBWEB-99]] API - Precarga postventa
- **relates to:** [[NBWEB-110]] APP - Maquetado y desarrollo Postventa

## Descripcion

Se trata de un recurso necesario para obtener informacion de un producto que tiene el cliente y quiere hacer el pre ingreso para enviarlo a postventa



```
GET {{API_URL}}/v1/postventa/serial/{serial}
```

Retorno:

```json
{
  clientId: 2,
  saleDate: '22-12-2021 00:00',
  warranty: 36, //son meses totales de la garantia
  elapsedMonths: 9, meses transcurridos desde la compra
  referSale: '0002-32432433', numero de pedido de la compra
  productoId: 2412,
  productDescription: 'Descripcion del producto',
  purchasePrice : 455,4, // preci de compra
  currentWarranty: true, // si la garantia aun esta vigente
  buyer:true //en caso de que la cuenta del cliente sea la misma que lo compro
}
```

Ejemplo sql para joinear las tablas necesarias



```sql
FROM [NewBytes_DBF].[dbo].[albclit]
INNER JOIN [NewBytes_DBF].[dbo].[albclil] ON albclil.ID_NROREMCLI_ENC = albclit.ID_NROREMCLI_ENC
INNER JOIN [NewBytes_DBF].[dbo].clientes on clientes.ccodcli = albclit.ccodcli
INNER JOIN [NEW_BYTES].[dbo].[ST_REMITOS_VENTA_DETALLE_SALIDA] on [ST_REMITOS_VENTA_DETALLE_SALIDA].REMITO_FP = albclit.cnumalb AND ST_REMITOS_VENTA_DETALLE_SALIDA.SUCURSAL_REMITO = ALBCLIT.cnumsuc AND ST_REMITOS_VENTA_DETALLE_SALIDA.CREF = albclil.cref
INNER JOIN [NEW_BYTES].[dbo].[ST_DETALLE_STOCK] ON ST_REMITOS_VENTA_DETALLE_SALIDA.ID_STOCK = ST_DETALLE_STOCK.ID_STOCK
INNER JOIN [NewBytes_DBF].[dbo].[articulo] ON articulo.cref = albclil.cref
where [ST_REMITOS_VENTA_DETALLE_SALIDA].SERIAL = 'WE4791013661'
```

o



```sql
FROM [NEW_BYTES].[dbo].[ST_DETALLE_STOCK] AS SERIALTAB
LEFT JOIN [NewBytes_DBF].[dbo].articulo ON articulo.cref = SERIALTAB.cref
LEFT join [NEW_BYTES].[dbo].[ST_REMITOS_VENTA_DETALLE_SALIDA] on SERIALTAB.SERIAL = ST_REMITOS_VENTA_DETALLE_SALIDA.serial
LEFT JOIN [NewBytes_DBF].[dbo].[albclit] ON ST_REMITOS_VENTA_DETALLE_SALIDA.REMITO_FP = albclit.cnumalb and ST_REMITOS_VENTA_DETALLE_SALIDA.SUCURSAL_REMITO = albclit.cnumsuc
```
