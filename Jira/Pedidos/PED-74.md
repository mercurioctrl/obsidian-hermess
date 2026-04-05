---
jira_key: "PED-74"
summary: "API - Feat - Obtener datos para editar orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-17 16:33"
updated: "2023-09-27 10:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-74"
---

# PED-74: API - Feat - Obtener datos para editar orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-17 16:33 |
| Actualizado | 2023-09-27 10:21 |
| Etiquetas | ninguna |
| Jira | [PED-74](https://bluinc.atlassian.net/browse/PED-74) |

## Descripción

Este recurso, al hacer clic en un accionable del front, sobre un pedido nos permite editarlo.

```
GET {API_URL}/getEditOrderData/{orderybranch}
```

```
[
    {
        "totalInPesos": 139711.59,
        "totalInDollars": 353.7,
        "branchNumber": "0002",
        "orderNumber": "10328549",
        "customerCode": "032103",
        "clientName": "Nombre del cliente",
        "currencyAmount": 350.5
    }
]
```

De tal modo de que podamos “instanciarlo” en el front para mostrar un widget similar a este

[attachment]
Solo es posible editar pedidos cuando `[NewBytes_DBF].[dbo].[pedclit].cestado = 'P'`

## Query de referencia 

```
SELECT
    npreunit,
    ncanped,
    articulo.ID_Articulo,
    pedclil.ndto,
    clientes.ccodcli,
    clientes.cnomcli,
    CASE 
        WHEN pedclit.nvaldiv IS NULL THEN
            (
                SELECT
                    COTIZACION
                FROM
                    NEW_BYTES.dbo.MS_COTIZACIONES 
                WHERE 
                    MS_COTIZACIONES.id=1
            )
        ELSE pedclit.nvaldiv
    END as currencyAmount
    
FROM [NewBytes_DBF].[dbo].[pedclit]
LEFT JOIN NewBytes_DBF.dbo.pedclil
ON pedclit.cnumped = pedclil.cnumped and pedclit.cnumsuc = pedclil.cnumsuc
LEFT JOIN [NewBytes_DBF].[dbo].articulo ON articulo.cRef = pedclil.cref
LEFT JOIN NewBytes_DBF.dbo.clientes ON clientes.ccodcli = pedclit.ccodcli
WHERE pedclit.cnumped = ? AND pedclit.cnumsuc = ?
```

Finalmente para poder obtener los totales (esto podemos hacerlo directo en la consulta o en el código) haremos:

`TotalPorItem = (cantidad * precio) - (cantidad*precio* descuento / 100)`

`TotalPorItemFinal = TotalPorItem * [(iva/100)+1]`
