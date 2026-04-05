---
jira_key: "EXP-32"
summary: "API - Feat - Listar pedidos de proveedores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-02 14:47"
updated: "2023-07-09 20:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-32"
---

# EXP-32: API - Feat - Listar pedidos de proveedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-02 14:47 |
| Actualizado | 2023-07-09 20:34 |
| Etiquetas | ninguna |
| Jira | [EXP-32](https://bluinc.atlassian.net/browse/EXP-32) |

## Descripción

```
GET {API_URL}/v1/providersOrders
```

Retorna

```
[
{
id: 3434
providerOrder:10477
date: //es la fecha del pedido a proveedor
distpatchName : '22 073 IC04 107453 U'
providerId: 88
providerName: NEW BYTES INC
userIdCreator: 5
userNameCreator: Daniel
fullSerialized: false // esto indica si fue serialzioado o no completo, lo veremos mas adelantes
},
{
id: 3434
providerOrder:10477
date: //es la fecha del pedido a proveedor
distpatchName : '22 073 IC04 107453 U'
providerId: 88
providerName: NEW BYTES INC
userIdCreator: 5
userNameCreator: Daniel
fullSerialized: false
}
]
```

**Tablas que utilizaremos**

`SELECT * FROM [NewBytes_DBF].[dbo].[FP_Proveedores][NewBytes_DBF].[dbo].[PedProT]`

`[NewBytes_DBF].[dbo].[PedProl]`

`[NEW_BYTES].[dbo].[ST_DESPACHOS_ENTRADAS_CABECERA]`
`[NEW_BYTES].[dbo].[ST_ENL_DESPACHOS_ENTRADAS_REMITOS]`
`[NEW_BYTES].[dbo].[ST_DESPACHOS_ENTRADAS_CABECERA]`

**Ejemplos de uso de las tablas**

```
SELECT DISTINCT TOP(300) ST_ENL_DESPACHOS_ENTRADAS_REMITOS.ID_DESPACHO_ENTRADA, ST_ENL_DESPACHOS_ENTRADAS_REMITOS.REMITO_PRV_FP, ST_ENL_DESPACHOS_ENTRADAS_REMITOS.ID_PROVEEDOR, FP_PROVEEDORES.cnompro, ST_DESPACHOS_ENTRADAS_CABECERA.DESCRIPCION, USU_IDENTIFICACION, ACTUALIZADO, DE_FECHA_DESPACHO FROM [NEW_BYTES].[dbo].[ST_DESPACHOS_ENTRADAS_CABECERA] INNER JOIN [NEW_BYTES].[dbo].[ST_ENL_DESPACHOS_ENTRADAS_REMITOS] ON [NEW_BYTES].[dbo].[ST_DESPACHOS_ENTRADAS_CABECERA].ID_DESPACHO_ENTRADA = [NEW_BYTES].[dbo].[ST_ENL_DESPACHOS_ENTRADAS_REMITOS].ID_DESPACHO_ENTRADA INNER JOIN NewBytes_DBF.dbo.FP_PROVEEDORES ON [NEW_BYTES].[dbo].[ST_ENL_DESPACHOS_ENTRADAS_REMITOS].ID_PROVEEDOR = NewBytes_DBF.dbo.FP_PROVEEDORES.CCODPRO WHERE ST_DESPACHOS_ENTRADAS_CABECERA.ID_DESPACHO_ENTRADA IS NOT NULL AND DE_FECHA_DESPACHO > 20220901 AND DE_FECHA_DESPACHO < 20221102 ORDER BY ID_DESPACHO_ENTRADA DESC
```
