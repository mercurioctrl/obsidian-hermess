---
jira_key: "PED-39"
summary: "API - Feat - Agregar/quitar item a una orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-21 19:39"
updated: "2025-10-09 15:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-39"
---

# PED-39: API - Feat - Agregar/quitar item a una orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-21 19:39 |
| Actualizado | 2025-10-09 15:48 |
| Etiquetas | ninguna |
| Jira | [PED-39](https://bluinc.atlassian.net/browse/PED-39) |

## Descripción

Lo que hace este recurso es cambiar la cantidad que la orden tiene de un determinado item

```
PATCH {API_URL}/v1/order/addItem
```

```
[
    {
        "order": "0002",
        "branch": "10328550",
        "amount": "9.000", <-- esta es la cantidad que quiero que el pedido tenga
        "itemId": 12434,
    }
]

```

Separaremos el proceso en algunas etapas

1 - Verificamos que el pedido sea editable y que las cantidades puedan satisfacer la petición que estoy haciendo, para esto:

`[NewBytes_DBF].[dbo].[pedclit].cestado` debe ser ‘P' y el pedido debe ser  ‘INTERNO’, 'PRESUPUESTO' o ‘DESCARGADO’.

2 - Verificamos que el stock satisface el stock que tengo disponible en combinación con los que tengo metidos dentro de pedidos:

Si (`nstock` - `ncanped_internos`) >= `amount` o bien es un 'PRESUPUESTO' entonces procedemos a guardar el cambio.

Recodemos que `ncanped_internos` sale de algo como esto:

```
(
        SELECT SUM(ncanped) 
        FROM [NewBytes_DBF].[dbo].pedclil pl_sub
        LEFT JOIN NewBytes_DBF.dbo.pedclit pt_sub 
        ON pl_sub.cnumsuc = pt_sub.cnumsuc
        AND pl_sub.cnumped = pt_sub.cnumped
        WHERE
            (pt_sub.cobserv = 'INTERNO' OR pt_sub.cobserv = 'DESCARGADO')
            AND pt_sub.cestado = 'P'
            AND (pl_sub.cref = A.cRef OR pl_sub.ID_Articulo = A.ID_ARTICULO)
    ) AS ncanped_internos
```

3 - Si se dan las condiciones entonces obtendremos el precio del item con nuestra clase del precio y el cliente, en caso de que sea necesario

y luego haremos algo como esto para agregar el item a `NewBytes_DBF.dbo.pedclil` en la cantidad que le pedimos.

```
  IF EXISTS(
  SELECT cnumped FROM NewBytes_DBF.dbo.pedclil WHERE pedclil.cnumped = '" . $cnumped . "' AND pedclil.cnumsuc = '" . $cnumsuc . "' AND (ID_Articulo = '" . $id_Articulo . "' OR cref = '" . $id_Articulo . "')
  )
  BEGIN
  UPDATE NewBytes_DBF.dbo.pedclil SET  niva = " . $niva . ", ncanped = " . $cantidad . ", npreunit = " . $npreunit . ", ndto = " . $ndto . ", listaPrecio = '" . $listaLetra . "' WHERE pedclil.cnumped = '" . $cnumped . "' AND pedclil.cnumsuc = '" . $cnumsuc . "' AND (ID_Articulo = '" . $id_Articulo . "' OR cref = '" . $id_Articulo . "')
  END
  ELSE
  begin
  INSERT INTO NewBytes_DBF.dbo.pedclil (cnumsuc, cnumped, ncanped, npreunit, cref, id_articulo, ndto, niva, listaPrecio) values ('" . $cnumsuc . "' , '" . $cnumped . "', " . $cantidad . ", " . $npreunit . ", '" . $id_Articulo . "', " . $id_Articulo . ", " . $ndto . ", " . $niva . ", '" . $listaLetra . "')
  END
```

Si todo se pudo hacer de manera correcta, entonces devolvemos el objeto que demuestra succes:`true`, caso contrario `false`
