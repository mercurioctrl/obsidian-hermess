---
jira_key: "POS-236"
aliases: ["POS-236"]
summary: "API - Feat - Listar articulos pendientes de recepcion para postventa proveedores"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-08 12:06"
updated: "2023-04-12 14:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-236"
---

# POS-236: API - Feat - Listar articulos pendientes de recepcion para postventa proveedores

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-08 12:06 |
| Actualizado | 2023-04-12 14:25 |
| Etiquetas | ninguna |
| Jira | [POS-236](https://bluinc.atlassian.net/browse/POS-236) |

## Relaciones

- **Padre:** [[POS-235]] Postventa Proveedores Recepcion

## Descripcion

```
GET {API_URL}/v1/afterSaleProviders
```



Basándose en `[NEW_BYTES].[dbo].[ST_RMADETALLE]` y `[NEW_BYTES].[dbo].[ST_RMACABECERA]` se debe mostrar un listado de items con las columnas

```
{
  "itemId": 12345,
  "Description": "Example product",
  "serial": "A1B2C3D4",
  "brandId": 67890,
  "brandDescription": "Example brand",
  "providerId": 13579,
  "providerDescription": "Example provider",
  "afterSaleId": 24680,
  "afterSaleDetailId": 13579,
  "afterSaleInboundDate": "2022-03-08",
  "categoryId": 9876,
  "categoryDescription": "Example category"
}

```

### Se debe poder ordernar por 

- Marca


- categoryDescription


- providerDescription


- description



### Se debe poder filtrar por

- providerDescription 


- providerId


- Serial


- aftersaleId


- afterSaleInboundDate (between de fechas)



Se debe poder filtrar por: Estado, Deposito, Proveedor, serial, nro rma, fecha, factura proveedor

### Otras tablas que intervienen:

`[NewBytes_DBF].[dbo].[articulo]`

`[NewBytes_DBF].[dbo].[FP_Proveedores]`

`NB_WEB.dbo.marcas`
`NewBytes_DBF.dbo.familias`
