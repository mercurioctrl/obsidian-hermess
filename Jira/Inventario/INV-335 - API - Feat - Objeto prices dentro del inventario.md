---
jira_key: "INV-335"
aliases: ["INV-335"]
summary: "API - Feat - Objeto prices dentro del inventario"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-02-05 09:13"
updated: "2026-02-24 10:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-335"
---

# INV-335: API - Feat - Objeto prices dentro del inventario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-05 09:13 |
| Actualizado | 2026-02-24 10:39 |
| Etiquetas | ninguna |
| Jira | [INV-335](https://bluinc.atlassian.net/browse/INV-335) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios

## Descripcion

Extender el recurso **GET **`/itemsStocks` para que **incluya información de control de precios** únicamente cuando el cliente lo solicite explícitamente mediante el query param `controlPrices=true`.
Cuando `controlPrices` no venga en `true`, **no se debe ejecutar ningún join/subquery adicional** asociado a precios, para no degradar performance.

```
GET /itemsStocks?currentPage=1&itemsPerPage=500&companyCode=4&brandId=43&controlPrices={controlPrices}
```

Devuelve

```
{
  "title": "PROCESADOR AMD (AM4) RYZEN 9 5900XT",
  "sku": "100-100001581WOF",
  "id": 119140,
  "category": "PROCESADORES",
  "categoryId": 3,
  "brand": "AMD                                               ",
  "brandId": 43,
  "mainImage": "http://static.nb.com.ar/img/7d7b764168469f7732fca173e97dbebd.jpg",
  "globalRegularization": 0.0,
  "stock": 0,
  "virtualStock": 0,
  "stockLio": 0,
  "stockInOrders": 0,
  "stockAfterSale": 0,
  "nstockHide": 0,
  "stockWarehouseId": null,
  "stockWarehouseDescription": null,
  "stockWarehouseCode": null,
  "WarehouseSensitive": false,
  "usedSerialNumbers": 138,
  "totalSerialNumbers": 138,
  "companyCode": 4,
  "companyName": "NB DISTRIBUIDORA MAYORISTA SRL",
  "notSerializable": 0,
  "distributorId": 1,
  "stockCtrl": 0,
  "stockLoQueue": 0,
  "inProviderOrder": 0,
  "inProviderOrderInbound": 138.0,
  "creditNoteReturn": 1,
  "aftersalesCreditNote": 1,
  "regularizations": 0,
  "salesReserved": 0.0,
  "sales": 138.0,
  "stockDelta": 0.0,
  "controlPrices": 
    {
      "itemId": 119140,
      "fob": 31200000.0,
      "cost": 28400000.0,
      "unitPrice": 32944000.0,
      "mayPrice": 30104000.0,
      "loCost": 31524000.0,
      "priceLoReseller": 504904.39,
      "PVP": null,
      "mlPrice": 487331.08,
      "PL": 14.0,
      "PLI": 2.0,
      "MAY1": 4.0,
      "PML": 0.0,
      "MAY2": 2.0,
      "DT2": 190.0,
      "DT3": 320.0,
      "LO1": 6.0,
      "LO2": 5.0,
      "MK1": 0.0,
      "PCAM": 6.0,
      "IINT": null,
      "IVA": 105.0
    }
  
}

  ....
```

### ¿Como se calculan estas cosas?

```
;WITH Cot AS (
    SELECT
        PesosLo = MAX(CASE WHEN c.NOMBRE = 'PESOSLO' THEN c.COTIZACION END),
        CotId1  = MAX(CASE WHEN c.ID = 1 THEN c.COTIZACION END)
    FROM NEW_BYTES.dbo.MS_COTIZACIONES c
)
SELECT
    a.ID_ARTICULO                                         AS itemId,
    fob.FOB                                               AS fob,
    ROUND(a.NCOSTEPROM, 2)                                AS cost,
    ROUND(a.npvp1, 2)                                     AS unitPrice,
    ROUND(a.npvp5, 2)                                     AS mayPrice,
    ROUND(a.NPLO, 2)                                      AS loCost,
    lop.LOP_EnLo                                          AS priceLoReseller,
    ROUND(pvp.precio, 2)                                  AS PVP,
    ROUND(a.npvp3 * c.CotId1 * (a.ivaVenta / 100.0 + 1), 2) AS mlPrice    
    ROUND(g.PORC_GANAN_ESTIP, 2)                           AS PL,
    ROUND(g.PORC_GANAN_ESTIP2, 2)                          AS PLI,
    ROUND(g.PORC_GANAN_ESTIP3, 2)                          AS MAY1,
    ROUND(g.PORC_GANAN_ESTIPMK1, 2)                        AS PML,
    ROUND(g.PORC_GANAN_ESTIP4, 2)                          AS MAY2,
    ROUND(a.NDTO2, 2)                                      AS DT2,
    ROUND(a.NDTO3, 2)                                      AS DT3,
    ROUND(g.PORC_GANAN_ESTIPLO, 2)                         AS LO1,
    ROUND(g.PORC_GANAN_ESTIPLO1, 2)                        AS LO2,
    ROUND(g.PORC_GANAN_ESTIPMK1, 2)                        AS MK1,
    ROUND(g.PORC_GANAN_ESTIP6, 2)                          AS PCAM,
    ROUND(a.internalTax, 2)                                AS IINT,
    a.ivaVenta                                            AS IVA
FROM NewBytes_DBF.dbo.articulo a
CROSS JOIN Cot c
LEFT JOIN NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS g
    ON a.cref = g.ID_ARTICULO
LEFT JOIN NewBytes_DBF.dbo.scrap_hg hg
    ON a.ID_ARTICULO = hg.id_articulo
LEFT JOIN NewBytes_DBF.dbo.PVP pvp
    ON a.ID_ARTICULO = pvp.id_articulo

OUTER APPLY (
    SELECT TOP (1)
        albprol.nprediv AS FOB
    FROM NewBytes_DBF.dbo.albprol
    JOIN NewBytes_DBF.dbo.albprot
        ON albprol.nnumalb = albprot.nnumalb
    WHERE albprol.cref = a.cref
    ORDER BY albprot.dfecalb DESC
) fob

OUTER APPLY (
    SELECT TOP (1)
        ROUND(x.precioLo, 2) AS LOP_EnLo
    FROM (
        SELECT
            precioLo =
                (p.precioDolar * c.PesosLo)
                - (p.precioDolar * c.PesosLo * p.descuento / 100.0)
        FROM CS.dbo.productos p
        WHERE p.id_interno = a.ID_ARTICULO
          AND p.precioFinal > 1
          AND p.activo = 1
    ) x
    ORDER BY x.precioLo
) lop

WHERE a.CODIGO IS NOT NULL
  AND a.EXCLUIR <> 1
  AND a.ID_ARTICULO = ?
ORDER BY a.CDETALLE ASC;

```

Se debe elegir el camino mas performativo para agregregar la funcionaldiad. 

Cuando pricesControl no viene en true, ni agrego los elemmentos a la query para evitar penalizar la performance
