---
jira_key: "PED-66"
summary: "API - Feat - Listar productos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-12 08:37"
updated: "2023-12-21 14:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-66"
---

# PED-66: API - Feat - Listar productos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-12 08:37 |
| Actualizado | 2023-12-21 14:35 |
| Etiquetas | ninguna |
| Jira | [PED-66](https://bluinc.atlassian.net/browse/PED-66) |

## Descripción

Crearemos un recurso especifico para poder buscar/listar items tanto para ver sus atributos en un listado como para meterlos en una orden o navegarlos.

Para esto mostraremos los siguientes atributos y prestaremos especial atencion a aquellos que dan cuenta del stock

### ¿Cual es el criterio para mostrar el stock?

Lo que se intenta es dar cuenta de la cantidad que hay disponible para cada item, teniendo en cuenta aquellos que se encuentran en un pedido (osea tomados por otro vendedor).

Entonces seria muy simple:

`availableStock` = `stock` -` stockInOrders` 

```
GET {API_URL}/v1/items
```

Devuelve

```json
[
    {
        "title": "MEMORIA GSKILL FLARE X5 SERIES AMD EXPO DDR5 32GB 6000 MHZ 2X16GB",
        "sku": "F5-6000J3636F16GX2-FX5",
        "id": 118272,
        "category": "MEMORIAS",
        "categoryId": 1,
        "brand": "G.SKILL",
        "brandId": 17,
        "mainImage": "https:\/\/static.nb.com.ar\/i\/nb_MEMORIA-GSKILL-FLARE-X5-SERIES-AMD-EXPO-DDR5-32GB-6000-MHZ-2X16GB_ver_2832ed0c68ba5e53292af10c2812f57c.jpg",
        "brandImage": "https:\/\/static.nb.com.ar\/img\/b886ce36af0f66e6a003d2bf88be904c.jpeg",
        "price": {
            "value": 241.9,
            "iva": 10.5,
            "finalPrice": 267.2995,
            "percepcion": null
        },
        "warranty": "12 meses",
        "stock":4,
        "stockLio":2,
        "stockInOrders":2,
        "availableStock": 2,
        "stockInMyOrder": 0 <-- Esta parametro seteado en cero por ahora lo usaremos para determinar si tengo agregado stock del item en la orden que estoy editando, si lo estoy
    },
    {
        "title": "MINI PC GIGABYTE BRIX BSRE-1505 (AMD Ryzen 1505G)",
        "sku": "GB-BSRE-1505",
        "id": 116741,
        "category": "COMPUTADORAS",
        "categoryId": 31,
        "brand": "GIGABYTE",
        "brandId": 4,
        "mainImage": "https:\/\/static.nb.com.ar\/i\/nb_MINI-PC-GIGABYTE-BRIX-BSRE-1505-(AMD-Ryzen-1505G)_ver_cc931534c55dd0fe2ee6a3fa0aa4378f.jpeg",
        "brandImage": "https:\/\/static.nb.com.ar\/img\/f2aae2c829b051430eb6a039ad6bc7ae.jpg",
        "price": {
            "value": 668,
            "iva": 10.5,
            "finalPrice": 738.14,
        },
        "warranty": "36 meses",
        "stock":4,
        "stockLio":2,
        "stockInOrders":2,
        "availableStock": 2,
        "stockInMyOrder": 0
    }
  ]
```

**Repositorio de orientación **

```sql
SELECT
    A.ID_ARTICULO,
    A.CDETALLE,
    W.marca AS MARCA,
    F.cnomfam AS FAMILIA,
    A.ID_PRODUCTO,
    A.ivaVenta,
    A.cpredef2,
    S.nstock,
    S.nstock_d1,
    S.nstock_lo,
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
    ) AS ncanped_internos,
    [checksum]
FROM [NewBytes_DBF].[dbo].[articulo] A
LEFT JOIN [NB_WEB].[dbo].[WebArtComplement] W ON A.codigo = W.codigoArt
LEFT JOIN [NewBytes_DBF].[dbo].familias F ON F.ccodfam = A.ccodfam
LEFT JOIN [NewBytes_DBF].[dbo].stocks S ON S.ID_ARTICULO = A.ID_ARTICULO
LEFT JOIN [NB_WEB].[dbo].[fotos_productos] FP ON FP.id_nb_producto = A.codigo AND portada = 1
LEFT JOIN PRODUCTOS.dbo.fotos FOT ON FP.id_productos_fotos = FOT.id
WHERE 
    EXCLUIR <> 1 
    AND id_distribuidora = 1 
    AND ocultarDeNb <> 1 
GROUP BY 
    A.ID_ARTICULO,
    A.CDETALLE,
    W.marca,
    F.cnomfam,
    A.ID_PRODUCTO,
    A.ivaVenta,
    A.cpredef2,
    S.nstock,
    S.nstock_d1,
    S.nstock_lo,
    A.cref,
    [checksum]
ORDER BY 
    F.cnomfam ASC, 
    W.marca ASC, 
    A.CDETALLE ASC;

```
