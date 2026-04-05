---
jira_key: "EXP-89"
aliases: ["EXP-89"]
summary: "API - Feat - Pedir control sobre un producto"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-22 10:09"
updated: "2022-12-12 12:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-89"
---

# EXP-89: API - Feat - Pedir control sobre un producto

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-22 10:09 |
| Actualizado | 2022-12-12 12:33 |
| Etiquetas | ninguna |
| Jira | [EXP-89](https://bluinc.atlassian.net/browse/EXP-89) |

## Relaciones

- **Padre:** [[EXP-17 - Feat - Listar productos (Control de stock)|EXP-17]] Feat - Listar productos (Control de stock)
- **blocks:** [[EXP-88 - API - Feat - Listar productos|EXP-88]] API - Feat - Listar productos
- **is blocked by:** [[EXP-88 - API - Feat - Listar productos|EXP-88]] API - Feat - Listar productos

## Descripcion

```
POST {API_URL}/v1/items
```

```
[
{
"Id":"104964"
},
{
"Id":"104965"
}
]
```

Este recurso se encarga de “pedir el control sobre un producto”. Es decir: Ubicarlo en la lista para ser contabilizado fisicamente.

Para eso, los id que se reciben se incluirán en` [NewBytes_DBF].[dbo].[stocksControl]`, solo si no existe en la tabla un registro para el mismo producto, que tenga la columna `counted` en `null`

Caso contrario, informaremos que el mismo ya fue contabilizado.

Ademas guardaremos quien pidió el control (`requestingUser`)

---

Estructura de `[NewBytes_DBF].[dbo].[stocksControl]`:

- `id`


- `itemId` // el id para relacionarlo con los items


- `counted` // Es la cantidad contada (esto se hace en un paso posterior), inicio nuall


- `nstock` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `nstock_lo` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `nstock_en_cola` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `regularizacion_global` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `nstock_virtual` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `nstock_reserva_pedidos` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `nstock_postventa` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `nstock_lo_reserva_pedidos` // Trae el dato de ese momento de `newbytes_dbf.dbo.stocks` , inicio nuall


- `countedDate` // La fecha de cuando se contabilizo  (esto se hace en un paso posterior) , inicio nuall


- `createDate` // corresponde a la fecha de inserción de la fila 


- `requestingUser` // el usuario que solicito el control
